---
layout: post
title: "Quarkus 实践"
tagline: "Quarkus"
---

使用 Quarkus 编写 client-service。


## 创建空项目
使用 initializer
https://code.quarkus.io/?a=client-service-with-quarkus&e=resteasy-reactive&e=jdbc-h2  
![img.png](https://raw.githubusercontent.com/yuqisun/yuqisun.github.io/master/_posts/images/client-demo/client_quarkus.png)
![img_1.png](https://raw.githubusercontent.com/yuqisun/yuqisun.github.io/master/_posts/images/client-demo/client_quarkus_2.png)


## Update POM
因为 `io.quarkus:quarkus-datasource-deployment-spi:jar:2.16.4.Final was not found in http://maven.aliyun.com/nexus/content/repositories/central/`
```xml
<quarkus.platform.version>2.16.3.Final</quarkus.platform.version>
```

## 运行项目
```shell
D:\SDisk\workspace\Java\demo\client-svc-with-quarkus>quarkus dev
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------< org.acme:client-svc-with-quarkus >------------------
[INFO] Building client-svc-with-quarkus 1.0.0-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- quarkus-maven-plugin:2.16.3.Final:dev (default-cli) @ client-svc-with-quarkus ---
[INFO] Invoking org.apache.maven.plugins:maven-resources-plugin:2.6:resources @ client-svc-with-quarkus
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] Copying 2 resources
[INFO] Invoking io.quarkus.platform:quarkus-maven-plugin:2.16.3.Final:generate-code @ client-svc-with-quarkus
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-jdbc-h2-deployment/2.16.3.Final/quarkus-jdbc-h2-deployment-2.16.3.Final.jar
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-jdbc-h2-deployment/2.16.3.Final/quarkus-jdbc-h2-deployment-2.16.3.Final.jar (7.3 kB at 11 kB/s)
[INFO] Invoking org.apache.maven.plugins:maven-compiler-plugin:3.10.1:compile @ client-svc-with-quarkus
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 1 source file to D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\target\classes
[INFO] Invoking org.apache.maven.plugins:maven-resources-plugin:2.6:testResources @ client-svc-with-quarkus
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\src\test\resources
[INFO] Invoking io.quarkus.platform:quarkus-maven-plugin:2.16.3.Final:generate-code-tests @ client-svc-with-quarkus
[INFO] Invoking org.apache.maven.plugins:maven-compiler-plugin:3.10.1:testCompile @ client-svc-with-quarkus
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 2 source files to D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\target\test-classes
Listening for transport dt_socket at address: 5005
__  ____  __  _____   ___  __ ____  ______
 --/ __ \/ / / / _ | / _ \/ //_/ / / / __/
 -/ /_/ / /_/ / __ |/ , _/ ,< / /_/ /\ \
--\___\_\____/_/ |_/_/|_/_/|_|\____/___/
2023-03-05 22:27:11,107 INFO  [io.quarkus] (Quarkus Main Thread) client-svc-with-quarkus 1.0.0-SNAPSHOT on JVM (powered by Quarkus 2.16.3.Final) started in 2.063s. Listening on: http://localhost:8080

2023-03-05 22:27:11,119 INFO  [io.quarkus] (Quarkus Main Thread) Profile dev activated. Live Coding activated.
2023-03-05 22:27:11,124 INFO  [io.quarkus] (Quarkus Main Thread) Installed features: [cdi, jdbc-h2, resteasy-reactive, smallrye-context-propagation, vertx]

--
Tests paused
Press [r] to resume testing, [o] Toggle test output, [:] for the terminal, [h] for more options>
```


## Build native-image

