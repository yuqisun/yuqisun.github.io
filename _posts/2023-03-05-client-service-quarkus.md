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

## Update properties
```properties
quarkus.http.port=5888
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
[INFO] Invoking org.apache.maven.plugins:maven-compiler-plugin:3.10.1:compile @ client-svc-with-quarkus
[INFO] Nothing to compile - all classes are up to date
[INFO] Invoking org.apache.maven.plugins:maven-resources-plugin:2.6:testResources @ client-svc-with-quarkus
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\src\test\resources
[INFO] Invoking io.quarkus.platform:quarkus-maven-plugin:2.16.3.Final:generate-code-tests @ client-svc-with-quarkus
[INFO] Invoking org.apache.maven.plugins:maven-compiler-plugin:3.10.1:testCompile @ client-svc-with-quarkus
[INFO] Nothing to compile - all classes are up to date
Listening for transport dt_socket at address: 5005
2023-03-05 23:13:41,365 WARN  [io.qua.hib.orm.dep.HibernateOrmProcessor] (build-2) Hibernate ORM is disabled because no JPA entities were found
__  ____  __  _____   ___  __ ____  ______
 --/ __ \/ / / / _ | / _ \/ //_/ / / / __/
 -/ /_/ / /_/ / __ |/ , _/ ,< / /_/ /\ \
--\___\_\____/_/ |_/_/|_/_/|_|\____/___/
2023-03-05 23:13:42,560 INFO  [io.quarkus] (Quarkus Main Thread) client-svc-with-quarkus 1.0.0-SNAPSHOT on JVM (powered by Quarkus 2.16.3.Final) started in 1.987s. Listening on: http://localhost:5888

2023-03-05 23:13:42,563 INFO  [io.quarkus] (Quarkus Main Thread) Profile dev activated. Live Coding activated.
2023-03-05 23:13:42,567 INFO  [io.quarkus] (Quarkus Main Thread) Installed features: [agroal, cdi, hibernate-orm, jdbc-h2, narayana-jta, resteasy-reactive, smallrye-context-propagation, vertx]

--
Tests paused
Press [r] to resume testing, [o] Toggle test output, [:] for the terminal, [h] for more options>
```


