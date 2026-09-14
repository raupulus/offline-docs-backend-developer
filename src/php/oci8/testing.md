---
title: Pruebas
source_url: https://www.php.net/manual/es/oci8.test.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/testing.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: f4c44b869
order: 58550
---

## Pruebas

El conjunto de pruebas de OCI8 está en el directorio `ext/oci8/tests`. Después de ejecutar las pruebas de OCI8, este directorio también contendrá los registros de cualquier fallo.

Antes de ejecutar las pruebas de PHP, edite `details.inc` y establezca \$user, \$password y la cadena de conexión \$dbase. El conjunto de pruebas de OCI8 ha sido desarrollado usando la cuenta `SYSTEM`. Algunas pruebas fallarán si el usuario de las mismas no tiene permisos equivalentes.

Si se está comprobando Oracle Database Resident Connection Pooling, establezca \$test_drcp a `true` y asegúrese de que la cadena de conexión utiliza un servidor de la agrupación DRCP apropiado.

Una alternativa a editar `details.inc` es el establecimiento de variables de entorno, por ejemplo:

        $ export PHP_OCI8_TEST_USER=system
        $ export PHP_OCI8_TEST_PASS=oracle
        $ export PHP_OCI8_TEST_DB=localhost/XE
        $ export PHP_OCI8_TEST_DRCP=FALSE

       

Observe que en algunas shell, estas variables no se propagan correctamente por proceso de PHP y que las pruebas fallarán al conectar si se utiliza este método.

Lo siguiente es establecer cualquier entorno necesario para la base de datos de Oracle. Con Oracle 10*g*R2 XE, haga lo siguiente:

        $ . /usr/lib/oracle/xe/app/oracle/product/10.2.0/server/bin/oracle_env.sh

       

Con Oracle 11*g*R2 XE:

        $ . /u01/app/oracle/product/11.2.0/xe/bin/oracle_env.sh

       

Para otras versiones de la base de datos de Oracle, haga:

        $ . /usr/local/bin/oraenv

       

Algunas shells requieren que `php.ini` contenga `E` en el parámetro variables_order, por ejemplo:

        variables_order = "EGPCS"

       

Ejecute todas las pruebas de PHP con:

        $ cd your_php_src_directory
        $ make test

       

o ejecute únicamente las pruebas de OCI8 con

        $ cd your_php_src_directory
        $ make test TESTS=ext/oci8

       

Cuando hayan finalizado las pruebas, revise cualquier fallo. En sistemas lentos, algunas pruebas podrían tomar más tiempo que el tiempo de espera de prueba predeterminado de `run-tests.php`. Para corregir esto, establezca la variable de entorno `TEST_TIMEOUT` a un número mayor de segundos.

En máquinas rápidas con una base de datos local configurada para una carga ligera (p.ej. Oracle 11*g*R2 XE), algunas pruebas podrían ocasionar los errores ORA-12516 u ORA-12520. Para evitarlo, aumente el parámetro `PROCESSES` de la base de datos siguiendo estos pasos:

Conéctese como propietario del software de Oracle:

        $ su - oracle

       

Establezca el entorno de Oracle necesario con `oracle_env.sh` u `oraenv`, tal como está descrito arriba.

Inicie la herramienta de línea de comandos SQL\*Plus y aumente `PROCESSES`

        $ sqlplus / as sysdba
        SQL> alter system set processes=100 scope=spfile

       

Reinicie la base de datos:

        SQL> startup force
