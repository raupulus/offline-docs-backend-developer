---
title: Nuevas Funciones
source_url: https://www.php.net/manual/es/migration81.new-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration81/new-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: fa107f441
order: 890
---

## Nuevas Funciones

## Núcleo de PHP

- `array_is_list`

## GD

- `imagecreatefromavif`

- `imageavif`

## MySQLi

- `mysqli_result::fetch_column`

- `mysqli_fetch_column`

## Control de Procesos

- `pcntl_rfork`

## Reflexión

- ReflectionFunctionAbstract::getClosureUsedVariables

## Estándar

- `fsync`

- `fdatasync`

## Sodium

### XChaCha20

- `sodium_crypto_stream_xchacha20`

- `sodium_crypto_stream_xchacha20_keygen`

- `sodium_crypto_stream_xchacha20_xor`

### Ristretto255

Las funciones Ristretto255 están disponibles desde libsodium 1.0.18.

- `sodium_crypto_core_ristretto255_add`

- `sodium_crypto_core_ristretto255_from_hash`

- `sodium_crypto_core_ristretto255_is_valid_point`

- `sodium_crypto_core_ristretto255_random`

- `sodium_crypto_core_ristretto255_scalar_add`

- `sodium_crypto_core_ristretto255_scalar_complement`

- `sodium_crypto_core_ristretto255_scalar_invert`

- `sodium_crypto_core_ristretto255_scalar_mul`

- `sodium_crypto_core_ristretto255_scalar_negate`

- `sodium_crypto_core_ristretto255_scalar_random`

- `sodium_crypto_core_ristretto255_scalar_reduce`

- `sodium_crypto_core_ristretto255_scalar_sub`

- `sodium_crypto_core_ristretto255_sub`

- `sodium_crypto_scalarmult_ristretto255`

- `sodium_crypto_scalarmult_ristretto255_base`
