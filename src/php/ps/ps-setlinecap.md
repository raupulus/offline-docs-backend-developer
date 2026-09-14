---
title: ps_setlinecap
description: Establecer la apariencia de los extremos de línea
source_url: https://www.php.net/manual/es/function.ps-setlinecap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setlinecap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66110
---

ps_setlinecap

Establecer la apariencia de los extremos de línea

## Descripción

```php
ps_setlinecap(resource $psdoc, int $type): bool
```php

Establece la apariencia de los extremos de línea.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`type`  
El tipo de extremo de línea. Los valores posibles son `PS_LINECAP_BUTT`, `PS_LINECAP_ROUND`, o `PS_LINECAP_SQUARED`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_setlinejoin`, `ps_setlinewidth`, `ps_setmiterlimit`
