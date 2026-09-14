---
title: func_get_arg
description: Devuelve un elemento de la lista de argumentos
source_url: https://www.php.net/manual/es/function.func-get-arg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/func-get-arg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_reviewed: false
translation_revision: de42b5016
order: 24770
---

func_get_arg

Devuelve un elemento de la lista de argumentos

## Descripción

```php
func_get_arg(int $position): mixed
```php

Recupera un elemento de la lista de argumentos de una función de usuario.

`func_get_arg` puede ser utilizado conjuntamente con `func_num_args` y `func_get_args` para permitir que las funciones de usuario acepten un número variable de argumentos.

## Parámetros

`position`  
La posición del argumento. Los argumentos de la función son contados comenzando desde `0`.

## Valores devueltos

Devuelve el argumento especificado, o `false` si ocurre un error.

## Errores/Excepciones

Generará una advertencia si es llamada fuera de una función de usuario, o si `position` es mayor que el número de argumentos pasados.

## Ejemplos

Ejemplo con `func_get_arg`

```
<?php
function foo()
{
     $numargs = func_num_args();
     echo "Número de argumentos : $numargs\n";
     if ($numargs >= 2) {
         echo "El segundo argumento es : " . func_get_arg(1) . "\n";
     }
}

foo(1, 2, 3);
?>

    
```php

El ejemplo anterior mostrará:

    Número de argumentos : 3
    El segundo argumento es : 2

Ejemplo `func_get_arg` con argumentos por referencia y por valor

```
<?php
function byVal($arg) {
    echo 'Tal como se pasó     : ', var_export(func_get_arg(0)), PHP_EOL;
    $arg = 'baz';
    echo 'Después del cambio  : ', var_export(func_get_arg(0)), PHP_EOL;
}

function byRef(&$arg) {
    echo 'Tal como se pasó     : ', var_export(func_get_arg(0)), PHP_EOL;
    $arg = 'baz';
    echo 'Después del cambio  : ', var_export(func_get_arg(0)), PHP_EOL;
}

$arg = 'bar';
byVal($arg);
byRef($arg);
?>

    
```php

El ejemplo anterior mostrará:

    Tal como se pasó     : 'bar'
    Después del cambio  : 'baz'
    Tal como se pasó     : 'bar'
    Después del cambio  : 'baz'

## Notas

> [!NOTE]
> A partir de PHP 8.0.0, la familia de funciones func\_\*() está diseñada para ser esencialmente transparente con respecto a los argumentos nombrados, tratando los argumentos como si fueran todos pasados de manera posicional, y los argumentos faltantes son reemplazados con sus valores por defecto. Esta función ignora la colección de argumentos variádicos nombrados desconocidos. Los argumentos nombrados que son recolectados solo son accesibles a través del parámetro variádico.

> [!NOTE]
> Si los argumentos son pasados por referencia, todas sus modificaciones serán reflejadas en los valores devueltos por esta función. A partir de PHP 7, los valores actuales también serán devueltos si los argumentos son pasados por su valor.

> [!NOTE]
> Esta función devuelve únicamente una copia de los argumentos pasados, y no cuenta como argumentos por defecto (no pasados).

## Véase también

La sintaxis [`...`](#functions.variable-arg-list), `func_get_args`, `func_num_args`
