---
title: hexdec
description: Convierte de hexadecimal a decimal
source_url: https://www.php.net/manual/es/function.hexdec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/hexdec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44700
---

hexdec

Convierte de hexadecimal a decimal

## Descripción

```php
hexdec(string $hex_string): int
```php

Devuelve el valor decimal equivalente a la `string` hexadecimal representada por el argumento `hex_string`. `hexdec` convierte una `string` hexadecimal en un número decimal.

`hexdec` ignorará cualquier carácter no hexadecimal que encuentre. A partir de PHP 7.4.0, proporcionar caracteres inválidos está deprecado.

## Parámetros

`hex_string`  
La cadena hexadecimal a convertir

## Valores devueltos

La representación decimal de `hex_string`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Pasar caracteres inválidos generará ahora una advertencia deprecada. El resultado siempre será calculado como si los caracteres inválidos no existieran. |

## Ejemplos

Ejemplo con `hexdec`

```
<?php

var_dump(hexdec("ee")); // muestra "int(238)"
var_dump(hexdec("a0")); // muestra "int(160)"
?>

    
```php

`hexdec` con caracteres inválidos

```
<?php
var_dump(hexdec("See"));  // muestra "int(238)"
var_dump(hexdec("that")); // muestra "int(10)"
?>

    
```php

## Notas

> [!NOTE]
> La función puede convertir números que son demasiado grandes para caber en un tipo `int`, en cuyo caso estos valores son devueltos como `float`.

## Véase también

`dechex`, `bindec`, `octdec`, `base_convert`
