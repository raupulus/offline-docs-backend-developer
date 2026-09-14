---
title: get_defined_vars
description: Lista todas las variables definidas
source_url: https://www.php.net/manual/es/function.get-defined-vars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/get-defined-vars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: ccc438a27
order: 100500
---

get_defined_vars

Lista todas las variables definidas

## Descripción

```php
get_defined_vars(): array
```php

`get_defined_vars` devuelve un array multidimensional que contiene la lista de todas las variables definidas, ya sean variables de entorno, de servidor o definidas por el usuario en el ámbito de llamada de la función `get_defined_vars`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array multidimensional que contiene todas las variables.

## Ejemplos

Ejemplo con `get_defined_vars`

```
<?php
$b = array(1, 1, 2, 3, 5, 8);

$arr = get_defined_vars();

// Muestra $b
print_r($arr["b"]);

/* Muestra la ruta hacia el intérprete PHP (si se usa como CGI)
 * p. ej. /usr/local/bin/php */
echo $arr["_"];

// Muestra los argumentos de la línea de comandos si los hay
print_r($arr["argv"]);

// Muestra todas las variables de servidor
print_r($arr["_SERVER"]);

// Muestra todas las claves disponibles del array de variables
print_r(array_keys(get_defined_vars()));
?>

    
```php

## Véase también

`isset`, `get_defined_functions`, `get_defined_constants`
