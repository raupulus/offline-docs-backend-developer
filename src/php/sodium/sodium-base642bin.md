---
title: sodium_base642bin
description: Decodifica una cadena codificada en base64 en binario sin tratar.
source_url: https://www.php.net/manual/es/function.sodium-base642bin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-base642bin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 75970
---

sodium_base642bin

Decodifica una cadena codificada en base64 en binario sin tratar.

## Descripción

```php
#[\SensitiveParameter] sodium_base642bin(string $string, int $id, [string $ignore]): string
```php

Convierte una cadena codificada en base64 en binario sin tratar. A diferencia de `base64_decode`, `sodium_base642bin` es de tiempo constante (una propiedad importante para cualquier código que manipule entradas criptográficas, tales como textos en claro o claves) y soporta múltiples conjuntos de caracteres.

## Parámetros

`string`  
`string`; Cadena codificada.

`id`  
SODIUM_BASE64_VARIANT_ORIGINAL

para el estándar (

A-Za-z0-9/\\

) codificado en base64.

SODIUM_BASE64_VARIANT_ORIGINAL_NO_PADDING

para el estándar (

A-Za-z0-9/\\

) codificado en base64, sin caracteres de relleno

=

.

SODIUM_BASE64_VARIANT_URLSAFE

para la codificación Base64 segura para URL (

A-Za-z0-9\\\_

).

SODIUM_BASE64_VARIANT_URLSAFE_NO_PADDING

para la codificación Base64 segura para URL (

A-Za-z0-9\\\_

), sin caracteres de relleno

=

.

`ignore`  
Los caracteres a ignorar durante la decodificación (por ejemplo, los caracteres de espaciado).

## Valores devueltos

La cadena decodificada.
