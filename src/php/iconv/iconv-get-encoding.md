---
title: iconv_get_encoding
description: Lee el juego de caracteres actual
source_url: https://www.php.net/manual/es/function.iconv-get-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv-get-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: ab9a7d2e3
order: 31170
---

iconv_get_encoding

Lee el juego de caracteres actual

## Descripción

```php
iconv_get_encoding([string $type]): array
```php

Devuelve la configuración actual del gestor `ob_iconv_handler`.

## Parámetros

`type`  
Los valores posibles para el argumento opcional `type` son: all, input_encoding, output_encoding, internal_encoding

## Valores devueltos

Devuelve el valor actual de la variable de configuración en caso de éxito o `false` si ocurre un error.

Si `type` es omitido o diferente de `all` (es decir "todos"), `iconv_get_encoding` devuelve un array que contiene todos los valores de estas constantes.

## Ejemplos

Ejemplo con `iconv_get_encoding`

```
<pre>
<?php
iconv_set_encoding("internal_encoding", "UTF-8");
iconv_set_encoding("output_encoding", "ISO-8859-1");
var_dump(iconv_get_encoding('all'));
?>
</pre>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [input_encoding] => ISO-8859-1
        [output_encoding] => ISO-8859-1
        [internal_encoding] => UTF-8
    )

## Véase también

`iconv_set_encoding`, `ob_iconv_handler`
