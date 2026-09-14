---
title: Funcionalidades obsoletas
source_url: https://www.php.net/manual/es/migration85.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration85/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 7385bb692
order: 1200
---

## Funcionalidades obsoletas

## Núcleo de PHP

### Cambios en el controlador de salida del usuario

Intentar generar salida (p. ej., con `echo`) dentro de un controlador de salida de usuario está obsoleto. La advertencia de obsolescencia omitirá el controlador que genera la salida para garantizar su visibilidad; si existen controladores de salida anidados, se seguirá utilizando el siguiente.

### Nombres de conversiones no canónicos

Los nombres de conversiones no canónicos `(boolean)`, `(integer)`, `(double)`, y `(binary)` han quedado obsoletos, use `(bool)`, `(int)`, `(float)`, y `(string)` respectivamente.

### Finalizar las declaraciones de caso con un punto y coma

Finalizar las sentencias case con un punto y coma en lugar de dos puntos, se considera obsoleto.

### El operador de ejecución

[El operador de ejecución](#language.operators.execution) como un alias para `shell_exec` ha quedado obsoleto.

### Devolviendo null desde \_\_debugInfo()

Devolver `null` desde [\_\_debugInfo()](#language.oop5.magic.debuginfo) ha quedado obsoleto. En su lugar, devuelva un array vacío.

### Directiva INI report_memleaks

La directiva INI [report_memleaks](#ini.report-memleaks) ha quedado obsoleta.

### Redeclaración de constantes

La redeclaración de constantes está obsoleta. Tenga en cuenta que esto ya generó una advertencia y seguirá haciéndolo.

### Problemas de enlace de cierres

Los siguientes problemas de enlace de cierre, que ya emiten un `E_WARNING`, ahora están obsoletos: Enlazar una instancia a un cierre estático., Enlazar métodos a objetos que no son instancias de la clase (o subclase) en la que se define el método., Desenlazar \$this de un método., Desenlazar \$this de un cierre que utiliza \$this., Enlazar un cierre al ámbito de una clase interna., Reenlazar el ámbito de un cierre creado a partir de una función o método.

### Métodos mágicos \_\_sleep() y \_\_wakeup()

Los métodos mágicos[\_\_sleep()](#object.sleep) y [\_\_wakeup()](#object.wakeup) son ligeramente-obsoletos. En su lugar, o al mismo tiempo si se requiere compatibilidad con PHP 7, se deben usar los métodos mágicos [\_\_serialize()](#object.serialize) y [\_\_unserialize()](#object.unserialize).

### Usando null como índice de un array

El uso de `null` como índice de un array o al llamar a `array_key_exists` está obsoleto. En su lugar, debe utilizarse un string vacío.

### Incrementando strings no numéricos

El incremento de strings no numéricos está obsoleto. En su lugar, debe utilizarse la función `str_increment`.

### Directiva INI register_argc_argv

Usar `$_SERVER['argc']` y `$_SERVER['argv']` a partir del string de consulta para las SAPI que no son de línea de comandos ha quedado obsoleto. Configure `register_argc_argv=0` y utilice `$_GET` o `$_SERVER['QUERY_STRING']` para acceder a la información, tras verificar que su uso es seguro.

## cURL

La función `curl_close` ha quedado obsoleta, ya que los objetos `CurlHandle` se liberan automáticamente.

La función `curl_share_close` ha quedado obsoleta, ya que los objetos `CurlShareHandle` se liberan automáticamente.

## Fecha

Las constantes `DATE_RFC7231` y `DateTimeInterface::RFC7231` han quedado obsoletas. Esto se debe a que ignoran la zona horaria asociada y siempre utilizan GMT.

## FileInfo

La función `finfo_close` ha quedado obsoleta. Los objetos `finfo` se liberan automáticamente.

El parámetro `context` de la función `finfo_buffer` ha quedado obsoleto ya que se ignora.

## GD

La función `imagedestroy` ha quedado obsoleta, ya que los objetos `GdImage` se liberan automáticamente.

## Hash

Las constantes `MHASH_*` han quedado obsoletas.

## Intl

La configuración INI [intl.error_level](#ini.intl.error-level) ha quedado obsoleta. Se recomienda comprobar los errores manualmente o habilitar las excepciones mediante la configuración INI [intl.use_exceptions](#ini.intl.use-exceptions).

## LDAP

Se han marcado como obsoletas ciertas llamadas y constantes de Oracle Instant Client. Lista de llamadas afectadas: `ldap_connect` con soporte para billetera, `ldap_connect_wallet` Lista de constantes afectadas: `GSLC_SSL_NO_UATH`, `GSLC_SSL_ONEWAY_UATH`, `GSLC_SSL_TWOWAY_UATH`

## MySQLi

La función alias `mysqli_execute` ha quedado obsoleta. Utilice `mysqli_stmt_execute` en su lugar.

## OpenSSL

El parámetro `key_length` de `openssl_pkey_derive` ha quedado obsoleto. Esto se debe a que se ignora o trunca la clave, lo que puede suponer una vulnerabilidad de seguridad.

## PDO

El esquema DSN `"uri:"` ha quedado obsoleto debido a problemas de seguridad relacionados con los DSN procedentes de URI remotos.

Las constantes específicas del controlador en la clase PDO han quedado obsoletas. Lista de constantes afectadas y sus reemplazos: `PDO::DBLIB_ATTR_CONNECTION_TIMEOUT` =\> `Pdo\Dblib::ATTR_CONNECTION_TIMEOUT`, `PDO::DBLIB_ATTR_QUERY_TIMEOUT` =\> `Pdo\Dblib::ATTR_QUERY_TIMEOUT`, `PDO::DBLIB_ATTR_STRINGIFY_UNIQUEIDENTIFIER` =\> `Pdo\Dblib::ATTR_STRINGIFY_UNIQUEIDENTIFIER`, `PDO::DBLIB_ATTR_VERSION` =\> `Pdo\Dblib::ATTR_VERSION`, `PDO::DBLIB_ATTR_TDS_VERSION` =\> `Pdo\Dblib::ATTR_TDS_VERSION`, `PDO::DBLIB_ATTR_SKIP_EMPTY_ROWSETS` =\> `Pdo\Dblib::ATTR_SKIP_EMPTY_ROWSETS`, `PDO::DBLIB_ATTR_DATETIME_CONVERT` =\> `Pdo\Dblib::ATTR_DATETIME_CONVERT`, `PDO::FB_ATTR_DATE_FORMAT` =\> `Pdo\Firebird::ATTR_DATE_FORMAT`, `PDO::FB_ATTR_TIME_FORMAT` =\> `Pdo\Firebird::ATTR_TIME_FORMAT`, `PDO::FB_ATTR_TIMESTAMP_FORMAT` =\> `Pdo\Firebird::ATTR_TIMESTAMP_FORMAT`, `PDO::MYSQL_ATTR_USE_BUFFERED_QUERY` =\> `Pdo\Mysql::ATTR_USE_BUFFERED_QUERY`, `PDO::MYSQL_ATTR_LOCAL_INFILE` =\> `Pdo\Mysql::ATTR_LOCAL_INFILE`, `PDO::MYSQL_ATTR_LOCAL_INFILE_DIRECTORY` =\> `Pdo\Mysql::ATTR_LOCAL_INFILE_DIRECTORY`, `PDO::MYSQL_ATTR_INIT_COMMAND` =\> `Pdo\Mysql::ATTR_INIT_COMMAND`, `PDO::MYSQL_ATTR_MAX_BUFFER_SIZE` =\> `Pdo\Mysql::ATTR_MAX_BUFFER_SIZE`, `PDO::MYSQL_ATTR_READ_DEFAULT_FILE` =\> `Pdo\Mysql::ATTR_READ_DEFAULT_FILE`, `PDO::MYSQL_ATTR_READ_DEFAULT_GROUP` =\> `Pdo\Mysql::ATTR_READ_DEFAULT_GROUP`, `PDO::MYSQL_ATTR_COMPRESS` =\> `Pdo\Mysql::ATTR_COMPRESS`, `PDO::MYSQL_ATTR_DIRECT_QUERY` =\> `Pdo\Mysql::ATTR_DIRECT_QUERY`, `PDO::MYSQL_ATTR_FOUND_ROWS` =\> `Pdo\Mysql::ATTR_FOUND_ROWS`, `PDO::MYSQL_ATTR_IGNORE_SPACE` =\> `Pdo\Mysql::ATTR_IGNORE_SPACE`, `PDO::MYSQL_ATTR_SSL_KEY` =\> `Pdo\Mysql::ATTR_SSL_KEY`, `PDO::MYSQL_ATTR_SSL_CERT` =\> `Pdo\Mysql::ATTR_SSL_CERT`, `PDO::MYSQL_ATTR_SSL_CA` =\> `Pdo\Mysql::ATTR_SSL_CA`, `PDO::MYSQL_ATTR_SSL_CAPATH` =\> `Pdo\Mysql::ATTR_SSL_CAPATH`, `PDO::MYSQL_ATTR_SSL_CIPHER` =\> `Pdo\Mysql::ATTR_SSL_CIPHER`, `PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT` =\> `Pdo\Mysql::ATTR_SSL_VERIFY_SERVER_CERT`, `PDO::MYSQL_ATTR_SERVER_PUBLIC_KEY` =\> `Pdo\Mysql::ATTR_SERVER_PUBLIC_KEY`, `PDO::MYSQL_ATTR_MULTI_STATEMENTS` =\> `Pdo\Mysql::ATTR_MULTI_STATEMENTS`, `PDO::ODBC_ATTR_USE_CURSOR_LIBRARY` =\> `Pdo\Odbc::ATTR_USE_CURSOR_LIBRARY`, `PDO::ODBC_ATTR_ASSUME_UTF8` =\> `Pdo\Odbc::ATTR_ASSUME_UTF8`, `PDO::ODBC_SQL_USE_IF_NEEDED` =\> `Pdo\Odbc::SQL_USE_IF_NEEDED`, `PDO::ODBC_SQL_USE_DRIVER` =\> `Pdo\Odbc::SQL_USE_DRIVER`, `PDO::ODBC_SQL_USE_ODBC` =\> `Pdo\Odbc::SQL_USE_ODBC`, `PDO::PGSQL_ATTR_DISABLE_PREPARES` =\> `Pdo\Pgsql::ATTR_DISABLE_PREPARES`, `PDO::SQLITE_ATTR_EXTENDED_RESULT_CODES` =\> `Pdo\Sqlite::ATTR_EXTENDED_RESULT_CODES`, `PDO::SQLITE_ATTR_OPEN_FLAGS` =\> `Pdo\Sqlite::ATTR_OPEN_FLAGS`, `PDO::SQLITE_ATTR_READONLY_STATEMENT` =\> `Pdo\Sqlite::ATTR_READONLY_STATEMENT`, `PDO::SQLITE_DETERMINISTIC` =\> `Pdo\Sqlite::DETERMINISTIC`, `PDO::SQLITE_OPEN_READONLY` =\> `Pdo\Sqlite::OPEN_READONLY`, `PDO::SQLITE_OPEN_READWRITE` =\> `Pdo\Sqlite::OPEN_READWRITE`, `PDO::SQLITE_OPEN_CREATE` =\> `Pdo\Sqlite::OPEN_CREATE`

Los métodos específicos del controlador en la clase PDO han quedado obsoletos. Lista de métodos afectados y sus reemplazos: PDO::pgsqlCopyFromArray =\> Pdo\Pgsql::copyFromArray, PDO::pgsqlCopyFromFile =\> Pdo\Pgsql::copyFromFile, PDO::pgsqlCopyToArray =\> Pdo\Pgsql::copyToArray, PDO::pgsqlCopyToFile =\> Pdo\Pgsql::copyToFile, PDO::pgsqlGetNotify =\> Pdo\Pgsql::getNotify, PDO::pgsqlGetPid =\> Pdo\Pgsql::getPid, PDO::pgsqlLOBCreate =\> Pdo\Pgsql::lobCreate, PDO::pgsqlLOBOpen =\> Pdo\Pgsql::lobOpen, PDO::pgsqlLOBUnlink =\> Pdo\Pgsql::lobUnlink, PDO::sqliteCreateAggregate =\> Pdo\Sqlite::createAggregate, PDO::sqliteCreateCollation =\> Pdo\Sqlite::createCollation, PDO::sqliteCreateFunction =\> Pdo\Sqlite::createFunction

## PDO_PGSQL

Las constantes relacionadas con los estados de las transacciones han quedado obsoletas ya que esta función no está disponible con PDO: `PDO::PGSQL_TRANSACTION_IDLE`, `PDO::PGSQL_TRANSACTION_ACTIVE`, `PDO::PGSQL_TRANSACTION_INTRANS`, `PDO::PGSQL_TRANSACTION_INERROR`, `PDO::PGSQL_TRANSACTION_UNKNOWN`

## Reflection

Los métodos `setAccessible()` de varios objetos Reflection han quedado obsoletos, ya que ya no tienen efecto.

Llamar a ReflectionClass::getConstant para constantes que no existen ha quedado obsoleto.

Llamar a ReflectionProperty::getDefaultValue para propiedades sin valores predeterminados ha quedado obsoleto.

## SPL

Anular el registro de todos los autocargadores pasando la función `spl_autoload_call` como argumento de devolución de llamada a `spl_autoload_unregister` ha quedado obsoleto. En su lugar, si es necesario, se debe iterar sobre el valor devuelto por `spl_autoload_functions` y llamar a `spl_autoload_unregister` en cada valor.

Los métodos SplObjectStorage::contains, SplObjectStorage::attach y SplObjectStorage::detach han quedado obsoletos y se han sustituido por SplObjectStorage::offsetExists, SplObjectStorage::offsetSet y SplObjectStorage::offsetUnset, respectivamente.

El uso de `ArrayObject` y `ArrayIterator` con objetos ha quedado obsoleto.

## Estándar

La función alias `socket_set_timeout` ha quedado obsoleta. Utilice `stream_set_timeout` en su lugar.

Pasar `null` a `readdir`, `rewinddir` y `closedir` para usar el último directorio abierto ha quedado obsoleto. En su lugar, proporcione explícitamente el último directorio abierto.

Pasar enteros fuera del intervalo `[0, 255]` a `chr` está obsoleto. Esto se debe a que un byte solo puede contener un valor dentro de este intervalo.

Pasar un string que no sea un solo byte a `ord` ahora está obsoleto, esto es indicativo de un error.

La variable predefinida localmente [\$http_response_header](#reserved.variables.httpresponseheader) está obsoleta. En su lugar, se debe llamar a la función `http_get_last_response_headers`.

## XML

La función `xml_parser_free` ha quedado obsoleta, ya que los objetos `XMLParser` se liberan automáticamente.
