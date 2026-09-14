---
title: tidy::$errorBuffer
description: Devuelve advertencias y errores que ocurrieron al analizar el documento
  especificado
source_url: https://www.php.net/manual/es/tidy.props.errorbuffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/errorbuffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: c01482dee
order: 94020
---

tidy::\$errorBuffer

tidy_get_error_buffer

Devuelve advertencias y errores que ocurrieron al analizar el documento especificado

## Descripción

Estilo orientado a objetos (propiedad):

public

string

null

tidy-\>errorBuffer

Estilo procedimental:

```php
tidy_get_error_buffer(tidy $tidy): string
```php

Devuelve advertencias y errores que ocurrieron al analizar el documento especificado.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve el búfer de errores como una cadena, o `false` si el búfer está vacío.

## Ejemplos

Ejemplo de `tidy_get_error_buffer`

```
<?php
$html = '<p>párrafo</p>';

$tidy = tidy_parse_string($html);

echo tidy_get_error_buffer($tidy);
/* o utilizando OO: */
echo $tidy->errorBuffer;
?>

    
```php

El ejemplo anterior mostrará:

    line 1 column 1 - Warning: missing <!DOCTYPE> declaration
    line 1 column 1 - Warning: inserting missing 'title' element

## Véase también

tidy_access_count

tidy_error_count

tidy_warning_count
