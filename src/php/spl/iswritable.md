---
title: SplFileInfo::isWritable
description: Comprueba si se puede escribir en el fichero
source_url: https://www.php.net/manual/es/splfileinfo.iswritable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/iswritable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: b07b628d6
order: 84250
---

SplFileInfo::isWritable

Comprueba si se puede escribir en el fichero

## Descripción

```php
public SplFileInfo::isWritable(): bool
```php

Comprueba si se puede escribir en el fichero actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si se puede escribir, en caso contrario `false`

## Ejemplos

Ejemplo de SplFileInfo::isWritable

```
<?php
$info = new SplFileInfo('locked.jpg');
if (!$info->isWritable()) {
    echo $info->getFilename() . ' is not writable';
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    locked.jpg is not writable
