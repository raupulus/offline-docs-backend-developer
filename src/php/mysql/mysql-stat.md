---
title: mysql_stat
description: Obtiene el estado actual del sistema
source_url: https://www.php.net/manual/es/function.mysql-stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52470
---

mysql_stat

Obtiene el estado actual del sistema

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_stat
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::getAttribute
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> con
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> attribute
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> como
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::ATTR_SERVER_INFO
>
> </div>

## Descripción

```php
mysql_stat([resource $link_identifier]): string
```php

`mysql_stat` devuelve el estado actual del servidor.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve un string con el estado del tiempo de funcionamiento, hilos, consultas, tablas abiertas, tablas de volcado y consultas por segundo. Para obtener una lista completa de variables de estado, es necesario usar el comando SQL `SHOW STATUS`. Si `link_identifier` no es válido, se devuelve `null`.

## Ejemplos

Ejemplo de `mysql_stat`

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
$estado = explode('  ', mysql_stat($enlace));
print_r($estado);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Uptime: 5380
        [1] => Threads: 2
        [2] => Questions: 1321299
        [3] => Slow queries: 0
        [4] => Opens: 26
        [5] => Flush tables: 1
        [6] => Open tables: 17
        [7] => Queries per second avg: 245.595
    )

Ejemplo alternativo de `mysql_stat`

```
<?php
$enlace    = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
$resultado = mysql_query('SHOW STATUS', $enlace);
while ($fila = mysql_fetch_assoc($resultado)) {
    echo $fila['Nombre_variable'] . ' = ' . $fila['Valor'] . "\n";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    back_log = 50
    basedir = /usr/local/
    bdb_cache_size = 8388600
    bdb_log_buffer_size = 32768
    bdb_home = /var/db/mysql/
    bdb_max_lock = 10000
    bdb_logdir =
    bdb_shared_data = OFF
    bdb_tmpdir = /var/tmp/
    ...

## Véase también

mysql_get_server_info

mysql_list_processes
