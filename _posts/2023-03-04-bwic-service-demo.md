---
layout: post
title: "Bwic service demo"
tagline: "Springboot"
---

使用 Springboot 编写 bwic-service。


## 创建空项目
使用 initializer
https://start.spring.io/

![img.png](https://raw.githubusercontent.com/yuqisun/yuqisun.github.io/master/_posts/images/bwic-demo/create_bwic_demo.png)

## application properties
```properties
server.port=8086

spring.datasource.url=jdbc:mysql://localhost:3306/bwic?serverTimezone=Asia/Shanghai
spring.datasource.username=root
spring.datasource.password=123456
spring.jpa.hibernate.ddl-auto=update

## Hibernate Properties
# The SQL dialect makes Hibernate generate better SQL for the chosen database
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQL5InnoDBDialect
```

## restTemplate
```java
@Bean
public RestTemplate restTemplate() {
    return new RestTemplate();
}
```

## Client bean
```java
@Data
public class Client {
    private Long id;
    private String name;
    private Double assetValue;
}
```

## Get client object
```java
@Service
public class LoginServiceImpl implements LoginService {
    @Autowired
    private RestTemplate restTemplate;

    @Override
    public Client getClient(Long clientId) {
        Client client = restTemplate.getForObject("http://localhost:8087/getClient/{id}", Client.class, clientId);

        return client;
    }
}
```

## data.sql
```mysql-sql
alter table bwic modify id int(11) auto_increment;
delete from bwic;
Insert into bwic(id, cusip, position, price, due_date, market_value, created_by, created_date) values
(1, '037833100', 20, 100.0, '20230222', 1500, 'Nicole Montgomery[trader]', '2023-02-10 11:12:12'),
(2, '02079K107', 30, 70.0, '20230222', 1800, 'Susan Wagner[trader]', '2023-02-10 11:12:12'),
(3, '011659109', 10, 80.0, '20230221', 500, 'Nicole Montgomery[trader]', '2023-02-10 11:12:12'),
(4, '931142103', 60, 40.0, '20230221', 1200, 'Susan Wagner[trader]', '2023-02-10 11:12:12'),
(5, 'G3921A955', 80, 90.0, '20230820', 5000, 'Susan Wagner[trader]', '2023-02-10 11:12:12'),
(6, 'G3921A955', 80, 90.0, '20230820', 5000, 'Susan Wagner[trader]', '2023-02-10 11:12:12'),
(7, 'G3921A955', 80, 90.0, '20230820', 5000, 'Susan Wagner[trader]', '2023-02-10 11:12:12'),
(8, 'G3921A955', 80, 90.0, '20230820', 5000, 'Susan Wagner[trader]', '2023-02-10 11:12:12'),
(9, 'G3921A955', 80, 90.0, '20230820', 5000, 'Susan Wagner[trader]', '2023-02-10 11:12:12'),
(10, 'G3921A955', 80, 90.0, '20230820', 5000, 'Susan Wagner[trader]', '2023-02-10 11:12:12'),
(11, 'G3930E101', 100, 10.0, '20230920', 300, 'Nicole Montgomery[trader]', '2023-02-10 11:12:12');

alter table bid modify id int(11) auto_increment;
delete from bid;
Insert into bid(id, bwic_id, client_id, bid_market_value, bid_time) values
(1, 1, 1, 1000, '2023-02-12 11:12:12'),
(2, 2, 1, 1800, '2023-02-12 11:12:12'),
(3, 3, 2, 500, '2023-02-12 11:12:12'),
(4, 3, 3, 1200, '2023-02-12 11:12:12'),
(5, 5, 1, 5000, '2023-02-12 11:12:12'),
(6, 6, 3, 5000, '2023-02-12 11:12:12'),
(7, 7, 3, 5000, '2023-02-12 11:12:12'),
(8, 8, 3, 5000, '2023-02-12 11:12:12'),
(9, 9, 3, 5000, '2023-02-12 11:12:12'),
(10, 9, 2, 5000, '2023-02-12 11:12:12'),
(11, 10, 2, 300, '2023-02-12 11:12:12');
```

