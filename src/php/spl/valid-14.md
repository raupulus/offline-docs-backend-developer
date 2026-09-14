---
title: SplFileObject::valid
description: Comprueba si el final del fichero ha sido alcanzado
source_url: https://www.php.net/manual/es/splfileobject.valid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/valid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84630
---

SplFileObject::valid

Comprueba si el final del fichero ha sido alcanzado

## Descripción

```php
public SplFileObject::valid(): bool
```php

Comprueba si el final del fichero ha sido alcanzado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el final no ha sido alcanzado, en caso contrario `false`.

## Ejemplos

Ejemplo de SplFileObject::valid

```
<?php
// Recorrer el fichero, línea por línea
$file = new SplFileObject("fichero.txt");
while ($file->valid()) {
    echo $file->fgets();
}
?>

    
```php

## Véase también

SplFileObject::current, SplFileObject::key, SplFileObject::seek, SplFileObject::next, SplFileObject::rewind
