---
title: MongoDB\Driver\ClientEncryption::decrypt
description: Descifra un valor
source_url: https://www.php.net/manual/es/mongodb-driver-clientencryption.decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/clientencryption/decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49120
---

MongoDB\Driver\ClientEncryption::decrypt

Descifra un valor

## Descripción

```php
final public MongoDB\Driver\ClientEncryption::decrypt(MongoDB\BSON\Binary $value): mixed
```php

Descifra el valor.

## Parámetros

`value`  
Una instancia de `MongoDB\BSON\Binary` con subtipo 6 que contiene el valor cifrado.

## Valores devueltos

Devuelve el valor descifrado tal como fue pasado a `MongoDB\Driver\ClientEncryption::encrypt`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza

MongoDB\Driver\Exception\EncryptionException

si ocurre un error durante el descifrado del valor

## Véase también

MongoDB\Driver\ClientEncryption::encrypt
