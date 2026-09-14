---
title: xml_get_current_column_number
description: Devuelve el número de columna actual de un analizador XML
source_url: https://www.php.net/manual/es/function.xml-get-current-column-number.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-get-current-column-number.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 462e61626
order: 102690
---

xml_get_current_column_number

Devuelve el número de columna actual de un analizador XML

## Descripción

```php
xml_get_current_column_number(XMLParser $parser): int
```php

Devuelve el número de columna actual del analizador XML dado.

## Parámetros

`parser`  
Una referencia a un analizador XML válido.

## Valores devueltos

`xml_get_current_column_number` devuelve el número de columna actual de la línea actual del analizador, que corresponde a la posición de análisis actual del analizador XML (como devuelto por `xml_get_current_line_number`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |

## Véase también

`xml_get_current_byte_index`, `xml_get_current_line_number`
