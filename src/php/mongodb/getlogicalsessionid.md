---
title: MongoDB\Driver\Session::getLogicalSessionId
description: Devuelve el identificador de sesión lógica para esta sesión
source_url: https://www.php.net/manual/es/mongodb-driver-session.getlogicalsessionid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/getlogicalsessionid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51320
---

MongoDB\Driver\Session::getLogicalSessionId

Devuelve el identificador de sesión lógica para esta sesión

## Descripción

```php
final public MongoDB\Driver\Session::getLogicalSessionId(): object
```php

Devuelve el identificador de sesión lógica para esta sesión, que puede ser utilizado para identificar las operaciones de esta sesión en el servidor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador de sesión lógica para esta sesión.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
