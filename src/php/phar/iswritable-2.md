---
title: PharData::isWritable
description: Verifica si el archivo tar/zip puede ser modificado
source_url: https://www.php.net/manual/es/phardata.iswritable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/isWritable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64610
---

PharData::isWritable

Verifica si el archivo tar/zip puede ser modificado

## Descripción

```php
public PharData::isWritable(): bool
```php

Este método devuelve `true` si el archivo tar/zip en el disco no es de solo lectura. A diferencia de `Phar::isWritable`, los archivos tar/zip de datos pueden ser modificados incluso si `phar.readonly` está a `1`.

## Parámetros

No se proporcionan argumentos.

## Valores devueltos

Devuelve `true` si el archivo tar/zip puede ser modificado

## Véase también

`Phar::canWrite`, `Phar::isWritable`
