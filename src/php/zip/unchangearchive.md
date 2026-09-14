---
title: ZipArchive::unchangeArchive
description: Revertir todos los cambios globales hechos en el archivo
source_url: https://www.php.net/manual/es/ziparchive.unchangearchive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/unchangearchive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108630
---

ZipArchive::unchangeArchive

Revertir todos los cambios globales hechos en el archivo

## Descripción

```php
public ZipArchive::unchangeArchive(): bool
```php

Revertir todos los cambios globales en el archivo. Por ahora, esto solamente revierte los cambios de los comentarios del archivo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
