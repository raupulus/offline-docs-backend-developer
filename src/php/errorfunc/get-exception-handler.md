---
title: get_exception_handler
description: Devuelve la función de gestión de excepciones definida por el usuario
source_url: https://www.php.net/manual/es/function.get-exception-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/get-exception-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: true
translation_revision: 99916949e
order: 17660
---

get_exception_handler

Devuelve la función de gestión de excepciones definida por el usuario

## Descripción

```php
get_exception_handler(): callable
```php

Devuelve la función de gestión de excepciones definida por el usuario, si se ha definido alguna.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la función de gestión de excepciones definida. Si no se ha definido ninguna, se devuelve `null`.

El gestor devuelto es la función de devolución de llamada exacta que se pasó a `set_exception_handler` para definirla.

## Ejemplos

Ejemplo de `get_exception_handler`

```
<?php

$handler = function (Throwable $ex) {
     echo "Exception: " . $ex::class . ": " . $ex->getMessage() . "\n";
};

var_dump(get_exception_handler()); // NULL

set_exception_handler($handler);

var_dump(get_exception_handler() === $handler); // bool(true)

?>

   
```php

## Notas

> [!TIP]
> Antes de PHP 8.5.0, esta funcionalidad podía ser proporcionada por el siguiente polyfill:
>
> <div class="informalexample">
>
> ```
> <?php
> if (!function_exists('get_exception_handler')) {
>     function noop_exception_handler() {
>     }
>     function get_exception_handler(): ?callable {
>         $handler = set_exception_handler('noop_exception_handler');
>         restore_exception_handler();
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

set_exception_handler

restore_exception_handler

restore_error_handler

error_reporting

Excepciones
