---
title: xml_parser_create
description: Creación de un analizador XML
source_url: https://www.php.net/manual/es/function.xml-parser-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-parser-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: false
translation_revision: b47e4bea1
order: 102750
---

xml_parser_create

Creación de un analizador XML

## Descripción

```php
xml_parser_create([string $encoding]): XMLParser
```php

`xml_parser_create` crea un analizador XML y devuelve una instancia de `XMLParser` para ser utilizada con las demás funciones XML.

## Parámetros

`encoding`  
La codificación de entrada se detecta automáticamente, por lo que el argumento `encoding` solo especifica la codificación de salida. Si se pasa una cadena vacía, el analizador intenta identificar en qué codificación está codificado el documento examinando los 3 o 4 octetos superiores. El juego de caracteres de salida por omisión es UTF-8. Las codificaciones admitidas son `ISO-8859-1`, `UTF-8`, y `US-ASCII`.

## Valores devueltos

Devuelve una nueva instancia de `XMLParser`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función devuelve ahora una instancia de `XMLParser`; anteriormente, se devolvía un `resource`, o `false` si ocurre un error. |
| 8.0.0 | `encoding` es ahora nullable. |

## Véase también

`xml_parser_create_ns`
