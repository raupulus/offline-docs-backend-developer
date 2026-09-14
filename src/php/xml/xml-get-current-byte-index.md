---
title: xml_get_current_byte_index
description: Devuelve el índice del byte actual de un analizador XML
source_url: https://www.php.net/manual/es/function.xml-get-current-byte-index.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-get-current-byte-index.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 5dc10a2e5
order: 102680
---

xml_get_current_byte_index

Devuelve el índice del byte actual de un analizador XML

## Descripción

```php
xml_get_current_byte_index(XMLParser $parser): int
```php

Devuelve el índice del byte actual del analizador XML dado.

## Parámetros

`parser`  
Una referencia a un analizador XML válido.

## Valores devueltos

`xml_get_current_byte_index` devuelve el índice del byte de análisis actual del analizador XML (comienza en 0).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |

## Notas

> [!WARNING]
> Esta función devuelve el índice del byte de acuerdo con el texto codificado en UTF-8 incluso si la entrada está en otra codificación.

## Véase también

`xml_get_current_column_number`, `xml_get_current_line_number`
