---
title: XMLReader::setParserProperty
description: Establecer las opciones del analizador
source_url: https://www.php.net/manual/es/xmlreader.setparserproperty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/setparserproperty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: b94d63fc0
order: 103310
---

XMLReader::setParserProperty

Establecer las opciones del analizador

## Descripción

```php
public XMLReader::setParserProperty(int $property, bool $value): bool
```php

Establece las opciones del analizador. Las opciones deben ser establecidas después de llamar a XMLReader::open o a XMLReader::XML, y antes de la primera llamada a XMLReader::read.

## Parámetros

`property`  
Una de las [constantes de opción del analizador](#xmlreader.constants).

`value`  
Si se establece a `true` la opción será habilitada, de otra manera será deshabilitada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
