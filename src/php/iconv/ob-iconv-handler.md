---
title: ob_iconv_handler
description: Convierte la codificación de caracteres al manejador del buffer de salida
source_url: https://www.php.net/manual/es/function.ob-iconv-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/ob-iconv-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_revision: 96c9d88ba
order: 31270
---

ob_iconv_handler

Convierte la codificación de caracteres al manejador del buffer de salida

## Descripción

```php
ob_iconv_handler(string $contents, int $status): string
```php

Convierte el string codificado en `internal_encoding` a `output_encoding`.

`internal_encoding` y `output_encoding` deberían estar definidos en el fichero `php.ini` o en `iconv_set_encoding`.

## Parámetros

Ver `ob_start` para más información sobre los parámetros del manejador.

## Valores devueltos

Ver `ob_start` para mas información sobre los valores de retorno del manejador.

## Ejemplos

Ejemplo de `ob_iconv_handler`

```
<?php
iconv_set_encoding("internal_encoding", "UTF-8");
iconv_set_encoding("output_encoding", "ISO-8859-1");
ob_start("ob_iconv_handler"); // empieza a usarse el buffer de salida
?>

    
```php

## Véase también

`iconv_get_encoding`, `iconv_set_encoding`, [funciones de control de salida](#ref.outcontrol)
