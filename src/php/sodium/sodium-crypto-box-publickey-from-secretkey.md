---
title: sodium_crypto_box_publickey_from_secretkey
description: Calcula la clave pública a partir de una clave secreta
source_url: https://www.php.net/manual/es/function.sodium-crypto-box-publickey-from-secretkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-box-publickey-from-secretkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 76260
---

sodium_crypto_box_publickey_from_secretkey

Calcula la clave pública a partir de una clave secreta

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_box_publickey_from_secretkey(string $secret_key): string
```php

Dada una clave secreta, se calcula la clave pública correspondiente.

Esto solo funciona con el tipo de claves destinadas a ser utilizadas con `crypto_box` (que utiliza el intercambio de claves de Diffie-Hellman sobre la curva de Montgomery, Curve25519; abreviado X25519), no con `crypto_sign` (que utiliza el algoritmo de firma digital de Edwards sobre la curva de Edwards con los parámetros correspondientes; abreviado Ed25519).

## Parámetros

`secret_key`  
La clave secreta X25519

## Valores devueltos

La clave pública X25519.
