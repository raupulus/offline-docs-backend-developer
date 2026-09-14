---
title: libxml_get_errors
description: Lee el array de errores
source_url: https://www.php.net/manual/es/function.libxml-get-errors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/libxml/functions/libxml-get-errors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: libxml
translation_status: ready
translation_reviewed: false
translation_revision: fed368268
order: 43670
---

libxml_get_errors

Lee el array de errores

## Descripción

```php
libxml_get_errors(): array
```php

Devuelve un array de errores.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`libxml_get_errors` devuelve un array con los objetos `LibXMLError` que representan los errores, o bien un array vacío si no hay errores.

## Ejemplos

Ejemplo con `libxml_get_errors`

Este ejemplo muestra cómo crear un gestor de errores libxml simple.

```
<?php

libxml_use_internal_errors(true);

$xmlstr = <<< XML

<movies>
 <movie>
  <titles>PHP: Behind the Parser</title>
 </movie>
</movies>
XML;

$doc = simplexml_load_string($xmlstr);
$xml = explode("\n", $xmlstr);

if ($doc === false) {
    $errors = libxml_get_errors();

    foreach ($errors as $error) {
        echo display_xml_error($error, $xml);
    }

    libxml_clear_errors();
}

function display_xml_error($error, $xml)
{
    $return  = $xml[$error->line - 1] . "\n";
    $return .= str_repeat('-', $error->column) . "^\n";

    switch ($error->level) {
        case LIBXML_ERR_WARNING:
            $return .= "Advertencia $error->code: ";
            break;
         case LIBXML_ERR_ERROR:
            $return .= "Error $error->code: ";
            break;
        case LIBXML_ERR_FATAL:
            $return .= "Error fatal $error->code: ";
            break;
    }

    $return .= trim($error->message) .
               "\n  Línea: $error->line" .
               "\n  Columna: $error->column";

    if ($error->file) {
        $return .= "\n  Fichero: $error->file";
    }

    return "$return\n\n--------------------------------------------\n\n";
}

?>

    
```php

El ejemplo anterior mostrará:

      <titles>PHP: Behind the Parser</title>
    ----------------------------------------------^
    Error fatal 76: Opening and ending tag mismatch: titles line 4 and title
      Línea: 4
      Columna: 46

    --------------------------------------------

## Véase también

`libxml_get_last_error`, `libxml_clear_errors`
