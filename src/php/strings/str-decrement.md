---
title: str_decrement
description: Decrementa un string alfanumérico
source_url: https://www.php.net/manual/es/function.str-decrement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-decrement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 57c83578b
order: 89110
---

str_decrement

Decrementa un string alfanumérico

## Descripción

```php
str_decrement(string $string): string
```php

Devuelve el string alfanumérico ASCII decrementado `string`.

## Parámetros

`string`  
El string a decrementar.

## Valores devueltos

Devuelve el string alfanumérico ASCII decrementado.

## Errores/Excepciones

Se lanza una excepción `ValueError` si `string` está vacío.

Se lanza una excepción `ValueError` si `string` no es un string alfanumérico ASCII.

Se lanza una excepción `ValueError` si `string` no puede ser decrementado. Por ejemplo, `"A"` o `"0"`.

## Ejemplos

Ejemplo básico de la función `str_decrement`

```
<?php
$str = 'ABC';
var_dump(str_decrement($str));
?>

    
```php

El ejemplo anterior mostrará:

    string(3) "ABB"

Ejemplo de la función `str_decrement` con una retención

```
<?php
$str = 'ZA';
var_dump(str_decrement($str));

$str = 'AA';
var_dump(str_decrement($str));
?>

    
```php

El ejemplo anterior mostrará:

    string(2) "YZ"
    string(1) "Z"

## Véase también

`str_increment`
