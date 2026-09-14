---
title: ZipArchive::getStatusString
description: 'Devuelve mensajes de: estado de error, de sistema y/o mensajes de zip'
source_url: https://www.php.net/manual/es/ziparchive.getstatusstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getstatusstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108340
---

ZipArchive::getStatusString

Devuelve mensajes de: estado de error, de sistema y/o mensajes de zip

## Descripción

```php
public ZipArchive::getStatusString(): string
```php

Devuelve mensajes de: estado de error, de sistema y/o mensajes de zip.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` con el mensaje de estado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL zip 1.18.0 | Este método puede ser llamado en un archivo cerrado. |
| 8.0.0, PECL zip 1.18.0 | Este método ya no devuelve `false` en caso de fallo. |
