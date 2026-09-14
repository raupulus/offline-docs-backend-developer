---
title: ps_set_parameter
description: Establecer ciertos parámetros
source_url: https://www.php.net/manual/es/function.ps-set-parameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-set-parameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66030
---

ps_set_parameter

Establecer ciertos parámetros

## Descripción

```php
ps_set_parameter(resource $psdoc, string $name, string $value): bool
```php

Establece varios parámetros que son utilizados por muchas funciones. Los parámetros son por definción valores de tipo string.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`name`  
Para una lista de los posibles nombres véase la función `ps_get_parameter`.

`value`  
El valor del parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_get_parameters`, `ps_set_value`
