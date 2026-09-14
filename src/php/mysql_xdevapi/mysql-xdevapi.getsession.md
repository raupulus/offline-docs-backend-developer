---
title: getSession
description: Conecta a un servidor MySQL
source_url: https://www.php.net/manual/es/function.mysql-xdevapi-getsession.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/functions/mysql-xdevapi.getsession.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: b0a34b2fc
order: 52570
---

getSession

Conecta a un servidor MySQL

## Descripción

```php
mysql_xdevapi\getSession(string $uri): mysql_xdevapi\Session
```php

Conecta al servidor MySQL.

## Parámetros

`uri`  
El URI del servidor MySQL, tal como `mysqlx://user:password@host`.

Formato de URI:

`scheme://[user[:[password]]@]target[:port][?attribute1=value1&attribute2=value2...`

- `scheme`: requerido, el protocolo de conexión

  En mysql_xdevapi es siempre 'mysqlx' (para el protocolo X)

- `user`: opcional, la cuenta de usuario MySQL para la autenticación

- `password`: opcional, la contraseña del usuario MySQL para la autenticación

- `target`: requerido, la instancia del servidor a la que se refiere la conexión:

  \* Conexión TCP (nombre de host, dirección IPv4 o dirección IPv6)

  \* Ruta de socket Unix (ruta de fichero local)

  \* Pipe nombrado Windows (ruta de fichero local)

- `port`: opcional, el puerto de red del servidor MySQL.

  Por omisión, el puerto para el protocolo X es 33060

- `?attribute=value`: este elemento es opcional y especifica un diccionario de datos que contiene diferentes opciones, incluyendo:

  - El atributo `auth` (mecanismo de autenticación) relacionado con las conexiones cifradas. Para más información, ver [Opciones de comando para las conexiones cifradas](https://dev.mysql.com/doc/refman/8.0/en/encrypted-connection-options.html). Los siguientes valores 'auth' son soportados: `plain`, `mysql41`, `external`, y `sha256_mem`.

  - El atributo `connect-timeout` afecta la conexión y no las operaciones siguientes. Se define por conexión, ya sea en un solo host o en varios.

    Pasar un entero positivo para definir el tiempo límite de conexión en segundos, o pasar 0 (cero) para desactivar el tiempo límite (infinito). No definir connect-timeout utiliza el valor por omisión de 10.

    En relación, las variables de entorno MYSQLX_CONNECTION_TIMEOUT (tiempo límite en segundos) y MYSQLX_TEST_CONNECTION_TIMEOUT (utilizado durante la ejecución de pruebas) pueden ser definidas y utilizadas en lugar de connect-timeout en el URI. La opción connect-timeout del URI tiene prioridad sobre estas variables de entorno.

  - El atributo opcional `compression` acepta estos valores: `preferred` (el cliente negocia con el servidor para encontrar un algoritmo soportado; la conexión no está comprimida si no se encuentra un algoritmo soportado mutuamente), `required` (como "preferred", pero la conexión se termina si no se encuentra un algoritmo soportado mutuamente), o `disabled` (la conexión no está comprimida). Por omisión, `preferred`.

    Esta opción fue añadida en la versión 8.0.20.

  - El atributo opcional `compression-algorithms` define los algoritmos de compresión deseados (y su orden de uso preferido): `zstd_stream` (alias: zstd), `lz4_message` (alias: lz4), o `deflate_stream` (alias: deflate o zlib). Por omisión, el orden utilizado (según la disponibilidad del sistema) es lz4_message, zstd_stream, y luego deflate_stream. Por ejemplo, pasar compression-algorithms=\[lz4,zstd_stream\] utiliza lz4 si está disponible, de lo contrario se utiliza zstd_stream. Si ninguno de los dos está disponible, el comportamiento depende del valor de compression por ejemplo, si compression=required entonces fallará con un error.

    Esta opción fue añadida en la versión 8.0.22.

Ejemplo de URI

```
mysqlx://foobar
mysqlx://root@localhost?socket=%2Ftmp%2Fmysqld.sock%2F
mysqlx://foo:bar@localhost:33060
mysqlx://foo:bar@localhost:33160?ssl-mode=disabled
mysqlx://foo:bar@localhost:33260?ssl-mode=required
mysqlx://foo:bar@localhost:33360?ssl-mode=required&auth=mysql41
mysqlx://foo:bar@(/path/to/socket)
mysqlx://foo:bar@(/path/to/socket)?auth=sha256_mem
mysqlx://foo:bar@[localhost:33060, 127.0.0.1:33061]
mysqlx://foobar?ssl-ca=(/path/to/ca.pem)&ssl-crl=(/path/to/crl.pem)
mysqlx://foo:bar@[localhost:33060, 127.0.0.1:33061]?ssl-mode=disabled
mysqlx://foo:bar@localhost:33160/?connect-timeout=0
mysqlx://foo:bar@localhost:33160/?connect-timeout=10&compression=required
mysqlx://foo:bar@localhost:33160/?connect-timeout=10&compression=required&compression-algorithms=[lz4,zstd_stream]
  
```php

Para más información, ver conexión a MySQL Shell [utilizando una cadena de URI](https://dev.mysql.com/doc/refman/8.0/en/mysql-shell-connection-using-uri.html).

## Valores devueltos

Un objeto `Session`.

## Errores/Excepciones

Un error de conexión lanza una excepción `Exception`.

## Ejemplos

Ejemplo de `mysql_xdevapi\getSession`

```
<?php
try {
    $session = mysql_xdevapi\getSession("mysqlx://user:password@host");
} catch(Exception $e) {
    die("La conexión no pudo ser establecida: " . $e->getMessage());
}

$schemas = $session->getSchemas();
print_r($schemas);

$mysql_version = $session->getServerVersion();
print_r($mysql_version);

var_dump($collection->find("name = 'Alfred'")->execute()->fetchOne());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => mysql_xdevapi\Schema Object
            (
                [name] => helloworld
            )
        [1] => mysql_xdevapi\Schema Object
            (
                [name] => information_schema
            )
        [2] => mysql_xdevapi\Schema Object
            (
                [name] => mysql
            )
        [3] => mysql_xdevapi\Schema Object
            (
                [name] => performance_schema
            )
        [4] => mysql_xdevapi\Schema Object
            (
                [name] => sys
            )
    )

    80012

    array(4) {
      ["_id"]=>
      string(28) "00005ad66abf0001000400000003"
      ["age"]=>
      int(42)
      ["job"]=>
      string(7) "Butler"
      ["name"]=>
      string(4) "Alfred"
    }
