---
title: XMLReader::fromStream
description: Crear un XMLReader a partir de un flujo para leer
source_url: https://www.php.net/manual/es/xmlreader.fromstream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/fromstream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: true
translation_revision: 2f92a27cd
order: 103100
---

XMLReader::fromStream

Crear un

XMLReader

a partir de un flujo para leer

## Descripción

```php
public static XMLReader::fromStream(resource $stream, [string $encoding], [int $flags], [string $documentUri]): static
```php

Crear un `XMLReader` a partir de un flujo para leer.

## Parámetros

`stream`  
El flujo desde el cual leer el XML.

`encoding`  
La codificación del documento o `null`.

`flags`  
Una máscara de bits de las constantes `LIBXML_*`.

`documentUri`  
La URI base opcional del documento.

## Valores devueltos

Devuelve un `XMLReader`.

## Errores/Excepciones

- Pasar un `encoding` inválido lanzará una ValueError.

- Pasar un recurso que no sea un flujo a `stream` lanzará una TypeError.

## Véase también

XMLReader::fromString

XMLReader::fromUri
