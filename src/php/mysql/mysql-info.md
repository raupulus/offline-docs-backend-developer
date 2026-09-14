---
title: mysql_info
description: Obtiene información sobre la consulta más reciente
source_url: https://www.php.net/manual/es/function.mysql-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52320
---

mysql_info

Obtiene información sobre la consulta más reciente

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_info
>
> </div>

## Descripción

```php
mysql_info([resource $link_identifier]): string
```php

Devuelve información detallada sobre la última consulta.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuele información sobre la sentencia en caso de éxito, o `false` en caso de error. Vea el ejemplo siguiente para conocer qué sentencias proveen información, y cuál puede ser la apariencia del valor devuelto. Las sentencias que no están en la lista devolverán `false`.

## Ejemplos

Sentencias MySQL Relevantes

Sentencias que devuelven valores de tipo cadena. Los números están únicamente por propósitos ilustrativos; sus valores corresponderán con la consulta.

```
INSERT INTO ... SELECT ...
String format: Records: 23 Duplicates: 0 Warnings: 0
INSERT INTO ... VALUES (...),(...),(...)...
String format: Records: 37 Duplicates: 0 Warnings: 0
LOAD DATA INFILE ...
String format: Records: 42 Deleted: 0 Skipped: 0 Warnings: 0
ALTER TABLE
String format: Records: 60 Duplicates: 0 Warnings: 0
UPDATE
String format: Rows matched: 65 Changed: 65 Warnings: 0

   
```php

## Notas

> [!NOTE]
> `mysql_info` devuelve un valor diferente a `false` para la sentencia INSERT ... VALUES sólo si se indican múltiples listas de valores en la sentencia.

## Véase también

mysql_affected_rows

mysql_insert_id

mysql_stat
