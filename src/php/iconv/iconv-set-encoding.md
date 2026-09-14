---
title: iconv_set_encoding
description: Modifica el juego de caracteres de codificación actual
source_url: https://www.php.net/manual/es/function.iconv-set-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv-set-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: ab9a7d2e3
order: 31210
---

iconv_set_encoding

Modifica el juego de caracteres de codificación actual

## Descripción

```php
iconv_set_encoding(string $type, string $encoding): bool
```php

Modifica el juego de caracteres actual, y reemplaza el valor actual del argumento `type` por `encoding`.

## Parámetros

`type`  
Los valores posibles de `type` son : input_encoding, output_encoding, internal_encoding

`encoding`  
El juego de caracteres.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `iconv_set_encoding`

```
<?php
iconv_set_encoding("internal_encoding", "UTF-8");
iconv_set_encoding("output_encoding", "ISO-8859-1");
?>

    
```php

## Véase también

`iconv_get_encoding`, `ob_iconv_handler`
