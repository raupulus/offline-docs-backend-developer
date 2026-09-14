---
title: SplFileObject::fflush
description: Vuelca el resultado en el fichero
source_url: https://www.php.net/manual/es/splfileobject.fflush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fflush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84340
---

SplFileObject::fflush

Vuelca el resultado en el fichero

## Descripción

```php
public SplFileObject::fflush(): bool
```php

Fuerza a escribir en todo el búfer de salida al fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de SplFileObject::fflush

```
<?php
$file = new SplFileObject('variado.txt', 'r+');
$file->rewind();
$file->fwrite("Foo");
$file->fflush();
$file->ftruncate($file->ftell());
?>

    
```php

## Véase también

SplFileObject::fwrite
