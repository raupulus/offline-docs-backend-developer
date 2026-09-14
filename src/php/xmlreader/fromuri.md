---
title: XMLReader::fromUri
description: Crear un XMLReader a partir de una URI para leer
source_url: https://www.php.net/manual/es/xmlreader.fromuri.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/fromuri.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: true
translation_revision: 2df06506a
order: 103120
---

XMLReader::fromUri

Crear un

XMLReader

a partir de una URI para leer

## Descripción

```php
public static XMLReader::fromUri(string $uri, [string $encoding], [int $flags]): static
```php

Crear una instancia de `XMLReader` a partir de una URI para leer.

## 

## Valores devueltos

Devuelve un `XMLReader`.

## Errores/Excepciones

- Pasar un `uri` inválido lanzará una ValueError.

## Véase también

XMLReader::fromStream

XMLReader::fromString
