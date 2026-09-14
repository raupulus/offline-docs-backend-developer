---
title: MongoDB\Driver\Session::endSession
description: Termina una sesión
source_url: https://www.php.net/manual/es/mongodb-driver-session.endsession.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/endsession.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51300
---

MongoDB\Driver\Session::endSession

Termina una sesión

## Descripción

```php
final public MongoDB\Driver\Session::endSession(): void
```php

Este método cierra una sesión existente. Si una transacción estaba asociada a esta sesión, la transacción será anulada. Después de llamar a este método, las aplicaciones no deben invocar otros métodos en la sesión.

> [!NOTE]
> Las sesiones también se cierran durante la recolección de basura. No debería ser necesario llamar a este método en circunstancias normales.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Manager::startSession

MongoDB\Driver\Session::abortTransaction

MongoDB\Driver\Session::commitTransaction

MongoDB\Driver\Session::startTransaction
