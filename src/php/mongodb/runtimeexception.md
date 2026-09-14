---
title: La clase MongoDB\Driver\Exception\RuntimeException
source_url: https://www.php.net/manual/es/class.mongodb-driver-exception-runtimeexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/runtimeexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49630
---

## Introducción

Se lanza cuando el controlador encuentra un error en tiempo de ejecución (por ejemplo, error interno de [libmongoc](https://github.com/mongodb/mongo-c-driver)).

## Sinopsis de la clase

MongoDB\Driver\Exception\RuntimeException

MongoDB\Driver\Exception\RuntimeException

extends

RuntimeException

MongoDB\Driver\Exception\Exception

Propiedades

protected

array

null

errorLabels

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`errorLabels`  
Contiene un array de etiquetas de error asociadas a una excepción. Por ejemplo, las etiquetas de error pueden usarse para detectar si una transacción puede volver a intentarse de forma segura si está presente la etiqueta `TransientTransactionError`. La existencia de una etiqueta de error específica debe verificarse con el método MongoDB\Driver\Exception\RuntimeException::hasErrorLabel, en lugar de interpretar manualmente esta propiedad `errorLabels`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.6.0 | Se han añadido el método MongoDB\Driver\Exception\RuntimeException::hasErrorLabel y la propiedad [MongoDB\Driver\Exception\RuntimeException::errorLabels](#mongodb-driver-exception-runtimeexception.props.errorlabels). |
