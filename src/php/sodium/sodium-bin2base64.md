---
title: sodium_bin2base64
description: Codifica una string binaria bruta en base64.
source_url: https://www.php.net/manual/es/function.sodium-bin2base64.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-bin2base64.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 75980
---

sodium_bin2base64

Codifica una string binaria bruta en base64.

## Descripción

```php
#[\SensitiveParameter] sodium_bin2base64(string $string, int $id): string
```php

Convierte una string binaria bruta en una string codificada en base64. A diferencia de `base64_encode`, `sodium_bin2base64` es de tiempo constante (una propiedad importante para cualquier código que manipule entradas criptográficas, como textos en claro o claves) y admite varios conjuntos de caracteres.

## Parámetros

`string`  
La string binaria bruta.

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

## Valores devueltos

La string codificada en base64.
