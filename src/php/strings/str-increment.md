---
title: str_increment
description: Incrementa un string alfanumérica
source_url: https://www.php.net/manual/es/function.str-increment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-increment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 57c83578b
order: 89140
---

str_increment

Incrementa un string alfanumérica

## Descripción

```php
str_increment(string $string): string
```php

Devuelve el string alfanumérico ASCII incrementado `string`.

## Parámetros

`string`  
El string a incrementar.

## Valores devueltos

Devuelve el string alfanumérico ASCII incrementado.

## Errores/Excepciones

Se lanza una excepción `ValueError` si `string` está vacío.

Se lanza una excepción `ValueError` si `string` no es un string alfanumérico ASCII.

## Ejemplos

Ejemplo básico de la función `str_increment`

```
<?php
$str = 'ABC';
var_dump(str_increment($str));
?>

    
```php

El ejemplo anterior mostrará:

    string(3) "ABD"

Ejemplo de `str_increment` con acarreo

```
<?php
$str = 'DZ';
var_dump(str_increment($str));

$str = 'ZZ';
var_dump(str_increment($str));
?>

    
```php

El ejemplo anterior mostrará:

    string(2) "EA"
    string(3) "AAA"

## Véase también

`str_decrement`
