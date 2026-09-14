---
title: lzf_decompress
description: Descompresión LZF
source_url: https://www.php.net/manual/es/function.lzf-decompress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/lzf/functions/lzf-decompress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: lzf
translation_status: ready
translation_reviewed: false
translation_revision: b274da1f1
order: 44220
---

lzf_decompress

Descompresión LZF

## Descripción

```php
lzf_decompress(string $data): string
```php

`lzf_compress` descomprime la cadena `data` dada que contiene los datos codificados en lzf.

## Parámetros

`data`  
La cadena comprimida.

## Valores devueltos

Devuelve los datos descomprimidos o `false` si ocurrió un error.

## Véase también

lzf_compress
