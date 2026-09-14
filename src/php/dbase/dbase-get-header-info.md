---
title: dbase_get_header_info
description: Recupera información de encabezado de una base de datos dBase
source_url: https://www.php.net/manual/es/function.dbase-get-header-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-get-header-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11740
---

dbase_get_header_info

Recupera información de encabezado de una base de datos dBase

## Descripción

```php
dbase_get_header_info(resource $database): array
```php

`dbase_get_header_info` devuelve información sobre la estructura de las columnas de la base de datos referenciada por el recurso `database`.

## Parámetros

`database`  
El recurso de base de datos, devuelto por `dbase_open` o `dbase_create`.

## Valores devueltos

Un array indexado con una entrada para cada columna de la base de datos. El índice del array comienza en 0.

Cada elemento del array contiene un array asociativo que contiene la información sobre las columnas, como se describe aquí:

name  
El nombre de la columna

type  
El nombre legible del tipo de la columna (i.e. date, boolean, etc.) Los tipos de campos soportados están enumerados en la [sección de introducción](#intro.dbase).

length  
El número de bytes que puede contener esta columna

precision  
El número de decimales para la columna

format  
Un formato `printf` sugerido para la columna

offset  
La posición de la columna desde el inicio de la línea

Si la información de encabezado de la base de datos no puede ser leída, `false` es devuelto.

## Historial de cambios

| Versión          | Descripción                                             |
|------------------|---------------------------------------------------------|
| PECL dbase 7.0.0 | `database` es ahora un `resource` en lugar de un `int`. |

## Ejemplos

Muestra la información de encabezado para un fichero de base de datos dBase

```
<?php
// Ruta hacia el fichero dBase
$db_path = "/tmp/test.dbf";

// Abre el fichero dBase
$dbh = dbase_open($db_path, 0)
or die("¡Error! Imposible abrir el fichero dBase '$db_path'.");

// Recuperación de la información de las columnas
$column_info = dbase_get_header_info($dbh);

// Muestra la información
print_r($column_info);
?>

    
```php
