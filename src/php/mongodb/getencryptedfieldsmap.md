---
title: MongoDB\Driver\Manager::getEncryptedFieldsMap
description: Devuelve la opción de cifrado automático encryptedFieldsMap para el Manager
source_url: https://www.php.net/manual/es/mongodb-driver-manager.getencryptedfieldsmap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/getencryptedfieldsmap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49790
---

MongoDB\Driver\Manager::getEncryptedFieldsMap

Devuelve la opción de cifrado automático encryptedFieldsMap para el Manager

## Descripción

```php
final public MongoDB\Driver\Manager::getEncryptedFieldsMap(): array
```php

Devuelve la opción de cifrado automático `encryptedFieldsMap` para el Manager, si se ha especificado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La opción de cifrado automático `encryptedFieldsMap` para el Manager, o `null` si no se ha especificado.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Manager::\_\_construct
