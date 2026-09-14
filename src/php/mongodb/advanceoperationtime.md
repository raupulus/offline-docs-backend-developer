---
title: MongoDB\Driver\Session::advanceOperationTime
description: Avance el tiempo de operación para esta sesión
source_url: https://www.php.net/manual/es/mongodb-driver-session.advanceoperationtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/advanceoperationtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51270
---

MongoDB\Driver\Session::advanceOperationTime

Avance el tiempo de operación para esta sesión

## Descripción

```php
final public MongoDB\Driver\Session::advanceOperationTime(MongoDB\BSON\TimestampInterface $operationTime): void
```php

Avance el tiempo de operación para esta sesión. Si el tiempo de operación es inferior o igual al tiempo de operación actual de la sesión, esta función no hace nada.

Al utilizar este método en conjunción con MongoDB\Driver\Session::advanceClusterTime para copiar los tiempos de operación y de cluster de otra sesión se puede asegurar que las operaciones en esta sesión sean coherentes con la última operación en la otra sesión.

## Parámetros

`operationTime`  
La operación es un timestamp lógico. Típicamente, este valor será obtenido llamando a MongoDB\Driver\Session::getOperationTime en otro objeto de sesión.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Session::advanceClusterTime

MongoDB\Driver\Session::getClusterTime
