---
title: getimagesizefromstring
description: Obtiene el tamaño de una imagen desde una cadena
source_url: https://www.php.net/manual/es/function.getimagesizefromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/getimagesizefromstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 31390
---

getimagesizefromstring

Obtiene el tamaño de una imagen desde una cadena

## Descripción

```php
getimagesizefromstring(string $string, [array $image_info]): array
```php

Idéntico a la función `getimagesize` excepto que la función `getimagesizefromstring` acepta una cadena en lugar de un nombre de fichero como primer argumento.

Consulte la documentación de la función `getimagesize` para obtener más detalles sobre cómo funciona esta función.

## Parámetros

`string`  
Los datos de la imagen, en forma de cadena.

`image_info`  
Consulte la función `getimagesize`.

## Valores devueltos

Consulte la función `getimagesize`.

## Ejemplos

Ejemplo con `getimagesizefromstring`

```
<?php
$img = '/path/to/test.png';

// Apertura mediante un fichero
$size_info1 = getimagesize($img);

// Apertura mediante una cadena
$data       = file_get_contents($img);
$size_info2 = getimagesizefromstring($data);
?>

    
```php

## Véase también

getimagesize
