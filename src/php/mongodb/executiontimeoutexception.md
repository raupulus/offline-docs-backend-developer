---
title: La clase MongoDB\Driver\Exception\ExecutionTimeoutException
source_url: https://www.php.net/manual/es/class.mongodb-driver-exception-executiontimeoutexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/executiontimeoutexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49590
---

## Introducción

Se lanza cuando una consulta o comando no logra completarse dentro del tiempo límite especificado (por ejemplo, [maxTimeMS](https://www.mongodb.com/docs/manual/tutorial/terminate-running-operations/#maxtimems)).

## Sinopsis de la clase

MongoDB\Driver\Exception\ExecutionTimeoutException

final

MongoDB\Driver\Exception\ExecutionTimeoutException

extends

MongoDB\Driver\Exception\ServerException

MongoDB\Driver\Exception\Exception

Propiedades heredadas

Métodos heredados

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.5.0 | Esta clase ahora extiende `MongoDB\Driver\Exception\ServerException` en lugar de `MongoDB\Driver\Exception\RuntimeException`. |
