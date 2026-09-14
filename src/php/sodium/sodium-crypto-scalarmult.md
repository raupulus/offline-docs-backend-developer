---
title: sodium_crypto_scalarmult
description: Calcula un secreto compartido a partir de una clave secreta y una clave
  pública
source_url: https://www.php.net/manual/es/function.sodium-crypto-scalarmult.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-scalarmult.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76690
---

sodium_crypto_scalarmult

Calcula un secreto compartido a partir de una clave secreta y una clave pública

## Descripción

```php
sodium_crypto_scalarmult(string $n, string $p): string
```php

Curva elíptica Diffie-Hellman. Calcula el escalar n veces el punto p, sobre una curva elíptica.

## Parámetros

`n`  
Escalar, que es típicamente una clave secreta.

`p`  
Un punto (coordenada x), que es típicamente una clave pública.

## Valores devueltos

Una string aleatoria de 32 bytes.
