---
title: func_num_args
description: Devuelve el número de argumentos pasados a la función
source_url: https://www.php.net/manual/es/function.func-num-args.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/func-num-args.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_reviewed: false
translation_revision: 6de3c4088
order: 24790
---

func_num_args

Devuelve el número de argumentos pasados a la función

## Descripción

```php
func_num_args(): int
```php

Obtiene el número de argumentos pasados a la función.

`func_get_arg` puede ser utilizado conjuntamente con `func_num_args` y `func_get_args` para permitir que las funciones de usuario acepten un número variable de argumentos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de argumentos pasados a la función de usuario actual.

## Errores/Excepciones

Genera una advertencia si es llamada fuera de una función de usuario.

## Ejemplos

Ejemplo con `func_num_args`

```
<?php

function foo()
{
    echo "Número de argumentos: ", func_num_args(), PHP_EOL;
}

foo(1, 2, 3);    // muestra ''
?>

    
```php

El ejemplo anterior mostrará:

    Número de argumentos: 3

## Notas

> [!NOTE]
> A partir de PHP 8.0.0, la familia de funciones func\_\*() está diseñada para ser esencialmente transparente con respecto a los argumentos nombrados, tratando los argumentos como si fueran todos pasados de manera posicional, y los argumentos faltantes son reemplazados con sus valores por defecto. Esta función ignora la colección de argumentos variádicos nombrados desconocidos. Los argumentos nombrados que son recolectados solo son accesibles a través del parámetro variádico.

## Véase también

La sintaxis [`...`](#functions.variable-arg-list), `func_get_arg`, `func_get_args`, ReflectionFunctionAbstract::getNumberOfParameters
