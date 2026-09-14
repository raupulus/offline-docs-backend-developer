---
title: mysql_insert_id
description: Obtiene el ID generado en la última consulta
source_url: https://www.php.net/manual/es/function.mysql-insert-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-insert-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52330
---

mysql_insert_id

Obtiene el ID generado en la última consulta

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_insert_id
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::lastInsertId
>
> </div>

## Descripción

```php
mysql_insert_id([resource $link_identifier]): int
```php

Recupera el ID generado por la consulta anterior (normalmente INSERT) para una columna AUTO_INCREMENT.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

El ID generado por la consulta anterior para una columna AUTO_INCREMENT en caso de éxito, `0` si la consulta anterior no genera un valor AUTO_INCREMENT, o `false` si no se estableció una conexión MySQL.

## Ejemplos

Ejemplo de `mysql_insert_id`

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
if (!$enlace) {
    die('No se pudo conectar: ' . mysql_error());
}
mysql_select_db('mibd');

mysql_query("INSERT INTO mitabla (producto) values ('kossu')");
printf("El último registro insertado tiene el id %d\n", mysql_insert_id());
?>

   
```php

## Notas

> [!CAUTION]
> `mysql_insert_id` convertirá el tipo devuelto de la función nativa `mysql_insert_id()` de la API de C de MySQL a un tipo `long` (llamado `int` en PHP). Si la columna AUTO_INCREMENT tiene un tipo BIGINT (64 bits) la conversión puede resultar en un valor incorrecto. En su lugar, use la función de SQL interna LAST_INSERT_ID() de MySQL en una consulta SQL. Para más información sobre los valores máximos de tipo integer, por favor vea la documentación de [integer](#language.types.integer).

> [!NOTE]
> Como `mysql_insert_id` actúa en la última consulta realizada, asegúrese de llamar a `mysql_insert_id` inmediatamente después de la consulta que genera el valor.

> [!NOTE]
> El valor de la función de SQL `LAST_INSERT_ID()` de MySQL siempre contiene el valor AUTO_INCREMENT generado más recientientemente, y no se restablece entre consultas.

## Véase también

mysql_query

mysql_info
