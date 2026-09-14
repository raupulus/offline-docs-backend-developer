---
title: get_extension_funcs
description: Lista las funciones de una extensión
source_url: https://www.php.net/manual/es/function.get-extension-funcs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/get-extension-funcs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 99d758bd2
order: 38870
---

get_extension_funcs

Lista las funciones de una extensión

## Descripción

```php
get_extension_funcs(string $extension): array
```php

Devuelve el nombre de las funciones definidas en el módulo `extension`.

## Parámetros

`extension`  
El nombre del módulo.

> [!NOTE]
> Este argumento debe estar en *minúsculas*.

## Valores devueltos

Devuelve un array que contiene todas las funciones, o `false` si `extension` no es una extensión válida.

## Ejemplos

Muestra todas las funciones XML

```
<?php
print_r(get_extension_funcs("xml"));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => xml_parser_create
        [1] => xml_parser_create_ns
        [2] => xml_set_object
        [3] => xml_set_element_handler
        [4] => xml_set_character_data_handler
        [5] => xml_set_processing_instruction_handler
        [6] => xml_set_default_handler
        [7] => xml_set_unparsed_entity_decl_handler
        [8] => xml_set_notation_decl_handler
        [9] => xml_set_external_entity_ref_handler
        [10] => xml_set_start_namespace_decl_handler
        [11] => xml_set_end_namespace_decl_handler
        [12] => xml_parse
        [13] => xml_parse_into_struct
        [14] => xml_get_error_code
        [15] => xml_error_string
        [16] => xml_get_current_line_number
        [17] => xml_get_current_column_number
        [18] => xml_get_current_byte_index
        [19] => xml_parser_free
        [20] => xml_parser_set_option
        [21] => xml_parser_get_option
    )

## Véase también

`get_loaded_extensions`, ReflectionExtension::getFunctions
