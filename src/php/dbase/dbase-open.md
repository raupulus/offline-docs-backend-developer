---
title: dbase_open
description: Abre una base dBase
source_url: https://www.php.net/manual/es/function.dbase-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dbase/functions/dbase-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dbase
translation_status: ready
translation_reviewed: false
translation_revision: 0545e305c
order: 11790
---

dbase_open

Abre una base dBase

## Descripción

```php
dbase_open(string $path, int $mode): resource
```php

`dbase_open` abre una base de datos dBase con un modo de acceso dado.

> [!NOTE]
> Esta función es afectada por la directiva de configuración [open_basedir](#ini.open-basedir).

## Parámetros

`path`  
La ruta hacia la base de datos. Puede ser una ruta relativa o absoluta hacia el fichero donde dBase almacenará sus datos.

`mode`  
Un entero correspondiente al utilizado para la llamada al sistema `open()` (Típicamente, 0 significa solo lectura, 1 significa solo escritura, y 2 significa lectura y escritura).

> [!NOTE]
> No se puede abrir un fichero dBase en modo solo escritura, ya que la función fallará al leer la información de encabezado y, por lo tanto, no se puede utilizar 1 como `mode`.

A partir de dbase 7.0.0 `DBASE_RDONLY` y `DBASE_RDWR` pueden ser utilizados, respectivamente, para definir el `mode`.

## Valores devueltos

Devuelve un recurso de base de datos en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL dbase 7.0.0 | El valor devuelto es ahora un `resource` en lugar de un `int`. |

## Ejemplos

Apertura de un fichero de base de datos dBase

```
<?php

// Apertura en modo solo lectura
$db = dbase_open('/tmp/test.dbf', 0);

if ($db) {
// lectura de datos ..

dbase_close($db);
}

?>

    
```php

## Véase también

`dbase_create`, `dbase_close`
