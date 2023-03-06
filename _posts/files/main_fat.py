import json
import logging
from threading import Thread
from typing import Optional

import redis
import uvicorn
from fastapi import FastAPI

logger = logging.getLogger(__name__)

redis = redis.StrictRedis(host='localhost', port=6379, db=0)

count_name = "bwic:count:"
rank_name = "bwic:rank:bwic:"
def count(bwic_id):
    redis.incr(count_name+str(bwic_id))

def rank(bwic_id, client_id, market_value):
    mapping = {"client:"+str(client_id): market_value}
    redis.zadd(rank_name+str(bwic_id), mapping)

def cancel(bwic_id, client_id):
    redis.zrem(rank_name+str(bwic_id), "client:"+str(client_id))

def get_rank(bwic_id, client_id):
    # current rank
    my_rank = redis.zrevrank(rank_name+str(bwic_id), "client:"+str(client_id))
    # total count
    bwic_count = redis.zcount(rank_name+str(bwic_id), '-inf', '+inf')
    if my_rank is not None and bwic_count > 0:
        result = f"{my_rank+1}/{bwic_count}"
        return result

def get_count(bwic_id):
    count_key = count_name + str(bwic_id)
    return redis.get(count_key)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/myrank/{bwic_id}/{client_id}")
async def my_rank(bwic_id, client_id):
    print(f"Rank request: bwic id: {bwic_id}, client id: {client_id}")
    return get_rank(bwic_id, client_id)

@app.get("/count/{bwic_id}")
async def get_count(bwic_id):
    print(f"Count request: bwic id: {bwic_id}")
    return get_count(bwic_id)

from confluent_kafka import Consumer
################
consumer = Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'latest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', consumer.list_topics().topics)
consumer.subscribe(['bid-topic', 'cancel-topic'])

def consume_message():
    while True:
        msg = consumer.poll(0.01) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data = json.loads(msg.value().decode('utf-8'))

        bwicId = data['bwicId']
        clientId = data['clientId']
        if 'bidMarketValue' in data:
            bidMarketValue = data['bidMarketValue']
            print(f"Bid request: bwicId: {bwicId}, clientId: {clientId}, bidMarketValue: {bidMarketValue}")
            count(bwicId)
            rank(bwicId, clientId, bidMarketValue)
        else:
            print(f"Cancel request: bwicId: {bwicId}, clientId: {clientId}")
            cancel(bwicId, clientId)
    consumer.close()

t = Thread(target=consume_message)
t.start()


if __name__ == '__main__':
    port = 8000
    logger.info(f'Started uvicorn server on 0.0.0.0 on {port}')
    uvicorn.run('main:app',
                host='0.0.0.0',
                port=port,
                reload=True)
