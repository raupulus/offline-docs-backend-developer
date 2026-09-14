---
title: xml_parser_create_ns
description: Crea un analizador XML
source_url: https://www.php.net/manual/es/function.xml-parser-create-ns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-parser-create-ns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: b47e4bea1
order: 102740
---

xml_parser_create_ns

Crea un analizador XML

## Descripción

```php
xml_parser_create_ns([string $encoding], [string $separator]): XMLParser
```php

`xml_parser_create_ns` crea un nuevo analizador XML con soporte para espacios de nombres y devuelve una instancia de `XMLParser` para ser utilizada con otras funciones XML.

## Parámetros

`encoding`  
El juego de caracteres es detectado automáticamente y, por lo tanto, el argumento `encoding` solo especifica la salida. El juego de caracteres de salida por omisión es UTF-8. Los juegos de caracteres soportados son `ISO-8859-1`, `UTF-8` y `US-ASCII`.

`separator`  
Con un analizador que soporta espacios de nombres, las etiquetas que son pasadas a las diferentes funciones de gestión estarán constituidas por el nombre del espacio y el nombre de la etiqueta, separados por la cadena `separator`.

## Valores devueltos

Devuelve una nueva instancia de `XMLParser`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función devuelve ahora una instancia de `XMLParser`; anteriormente, se devolvía un `resource`, o `false` si ocurre un error. |
| 8.0.0 | `encoding` es ahora nullable. |

## Véase también

`xml_parser_create`
