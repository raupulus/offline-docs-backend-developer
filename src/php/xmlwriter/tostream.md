---
title: XMLWriter::toStream
description: Crear un nuevo XMLWriter utilizando un flujo para la salida
source_url: https://www.php.net/manual/es/xmlwriter.tostream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/tostream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: true
translation_revision: fecb2f5bb
order: 103860
---

XMLWriter::toStream

Crear un nuevo

XMLWriter

utilizando un flujo para la salida

## Descripción

```php
public static XMLWriter::toStream(resource $stream): static
```php

Crear un nuevo `XMLWriter` utilizando un flujo para la salida.

## Parámetros

`stream`  
El flujo a utilizar para la salida.

## Valores devueltos

Devuelve un `XMLWriter`.

## Errores/Excepciones

- Pasar un recurso que no sea un flujo a `stream` lanzará una TypeError.

## Véase también

XMLWriter::toMemory

XMLWriter::toUri
