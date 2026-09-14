---
title: MongoDB\Driver\ClientEncryption::addKeyAltName
description: Añade un nombre alternativo a un documento de clave
source_url: https://www.php.net/manual/es/mongodb-driver-clientencryption.addkeyaltname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/clientencryption/addkeyaltname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49090
---

MongoDB\Driver\ClientEncryption::addKeyAltName

Añade un nombre alternativo a un documento de clave

## Descripción

```php
final public MongoDB\Driver\ClientEncryption::addKeyAltName(MongoDB\BSON\Binary $keyId, string $keyAltName): object
```php

Añade `keyAltName` al conjunto de nombres alternativos para el documento de clave con el UUID dado `keyId`.

## Parámetros

`keyId`  
Una instancia de `MongoDB\BSON\Binary` con subtipo 4 (UUID) que identifica el documento de clave.

`keyAltName`  
Nombre alternativo que se añadirá al documento de clave.

## Valores devueltos

Devuelve la versión anterior del documento de clave, o `null` si no se encontró ningún documento coincidente.

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

## Véase también

MongoDB\Driver\ClientEncryption::getKeyByAltName

MongoDB\Driver\ClientEncryption::removeKeyAltName
