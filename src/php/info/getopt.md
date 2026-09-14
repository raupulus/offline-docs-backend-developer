---
title: getopt
description: Lee las opciones pasadas en la línea de comandos
source_url: https://www.php.net/manual/es/function.getopt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/getopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 4d02fe98d
order: 39010
---

getopt

Lee las opciones pasadas en la línea de comandos

## Descripción

```php
getopt(string $short_options, [array $long_options], [int $rest_index]): array
```php

`getopt` lee las opciones pasadas en la línea de comandos.

## Parámetros

`short_options`  
Cada carácter en esta cadena será utilizado como caracteres opcionales y deberá coincidir con las opciones pasadas, comenzando por un guión simple (`-`).

Por ejemplo, una cadena opcional `"x"` coincidirá con la opción `-x`.

Solo se permiten a-z, A-Z y 0-9.

`long_options`  
Un array de opciones. Cada elemento de este array será utilizado como opción y deberá coincidir con las opciones pasadas, comenzando por un guión doble (`--`).

Por ejemplo, un elemento `longopts` `"opt"` coincidirá con la opción `--opt`.

`rest_index`  
Si el parámetro `rest_index` está presente, entonces el índice donde se detuvo el análisis de los argumentos será escrito en esta variable.

El parámetro `short_options` puede contener los siguientes elementos: Caracteres individuales (no aceptan valor), Caracteres seguidos por un dos-puntos (el parámetro requiere un valor), Caracteres seguidos por dos dos-puntos (valor opcional) Los valores opcionales son los primeros argumentos después de la cadena. Si un valor es requerido, no importa si el valor está seguido de un espacio o no. Ver la nota.

> [!NOTE]
> Los valores opcionales no aceptan el espacio como separador.

El array de valores `long_options` puede contener: String (parámetro no acepta ningún valor), String seguido de un dos-puntos (parámetro requiere un valor), String seguido de dos dos-puntos (valor opcional)

> [!NOTE]
> El formato de los parámetros `short_options` y `long_options` es idéntico; la única diferencia es que `long_options` toma un array en opción (donde cada elemento es una opción) mientras que `short_options` toma una cadena (donde cada carácter es una opción).

## Valores devueltos

Esta función devuelve un array de opciones/argumentos, o `false` si ocurre un error.

> [!NOTE]
> El análisis de las opciones se detendrá cuando se encuentre la primera opción incorrecta, y todo lo que siga será ignorado.

## Historial de cambios

| Versión | Descripción                          |
|---------|--------------------------------------|
| 7.1.0   | Se añadió el parámetro `rest_index`. |

## Ejemplos

Ejemplo con `getopt`: los fundamentos

```
<?php
// Script example.php
$options = getopt("f:hp:");
var_dump($options);
?>

    
```php

```
shell> php example.php -fvalue -h

    
```php

El ejemplo anterior mostrará:

    array(2) {
      ["f"]=>
      string(5) "value"
      ["h"]=>
      bool(false)
    }

Segundo ejemplo con `getopt`: Introducción a las opciones largas

```
<?php
// Script example.php
$shortopts  = "";
$shortopts .= "f:";  // Valor requerido
$shortopts .= "v::"; // Valor opcional
$shortopts .= "abc"; // Estas opciones no aceptan valor

$longopts  = array(
    "required:",     // Valor requerido
    "optional::",    // Valor opcional
    "option",        // Ningún valor
    "opt",           // Ningún valor
);
$options = getopt($shortopts, $longopts);
var_dump($options);
?>

    
```php

```
shell> php example.php -f "value for f" -v -a --required value --optional="optional value" --option

    
```php

El ejemplo anterior mostrará:

    array(6) {
      ["f"]=>
      string(11) "value for f"
      ["v"]=>
      bool(false)
      ["a"]=>
      bool(false)
      ["required"]=>
      string(5) "value"
      ["optional"]=>
      string(14) "optional value"
      ["option"]=>
      bool(false)
    }

Tercer ejemplo con `getopt`: Pasar múltiples opciones

```
<?php
// Script example.php
$options = getopt("abc");
var_dump($options);
?>

    
```php

```
shell> php example.php -aaac

    
```php

El ejemplo anterior mostrará:

    array(2) {
      ["a"]=>
      array(3) {
        [0]=>
        bool(false)
        [1]=>
        bool(false)
        [2]=>
        bool(false)
      }
      ["c"]=>
      bool(false)
    }

Ejemplo de `getopt`: Utilizando `rest_index`

```
<?php
// Script example.php
$rest_index = null;
$opts = getopt('a:b:', [], $rest_index);
$pos_args = array_slice($argv, $rest_index);
var_dump($pos_args);

    
```php

```
shell> php example.php -a 1 -b 2 -- test

    
```php

El ejemplo anterior mostrará:

    array(1) {
      [0]=>
      string(4) "test"
    }

## Véase también

[`$argv`](#reserved.variables.argv)
