---
title: set_exception_handler
description: Define una función de usuario para gestionar excepciones
source_url: https://www.php.net/manual/es/function.set-exception-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/set-exception-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: false
translation_revision: 4a6671fe6
order: 17700
---

set_exception_handler

Define una función de usuario para gestionar excepciones

## Descripción

```php
set_exception_handler(callable $callback): callable
```php

`set_exception_handler` define el manejador de excepciones por defecto si una excepción no es capturada con un bloque de prueba/atrapa. La ejecución se detendrá después de la llamada a la función `callback`.

## Parámetros

`callback`  
La función a llamar cuando ocurre una excepción no capturada. Esta función de gestión debe aceptar un argumento, que será el objeto `Throwable` que fue lanzado. Las clases `Error` y `Exception` implementan la interfaz `Throwable`. Esta es la firma del manejador:

```php
handler(Throwable $ex): void
```

`null` puede ser pasado en su lugar, para reinicializar este manejador a su estado inicial.

## Valores devueltos

Retorna el manejador previamente definido o `null` en caso de error. Si ningún manejador fue previamente definido, `null` es también retornado.

## Ejemplos

Ejemplo con `set_exception_handler`

```php
<?php
function exception_handler(Throwable $exception) {
  echo "Excepción no capturada: " , $exception->getMessage(), "\n";
}

set_exception_handler('exception_handler');

throw new Exception('Excepción no capturada');
echo "No ejecutado\n";
?>

    
```

## Véase también

`get_exception_handler`, `restore_exception_handler`, `restore_error_handler`, `error_reporting`, Las [excepciones](#language.exceptions)
