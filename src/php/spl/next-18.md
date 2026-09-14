---
title: SplFileObject::next
description: Leer la siguiente línea
source_url: https://www.php.net/manual/es/splfileobject.next.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/next.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84560
---

SplFileObject::next

Leer la siguiente línea

## Descripción

```php
public SplFileObject::next(): void
```php

Mover a la siguiente línea en el fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de SplFileObject::next

```
<?php
// Leer el fichero línea por línea
$file = new SplFileObject("variado.txt");
while (!$file->eof()) {
    echo $file->current();
    $file->next();
}
?>

    
```php

## Véase también

SplFileObject::current, SplFileObject::key, SplFileObject::seek, SplFileObject::rewind, SplFileObject::valid
