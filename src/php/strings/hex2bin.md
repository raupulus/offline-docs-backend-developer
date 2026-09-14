---
title: hex2bin
description: Convierte una string codificada en hexadecimal a binario
source_url: https://www.php.net/manual/es/function.hex2bin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/hex2bin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: e095023e4
order: 88770
---

hex2bin

Convierte una string codificada en hexadecimal a binario

## Descripción

```php
hex2bin(string $string): string
```php

Convierte una string binaria codificada en hexadecimal.

> [!CAUTION]
> Esta función no convierte un número hexadecimal a un número binario. Esto puede realizarse utilizando la función `base_convert`.

## Parámetros

`string`  
Representación hexadecimal de los datos.

## Valores devueltos

Devuelve la representación binaria de los datos o `false` si ocurre un error.

## Errores/Excepciones

Si la string de entrada en hexadecimal tiene una longitud impar o si la string en hexadecimal es inválida, se emitirá una alerta de nivel `E_WARNING`.

## Ejemplos

Ejemplo con `hex2bin`

```
<?php
$hex = hex2bin("6578616d706c65206865782064617461");
var_dump($hex);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(16) "example hex data"

## Véase también

`bin2hex`, `unpack`
