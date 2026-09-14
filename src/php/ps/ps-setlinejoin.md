---
title: ps_setlinejoin
description: Establecer cómo están unidas las líneas conectadas
source_url: https://www.php.net/manual/es/function.ps-setlinejoin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setlinejoin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66120
---

ps_setlinejoin

Establecer cómo están unidas las líneas conectadas

## Descripción

```php
ps_setlinejoin(resource $psdoc, int $type): bool
```php

Establece cómo se unen las líneas

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`type`  
La forma de unir las líneas. Los valores posibles son `PS_LINEJOIN_MITER`, `PS_LINEJOIN_ROUND`, o `PS_LINEJOIN_BEVEL`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_setlinecap`, `ps_setlinewidth`, `ps_setmiterlimit`
