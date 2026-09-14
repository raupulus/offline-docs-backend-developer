---
title: MongoDB\Driver\Exception Clases de excepciones
source_url: https://www.php.net/manual/es/mongodb.exceptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/exceptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48740
---

## Clases de excepciones

La jerarquía de clases para las excepciones de MongoDB está modelada siguiendo la de las [excepciones SPL](#spl.exceptions). Las clases base extienden su contraparte de SPL y todas las clases de excepciones en la extensión implementan la interfaz `MongoDB\Driver\Exception\Exception`.

- `MongoDB\Driver\Exception\LogicException` (extiende `LogicException`)

- `MongoDB\Driver\Exception\InvalidArgumentException` (extiende `InvalidArgumentException`)

- `MongoDB\Driver\Exception\UnexpectedValueException` (extiende `UnexpectedValueException`)

- `MongoDB\Driver\Exception\RuntimeException` (extiende `RuntimeException`)

  - `MongoDB\Driver\Exception\ConnectionException`

    - `MongoDB\Driver\Exception\AuthenticationException`

    - `MongoDB\Driver\Exception\ConnectionTimeoutException`

    - `MongoDB\Driver\Exception\SSLConnectionException` (obsoleto)

  - `MongoDB\Driver\Exception\EncryptionException`

  - `MongoDB\Driver\Exception\ServerException`

    - `MongoDB\Driver\Exception\BulkWriteCommandException`

    - `MongoDB\Driver\Exception\CommandException`

    - `MongoDB\Driver\Exception\ExecutionTimeoutException`

    - `MongoDB\Driver\Exception\WriteException` (obsoleto)

      - `MongoDB\Driver\Exception\BulkWriteException`
