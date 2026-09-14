---
title: ZipArchive::registerProgressCallback
description: Registra una llamada para proporcionar actualizaciones durante el cierre
  del archivo
source_url: https://www.php.net/manual/es/ziparchive.registerprogresscallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/registerprogresscallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108430
---

ZipArchive::registerProgressCallback

Registra una llamada para proporcionar actualizaciones durante el cierre del archivo

## Descripción

```php
public ZipArchive::registerProgressCallback(float $rate, callable $callback): bool
```php

Registra una función `callback` para proporcionar actualizaciones durante el cierre del archivo.

## Parámetros

`rate`  
Cambiar entre cada llamada de la devolución de llamada (de 0.0 a 1.0).

`callback`  
Esta función recibirá el actual `state` como un `float` (de 0.0 a 1.0).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Este ejemplo crea un archivo ZIP `php.zip` y muestra la progresión.

Archivar un fichero

```
$zip = new ZipArchive();
if ($zip->open('php.zip', ZipArchive::CREATE | ZipArchive::OVERWRITE)) {
    $zip->addFile(PHP_BINARY, 'php');
    $zip->registerProgressCallback(0.05, function ($r) {
        printf("%d%%\n", $r * 100);
    });
    $zip->close();
}

     
```php

## Notas

> [!NOTE]
> Esta función sólo está disponible si se construye con libzip ≥ 1.3.0.

## Véase también

ZipArchive::registerCancelCallback
