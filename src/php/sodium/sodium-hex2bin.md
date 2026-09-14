---
title: sodium_hex2bin
description: Decodifica una cadena binaria codificada en hexadecimal
source_url: https://www.php.net/manual/es/function.sodium-hex2bin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-hex2bin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 77000
---

sodium_hex2bin

Decodifica una cadena binaria codificada en hexadecimal

## Descripción

```php
#[\SensitiveParameter] sodium_hex2bin(string $string, [string $ignore]): string
```php

Decodifica una cadena binaria codificada en hexadecimal.

Al igual que `sodium_bin2hex`, `sodium_hex2bin` son resistentes a ataques por canales secundarios, mientras que `hex2bin` no lo es.

## Parámetros

`string`  
La representación hexadecimal de los datos.

`ignore`  
Una cadena de caracteres opcional para los caracteres a ignorar.

## Valores devueltos

Devuelve la representación binaria de los datos de la cadena `string`.
