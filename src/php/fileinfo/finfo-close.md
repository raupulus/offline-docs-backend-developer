---
title: finfo_close
description: Cierra una instancia finfo
source_url: https://www.php.net/manual/es/function.finfo-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fileinfo/functions/finfo-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fileinfo
translation_status: ready
translation_revision: fcd921429
order: 23200
---

finfo_close

Cierra una instancia finfo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] finfo_close(finfo $finfo): true
```php

Esta función se utilizaba para cerrar la instancia abierta por `finfo_open` hasta PHP 7.4, pero es una operación sin efecto (no-op) desde la conversión del recurso `finfo` a objeto realizada en PHP 8.0, y ha sido declarada obsoleta en PHP 8.5.

## Parámetros

`finfo`  
Una instancia `finfo`, retornada por `finfo_open`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Esta función ha sido declarada obsoleta. |
| 8.5.0 | El tipo de retorno es ahora `true`; anteriormente, era `bool`. |
| 8.1.0 | Esta función es ahora una NOP. |
| 8.1.0 | El parámetro `finfo` ahora espera una instancia de `finfo` ; anteriormente, una `resource` era esperado. |
