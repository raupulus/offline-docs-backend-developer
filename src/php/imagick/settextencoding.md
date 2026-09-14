---
title: ImagickDraw::setTextEncoding
description: Especifica el juego de caracteres
source_url: https://www.php.net/manual/es/imagickdraw.settextencoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/settextencoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37280
---

ImagickDraw::setTextEncoding

Especifica el juego de caracteres

## Descripción

```php
public ImagickDraw::setTextEncoding(string $encoding): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Especifica el juego de caracteres a utilizar para las anotaciones de texto. El único juego de caracteres que puede ser especificado actualmente es "UTF-8", que representa el Unicode bajo la forma de una secuencia de octetos. Especifique una cadena vacía para utilizar el juego de caracteres del sistema. El dibujo de textos puede requerir una fuente que soporte Unicode.

## Parámetros

`encoding`  
El juego de caracteres

## Valores devueltos

No se retorna ningún valor.
