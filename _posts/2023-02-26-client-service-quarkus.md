---
layout: post
title: "Quarkus 实践"
tagline: "Quarkus"
---

使用 Quarkus 编写 client-service。


## 创建空项目
使用 initializer
https://code.quarkus.io/?a=client-service-with-quarkus&e=resteasy-reactive&e=jdbc-h2

## 运行项目
```shell
D:\SDisk\workspace\Java\client-service-with-quarkus>quarkus dev
[INFO] Scanning for projects...
[INFO]
[INFO] ----------------< org.acme:client-service-with-quarkus >----------------
[INFO] Building client-service-with-quarkus 1.0.0-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- quarkus-maven-plugin:2.16.3.Final:dev (default-cli) @ client-service-with-quarkus ---
[INFO] Invoking org.apache.maven.plugins:maven-resources-plugin:2.6:resources @ client-service-with-quarkus
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] Copying 2 resources
[INFO] Invoking io.quarkus.platform:quarkus-maven-plugin:2.16.3.Final:generate-code @ client-service-with-quarkus
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-jdbc-h2-deployment/2.9.2.Final/quarkus-jdbc-h2-deployment-2.9.2.Final.pom
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-jdbc-h2-deployment/2.9.2.Final/quarkus-jdbc-h2-deployment-2.9.2.Final.pom (1.9 kB at 3.0 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-deployment-spi/2.16.3.Final/quarkus-datasource-deployment-spi-2.16.3.Final.pom
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-deployment-spi/2.16.3.Final/quarkus-datasource-deployment-spi-2.16.3.Final.pom (1.1 kB at 3.9 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-parent/2.16.3.Final/quarkus-datasource-parent-2.16.3.Final.pom
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-parent/2.16.3.Final/quarkus-datasource-parent-2.16.3.Final.pom (820 B at 2.8 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-common/2.16.3.Final/quarkus-datasource-common-2.16.3.Final.pom
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-common/2.16.3.Final/quarkus-datasource-common-2.16.3.Final.pom (987 B at 2.7 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-devservices-h2/2.16.3.Final/quarkus-devservices-h2-2.16.3.Final.pom
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-devservices-h2/2.16.3.Final/quarkus-devservices-h2-2.16.3.Final.pom (1.9 kB at 6.7 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-devservices-parent/2.16.3.Final/quarkus-devservices-parent-2.16.3.Final.pom
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-devservices-parent/2.16.3.Final/quarkus-devservices-parent-2.16.3.Final.pom (1.2 kB at 4.5 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-agroal-spi/2.16.3.Final/quarkus-agroal-spi-2.16.3.Final.pom
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-agroal-spi/2.16.3.Final/quarkus-agroal-spi-2.16.3.Final.pom (1.1 kB at 3.8 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-agroal-parent/2.16.3.Final/quarkus-agroal-parent-2.16.3.Final.pom
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-agroal-parent/2.16.3.Final/quarkus-agroal-parent-2.16.3.Final.pom (769 B at 2.0 kB/s)
[WARNING] The POM for io.quarkus:quarkus-jdbc-h2:jar:2.16.3.Final is missing, no dependency information available
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-common/2.16.3.Final/quarkus-datasource-common-2.16.3.Final.jar
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-common/2.16.3.Final/quarkus-datasource-common-2.16.3.Final.jar (7.0 kB at 22 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-deployment-spi/2.16.3.Final/quarkus-datasource-deployment-spi-2.16.3.Final.jar
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-datasource-deployment-spi/2.16.3.Final/quarkus-datasource-deployment-spi-2.16.3.Final.jar (17 kB at 44 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-devservices-h2/2.16.3.Final/quarkus-devservices-h2-2.16.3.Final.jar
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-devservices-h2/2.16.3.Final/quarkus-devservices-h2-2.16.3.Final.jar (8.3 kB at 27 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-agroal-spi/2.16.3.Final/quarkus-agroal-spi-2.16.3.Final.jar
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-agroal-spi/2.16.3.Final/quarkus-agroal-spi-2.16.3.Final.jar (5.2 kB at 18 kB/s)
Downloading from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-jdbc-h2-deployment/2.9.2.Final/quarkus-jdbc-h2-deployment-2.9.2.Final.jar
Downloaded from alimaven: http://maven.aliyun.com/nexus/content/repositories/central/io/quarkus/quarkus-jdbc-h2-deployment/2.9.2.Final/quarkus-jdbc-h2-deployment-2.9.2.Final.jar (5.6 kB at 13 kB/s)
[INFO] Invoking org.apache.maven.plugins:maven-compiler-plugin:3.10.1:compile @ client-service-with-quarkus
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 1 source file to D:\SDisk\workspace\Java\client-service-with-quarkus\target\classes
[INFO] Invoking org.apache.maven.plugins:maven-resources-plugin:2.6:testResources @ client-service-with-quarkus
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory D:\SDisk\workspace\Java\client-service-with-quarkus\src\test\resources
[INFO] Invoking io.quarkus.platform:quarkus-maven-plugin:2.16.3.Final:generate-code-tests @ client-service-with-quarkus
[INFO] Invoking org.apache.maven.plugins:maven-compiler-plugin:3.10.1:testCompile @ client-service-with-quarkus
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 2 source files to D:\SDisk\workspace\Java\client-service-with-quarkus\target\test-classes
Listening for transport dt_socket at address: 5005
__  ____  __  _____   ___  __ ____  ______
 --/ __ \/ / / / _ | / _ \/ //_/ / / / __/
 -/ /_/ / /_/ / __ |/ , _/ ,< / /_/ /\ \
--\___\_\____/_/ |_/_/|_/_/|_|\____/___/
2023-02-26 11:31:25,369 INFO  [io.quarkus] (Quarkus Main Thread) client-service-with-quarkus 1.0.0-SNAPSHOT on JVM (powered by Quarkus 2.16.3.Final) started in 1.794s. Listening on: http://localhost:8080

2023-02-26 11:31:25,384 INFO  [io.quarkus] (Quarkus Main Thread) Profile dev activated. Live Coding activated.
2023-02-26 11:31:25,385 INFO  [io.quarkus] (Quarkus Main Thread) Installed features: [cdi, jdbc-h2, resteasy-reactive, smallrye-context-propagation, vertx]




--
Tests paused
Press [r] to resume testing, [o] Toggle test output, [:] for the terminal, [h] for more options>
```