---
title: ZipArchive::close
description: Cierra el fichero activo (abierto o el nuevo creado)
source_url: https://www.php.net/manual/es/ziparchive.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108200
---

ZipArchive::close

Cierra el fichero activo (abierto o el nuevo creado)

## Descripción

```php
public ZipArchive::close(): bool
```php

Cierra fichero abierto o creado y guarda los cambios. Este método es automáticamente llamado al finalizar el script.

Si el archivo no contiene ningún fichero, el fichero es completamente eliminado por defecto (no se escribe ningún archivo vacío) según el valor de la bandera global `ZipArchive::AFL_CREATE_OR_KEEP_FILE_FOR_EMPTY_ARCHIVE`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ZipArchive::setArchiveFlag
