---
title: SplFileInfo::getMTime
description: Obtiene la fecha de la última modificación
source_url: https://www.php.net/manual/es/splfileinfo.getmtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getmtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 84d643420
order: 84110
---

SplFileInfo::getMTime

Obtiene la fecha de la última modificación

## Descripción

```php
public SplFileInfo::getMTime(): int
```php

Devuelve el tiempo cuando el contenido de el fichero ha sido cambiado. El tiempo retornado en formato Unix timestamp.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la fecha de modificación de el fichero, en formato Unix timestamp en caso de éxito, o `false` en caso de error.

## Ejemplos

Ejemplo de SplFileInfo::getMTime

```
<?php
$info = new SplFileInfo('example.jpg');
echo 'Last modified at ' . date('g:i a', $info->getMTime());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Last modified at 1:49 pm

## Véase también

`filemtime`, SplFileInfo::getATime, SplFileInfo::getCTime
