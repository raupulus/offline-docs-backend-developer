---
title: mime_content_type
description: Detecta el tipo de contenido de un fichero
source_url: https://www.php.net/manual/es/function.mime-content-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fileinfo/functions/mime-content-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fileinfo
translation_status: ready
translation_reviewed: false
translation_revision: 82ddd2ec8
order: 23240
---

mime_content_type

Detecta el tipo de contenido de un fichero

## Descripción

```php
mime_content_type(resource $filename): string
```php

Devuelve el contenido MIME de un fichero utilizando las informaciones desde el fichero `magic.mime`.

## Parámetros

`filename`  
Ruta hacia el fichero a probar.

## Valores devueltos

Devuelve el tipo de contenido en formato MIME, como `text/plain` o `application/octet-stream`, o `false` si ocurre un error.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `mime_content_type`

```
<?php
echo mime_content_type('php.gif') . "\n";
echo mime_content_type('test.php');
?>

   
```php

El ejemplo anterior mostrará:

    image/gif
    text/plain

## Véase también

finfo_file

finfo_buffer
