---
title: ZipArchive::isCompressionMethodSupported
description: Verifica si un método de compresión es soportado por libzip
source_url: https://www.php.net/manual/es/ziparchive.iscompressionmethoddupported.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/iscompressionmethoddupported.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108380
---

ZipArchive::isCompressionMethodSupported

Verifica si un método de compresión es soportado por libzip

## Descripción

```php
public static ZipArchive::isCompressionMethodSupported(int $method, [bool $enc]): bool
```php

Verifica si un método de compresión es soportado por libzip.

## Parámetros

`method`  
El método de compresión, una de las constantes `ZipArchive::CM_*`.

`enc`  
Si es `true`, verifica la compresión; si es `false`, verifica la descompresión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!NOTE]
> Esta función está disponible solo si la compilación se realizó con ≥ 1.7.0.

## Véase también

ZipArchive::setCompressionIndex, ZipArchive::setCompressionName
