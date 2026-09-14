---
title: SplFileObject::fstat
description: Obtiene información de el fichero
source_url: https://www.php.net/manual/es/splfileobject.fstat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fstat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84450
---

SplFileObject::fstat

Obtiene información de el fichero

## Descripción

```php
public SplFileObject::fstat(): array
```php

Obtiene estadísticas de el fichero. Se comporta de forma idéntica a `fstat`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array con las estadísticas de el fichero; el formato de el array es descrito en detalle en la página del manual de `stat`.

## Ejemplos

Ejemplo de SplFileObject::fstat

```
<?php
$file = new SplFileObject("/etc/passwd");
$stat = $file->fstat();

// Imprimir sólo la parte asociada
print_r(array_slice($stat, 13));

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [dev] => 771
        [ino] => 488704
        [mode] => 33188
        [nlink] => 1
        [uid] => 0
        [gid] => 0
        [rdev] => 0
        [size] => 1114
        [atime] => 1061067181
        [mtime] => 1056136526
        [ctime] => 1056136526
        [blksize] => 4096
        [blocks] => 8
    )

## Véase también

`fstat`, `stat`
