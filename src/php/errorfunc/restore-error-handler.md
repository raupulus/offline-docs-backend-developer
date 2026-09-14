---
title: restore_error_handler
description: Restaura la función anterior de manejo de errores
source_url: https://www.php.net/manual/es/function.restore-error-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/restore-error-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: false
translation_revision: 4a6671fe6
order: 17670
---

restore_error_handler

Restaura la función anterior de manejo de errores

## Descripción

```php
restore_error_handler(): true
```php

Utilizada después de modificar la función de manejo de errores, gracias a `set_error_handler`, `restore_error_handler` permite reutilizar la versión anterior de manejo de errores (que puede ser la función PHP por defecto, o alguna otra función del usuario).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Ejemplos

Ejemplo con `restore_error_handler`

Si `unserialize` causa un error, entonces el manejador de errores original es restaurado.

```
<?php
function unserialize_handler($errno, $errstr)
{
echo "Valor incorrectamente serializado.\n";
}

$serialized = 'foo';
set_error_handler('unserialize_handler');
$original = unserialize($serialized);
restore_error_handler();
?>

    
```php

El ejemplo anterior mostrará:

    Valor incorrectamente serializado.

## Véase también

`error_reporting`, `set_error_handler`, `get_error_handler`, `restore_exception_handler`, `trigger_error`
