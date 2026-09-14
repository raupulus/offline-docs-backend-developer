---
title: xml_parse
description: Inicia el análisis de un documento XML
source_url: https://www.php.net/manual/es/function.xml-parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: b47e4bea1
order: 102730
---

xml_parse

Inicia el análisis de un documento XML

## Descripción

```php
xml_parse(XMLParser $parser, string $data, [bool $is_final]): int
```php

`xml_parse` analiza un documento XML. Los gestores para los eventos configurados son llamados tantas veces como sea necesario.

## Parámetros

`parser`  
Una referencia al analizador XML a utilizar.

`data`  
Una parte de los datos a analizar. Un documento puede ser analizado por partes mediante llamadas sucesivas a `xml_parse` con nuevos datos, siempre que el parámetro `is_final` esté definido como `true` cuando se analicen los últimos datos.

`is_final`  
Si está definido y vale `true`, `data` será el último fragmento de datos enviado al analizador.

## Valores devueltos

Devuelve 1 en caso de éxito o 0 en caso de fallo.

En caso de fallo en el análisis, la causa del error puede obtenerse mediante las funciones `xml_get_error_code`, `xml_error_string`, `xml_get_current_line_number`, `xml_get_current_column_number` y `xml_get_current_byte_index`.

> [!NOTE]
> Algunos errores (incluyendo errores de entidades) son reportados al final de los datos, esto únicamente si `is_final` vale `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |

## Ejemplos

Análisis de documentos XML grandes por partes

Este ejemplo muestra cómo los documentos XML grandes pueden ser leídos y analizados por partes, permitiendo así no mantener en memoria la totalidad del documento. No se ha establecido ningún gestor de errores para hacer el ejemplo más conciso.

```
<?php
$stream = fopen('examples/book-simple.xml', 'r');
$parser = xml_parser_create();

xml_set_element_handler(
    $parser,
    function($parser, $name, $attributes) { echo $name, PHP_EOL; },
    function($parser, $name) { echo $name, PHP_EOL; }
);

while (($data = fread($stream, 16384))) {
    xml_parse($parser, $data); // análisis de la parte actual
}
xml_parse($parser, '', true); // finalización del análisis
fclose($stream);

   
```php
