---
title: MongoDB\Driver\Cursor::next
description: Avanza el cursor al siguiente resultado
source_url: https://www.php.net/manual/es/mongodb-driver-cursor.next.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursor/next.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49300
---

MongoDB\Driver\Cursor::next

Avanza el cursor al siguiente resultado

## Descripción

```php
public MongoDB\Driver\Cursor::next(): void
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Mueve la posición actual al siguiente elemento del cursor.

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

## Véase también

Iterator::next
