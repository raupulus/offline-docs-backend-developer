---
title: MongoDB\Driver\Session::advanceClusterTime
description: Avance el tiempo del cluster para esta sesión
source_url: https://www.php.net/manual/es/mongodb-driver-session.advanceclustertime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/advanceclustertime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51260
---

MongoDB\Driver\Session::advanceClusterTime

Avance el tiempo del cluster para esta sesión

## Descripción

```php
final public MongoDB\Driver\Session::advanceClusterTime(array $clusterTime): void
```php

Avance el tiempo del cluster para esta sesión. Si el tiempo del cluster es inferior o igual al tiempo del cluster actual de la sesión, esta función no hace nada.

Al utilizar este método en conjunción con MongoDB\Driver\Session::advanceOperationTime para copiar los tiempos del cluster y de las operaciones de otra sesión se puede asegurar que las operaciones en esta sesión sean coherentes con la última operación en la otra sesión.

## Parámetros

`clusterTime`  
El tiempo del cluster es un documento que contiene un horodatage lógico y una firma de servidor. Típicamente, este valor se obtendrá llamando a MongoDB\Driver\Session::getClusterTime en otro objeto de sesión.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Session::advanceOperationTime

MongoDB\Driver\Session::getClusterTime