## Build native-image (22 seconds)
open x64 Native Tools Command Prompt
```shell
D:\SDisk\workspace\Java\demo\client-svc-with-quarkus>mvnw package -Pnative
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------< org.acme:client-svc-with-quarkus >------------------
[INFO] Building client-svc-with-quarkus 1.0.0-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- maven-resources-plugin:2.6:resources (default-resources) @ client-svc-with-quarkus ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] Copying 2 resources
[INFO]
[INFO] --- quarkus-maven-plugin:2.16.3.Final:generate-code (default) @ client-svc-with-quarkus ---
[INFO]
[INFO] --- maven-compiler-plugin:3.10.1:compile (default-compile) @ client-svc-with-quarkus ---
[INFO] Nothing to compile - all classes are up to date
[INFO]
[INFO] --- quarkus-maven-plugin:2.16.3.Final:generate-code-tests (default) @ client-svc-with-quarkus ---
[INFO]
[INFO] --- maven-resources-plugin:2.6:testResources (default-testResources) @ client-svc-with-quarkus ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\src\test\resources
[INFO]
[INFO] --- maven-compiler-plugin:3.10.1:testCompile (default-testCompile) @ client-svc-with-quarkus ---
[INFO] Nothing to compile - all classes are up to date
[INFO]
[INFO] --- maven-surefire-plugin:3.0.0-M7:test (default-test) @ client-svc-with-quarkus ---
[INFO] Using auto detected provider org.apache.maven.surefire.junitplatform.JUnitPlatformProvider
[INFO]
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running org.acme.GreetingResourceTest
2023-03-05 23:14:29,607 WARN  [io.qua.hib.orm.dep.HibernateOrmProcessor] (build-9) Hibernate ORM is disabled because no JPA entities were found
2023-03-05 23:14:30,453 INFO  [io.quarkus] (main) client-svc-with-quarkus 1.0.0-SNAPSHOT on JVM (powered by Quarkus 2.16.3.Final) started in 1.591s. Listening on: http://localhost:8081
2023-03-05 23:14:30,454 INFO  [io.quarkus] (main) Profile test activated.
2023-03-05 23:14:30,454 INFO  [io.quarkus] (main) Installed features: [agroal, cdi, hibernate-orm, jdbc-h2, narayana-jta, resteasy-reactive, smallrye-context-propagation, vertx]
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 2.985 s - in org.acme.GreetingResourceTest
2023-03-05 23:14:31,330 INFO  [io.quarkus] (main) client-svc-with-quarkus stopped in 0.020s
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
[INFO]
[INFO]
[INFO] --- maven-jar-plugin:2.4:jar (default-jar) @ client-svc-with-quarkus ---
[INFO] Building jar: D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\target\client-svc-with-quarkus-1.0.0-SNAPSHOT.jar
[INFO]
[INFO] --- quarkus-maven-plugin:2.16.3.Final:build (default) @ client-svc-with-quarkus ---
[WARNING] [io.quarkus.hibernate.orm.deployment.HibernateOrmProcessor] Hibernate ORM is disabled because no JPA entities were found
[INFO] [org.hibernate.Version] HHH000412: Hibernate ORM core version 5.6.15.Final
[INFO] [io.quarkus.deployment.pkg.steps.JarResultBuildStep] Building native image source jar: D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\target\client-svc-with-quarkus-1.0.0-SNAPSHOT-native-image-source-jar\client-svc-with-quarkus-1.0.0-SNAPSHOT-runner.jar
[INFO] [io.quarkus.deployment.pkg.steps.NativeImageBuildStep] Building native image from D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\target\client-svc-with-quarkus-1.0.0-SNAPSHOT-native-image-source-jar\client-svc-with-quarkus-1.0.0-SNAPSHOT-runner.jar
[INFO] [io.quarkus.deployment.pkg.steps.NativeImageBuildStep] Running Quarkus native-image plugin on GraalVM 22.3.1 Java 17 CE (Java Version 17.0.6+10-jvmci-22.3-b13)
[INFO] [io.quarkus.deployment.pkg.steps.NativeImageBuildRunner] D:\SDisk\app\graalvm-ce-java17-22.3.1\bin\native-image.cmd -J-Djava.util.logging.manager=org.jboss.logmanager.LogManager -J-Dsun.nio.ch.maxUpdateArraySize=100 -J-DCoordinatorEnvironmentBean.transactionStatusManagerEnable=false -J-Dlogging.initial-configurator.min-level=500 -J-Dvertx.logger-delegate-factory-class-name=io.quarkus.vertx.core.runtime.VertxLogDelegateFactory -J-Dvertx.disableDnsResolver=true -J-Dio.netty.noUnsafe=true -J-Dio.netty.leakDetection.level=DISABLED -J-Dio.netty.allocator.maxOrder=3 -J-Duser.language=en -J-Duser.country=US -J-Dfile.encoding=UTF-8 --features=org.hibernate.graalvm.internal.QueryParsingSupport,io.quarkus.runner.Feature,io.quarkus.jdbc.h2.runtime.H2Reflections,org.hibernate.graalvm.internal.GraalVMStaticFeature,io.quarkus.runtime.graal.ResourcesFeature,io.quarkus.hibernate.orm.runtime.graal.DisableLoggingFeature,io.quarkus.caffeine.runtime.graal.CacheConstructorsFeature,io.quarkus.runtime.graal.DisableLoggingFeature -J--add-exports=java.security.jgss/sun.security.krb5=ALL-UNNAMED -J--add-opens=java.base/java.text=ALL-UNNAMED -J--add-opens=java.base/java.io=ALL-UNNAMED -J--add-opens=java.base/java.lang.invoke=ALL-UNNAMED -J--add-opens=java.base/java.util=ALL-UNNAMED -H:+CollectImageBuildStatistics -H:ImageBuildStatisticsFile=client-svc-with-quarkus-1.0.0-SNAPSHOT-runner-timing-stats.json -H:BuildOutputJSONFile=client-svc-with-quarkus-1.0.0-SNAPSHOT-runner-build-output-stats.json -H:+AllowFoldMethods -J-Djava.awt.headless=true --no-fallback --link-at-build-time -H:+ReportExceptionStackTraces -H:-AddAllCharsets --enable-url-protocols=http,https -H:-UseServiceLoaderFeature -H:+StackTrace -J--add-exports=org.graalvm.sdk/org.graalvm.nativeimage.impl=ALL-UNNAMED -J--add-exports=org.graalvm.nativeimage.builder/com.oracle.svm.core.jdk=ALL-UNNAMED --add-modules=jdk.net --exclude-config io\.netty\.netty-codec /META-INF/native-image/io\.netty/netty-codec/generated/handlers/reflect-config\.json --exclude-config io\.netty\.netty-handler /META-INF/native-image/io\.netty/netty-handler/generated/handlers/reflect-config\.json client-svc-with-quarkus-1.0.0-SNAPSHOT-runner -jar client-svc-with-quarkus-1.0.0-SNAPSHOT-runner.jar
========================================================================================================================
GraalVM Native Image: Generating 'client-svc-with-quarkus-1.0.0-SNAPSHOT-runner' (executable)...
========================================================================================================================
[1/7] Initializing...                                                                                    (9.0s @ 0.41GB)
 Version info: 'GraalVM 22.3.1 Java 17 CE'
 Java version info: '17.0.6+10-jvmci-22.3-b13'
 C compiler: cl.exe (microsoft, x64, 19.16.27049)
 Garbage collector: Serial GC
 8 user-specific feature(s)
 - io.quarkus.caffeine.runtime.graal.CacheConstructorsFeature
 - io.quarkus.hibernate.orm.runtime.graal.DisableLoggingFeature: Disables INFO logging during the analysis phase for the [org.hibernate.Version, org.hibernate.annotations.common.Version, org.hibernate.dialect.Dialect] categories
 - io.quarkus.jdbc.h2.runtime.H2Reflections: Support for H2 Database's extended data types
 - io.quarkus.runner.Feature: Auto-generated class by Quarkus from the existing extensions
 - io.quarkus.runtime.graal.DisableLoggingFeature: Disables INFO logging during the analysis phase for the [org.jboss.threads] categories
 - io.quarkus.runtime.graal.ResourcesFeature: Register each line in META-INF/quarkus-native-resources.txt as a resource on Substrate VM
 - org.hibernate.graalvm.internal.GraalVMStaticFeature: Hibernate ORM's static reflection registrations for GraalVM
 - org.hibernate.graalvm.internal.QueryParsingSupport: Hibernate ORM's support for HQL Parser in GraalVM
[2/7] Performing analysis...  [*********]                                                               (33.7s @ 4.15GB)
  13,550 (88.06%) of 15,388 classes reachable
  22,049 (61.91%) of 35,615 fields reachable
  71,628 (55.72%) of 128,559 methods reachable
     624 classes,   130 fields, and 2,602 methods registered for reflection
      83 classes,    78 fields, and    68 methods registered for JNI access
       5 native libraries: crypt32, ncrypt, psapi, version, winhttp
[3/7] Building universe...                                                                               (4.1s @ 3.09GB)
[4/7] Parsing methods...      [**]                                                                       (2.9s @ 3.40GB)
[5/7] Inlining methods...     [***]                                                                      (1.7s @ 1.51GB)
[6/7] Compiling methods...    [*****]                                                                   (22.8s @ 3.57GB)
[7/7] Creating image...                                                                                  (3.8s @ 1.59GB)
  29.54MB (50.74%) for code area:    46,141 compilation units
  28.22MB (48.47%) for image heap:  332,546 objects and 188 resources
 471.42KB ( 0.79%) for other data
  58.22MB in total
------------------------------------------------------------------------------------------------------------------------
Top 10 packages in code area:                               Top 10 object types in image heap:
   1.65MB sun.security.ssl                                     6.56MB byte[] for code metadata
   1.04MB java.util                                            3.29MB java.lang.Class
 760.25KB java.lang.invoke                                     3.18MB java.lang.String
 730.10KB com.sun.crypto.provider                              2.78MB byte[] for general heap data
 595.06KB org.h2.table                                         2.47MB byte[] for java.lang.String
 573.28KB org.h2.command                                       1.21MB byte[] for embedded resources
 470.06KB c.s.org.apache.xerces.internal.impl.xs.traversers    1.14MB com.oracle.svm.core.hub.DynamicHubCompanion
 464.76KB java.lang                                          723.34KB byte[] for reflection metadata
 453.83KB sun.security.x509                                  719.63KB java.util.HashMap$Node
 450.91KB io.netty.buffer                                    650.27KB java.lang.String[]
  22.11MB for 561 more packages                                5.43MB for 2998 more object types
------------------------------------------------------------------------------------------------------------------------
                        3.4s (4.1% of total time) in 37 GCs | Peak RSS: 6.41GB | CPU load: 4.51
------------------------------------------------------------------------------------------------------------------------
Produced artifacts:
 D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\target\client-svc-with-quarkus-1.0.0-SNAPSHOT-native-image-source-jar\client-svc-with-quarkus-1.0.0-SNAPSHOT-runner-build-output-stats.json (json)
 D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\target\client-svc-with-quarkus-1.0.0-SNAPSHOT-native-image-source-jar\client-svc-with-quarkus-1.0.0-SNAPSHOT-runner-timing-stats.json (raw)
 D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\target\client-svc-with-quarkus-1.0.0-SNAPSHOT-native-image-source-jar\client-svc-with-quarkus-1.0.0-SNAPSHOT-runner.build_artifacts.txt (txt)
 D:\SDisk\workspace\Java\demo\client-svc-with-quarkus\target\client-svc-with-quarkus-1.0.0-SNAPSHOT-native-image-source-jar\client-svc-with-quarkus-1.0.0-SNAPSHOT-runner.exe (executable)
========================================================================================================================
Finished generating 'client-svc-with-quarkus-1.0.0-SNAPSHOT-runner' in 1m 22s.
[INFO] [io.quarkus.deployment.QuarkusAugmentor] Quarkus augmentation completed in 86601ms
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  01:33 min
[INFO] Finished at: 2023-03-05T23:15:58+08:00
[INFO] ------------------------------------------------------------------------
```


