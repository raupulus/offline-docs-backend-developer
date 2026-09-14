---
title: xml_parser_set_option
description: Establece las opciones de un analizador XML
source_url: https://www.php.net/manual/es/function.xml-parser-set-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-parser-set-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 102780
---

xml_parser_set_option

Establece las opciones de un analizador XML

## Descripción

```php
xml_parser_set_option(XMLParser $parser, int $option, string $value): bool
```php

Establece las opciones de un analizador XML.

## Parámetros

`parser`  
Una referencia a un analizador XML.

`option`  
La opción a modificar. Ver más abajo.

Las siguientes opciones están disponibles:

| Opción | Tipo de datos | Descripción |
|----|----|----|
| `XML_OPTION_CASE_FOLDING` | bool | Controla el manejo de la [caja](#xml.case-folding) de las etiquetas de este analizador XML. Por omisión, está activado. |
| `XML_OPTION_PARSE_HUGE` | bool | Permite analizar documentos de más de 10 MB. Esta opción solo debe activarse si el tamaño del documento está limitado, ya que de lo contrario podría conducir a un ataque de denegación de servicio (DoS). Esta opción solo está disponible al usar libxml2. |
| `XML_OPTION_SKIP_TAGSTART` | bool | Especifica cuántos caracteres deben omitirse al inicio del nombre de la etiqueta. |
| `XML_OPTION_SKIP_WHITE` | `int` | Omite o no los valores que contienen caracteres en blanco. |
| `XML_OPTION_TARGET_ENCODING` | string | Modifica la [codificación de destino](#xml.encoding) utilizada por este analizador XML. Por omisión, es la que se especificó al llamar a `xml_parser_create`. Las codificaciones soportadas son `ISO-8859-1`, `US-ASCII` y `UTF-8`. |

Opciones del analizador XML

`value`  
El nuevo valor de la opción.

## Valores devueltos

Devuelve `true` en caso de éxito o `false` en caso de fallo.

## Errores/Excepciones

Lanza una `ValueError` cuando se pasa un valor inválido a `option`.

Antes de PHP 8.0.0, pasar un valor inválido a `option` generaba una advertencia `E_WARNING` y hacía que la función devolviera el valor `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se añadió la opción `XML_OPTION_PARSE_HUGE`. |
| 8.3.0 | El parámetro `value` ahora también acepta valores booleanos. Las opciones `XML_OPTION_CASE_FOLDING` y `XML_OPTION_SKIP_WHITE` ahora son opciones booleanas. |
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |
| 8.0.0 | Ahora se lanza una excepción `ValueError` si la `option` es inválida. |
