---
title: MongoDB\Driver\Session::commitTransaction
description: Valida la transacción
source_url: https://www.php.net/manual/es/mongodb-driver-session.committransaction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/committransaction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 51280
---

MongoDB\Driver\Session::commitTransaction

Valida la transacción

## Descripción

```php
final public MongoDB\Driver\Session::commitTransaction(): void
```php

Guarda los cambios realizados por las operaciones en la transacción multi-documento y finaliza la transacción. Hasta la validación, ninguno de los cambios de datos realizados por las operaciones en la transacción es visible fuera de la transacción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\CommandException

si el servidor no puede validar la transacción (por ejemplo, debido a conflictos, problemas de red). Si la excepción contiene un elemento

"errorLabels"

y este array contiene un valor

"TransientTransactionError"

o

"UnknownTransactionCommitResult"

, es seguro reintentar la

totalidad

de la transacción. En versiones más recientes de la extensión,

MongoDB\Driver\Exception\RuntimeException::hasErrorLabel

debería ser utilizado para probar esta situación en su lugar.

Lanza una

MongoDB\Driver\Exception\RuntimeException

si la transacción no puede ser validada (por ejemplo, una transacción no ha sido iniciada).

## Véase también

MongoDB\Driver\Manager::startSession

MongoDB\Driver\Session::abortTransaction

MongoDB\Driver\Session::startTransaction

MongoDB\Driver\Exception\RuntimeException::hasErrorLabel
