---
title: ZipArchive::isEncryptionMethodSupported
description: Verifica si un método de cifrado es soportado por libzip
source_url: https://www.php.net/manual/es/ziparchive.isencryptionmethoddupported.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/isencryptionmethoddupported.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108390
---

ZipArchive::isEncryptionMethodSupported

Verifica si un método de cifrado es soportado por libzip

## Descripción

```php
public static ZipArchive::isEncryptionMethodSupported(int $method, [bool $enc]): bool
```php

Verifica si un método de cifrado es soportado por libzip.

## Parámetros

`method`  
El método de cifrado, una de las constantes `ZipArchive::EM_*`.

`enc`  
Si es `true`, verifica el cifrado; si es `false`, verifica el descifrado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!NOTE]
> Esta función está disponible solo si la extensión ha sido compilada con libzip ≥ 1.7.0.

## Véase también

ZipArchive::setEncryptionIndex, ZipArchive::setEncryptionName
