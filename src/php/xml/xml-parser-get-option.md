---
title: xml_parser_get_option
description: Lee las opciones de un analizador XML
source_url: https://www.php.net/manual/es/function.xml-parser-get-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-parser-get-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 9acfa1897
order: 102770
---

xml_parser_get_option

Lee las opciones de un analizador XML

## Descripción

```php
xml_parser_get_option(XMLParser $parser, int $option): string
```php

Lee las opciones de un analizador XML.

## Parámetros

`parser`  
Una referencia a un analizador XML válido.

`option`  
La opción solicitada. `XML_OPTION_CASE_FOLDING`, `XML_OPTION_PARSE_HUGE`, `XML_OPTION_SKIP_TAGSTART`, `XML_OPTION_SKIP_WHITE` y `XML_OPTION_TARGET_ENCODING` están disponibles. Consulte `xml_parser_set_option` para sus descripciones.

## Valores devueltos

Devuelve el valor de la opción.

## Errores/Excepciones

Genera un `ValueError` cuando se pasa un valor inválido a `option`.

Anterior a PHP 8.0.0, pasar un valor inválido a `option` generaba asimismo un aviso `E_WARNING` y hacía que la función devolviera `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | La función devuelve ahora un booleano para las opciones booleanas. |
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |
| 8.0.0 | Un `ValueError` es generado ahora si `option` es inválido. |
| 7.1.24, 7.2.12, 7.3.0 | `options` soporta ahora `XML_OPTION_SKIP_TAGSTART` y `XML_OPTION_SKIP_WHITE`. |
