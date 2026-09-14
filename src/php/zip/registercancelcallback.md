---
title: ZipArchive::registerCancelCallback
description: Registrar una llamada para permitir la cancelación durante el cierre
  del archivo
source_url: https://www.php.net/manual/es/ziparchive.registercancelcallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/registercancelcallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108420
---

ZipArchive::registerCancelCallback

Registrar una llamada para permitir la cancelación durante el cierre del archivo

## Descripción

```php
public ZipArchive::registerCancelCallback(callable $callback): bool
```php

Registrar una función `callback` para permitir la cancelación durante el cierre del archivo.

## Parámetros

`callback`  
Si esta función vuelve a 0, la operación continuará, otro valor será cancelado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Este ejemplo crea un archivo ZIP `php.zip` y cancela la operación en alguna condición de operación.

Archivar un fichero

```
<?php
$zip = new ZipArchive();
if ($zip->open('php.zip', ZipArchive::CREATE | ZipArchive::OVERWRITE)) {
    $zip->addFile(PHP_BINARY, 'php');
    $zip->registerCancelCallback(function () {
        return ($someruncondition ? -1 : 0);
    });
    $zip->close();
}

   
```php

## Notas

> [!NOTE]
> Esta función sólo está disponible si se construye con libzip ≥ 1.6.0.

## Véase también

ZipArchive::registerProgressCallback
