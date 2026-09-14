---
title: sodium_crypto_kx_keypair
description: Crear una nueva pareja de claves sodium
source_url: https://www.php.net/manual/es/function.sodium-crypto-kx-keypair.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-kx-keypair.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76540
---

sodium_crypto_kx_keypair

Crear una nueva pareja de claves sodium

## Descripción

```php
sodium_crypto_kx_keypair(): string
```php

Crear una nueva pareja de claves sodium compuesta por la clave secreta (32 bytes) seguida de la clave pública (32 bytes). Las claves pueden ser recuperadas llamando a `sodium_crypto_kx_secretkey` y `sodium_crypto_kx_publickey`, respectivamente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la nueva pareja de claves en caso de éxito; lanza una excepción en caso contrario.

## Ejemplos

Uso de `sodium_crypto_kx_keypair`

Crear una nueva pareja de claves y recuperar la clave secreta y la clave pública asociada.

```
<?php
$keypair = sodium_crypto_kx_keypair();
$secret = sodium_crypto_kx_secretkey($keypair);
$public = sodium_crypto_kx_publickey($keypair);
printf("secret: %s\npublic: %s", sodium_bin2hex($secret), sodium_bin2hex($public));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    secret: e7c5c918fdc40762e6000542c0118f4368ce8fd242b0e48c1e17202797a25daf
    public: d1f59fda8652caf40ed1a01d2b6f3802b60846986372cd8fa337b7c12c428b18
