---
title: GmagickDraw::settextencoding
description: Especifica el conjunto de codificación del texto
source_url: https://www.php.net/manual/es/gmagickdraw.settextencoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagickdraw/settextencoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 28200
---

GmagickDraw::settextencoding

Especifica el conjunto de codificación del texto

## Descripción

```php
public GmagickDraw::settextencoding(string $encoding): GmagickDraw
```php

Especifica el conjunto de codificación usado para anotaciones el texto. La única codificación de caracteres que se puede especificar por ahora es "UTF-8" para representar Unicode como una secuencia de bytes. Especifique un string vacío para establecer la codificación de texto a la predeterminada por el sistema. El éxito con la anotación de texto usando Unicode puede requerir fuentes diseñadas para soportar Unicode.

## Parámetros

`encoding`  
Cadena de caracteres que especifica la codificación de texto

## Valores devueltos

El objeto `GmagickDraw` en caso de éxito
