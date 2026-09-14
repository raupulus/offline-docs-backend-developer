---
title: ps_setfont
description: Establecer la fuente a usar para la siguiente impresión
source_url: https://www.php.net/manual/es/function.ps-setfont.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setfont.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66090
---

ps_setfont

Establecer la fuente a usar para la siguiente impresión

## Descripción

```php
ps_setfont(resource $psdoc, int $fontid, float $size): bool
```php

Establece una fuente, la cual ha de ser cargada antes con la función `ps_findfont`. Imprimir texto sin establecer una fuente resultará en un error.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`fontid`  
El identificador de la fuente, como el devuelto por la función `ps_findfont`.

`size`  
El tamaño de la fuente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_findfont`, `ps_set_text_pos` para un ejemplo.
