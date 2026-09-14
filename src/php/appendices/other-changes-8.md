---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration82.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration82/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: b1116af46
order: 970
---

## Otros cambios

## Cambios en el núcleo

El tipo `iterable` ahora es un alias integrado en la compilación para el tipo `arrayTraversable`. Los mensajes de error relativos a `iterable` usarán por lo tanto `array|Traversable`. La reflexión sobre el tipo se preserva para los simples `iterable` (y `?iterable`) para producir una clase `ReflectionNamedType` con el nombre `iterable`, sin embargo, el uso de `iterable` en los tipos de unión se convertirá en `array|Traversable`.

El formato de fecha de las cookies enviadas ahora es `'D, d M Y H:i:s \G\M\T'`; anteriormente, era `'D, d-M-Y H:i:s T'`.

## Cambios en los módulos SAPI

### CLI

Los flujos STDOUT, STDERR y STDIN ya no se cierran al destruir los recursos, lo que generalmente ocurre cuando el CLI termina. Sin embargo, aún es posible cerrar explícitamente estos flujos usando `fclose` y similares.

## Funciones modificadas

### Núcleo

Las funciones `strcmp`, `strcasecmp`, `strncmp`, `strncasecmp` y `substr_compare`, utilizando la comparación de cadenas binarias seguras, ya no garantizan devolver `strlen($string1) - strlen($string2)` cuando las longitudes de las cadenas no son iguales, pero ahora pueden devolver `-1` o `1` en su lugar. En lugar de depender de un valor concreto, el valor de retorno debe compararse con `0`.

### DBA

`dba_open` y `dba_popen` ahora tienen la firma reforzada siguiente:

```php
dba_open(string $path, string $mode, [string $handler], [int $permission], [int $map_size], [int $flags]): resource
```php

El argumento opcional skip de `dba_fetch` ahora está al final de acuerdo con la semántica de PHP. Su firma es ahora:

```php
dba_fetch(string $key, resource $handle, int $skip): string
```

La firma sobrecargada:

```php
dba_fetch(string $key, int $skip, resource $handle): string
```php

sigue siendo aceptada, pero se recomienda usar la nueva variante estándar.

### Random

`random_bytes` y `random_int` ahora lanzan `\Random\RandomException` en caso de fallo del CSPRNG. Anteriormente, se lanzaba una simple `\Exception` en su lugar.

### SPL

El parámetro `iterator` de `iterator_to_array` y `iterator_count` se ha extendido a `iterable` en lugar de `Iterator`, lo que permite pasar arrays.

## Otros cambios en las extensiones

### Fecha

Las propiedades de `DatePeriod` ahora están correctamente declaradas.

### Intl

Las instancias de `IntlBreakIterator`, `IntlRuleBasedBreakIterator`, `IntlCodePointBreakIterator`, `IntlPartsIterator`, `IntlCalendar`, `Collator`, `IntlIterator`, `UConverter`, `IntlDateFormatter`, `IntlDatePatternGenerator`, `MessageFormatter`, `ResourceBundle`, `Spoofchecker`, `IntlTimeZone`, y `Transliterator` ya no son serializables. Anteriormente, podían ser serializadas, pero la deserialización producía objetos inutilizables o fallaba.

### MySQLi

