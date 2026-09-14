---
title: gmp_init
description: Crea un número GMP
source_url: https://www.php.net/manual/es/function.gmp-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 28530
---

gmp_init

Crea un número GMP

## Descripción

```php
gmp_init(int $num, [int $base]): GMP
```php

Crea un número GMP, a partir de un entero o de un string.

## Parámetros

`num`  
Un entero o un string. El string puede ser una representación decimal, hexadecimal, octal o binaria.

`base`  
La base a utilizar para convertir una representación en forma de `string`.

Una base explícita puede estar comprendida entre `2` y `62`. Para las bases hasta `36`, la casilla es ignorada: las letras mayúsculas y minúsculas tienen el mismo valor. Para las bases de `37` a `62`, las letras mayúsculas representan los valores de `10` a `35` y las letras minúsculas representan los valores de `36` a `61`.

Si `base` vale `0`, entonces la base real es determinada a partir de los caracteres iniciales de `num`. Si los dos primeros caracteres son `0x` o `0X`, el string es interpretado como un entero hexadecimal. Si los dos primeros caracteres son `0b` o `0B`, el string es interpretado como un entero binario. Si los dos primeros caracteres son `0o` o `0O`, el string es interpretado como un entero octal. Además, si el primer carácter es `0`, el string es igualmente interpretado como un entero octal. En todos los demás casos, el string es interpretado como un entero decimal.

## Valores devueltos

Un objeto `GMP`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El soporte para los prefijos octales explícitos `0o` y `0O` ha sido añadido para los strings `num`. La interpretación de estos prefijos cuando `base` vale `0` ha sido igualmente añadida. |

## Ejemplos

Creación de un número GMP

```
<?php
$a = gmp_init(123456);
$b = gmp_init("0xFFFFDEBACDFEDF7200");
?>

    
```php

## Notas

> [!NOTE]
> No es necesario llamar a esta función para utilizar enteros o strings en lugar de números GMP en las funciones GMP, como `gmp_add`. Los argumentos de estas funciones son automáticamente convertidos en números GMP, si esta conversión es posible y necesaria, utilizando las mismas reglas que `gmp_init`.

## Véase también

GMP::\_\_construct
