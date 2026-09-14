---
title: ps_setmiterlimit
description: Establecer el límite del inglete
source_url: https://www.php.net/manual/es/function.ps-setmiterlimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setmiterlimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66140
---

ps_setmiterlimit

Establecer el límite del inglete

## Descripción

```php
ps_setmiterlimit(resource $psdoc, float $value): bool
```php

Si dos líneas se unen en un ángulo pequeño y la unión de líneas está establecida a `PS_LINEJOIN_MITER`, el pico resultante será muy largo. El límite de inglete es la proporción máxima entre la longitud del inglete (la longitud del pico) y del ancho de línea.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`value`  
La proporción máxima entre la longitud del inglete y del ancho de línea. Los valores grandes (\> 10) resultarán en picos muy largos cuando dos líneas se encuentren en un ángulo pequeño. Mantenga el predeterminado a menos que sepa lo que está haciendo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_setlinecap`, `ps_setlinejoin`, `ps_setlinewidth`
