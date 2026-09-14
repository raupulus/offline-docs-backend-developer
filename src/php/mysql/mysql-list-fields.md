---
title: mysql_list_fields
description: Lista los campos de una tabla de MySQL
source_url: https://www.php.net/manual/es/function.mysql-list-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-list-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52350
---

mysql_list_fields

Lista los campos de una tabla de MySQL

> [!WARNING]
> Esta función estaba obsoleta en PHP 5.4.0, y toda la [extensión original MySQL](#book.mysql) fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> Consulta SQL:
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> SHOW COLUMNS FROM alguna_tabla
>
> </div>

## Descripción

```php
mysql_list_fields(string $database_name, string $table_name, [resource $link_identifier]): resource
```php

Devuelve información sobre el nombre de la tabla dado.

Esta función está obsoleta. Es preferible usar `mysql_query` para ejecutar una consulta SQL `SHOW COLUMNS FROM tabla [LIKE 'nombre']` en su lugar.

## Parámetros

`database_name`  
El nombre de la base de la base de datos que está siendo consultada.

`table_name`  
El nombre de la tabla que está siendo consultada.

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Un `resource` del puntero del resultado en caso de éxito, o `false` en caso de error.

El resultado devuelto puede ser usado con `mysql_field_flags`, `mysql_field_len`, `mysql_field_name` y `mysql_field_type`.

## Ejemplos

Alternativa para la obsoleta `mysql_list_fields`

```
<?php
$resultado = mysql_query("SHOW COLUMNS FROM alguna_tabla");
if (!$resultado) {
    echo 'No se pudo ejecutar la consulta: ' . mysql_error();
    exit;
}
if (mysql_num_rows($resultado) > 0) {
    while ($fila = mysql_fetch_assoc($resultado)) {
        print_r($fila);
    }
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [Field] => id
        [Type] => int(7)
        [Null] =>
        [Key] => PRI
        [Default] =>
        [Extra] => auto_increment
    )
    Array
    (
        [Field] => email
        [Type] => varchar(100)
        [Null] =>
        [Key] =>
        [Default] =>
        [Extra] =>
    )

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_listfields`

## Véase también

mysql_field_flags

mysql_info
