---
title: dbase_numfields
description: Cuenta el número de campos de una base dBase
source_url: https://www.php.net/manual/es/function.dbase-numfields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-numfields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_revision: 0545e305c
order: 11770
---

dbase_numfields

Cuenta el número de campos de una base dBase

## Descripción

```php
dbase_numfields(resource $database): int
```php

`dbase_numfields` devuelve el número de campos (columnas) de la base de datos `dbase_identifier`.

> [!NOTE]
> Los campos están numerados de 0 a `dbase_numfields($db)-1`, mientras que los registros están numerados de 1 a `dbase_numrecords($db)`.

## Parámetros

`database`  
El recurso de base de datos, devuelto por `dbase_open` o `dbase_create`.

## Valores devueltos

El número de campos de la base de datos, o `false` si ocurre un error.

## Historial de cambios

| Versión          | Descripción                                             |
|------------------|---------------------------------------------------------|
| PECL dbase 7.0.0 | `database` es ahora un `resource` en lugar de un `int`. |

## Ejemplos

Ejemplo con `dbase_numfields`

```
<?php

$rec = dbase_get_record($db, $recno);
$nf  = dbase_numfields($db);
for ($i = 0; $i < $nf; $i++) {
  echo $rec[$i], "\n";
}

?>

    
```php

## Véase también

`dbase_numrecords`
