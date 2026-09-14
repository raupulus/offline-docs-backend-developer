---
title: XMLReader::setRelaxNGSchema
description: Establece el nomb re del archivo o el URI para un esquema RelaxNG
source_url: https://www.php.net/manual/es/xmlreader.setrelaxngschema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/setrelaxngschema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103320
---

XMLReader::setRelaxNGSchema

Establece el nomb re del archivo o el URI para un esquema RelaxNG

## Descripción

```php
public XMLReader::setRelaxNGSchema(string $filename): bool
```php

Establece el nomb re del archivo o el URI para un esquema RelaxNG a usar para validación.

## Parámetros

`filename`  
El nombre del archivo o apuntador URI a un esquema RelaxNG.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

XMLReader::setRelaxNGSchemaSource, XMLReader::setSchema, XMLReader::isValid
