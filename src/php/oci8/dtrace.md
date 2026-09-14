---
title: OCI8 y rastreo dinámico de DTrace
source_url: https://www.php.net/manual/es/oci8.dtrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/dtrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: f4c44b869
order: 57150
---

## OCI8 y rastreo dinámico de DTrace

OCI8 2.0 sondeos de DTrace estáticos que se pueden usar en sistemas operativos que admiten DTrace. Véase [Rastreo dinámico de DTrace](#features.dtrace) para una visión general de PHP y DTrace.

## Instalar OCI8 con soporte para DTrace

Para habilitar el soporte para DTrace en OCI8 para PHP, construya OCI8 como una extensión compartida después de establecer `PHP_DTRACE`.

    $ export PHP_DTRACE=yes
    $ pecl install oci8

Edite php.ini, establezca [extension_dir](#ini.extension-dir) al directorio con el `oci8.so` creado y también habilite la extensión añadiendo:

    extension=oci8.so

Si instala PHP OCI8 2.0 desde PECL usando `phpize` y `configure` (en lugar de `pecl`), será necesario establecer `PHP_DTRACE=yes`. Esto es así debido a que la opción `--enable-dtrace` será ignorada por el script limitado `configure` de un PECL incluido.

Véase [Instalación de extensiones PECL](#install.pecl) para las instrucciones generales de instalación de PECL.

## Sondeos estáticos de DTrace en OCI8 para PHP

| Nombre del sondeo | Descripción del sondeo | Argumentos del sondeo |
|----|----|----|
| `oci8-connect-entry` | Iniciado por oci_connect(), oci_pconnect() y oci_new_connect(). Lanzado antes de establecer una conexión con una base de datos. | char \*`username`, char \*`dbname`, char \*`charset`, long `session_mode`, int `persistent`, int `exclusive` |
| `oci8-connect-return` | Lanzado al finallde una conexión. | void \*`connection` |
| `oci8-check-connection` | Lanzado si un error de Oracle podría haber causado que la conexión sea inválida. | void \*`connection`, char \*`client_id`, int `is_open`, long `errcode`, unsigned long `server_status` |
| `oci8-sqltext` | Lanzado cuando oci_parse() se ejecuta. | void \*`connection`, char \*`client_id`, void \*`statement`, char \*`sql` |
| `oci8-connection-close` | Lanzado cuando la conexión a la base de datos está completamente destruida. | void \*`connection` |
| `oci8-error` | Lanzado si ocurre un error de Oracle. | int `status`, long `errcode` |
| `oci8-execute-mode` | Lanzado en `oci_execute` para mostrar el modo de ejecución. | void \*`connection`, char \*`client_id`, void \*`statement`, unsigned int `mode` |

Los siguientes sondeos estáticos están disponibles en OCI8 para PHP

Estos sondeos son útiles para rastrear scripts de OCI8.

`connection` y `statement` son los punteros a las estructuras internas usadas para rastrear conexiones de PHP y ejecutar sentencias.

`client_id` es el valor establecido por `oci_set_client_identifier`.

El núcleo de PHP también posee sondeos estáticos. Véase [Sondeos estáticos de DTrace en el núcleo de PHP](#features.dtrace.static-probes).

| Nombre del sondeo             |
|-------------------------------|
| `oci8-connect-expiry`         |
| `oci8-connect-lookup`         |
| `oci8-connect-p-dtor-close`   |
| `oci8-connect-p-dtor-release` |
| `oci8-connect-type`           |
| `oci8-sesspool-create`        |
| `oci8-sesspool-stats`         |
| `oci8-sesspool-type`          |

Sondeos de DTrace de depuración interna en OCI8

Estos sondeos son útiles para mantenedores de OCI8. Consulte el código fuente de OCI8 para los argumentos y para ver cuando serán lanzados.

## Enumerar los Sondeos estáticos de DTrace en OCI8 para PHP

Para enumerar los sondeos disponibles, inicie un proceso de PHP y ejecute:

    # dtrace -l

La salida será similar a:

       ID   PROVIDER            MODULE                          FUNCTION NAME
       [ . . . ]
       17 phpoci22116           oci8.so   php_oci_dtrace_check_connection oci8-check-connection
       18 phpoci22116           oci8.so                php_oci_do_connect oci8-connect-entry
       19 phpoci22116           oci8.so         php_oci_persistent_helper oci8-connect-expiry
       20 phpoci22116           oci8.so             php_oci_do_connect_ex oci8-connect-lookup
       21 phpoci22116           oci8.so  php_oci_pconnection_list_np_dtor oci8-connect-p-dtor-close
       22 phpoci22116           oci8.so  php_oci_pconnection_list_np_dtor oci8-connect-p-dtor-release
       23 phpoci22116           oci8.so                php_oci_do_connect oci8-connect-return
       24 phpoci22116           oci8.so             php_oci_do_connect_ex oci8-connect-type
       25 phpoci22116           oci8.so          php_oci_connection_close oci8-connection-close
       26 phpoci22116           oci8.so                     php_oci_error oci8-error
       27 phpoci22116           oci8.so         php_oci_statement_execute oci8-execute-mode
       28 phpoci22116           oci8.so              php_oci_create_spool oci8-sesspool-create
       29 phpoci22116           oci8.so            php_oci_create_session oci8-sesspool-stats
       30 phpoci22116           oci8.so            php_oci_create_session oci8-sesspool-type
       31 phpoci22116           oci8.so          php_oci_statement_create oci8-sqltext

Los valores de la columna "Provider" (Proveedor) consisten en `phpoci` and el ID del proceso de PHP ejecutándose actualmente.

La columna "Function" (Función) se refiere a los nombres de funciones internas de la implementación en C de PHP donde cada proveedor está ubicado.

Si un proceso de PHP no se está ejecutando, no se mostrarán sondeos de PHP.

## Ejemplo de DTrace con OCI8 para PHP

Este ejemplo muestra lo básico del lenguaje de script D de DTrace.

`user_oci8_probes.d` para rasrear todos los Sondeos estáticos de OCI8 para PHP al nivel de usuario con DTrace

    #!/usr/sbin/dtrace -Zs

    #pragma D option quiet

    php*:::oci8-connect-entry
    {
        printf("%lld: PHP connect-entry\n", walltimestamp);
        printf("  credentials=\"%s@%s\"\n", arg0 ? copyinstr(arg0) : "", arg1 ? copyinstr(arg1) : "");
        printf("  charset=\"%s\"\n", arg2 ? copyinstr(arg2) : "");
        printf("  session_mode=%ld\n", (long)arg3);
        printf("  persistent=%d\n", (int)arg4);
        printf("  exclusive=%d\n", (int)arg5);
    }

    php*:::oci8-connect-return
    {
        printf("%lld: PHP oci8-connect-return\n", walltimestamp);
        printf("  connection=0x%p\n", (void *)arg0);
    }

    php*:::oci8-connection-close
    {
        printf("%lld: PHP oci8-connect-close\n", walltimestamp);
        printf("  connection=0x%p\n", (void *)arg0);
    }

    php*:::oci8-error
    {
        printf("%lld: PHP oci8-error\n", walltimestamp);
        printf("  status=%d\n", (int)arg0);
        printf("  errcode=%ld\n", (long)arg1);
    }

    php*:::oci8-check-connection
    {
        printf("%lld: PHP oci8-check-connection\n", walltimestamp);
        printf("  connection=0x%p\n", (void *)arg0);
        printf("  client_id=\"%s\"\n", arg1 ? copyinstr(arg1) : "");
        printf("  is_open=%d\n", arg2);
        printf("  errcode=%ld\n", (long)arg3);
        printf("  server_status=%lu\n", (unsigned long)arg4);
    }

    php*:::oci8-sqltext
    {
        printf("%lld: PHP oci8-sqltext\n", walltimestamp);
        printf("  connection=0x%p\n", (void *)arg0);
        printf("  client_id=\"%s\"\n", arg1 ? copyinstr(arg1) : "");
        printf("  statement=0x%p\n", (void *)arg2);
        printf("  sql=\"%s\"\n", arg3 ? copyinstr(arg3) : "");
    }

    php*:::oci8-execute-mode
    {
        printf("%lld: PHP oci8-execute-mode\n", walltimestamp);
        printf("  connection=0x%p\n", (void *)arg0);
        printf("  client_id=\"%s\"\n", arg1 ? copyinstr(arg1) : "");
        printf("  statement=0x%p\n", (void *)arg2);
        printf("  mode=0x%x\n", arg3);
    }

Este script usa la opción `-Z` para `dtrace`, permitiéndole que sea ejecutado cuando no exista un procesode PHP en ejecución. Si esta opción fuera omitida, el script terminaría inmediatamente cuando no se ejecutara PHP porque no sabe de la existencia de sondeos a ser monitorizados.

En máquinas multi-CPU, el orden de los sondeos no parecerá ser sencuencial. Esto depende de cuál CPU estaba procesando los sondeos, y de cómo los hilos migran entre CPUs. Mostrar las marcas de tiempo de los sondeos atudará a reducir la confusión.

El script rastrea todos los sondeos estáticos de OCI8 para PHP a nivel de usuario que apuntan a lo largo de la duración de un script de PHP en ejecución. Ejecute el script D:

    # ./user_oci8_probes.d

Ejecute un script o aplicación de PHP. El script D de monitorización generará cada argumento del sondeo mientras se lanza. Por ejemplo, un sencillo script de PHP que requiere una tabla podría producir la siguiente salida de rastreo:

    1381794982092854582: PHP connect-entry
      credentials="hr@localhost/pdborcl"
      charset=""
      session_mode=0
      persistent=0
      exclusive=0
    1381794982183158766: PHP oci8-connect-return
      connection=0x7f4a7907bfb8
    1381794982183594576: PHP oci8-sqltext
      connection=0x7f4a7907bfb8
      client_id="Chris"
      statement=0x7f4a7907c2a0
      sql="select * from employees"
    1381794982183783706: PHP oci8-execute-mode
      connection=0x7f4a7907bfb8
      client_id="Chris"
      statement=0x7f4a7907c2a0
      mode=0x20
    1381794982444344390: PHP oci8-connect-close
      connection=0x7f4a7907bfb8

Cuando la monitorización está completa, el script D puede terminarse con <span class="keycombo">CTRL+C</span>.

## Véase también

Rastreo dinámico de DTrace
