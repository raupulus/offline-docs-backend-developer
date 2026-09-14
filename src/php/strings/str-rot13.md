---
title: str_rot13
description: Realiza una transformación ROT13
source_url: https://www.php.net/manual/es/function.str-rot13.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-rot13.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: e095023e4
order: 89190
---

str_rot13

Realiza una transformación ROT13

## Descripción

```php
str_rot13(string $string): string
```php

Realiza una codificación ROT13 de la cadena `string` y devuelve el resultado.

La codificación ROT13 desplaza todas las letras 13 posiciones en el alfabeto, y deja todos los otros caracteres sin cambios. La codificación y el decodificado se realizan mediante la misma función: pasar el resultado de `str_rot13` nuevamente como argumento devolverá la cadena original.

## Parámetros

`string`  
La cadena de entrada.

## Valores devueltos

Devuelve la versión ROT13 de la cadena proporcionada.

## Ejemplos

Ejemplo con `str_rot13`

```
<?php

echo str_rot13('PHP 4.3.0'); // CUC 4.3.0

?>

    
```php
