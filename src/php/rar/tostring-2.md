---
title: RarEntry::__toString
description: Obtener texto representación de entrada
source_url: https://www.php.net/manual/es/rarentry.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68630
---

RarEntry::\_\_toString

Obtener texto representación de entrada

## Descripción

```php
public RarEntry::__toString(): string
```php

RarEntry::\_\_toString devuelve una representación textual de esta entrada. Esta incluye si la entrada es un archivo o un directorio (enlaces simbólicos y otros objetos especiales serán tratados como archivos), el nombre UTF-8 de la entrada y su CRC. La forma y el contenido de esta representación puede cambiar en el futuro, así que no son fiables.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una representación textual de la entrada.
