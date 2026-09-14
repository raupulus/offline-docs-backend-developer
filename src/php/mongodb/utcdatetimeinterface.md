---
title: La interfaz MongoDB\BSON\UTCDateTimeInterface
source_url: https://www.php.net/manual/es/class.mongodb-bson-utcdatetimeinterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/utcdatetimeinterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48690
---

## Introducción

Esta interfaz es implementada por `MongoDB\BSON\UTCDateTime` para ser utilizada como un parámetro, retorno, o tipo de propiedad en clases de usuario.

## Sinopsis de la clase

MongoDB\BSON\UTCDateTimeInterface

MongoDB\BSON\UTCDateTimeInterface

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Los tipos de retorno previamente declarados como provisionales ahora son aplicados. |
| PECL mongodb 1.15.0 | Los tipos de retorno de los métodos son declarados como provisionales en PHP 8.0 y posteriores, lo que desencadena avisos de depreciación en el código que implementa esta interfaz sin declarar los tipos de retorno apropiados. El atributo `#[ReturnTypeWillChange]` puede ser añadido para ignorar la notificación de depreciación. |
