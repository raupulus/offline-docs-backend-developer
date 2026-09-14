---
title: XMLReader::fromString
description: Crear un XMLReader a partir de una cadena XML
source_url: https://www.php.net/manual/es/xmlreader.fromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/fromstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: true
translation_revision: 2df06506a
order: 103110
---

XMLReader::fromString

Crear un

XMLReader

a partir de una cadena XML

## Descripción

```php
public static XMLReader::fromString(string $source, [string $encoding], [int $flags]): static
```php

Crear un `XMLReader` a partir de una cadena XML.

## 

## Valores devueltos

Devuelve un `XMLReader`.

## Errores/Excepciones

- Pasar un `encoding` inválido lanzará una ValueError.

## Véase también

XMLReader::fromStream

XMLReader::fromUri
