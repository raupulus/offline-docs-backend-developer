---
title: MongoDB\Driver\ClientEncryption::getKeys
description: Obtiene todos los documentos de claves
source_url: https://www.php.net/manual/es/mongodb-driver-clientencryption.getkeys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/clientencryption/getkeys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49180
---

MongoDB\Driver\ClientEncryption::getKeys

Obtiene todos los documentos de claves

## Descripción

```php
final public MongoDB\Driver\ClientEncryption::getKeys(): MongoDB\Driver\Cursor
```php

Busca todos los documentos de claves en la colección de almacén de claves.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna un `MongoDB\Driver\Cursor` en caso de éxito.

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
