---
title: restore_exception_handler
description: Reactiva la antigua función de gestión de excepciones
source_url: https://www.php.net/manual/es/function.restore-exception-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/restore-exception-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: false
translation_revision: 4a6671fe6
order: 17680
---

restore_exception_handler

Reactiva la antigua función de gestión de excepciones

## Descripción

```php
restore_exception_handler(): true
```php

`restore_exception_handler` se utiliza, después del cambio de la función de gestión de excepciones con la función `set_exception_handler`, para volver al antiguo gestor de excepciones (que puede ser la función interna o una función definida por el usuario).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Ejemplos

Ejemplo con `restore_exception_handler`

```
<?php
    function exception_handler_1(Exception $e)
    {
        echo '[' . __FUNCTION__ . '] ' . $e->getMessage();
    }

    function exception_handler_2(Exception $e)
    {
        echo '[' . __FUNCTION__ . '] ' . $e->getMessage();
    }

    set_exception_handler('exception_handler_1');
    set_exception_handler('exception_handler_2');

    restore_exception_handler();

    throw new Exception('Esto utiliza el primer gestor de excepciones...');
?>

    
```php

El ejemplo anterior mostrará:

    [exception_handler_1] Esto utiliza el primer gestor de excepciones...

## Véase también

`set_exception_handler`, `get_exception_handler`, `set_error_handler`, `restore_error_handler`, `error_reporting`
