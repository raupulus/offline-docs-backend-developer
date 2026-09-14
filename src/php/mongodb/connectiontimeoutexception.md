---
title: La clase MongoDB\Driver\Exception\ConnectionTimeoutException
source_url: https://www.php.net/manual/es/class.mongodb-driver-exception-connectiontimeoutexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/connectiontimeoutexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49560
---

## Introducción

Se lanza cuando el controlador no logra establecer una conexión con la base de datos dentro del límite de tiempo especificado ([connectTimeoutMS](#mongodb-driver-manager.construct-urioptions)) o falla la selección del servidor ([serverSelectionTimeoutMS](#mongodb-driver-manager.construct-urioptions)).

## Sinopsis de la clase

MongoDB\Driver\Exception\ConnectionTimeoutException

final

MongoDB\Driver\Exception\ConnectionTimeoutException

extends

MongoDB\Driver\Exception\ConnectionException

MongoDB\Driver\Exception\Exception

Propiedades heredadas

Métodos heredados
