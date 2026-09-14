---
title: SplFileInfo::isLink
description: Comprueba si el fichero es un link
source_url: https://www.php.net/manual/es/splfileinfo.islink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/islink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84230
---

SplFileInfo::isLink

Comprueba si el fichero es un link

## Descripción

```php
public SplFileInfo::isLink(): bool
```php

Use este método para comprobar si el fichero referenciado por el objeto SplFileInfo es un link.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el fichero es un link, en caso contrario `false`.

## Ejemplos

Ejemplo de `SplFileInfo::isLink`

```
<?php
$info = new SplFileInfo('/path/to/symlink');
if ($info->isLink()) {
    echo 'The real path is '.$info->getRealPath();
}
?>

    
```php

## Véase también

SplFileInfo::getRealPath
