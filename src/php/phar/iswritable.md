---
title: Phar::isWritable
description: Retorna true si el archivo phar puede ser modificado
source_url: https://www.php.net/manual/es/phar.iswritable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/isWritable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64240
---

Phar::isWritable

Retorna

true

si el archivo phar puede ser modificado

## Descripción

```php
public Phar::isWritable(): bool
```php

Este método retorna `true` si `phar.readonly` está en `0` y el archivo phar actual en el disco no es de solo lectura.

## Parámetros

No se admiten argumentos.

## Valores devueltos

Retorna `true` si el archivo phar puede ser modificado

## Véase también

`Phar::canWrite`, `PharData::isWritable`
