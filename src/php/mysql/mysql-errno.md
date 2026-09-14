---
title: mysql_errno
description: Devuelve el valor numérico del mensaje de error de la última operación
  MySQL
source_url: https://www.php.net/manual/es/function.mysql-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52120
---

mysql_errno

Devuelve el valor numérico del mensaje de error de la última operación MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_errno
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::errorCode
>
> </div>

## Descripción

```php
mysql_errno([resource $link_identifier]): int
```php

Devuelve el número de error de la última función MySQL.

Los errores que provienen del procesamiento de la base de datos MySQL ya no emiten advertencias. En su lugar, utilice `mysql_errno` para recuperar el código de error. Tenga en cuenta que ésta función solamente devolverá el código de error de la función MySQL ejecutada mas recientemente (sin incluir a `mysql_error` y `mysql_errno`), por lo que, si se quiere usar, hay que asegurarse de revisar el valor antes de llamar otra función MySQL.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve el número de error de la última función de MySQL, o `0` (cero) si no ha ocurrido ningún error.

## Ejemplos

Ejemplo de `mysql_errno`

```
<?php
$enlace = mysql_connect("localhost", "usuario_mysql", "contraseña_mysql");

if (!mysql_select_db("bd_inexistente", $enlace)) {
    echo mysql_errno($enlace) . ": " . mysql_error($enlace). "\n";
}

mysql_select_db("kossu", $enlace);
if (!mysql_query("SELECT * FROM tabla_inexistente", $enlace)) {
    echo mysql_errno($enlace) . ": " . mysql_error($enlace) . "\n";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    1049: Unknown database 'bd_inexistente'
    1146: Table 'kossu.tabla_inexistente' doesn't exist

## Véase también

mysql_error

Códigos de error de MySQL
