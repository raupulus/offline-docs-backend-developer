---
title: runkit7_function_redefine
description: Sustituye una definición de función por una nueva implementación
source_url: https://www.php.net/manual/es/function.runkit7-function-redefine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-function-redefine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72890
---

runkit7_function_redefine

Sustituye una definición de función por una nueva implementación

## Descripción

```php
runkit7_function_redefine(string $function_name, string $argument_list, string $code, [bool $return_by_reference], [string $doc_comment], [string $return_type], [bool $is_strict]): bool
```php

```php
runkit7_function_redefine(string $function_name, Closure $closure, [string $doc_comment], [string $return_type], [bool $is_strict]): bool
```

> [!NOTE]
> Por defecto, solo las funciones definidas por el usuario pueden ser eliminadas, renombradas o modificadas. Para sobrescribir funciones internas, se debe activar la configuración `runkit.internal_override` en el archivo `php.ini` del sistema entero.

## Parámetros

`function_name`  
El nombre de la función a redefinir

`argument_list`  
La nueva lista de argumentos a aceptar por la función

`code`  
El código de la nueva implementación

`closure`  
Una `closure` que define la función

`return_by_reference`  
Si la función debe devolver por referencia

`doc_comment`  
El comentario de documentación de la función

`return_type`  
El tipo de retorno de la función

`is_strict`  
Si la función se comporta como si estuviera declarada en un fichero con `strict_types=1`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Un ejemplo de `runkit7_function_redefine`

```php
<?php
function testme() {
  echo "Original Testme Implementation\n";
}
testme();
runkit7_function_redefine('testme','','echo "New Testme Implementation\n";');
testme();
?>

   
```

El ejemplo anterior mostrará:

    Original Testme Implementation
    New Testme Implementation

## Véase también

runkit7_function_add

runkit7_function_copy

runkit7_function_rename

runkit7_function_remove

runkit7_method_redefine
