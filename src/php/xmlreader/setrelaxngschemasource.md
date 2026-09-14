---
title: XMLReader::setRelaxNGSchemaSource
description: Establece los datos contenidos en un esquema RelaxNG
source_url: https://www.php.net/manual/es/xmlreader.setrelaxngschemasource.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/setrelaxngschemasource.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103330
---

XMLReader::setRelaxNGSchemaSource

Establece los datos contenidos en un esquema RelaxNG

## Descripción

```php
public XMLReader::setRelaxNGSchemaSource(string $source): bool
```php

Establece los datos contenidos en un esquema RelaxNG a usar para validación.

## Parámetros

`source`  
SCadena que contiene el esquema RelaxNG.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

XMLReader::setRelaxNGSchema, XMLReader::setSchema, XMLReader::isValid
