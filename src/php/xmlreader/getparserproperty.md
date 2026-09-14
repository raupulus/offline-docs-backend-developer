---
title: XMLReader::getParserProperty
description: Indica si la porpiedad especificada ha sido establecida
source_url: https://www.php.net/manual/es/xmlreader.getparserproperty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/getparserproperty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103160
---

XMLReader::getParserProperty

Indica si la porpiedad especificada ha sido establecida

## Descripción

```php
public XMLReader::getParserProperty(int $property): bool
```php

Indica si la porpiedad especificada ha sido establecida.

## Parámetros

`property`  
Una de las [constantes analizadoras de opción](#xmlreader.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

XMLReader::setParserProperty
