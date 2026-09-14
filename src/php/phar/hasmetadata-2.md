---
title: PharFileInfo::hasMetadata
description: Devuelve las metadatos de la entrada
source_url: https://www.php.net/manual/es/pharfileinfo.hasmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/hasMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64820
---

PharFileInfo::hasMetadata

Devuelve las metadatos de la entrada

## Descripción

```php
public PharFileInfo::hasMetadata(): bool
```php

Devuelve las metadatos de un fichero dentro de un archivo Phar.

## Parámetros

No se admiten argumentos.

## Valores devueltos

Devuelve `false` si no hay metadatos presentes o son `null`, `true` si las metadatos no son `null`

## Véase también

`PharFileInfo::setMetadata`, `PharFileInfo::getMetadata`, `PharFileInfo::delMetadata`, `Phar::setMetadata`, `Phar::hasMetadata`, `Phar::getMetadata`
