---
title: finfo_set_flags
description: Establece opciones de configuración de libmagic
source_url: https://www.php.net/manual/es/function.finfo-set-flags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fileinfo/functions/finfo-set-flags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fileinfo
translation_status: ready
translation_reviewed: false
translation_revision: 82ddd2ec8
order: 23230
---

finfo_set_flags

finfo::set_flags

Establece opciones de configuración de libmagic

## Descripción

Estilo procedimental

```php
finfo_set_flags(finfo $finfo, int $flags): true
```php

Estilo orientado a objetos

```php
public finfo::set_flags(int $flags): true
```

Esta función establece diversas opciones de Fileinfo. Las opciones pueden ser también establecidas directamente en `finfo_open` o por otras funciones Fileinfo.

## Parámetros

`finfo`  
Una instancia `finfo`, retornada por `finfo_open`.

`flags`  
Una o una unión de varias [constantes Fileinfo](#fileinfo.constants).

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `finfo` ahora espera una instancia de `finfo` ; anteriormente, una `resource` era esperado. |
