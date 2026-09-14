---
title: dbase_create
description: Crea una base de datos dBase
source_url: https://www.php.net/manual/es/function.dbase-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11720
---

dbase_create

Crea una base de datos dBase

## Descripción

```php
dbase_create(string $path, array $fields, [int $type]): resource
```php

`dbase_create` crea una base de datos dBase con la definición proporcionada. Si el fichero ya existe, no se trunca. `dbase_pack` puede ser llamado para forzar una troncación.

> [!NOTE]
> Esta función es afectada por la directiva de configuración [open_basedir](#ini.open-basedir).

## Parámetros

`path`  
La ruta de acceso a la base de datos. Puede ser una ruta relativa o absoluta al fichero donde dBase almacenará sus datos.

`fields`  
Un array de arrays, cada array describe el formato de un campo de la base de datos. Cada campo está compuesto por un nombre, un carácter que indica el tipo de campo y opcionalmente, una longitud, una precisión y un flag nullable. Los campos soportados se enumeran en la [sección de introducción](#intro.dbase).

> [!NOTE]
> Los nombres de los campos están limitados en longitud y no deben exceder los 10 caracteres.

`type`  
El tipo de base de datos a crear. Puede ser `DBASE_TYPE_DBASE` o `DBASE_TYPE_FOXPRO`.

## Valores devueltos

Devuelve un recurso de base de datos si la base de datos ha sido creada con éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL dbase 7.0.0 | El parámetro `type` ha sido añadido. |
| PECL dbase 7.0.0 | `dbase_identifier` es ahora un `resource` en lugar de un `int`. |

## Ejemplos

Creación de un fichero de base de datos dBase

```
<?php

// Definición de la base de datos
$def = array(
  array("date",     "D"),
  array("name",     "C",  50),
  array("age",      "N",   3, 0),
  array("email",    "C", 128),
  array("ismember", "L")
);

// Creación
if (!dbase_create('/tmp/test.dbf', $def)) {
  echo "Error, imposible crear la base de datos\n";
}

?>

    
```php

## Véase también

`dbase_open`, `dbase_close`
