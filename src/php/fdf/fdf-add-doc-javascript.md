---
title: fdf_add_doc_javascript
description: Añade código javascript a un documento FDF
source_url: https://www.php.net/manual/es/function.fdf-add-doc-javascript.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-add-doc-javascript.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22350
---

fdf_add_doc_javascript

Añade código javascript a un documento FDF

## Descripción

```php
fdf_add_doc_javascript(resource $fdf_document, string $script_name, string $script_code): bool
```php

Añade el código javascript `script_code` al documento `fdfdoc`, que Acrobat añadirá a los scripts de nivel de documento, una vez importado el FDF.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`script_name`  
El nombre del script.

`script_code`  
El código del script. Se recomienda encarecidamente utilizar '\r' como separador de líneas en el código `script_code`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Adición de código JavaScript a un documento FDF

```
<?php
$fdf = fdf_create();
fdf_add_doc_javascript($fdf, "PlusOne", "function PlusOne(x)\r{\r  return x+1;\r}\r");
fdf_save($fdf);
?>

   
```php

Este ejemplo creará un documento FDF como el siguiente:

    %FDF-1.2
    %âãÏÓ
    1 0 obj
    <<
    /FDF << /JavaScript << /Doc [ (PlusOne)(function PlusOne\(x\)\r{\r  return x+1;\r}\r)] >> >>
    >>
    endobj
    trailer
    <<
    /Root 1 0 R

    >>
    %%EOF
