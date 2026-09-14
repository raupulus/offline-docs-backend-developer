---
title: SplFileInfo::getATime
description: Obtiene la hora del último acceso al fichero
source_url: https://www.php.net/manual/es/splfileinfo.getatime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getatime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 84d643420
order: 84020
---

SplFileInfo::getATime

Obtiene la hora del último acceso al fichero

## Descripción

```php
public SplFileInfo::getATime(): int
```php

Obtiene la hora del último acceso al fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tiempo del ultimo acceso al fichero en caso de éxito, o `false` en caso de error.

## Errores/Excepciones

Lanza `RuntimeException` en caso de error.

## Ejemplos

Ejemplo de SplFileInfo::getATime

```
<?php
$info = new SplFileInfo('example.jpg');
echo 'Last accessed at ' . date('g:i a', $info->getATime());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Last accessed at 1:49 pm

## Véase también

`fileatime`, SplFileInfo::getCTime, SplFileInfo::getMTime
