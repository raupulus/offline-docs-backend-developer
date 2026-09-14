---
title: MongoDB\Driver\Exception\RuntimeException::hasErrorLabel
description: Devuelve si un label de error está asociado con una excepción
source_url: https://www.php.net/manual/es/mongodb-driver-runtimeexception.haserrorlabel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/runtimeexception/haserrorlabel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49620
---

MongoDB\Driver\Exception\RuntimeException::hasErrorLabel

Devuelve si un label de error está asociado con una excepción

## Descripción

```php
final public MongoDB\Driver\Exception\RuntimeException::hasErrorLabel(string $errorLabel): bool
```php

Devuelve si el `errorLabel` ha sido definido para esta excepción. Los labels de error son definidos por el servidor o por la extensión para indicar situaciones específicas donde se desea decidir cómo manejar una excepción específica. Una situación común sería determinar si se puede relanzar una transacción que ha fallado debido a un error pasajero (como un error de red o un conflicto de transacción) sin problemas. Ejemplos de labels de error son `TransientTransactionError` y `UnknownTransactionCommitResult`.

## Parámetros

`errorLabel`  
El nombre del `errorLabel` a verificar.

## Valores devueltos

Si el `errorLabel` proporcionado está asociado con esta excepción.

## Véase también

MongoDB\Driver\Session::commitTransaction

Documentación de MongoDB sobre las transacciones
