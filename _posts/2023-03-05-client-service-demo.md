---
layout: post
title: "Client service demo"
tagline: "Springboot"
---

使用 Springboot 编写 client-service。


## 创建空项目
使用 initializer
https://start.spring.io/

![img.png](https://raw.githubusercontent.com/yuqisun/yuqisun.github.io/master/_posts/images/client-demo/create_client_demo.png)

## application properties
```properties
server.port=8087

spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect

spring.jpa.defer-datasource-initialization=true
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console
spring.h2.console.settings.trace=false
spring.h2.console.settings.web-allow-others=false
```

## Client Entity
```java
@Entity
@Data
public class Client {
    @Id
    private Long id;
    private String name;
    private Long assetValue;
}
```

## data.sql
```mysql-sql
Insert into Client(id, name, asset_value) values
(1, 'Peter Fisher', 5000),
(2, 'Jorge Sullivan', 8000),
(3, 'Eric Woods', 6000),
(4, 'Norma Fisher', 12000),
(5, 'Kayla Sullivan', 800),
(6, 'Elizabeth Woods', 10000);
```

## endpoint
```java
@GetMapping("/getClient/{id}")
public Client getClient(@PathVariable Long id) {
    return clientService.getClient(id);
}
```
