## requirements.txt
1. pip install fastapi
2. pip install "uvicorn[standard]"
3. pip install redis
4. pip install confluent_kafka

## redis
1. count(bid request -> bwic id)
```shell
redis> incr bwic:count:bwicId
(integer) 1
redis> get bwic:count:bwicId
"1"
redis> incr bwic:count:bwicId
(integer) 2
redis> get bwic:count:bwicId
"2"
```

2. rank(bid, cancel request -> bwic id + client id + market value)
```shell
redis> zadd bwic:rank:bwic:bwicId 1800 client:1
(integer) 1
redis> zadd bwic:rank:bwic:bwicId 1200 client:2
(integer) 1
redis> zrevrank bwic:rank:bwic:bwicId client:1
(integer) 0
redis> zrevrank bwic:rank:bwic:bwicId client:2
(integer) 1
redis> zcount bwic:rank:bwic:bwicId -inf +inf
(integer) 2
redis> 
```

3. cancel:
```shell
redis> zrem bwic:rank:bwic:bwicId client:1
(integer) 1
```

