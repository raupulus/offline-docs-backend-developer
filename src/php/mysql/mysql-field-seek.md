---
title: mysql_field_seek
description: Establece el puntero del resultado en un índice de campo específicado
source_url: https://www.php.net/manual/es/function.mysql-field-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-field-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52240
---

mysql_field_seek

Establece el puntero del resultado en un índice de campo específicado

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_field_seek
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::fetch
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> empleando los parámetros
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> cursor_orientation
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> y
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> offset
>
> </div>

## Descripción

```php
mysql_field_seek(resource $result, int $field_offset): bool
```php

Busca el índice del campo especificado. Si la siguiente llamada a `mysql_fetch_field` no incluye un índice de campo, será devuelto el índice del campo especificado en `mysql_field_seek`.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`field_offset`  
La posición numérica del campo. `field_offset` comienza en `0`. Si `field_offset` no existe, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

mysql_fetch_field
