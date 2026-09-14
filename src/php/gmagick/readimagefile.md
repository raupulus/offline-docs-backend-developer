---
title: Gmagick::readimagefile
description: El propósito de readimagefile
source_url: https://www.php.net/manual/es/gmagick.readimagefile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/readimagefile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27390
---

Gmagick::readimagefile

El propósito de readimagefile

## Descripción

```php
public Gmagick::readimagefile(resource $fp, [string $filename]): Gmagick
```php

Lee una imagen o una secuencia de imágenes desde un descriptor de fichero abierto.

## Parámetros

`fp`  
El descriptor de fichero.

## Valores devueltos

Un objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
