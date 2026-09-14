---
title: xml_get_error_code
description: Obtiene el código de error del analizador XML
source_url: https://www.php.net/manual/es/function.xml-get-error-code.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-get-error-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 7b841d339
order: 102710
---

xml_get_error_code

Obtiene el código de error del analizador XML

## Descripción

```php
xml_get_error_code(XMLParser $parser): int
```php

Obtiene el código de error del analizador XML.

## Parámetros

`parser`  
Una referencia a un analizador XML válido.

## Valores devueltos

`xml_get_error_code` devuelve uno de los códigos de error listados en la sección [sobre los códigos de error](#xml.error-codes).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |

## Véase también

`xml_error_string`