## 运行 runner (started in 0.046s)
```shell
D:\SDisk\workspace\Java\demo\client-svc-with-quarkus>target\client-svc-with-quarkus-1.0.0-SNAPSHOT-runner.exe
__  ____  __  _____   ___  __ ____  ______
 --/ __ \/ / / / _ | / _ \/ //_/ / / / __/
 -/ /_/ / /_/ / __ |/ , _/ ,< / /_/ /\ \
--\___\_\____/_/ |_/_/|_/_/|_|\____/___/
2023-03-05 23:16:38,266 INFO  [io.net.uti.int.PlatformDependent] (Thread-10) Your platform does not provide complete low-level API for accessing direct buffers reliably. Unless explicitly requested, heap buffer will always be preferred to avoid potential system instability.
2023-03-05 23:16:38,278 INFO  [io.quarkus] (main) client-svc-with-quarkus 1.0.0-SNAPSHOT native (powered by Quarkus 2.16.3.Final) started in 0.046s. Listening on: http://0.0.0.0:5888
2023-03-05 23:16:38,278 INFO  [io.quarkus] (main) Profile prod activated.
2023-03-05 23:16:38,280 INFO  [io.quarkus] (main) Installed features: [agroal, cdi, hibernate-orm, jdbc-h2, narayana-jta, resteasy-reactive, smallrye-context-propagation, vertx]
```

## Stop service 
```shell
2023-03-05 23:22:46,386 INFO  [io.quarkus] (Shutdown thread) client-svc-with-quarkus stopped in 0.002s
```

