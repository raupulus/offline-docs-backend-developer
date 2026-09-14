---
title: SplFileInfo::getPerms
description: Obtiene los permisos del fichero
source_url: https://www.php.net/manual/es/splfileinfo.getperms.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getperms.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84160
---

SplFileInfo::getPerms

Obtiene los permisos del fichero

## Descripción

```php
public SplFileInfo::getPerms(): int
```php

Obtiene los permisos del fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve los permisos de el fichero en caso de éxito, o `false` en caso de error.

## Ejemplos

Ejemplo de `SplFileInfo::getPerms`

```
<?php
$info = new SplFileInfo('/tmp');
echo substr(sprintf('%o', $info->getPerms()), -4);

$info = new SplFileInfo(__FILE__);
echo substr(sprintf('%o', $info->getPerms()), -4);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    1777
    0644