Se ha eliminado el soporte de libmysql y ya no es posible compilar mysqli con libmysql. A partir de ahora, la extensión mysqli solo puede ser compilada con mysqlnd. Todas las funcionalidades de libmysql no disponibles en mysqlnd han sido eliminadas: La propiedad reconnect de `mysqli_driver`, La directiva INI [mysqli.reconnect](#ini.mysqli.reconnect), La constante `MYSQLI_IS_MARIADB` está obsoleta

### OCI8

La versión mínima requerida de la biblioteca Oracle Client ahora es 11.2.

### PCRE

Los caracteres NUL (`\0`) en las cadenas de patrones ahora son soportados.

### Sesión

Intentar modificar el [session.cookie_samesite](#ini.session.cookie-samesite) mientras la sesión está activa o después de que la salida haya sido enviada ahora fallará y emitirá una advertencia. El comportamiento ahora está alineado para todos los otros parámetros INI de sesión.

### SQLite3

[sqlite3.defensive](#ini.sqlite3.defensive) ahora es `INI_USER`.

### Estándar

`getimagesize` ahora informa las dimensiones reales de la imagen, bits y canales de las imágenes AVIF. Anteriormente, las dimensiones se informaban como 0x0, y los bits y canales no se informaban en absoluto.

### Tidy

Las propiedades de la clase `tidy` ahora están correctamente declaradas. Y las de la clase `tidyNode` ahora están correctamente declaradas como de solo lectura.

### Zip

La extensión Zip se ha actualizado a la versión 1.20.0, que añade los siguientes métodos: ZipArchive::clearError, ZipArchive::getStreamName, ZipArchive::getStreamIndex

## Cambios en la gestión de los archivos INI

Se ha añadido soporte para prefijos binarios (`0b`/`0B`) y octales (`0o`/`0O`) a los parámetros INI para números enteros. Los parámetros INI enteros que comienzan con un cero (`0`) siguen interpretándose como números enteros octales.

El análisis de ciertos valores mal formados ahora desencadena una advertencia, mientras que antes se ignoraba silenciosamente. Por razones de compatibilidad ascendente, la interpretación de estos valores no ha cambiado. Esto afecta a los siguientes parámetros: [bcmath.scale](#ini.bcmath.scale), [com.code_page](#ini.com.code-page), [default_socket_timeout](#ini.default-socket-timeout), [fiber.stack_size](#ini.fiber.stack-size), [hard_timeout](#ini.hard-timeout), [intl.error_level](#ini.intl.error-level), [ldap.max_links](#ini.ldap.max_links), [max_input_nesting_level](#ini.max-input-nesting-level), [max_input_vars](#ini.max-input-vars), [mbstring.regex_retry_limit](#ini.mbstring.regex-retry-limit), [mbstring.regex_stack_limit](#ini.mbstring.regex-stack-limit), [mysqli.allow_local_infile](#ini.mysqli.allow-local-infile), [mysqli.allow_persistent](#ini.mysqli.allow-persistent), [mysqli.default_port](#ini.mysqli.default-port), [mysqli.max_links](#ini.mysqli.max-links), [mysqli.max_persistent](#ini.mysqli.max-persistent), [mysqli.rollback_on_cached_plink](#ini.mysqli.rollback-on-cached-plink), [mysqlnd.log_mask](#ini.mysqlnd.log-mask), [mysqlnd.mempool_default_size](#ini.mysqlnd.mempool-default-size), [mysqlnd.net_read_buffer_size](#ini.mysqlnd.net-read-buffer-size), [mysqlnd.net_read_timeout](#ini.mysqlnd.net-read-timeout), [oci8.default_prefetch](#ini.oci8.default-prefetch), [oci8.max_persistent](#ini.oci8.max-persistent), [oci8.persistent_timeout](#ini.oci8.persistent-timeout), [oci8.ping_interval](#ini.oci8.ping-interval), [oci8.prefetch_lob_size](#ini.oci8.prefetch-lob-size), [oci8.privileged_connect](#ini.oci8.privileged-connect), [oci8.statement_cache_size](#ini.oci8.statement-cache-size), [odbc.allow_persistent](#ini.uodbc.allow-persistent), [odbc.check_persistent](#ini.uodbc.check-persistent), [odbc.max_persistent](#ini.uodbc.max-persistent), [odbc.max_links](#ini.uodbc.max-links), [odbc.defaultbinmode](#ini.uodbc.defaultbinmode), [odbc.default_cursortype](#ini.uodbc.defaultcursortype), [odbc.defaultlrl](#ini.uodbc.defaultlrl), [opcache.consistency_checks](#ini.opcache.consistency-checks), [opcache.file_update_protection](#ini.opcache.file_update_protection), [opcache.force_restart_timeout](#ini.opcache.force-restart-timeout), [opcache.interned_strings_buffer](#ini.opcache.interned-strings-buffer), [opcache.jit_bisect_limit](#ini.opcache.jit-bisect-limit), [opcache.jit_blacklist_root_trace](#ini.opcache.jit-blacklist-root-trace), [opcache.jit_blacklist_side_trace](#ini.opcache.jit-blacklist-side-trace), [opcache.jit_debug](#ini.opcache.jit-debug), [opcache.jit_hot_func](#ini.opcache.jit-hot-func), [opcache.jit_hot_loop](#ini.opcache.jit-hot-loop), [opcache.jit_hot_return](#ini.opcache.jit-hot-return), [opcache.jit_hot_side_exit](#ini.opcache.jit-hot-side-exit), [opcache.jit_max_exit_counters](#ini.opcache.jit-max-exit-counters), [opcache.jit_max_loop_unrolls](#ini.opcache.jit-max-loop-unrolls), [opcache.jit_max_polymorphic_calls](#ini.opcache.jit-max-polymorphic-calls), [opcache.jit_max_recursive_calls](#ini.opcache.jit-max-recursive-calls), [opcache.jit_max_recursive_returns](#ini.opcache.jit-max-recursive-return), [opcache.jit_max_root_traces](#ini.opcache.jit-max-root-traces), [opcache.jit_max_side_traces](#ini.opcache.jit-max-side-traces), [opcache.log_verbosity_level](#ini.opcache.log-verbosity-level), [opcache.max_file_size](#ini.opcache.max-file-size), [opcache.opt_debug_level](#ini.opcache.opt_debug_level), [opcache.optimization_level](#ini.opcache.optimization-level), [opcache.revalidate_freq](#ini.opcache.revalidate-freq), [output_buffering](#ini.output-buffering), [pcre.backtrack_limit](#ini.pcre.backtrack-limit), [pcre.recursion_limit](#ini.pcre.recursion-limit), [pgsql.max_links](#ini.pgsql.max-links), [pgsql.max_persistent](#ini.pgsql.max-persistent), [post_max_size](#ini.post-max-size), [realpath_cache_size](#ini.realpath-cache-size), [realpath_cache_ttl](#ini.realpath-cache-ttl), [session.cache_expire](#ini.session.cache-expire), [session.cookie_lifetime](#ini.session.cookie-lifetime), [session.gc_divisor](#ini.session.gc-divisor), [session.gc_maxlifetime](#ini.session.gc-maxlifetime), [session.gc_probability](#ini.session.gc-probability), [soap.wsdl_cache_limit](#ini.soap.wsdl-cache-limit), [soap.wsdl_cache_ttl](#ini.soap.wsdl-cache-ttl), [unserialize_max_depth](#ini.unserialize-max-depth), [upload_max_filesize](#ini.upload-max-filesize), [user_ini.cache_ttl](#ini.user-ini.cache-ttl), [xmlrpc_error_number](#ini.xmlrpc-error-number), [zend.assertions](#ini.zend.assertions), [zlib.output_compression_level](#ini.zlib.output-compression-level)
