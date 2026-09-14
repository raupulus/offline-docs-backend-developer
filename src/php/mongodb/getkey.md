---
title: MongoDB\Driver\ClientEncryption::getKey
description: Obtiene un documento de clave
source_url: https://www.php.net/manual/es/mongodb-driver-clientencryption.getkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/clientencryption/getkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49160
---

MongoDB\Driver\ClientEncryption::getKey

Obtiene un documento de clave

## Descripción

```php
final public MongoDB\Driver\ClientEncryption::getKey(MongoDB\BSON\Binary $keyId): object
```php

Busca un único documento de clave en la colección de almacén de claves con el UUID `keyId` proporcionado.

## Parámetros

`keyId`  
Una instancia de `MongoDB\BSON\Binary` con subtipo 4 (UUID) que identifica el documento de clave.

## Valores devueltos

Devuelve el documento de clave, o `null` si no se encontró ningún documento.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\ConnectionException

si la conexión al servidor falla por una razón distinta a un problema de identificación

Lanza una excepción

MongoDB\Driver\Exception\AuthenticationException

si se requiere una identificación pero falla

Lanza

MongoDB\Driver\Exception\RuntimeException

en caso de otros errores.
