---
title: apcu_cas
description: Actualiza un valor antiguo con un nuevo valor
source_url: https://www.php.net/manual/es/function.apcu-cas.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-cas.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 804d8a054
order: 4990
---

apcu_cas

Actualiza un valor antiguo con un nuevo valor

## Descripción

```php
apcu_cas(string $key, int $old, int $new): bool
```php

`apcu_cas` actualiza un valor entero ya existente si el parámetro `old` coincide el valor almacenado actualmente con el valor del parámetro `new`.

## Parámetros

`key`  
La clave del valor que se está actualizando.

`old`  
El valor antiguo (el valor actualmente almacenado).

`new`  
El nuevo valor al que actualizar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `apcu_cas`

```
<?php
apcu_store('foobar', 2);
echo '$foobar = 2', PHP_EOL;
echo '$foobar == 1 ? 2 : 1 = ', (apcu_cas('foobar', 1, 2) ? 'ok' : 'fail'), PHP_EOL;
echo '$foobar == 2 ? 1 : 2 = ', (apcu_cas('foobar', 2, 1) ? 'ok' : 'fail'), PHP_EOL;

echo '$foobar = ', apcu_fetch('foobar'), PHP_EOL;

echo '$f__bar == 1 ? 2 : 1 = ', (apcu_cas('f__bar', 1, 2) ? 'ok' : 'fail'), PHP_EOL;

apcu_store('perfection', 'xyz');
echo '$perfection == 2 ? 1 : 2 = ', (apcu_cas('perfection', 2, 1) ? 'ok' : 'epic fail'), PHP_EOL;

echo '$foobar = ', apcu_fetch('foobar'), PHP_EOL;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    $foobar = 2
    $foobar == 1 ? 2 : 1 = fail
    $foobar == 2 ? 1 : 2 = ok
    $foobar = 1
    $f__bar == 1 ? 2 : 1 = fail
    $perfection == 2 ? 1 : 2 = epic fail
    $foobar = 1

## Véase también

apcu_dec

apcu_store
