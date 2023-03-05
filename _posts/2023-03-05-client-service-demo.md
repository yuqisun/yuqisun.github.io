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

## Maven build jar
```shell
D:\SDisk\workspace\Java\client-service>mvn clean package -Dmaven.test.skip=true
[INFO] Scanning for projects...
[INFO]
[INFO] ---------------------< com.example:client-service >---------------------
[INFO] Building client-service 0.0.1-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- maven-clean-plugin:3.2.0:clean (default-clean) @ client-service ---
[INFO] Deleting D:\SDisk\workspace\Java\client-service\target
[INFO]
[INFO] --- maven-resources-plugin:3.2.0:resources (default-resources) @ client-service ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] Using 'UTF-8' encoding to copy filtered properties files.
[INFO] Copying 1 resource
[INFO] Copying 1 resource
[INFO]
[INFO] --- maven-compiler-plugin:3.10.1:compile (default-compile) @ client-service ---
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 6 source files to D:\SDisk\workspace\Java\client-service\target\classes
[INFO]
[INFO] --- maven-resources-plugin:3.2.0:testResources (default-testResources) @ client-service ---
[INFO] Not copying test resources
[INFO]
[INFO] --- maven-compiler-plugin:3.10.1:testCompile (default-testCompile) @ client-service ---
[INFO] Not compiling test sources
[INFO]
[INFO] --- maven-surefire-plugin:2.22.2:test (default-test) @ client-service ---
[INFO] Tests are skipped.
[INFO]
[INFO] --- maven-jar-plugin:3.2.2:jar (default-jar) @ client-service ---
[INFO] Building jar: D:\SDisk\workspace\Java\client-service\target\client-service-0.0.1-SNAPSHOT.jar
[INFO]
[INFO] --- spring-boot-maven-plugin:2.7.8:repackage (repackage) @ client-service ---
[INFO] Replacing main artifact with repackaged archive
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  2.644 s
[INFO] Finished at: 2023-03-05T22:09:30+08:00
[INFO] ------------------------------------------------------------------------
```

## Start service (about 3 seconds)
```shell
D:\SDisk\workspace\Java\client-service>java -jar target\client-service-0.0.1-SNAPSHOT.jar

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v2.7.8)

2023-03-05 22:10:53.599  INFO 17816 --- [           main] c.e.c.ClientServiceApplication           : Starting ClientServiceApplication v0.0.1-SNAPSHOT using Java 17.0.6 on DESKTOP-VG9BSQR with PID 17816 (D:\SDisk\workspace\Java\client-service\target\client-service-0.0.1-SNAPSHOT.jar started by syq in D:\SDisk\workspace\Java\client-service)
2023-03-05 22:10:53.601  INFO 17816 --- [           main] c.e.c.ClientServiceApplication           : No active profile set, falling back to 1 default profile: "default"
2023-03-05 22:10:54.124  INFO 17816 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Bootstrapping Spring Data JPA repositories in DEFAULT mode.
2023-03-05 22:10:54.175  INFO 17816 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Finished Spring Data repository scanning in 41 ms. Found 1 JPA repository interfaces.
2023-03-05 22:10:54.696  INFO 17816 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8087 (http)
2023-03-05 22:10:54.706  INFO 17816 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2023-03-05 22:10:54.706  INFO 17816 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.71]
2023-03-05 22:10:54.771  INFO 17816 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2023-03-05 22:10:54.772  INFO 17816 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 1126 ms
2023-03-05 22:10:54.799  INFO 17816 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Starting...
2023-03-05 22:10:54.988  INFO 17816 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Start completed.
2023-03-05 22:10:54.998  INFO 17816 --- [           main] o.s.b.a.h2.H2ConsoleAutoConfiguration    : H2 console available at '/h2-console'. Database available at 'jdbc:h2:mem:testdb'
2023-03-05 22:10:55.122  INFO 17816 --- [           main] o.hibernate.jpa.internal.util.LogHelper  : HHH000204: Processing PersistenceUnitInfo [name: default]
2023-03-05 22:10:55.170  INFO 17816 --- [           main] org.hibernate.Version                    : HHH000412: Hibernate ORM core version 5.6.14.Final
2023-03-05 22:10:55.323  INFO 17816 --- [           main] o.hibernate.annotations.common.Version   : HCANN000001: Hibernate Commons Annotations {5.1.2.Final}
2023-03-05 22:10:55.421  INFO 17816 --- [           main] org.hibernate.dialect.Dialect            : HHH000400: Using dialect: org.hibernate.dialect.H2Dialect
2023-03-05 22:10:55.869  INFO 17816 --- [           main] o.h.e.t.j.p.i.JtaPlatformInitiator       : HHH000490: Using JtaPlatform implementation: [org.hibernate.engine.transaction.jta.platform.internal.NoJtaPlatform]
2023-03-05 22:10:55.876  INFO 17816 --- [           main] j.LocalContainerEntityManagerFactoryBean : Initialized JPA EntityManagerFactory for persistence unit 'default'
2023-03-05 22:10:56.109  WARN 17816 --- [           main] JpaBaseConfiguration$JpaWebConfiguration : spring.jpa.open-in-view is enabled by default. Therefore, database queries may be performed during view rendering. Explicitly configure spring.jpa.open-in-view to disable this warning
2023-03-05 22:10:56.370  INFO 17816 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8087 (http) with context path ''
2023-03-05 22:10:56.377  INFO 17816 --- [           main] c.e.c.ClientServiceApplication           : Started ClientServiceApplication in 3.134 seconds (JVM running for 3.494)
```

