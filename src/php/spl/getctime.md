---
title: SplFileInfo::getCTime
description: Obtiene el i-nodo de el cambio de tiempo
source_url: https://www.php.net/manual/es/splfileinfo.getctime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getctime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 84d643420
order: 84040
---

SplFileInfo::getCTime

Obtiene el i-nodo de el cambio de tiempo

## Descripción

```php
public SplFileInfo::getCTime(): int
```php

Devuelve el i-nodo de el cambio de tiempo para el fichero. El tiempo es retornado en formato Unix timestamp.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El último cambio del tiempo, en formato Unix timestamp en caso de éxito, o `false` en caso de error.

## Errores/Excepciones

Lanza una `RuntimeException` en caso de error.

## Ejemplos

Ejemplo de SplFileInfo::getCTime

```
<?php
$info = new SplFileInfo('example.jpg');
echo 'El último cambio ' . date('g:i a', $info->getCTime());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    El último cambio 1:49 pm

## Véase también

`filectime`, SplFileInfo::getATime, SplFileInfo::getMTime
