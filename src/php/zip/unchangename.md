---
title: ZipArchive::unchangeName
description: Deshace todos los cambios realizados a una entrada con un nombre dado
source_url: https://www.php.net/manual/es/ziparchive.unchangename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/unchangename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108650
---

ZipArchive::unchangeName

Deshace todos los cambios realizados a una entrada con un nombre dado

## Descripción

```php
public ZipArchive::unchangeName(string $name): bool
```php

Deshacer todos los cambios hechos a una entrada.

## Parámetros

`name`  
Nombre de la entrada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
