---
title: SplFileInfo::isReadable
description: Comprueba si el fichero se puede leer
source_url: https://www.php.net/manual/es/splfileinfo.isreadable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/isreadable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 84d643420
order: 84240
---

SplFileInfo::isReadable

Comprueba si el fichero se puede leer

## Descripción

```php
public SplFileInfo::isReadable(): bool
```php

Comprueba si el fichero se puede leer.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si se puede leer, en caso contrario `false`.

## Ejemplos

Ejemplo de SplFileInfo::isReadable

```
<?php
$info = new SplFileInfo('readable.jpg');
if ($info->isReadable()) {
    echo $info->getFilename() . ' is readable';
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    readable.jpg is readable
