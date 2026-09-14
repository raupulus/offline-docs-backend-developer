---
title: base_convert
description: Convierte un número entre bases arbitrarias
source_url: https://www.php.net/manual/es/function.base-convert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/base-convert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 19e812213
order: 44550
---

base_convert

Convierte un número entre bases arbitrarias

## Descripción

```php
base_convert(string $num, int $from_base, int $to_base): string
```php

Devuelve un string que contiene el argumento `num` representado en la base `to_base`. La base de representación de `number` es dada por `from_base`. `from_base` y `to_base` deben estar comprendidos entre 2 y 36 inclusive. Los dígitos superiores a 10 de las bases superiores a 10 serán representados por las letras de A a Z, con A = 10 y Z = 35. El caso de las letras no tiene importancia, es decir `num` es interpretado de forma insensible al caso.

> [!WARNING]
> `base_convert` perderá la precisión sobre los grandes números, debido a las propiedades internas del tipo `float` utilizado. Leer la sección sobre los [números decimales](#language.types.float) de este manual para más información.

## Parámetros

`num`  
El número a convertir. Cualquier carácter inválido en `num` es ignorado silenciosamente. A partir de PHP 7.4.0 proporcionar caracteres inválidos es obsoleto.

`from_base`  
La base `num` en la que está

`to_base`  
La base en la que se debe convertir el número `num`

## Valores devueltos

El número `num` convertido en la base `to_base`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Pasar caracteres inválidos generará ahora una advertencia obsoleta. El resultado siempre será calculado como si los caracteres inválidos no existieran. |

## Ejemplos

Ejemplo con `base_convert`

```
<?php
$hexadecimal = 'a37334';
echo base_convert($hexadecimal, 16, 2);
?>

    
```php

El ejemplo anterior mostrará:

    101000110111001100110100

## Véase también

`intval`
