---
title: get_error_handler
description: Devuelve la función de manejo de errores definida por el usuario
source_url: https://www.php.net/manual/es/function.get-error-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/get-error-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: true
translation_revision: 99916949e
order: 17650
---

get_error_handler

Devuelve la función de manejo de errores definida por el usuario

## Descripción

```php
get_error_handler(): callable
```php

Devuelve la función de manejo de errores definida por el usuario, si se ha definido alguna.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la función de manejo de errores definida. Si se utiliza el gestor por defecto, se devuelve `null`.

El gestor devuelto es la función de devolución de llamada exacta que se pasó a `set_error_handler` para definirla.

## Ejemplos

Ejemplo de `get_error_handler`

```
<?php

$handler = function (int $errno, string $errstr, ?string $errfile, ?int $errline) {
     echo "Error: " . $errstr . "\n";
};

var_dump(get_error_handler()); // NULL

set_error_handler($handler);

var_dump(get_error_handler() === $handler); // bool(true)

?>

   
```php

## Notas

> [!TIP]
> Anteriormente a PHP 8.5.0, esta funcionalidad puede ser proporcionada por el polyfill siguiente:
>
> <div class="informalexample">
>
> ```
> <?php
> if (!function_exists('get_error_handler')) {
>     function noop_error_handler() {
>     }
>     function get_error_handler(): ?callable {
>         $handler = set_error_handler('noop_error_handler');
>         restore_error_handler();
>         return $handler;
>     }
> }
> ?>
>
>     
> ```
>
> </div>

## Véase también

error_reporting

set_error_handler

restore_error_handler

trigger_error

constante de nivel de error
