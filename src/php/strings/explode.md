---
title: explode
description: Divide una string en segmentos
source_url: https://www.php.net/manual/es/function.explode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/explode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 45042fef6
order: 88720
---

explode

Divide una string en segmentos

## Descripción

```php
explode(string $separator, string $string, [int $limit]): array
```php

`explode` retorna un array de strings, cada una de ellas siendo una substring del parámetro `string` extraída utilizando el separador `separator`.

## Parámetros

`separator`  
El separador.

`string`  
La string inicial.

`limit`  
Si `limit` está definido y es positivo, el array retornado contiene, como máximo, `limit` elementos, y el último elemento contendrá el resto de la string.

Si el parámetro `limit` es negativo, todos los elementos, excepto los últimos -`limit` elementos, son retornados.

Si `limit` vale cero, es tratado como si valiera 1.

> [!NOTE]
> Antes de PHP 8.0, `implode` aceptaba sus parámetros en cualquier orden. `explode` nunca ha soportado esto: se debe asegurar que el parámetro `separator` esté colocado antes del parámetro `string`.

## Valores devueltos

Retorna un `array` de strings creadas al dividir la string del parámetro `string` en varios trozos siguiendo el parámetro `separator`.

Si `separator` es una string vacía (""), `explode` lanzará una `ValueError`. Si `separator` contiene un valor que no está contenido en `string` así como un valor negativo para el parámetro `limit`, entonces `explode` retornará un `array` vacío, de lo contrario, un `array` conteniendo la string `string` entera. Si los valores de `separator` aparecen al inicio o al final de `string`, estos valores serán añadidos como un valor de un `array` vacío ya sea en la primera o última posición del `array` retornado respectivamente.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `explode` lanzará ahora una `ValueError` cuando el parámetro `separator` es una string vacía (`""`). Anteriormente, `explode` retornaba `false`. |

## Ejemplos

Ejemplo con `explode`

```
<?php
// Ejemplo 1
$pizza  = "piece1 piece2 piece3 piece4 piece5 piece6";
$pieces = explode(" ", $pizza);
echo $pieces[0], PHP_EOL; // piece1
echo $pieces[1], PHP_EOL; // piece2

// Ejemplo 2
$data = "foo:*:1023:1000::/home/foo:/bin/sh";
list($user, $pass, $uid, $gid, $gecos, $home, $shell) = explode(":", $data);
echo $user, PHP_EOL; // foo
echo $pass, PHP_EOL; // *

?>

    
```php

Ejemplo de valores retornados por la función `explode`

```
<?php
/* Una string que no contiene delimitador retornará un array
   conteniendo solo un elemento representando la string original */
$input1 = "hello";
$input2 = "hello,there";
$input3 = ',';
var_dump( explode( ',', $input1 ) );
var_dump( explode( ',', $input2 ) );
var_dump( explode( ',', $input3 ) );

?>

    
```php

El ejemplo anterior mostrará:

    array(1)
    (
        [0] => string(5) "hello"
    )
    array(2)
    (
        [0] => string(5) "hello"
        [1] => string(5) "there"
    )
    array(2)
    (
        [0] => string(0) ""
        [1] => string(0) ""
    )

Ejemplo con `explode` y el parámetro `limit`

```
<?php
$str = 'one|two|three|four';

// limit positivo
print_r(explode('|', $str, 2));

// limit negativo
print_r(explode('|', $str, -1));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => one
        [1] => two|three|four
    )
    Array
    (
        [0] => one
        [1] => two
        [2] => three
    )

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`preg_split`, `str_split`, `mb_split`, `str_word_count`, `strtok`, `implode`
