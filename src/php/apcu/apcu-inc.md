---
title: apcu_inc
description: Incrementa un número almacenado
source_url: https://www.php.net/manual/es/function.apcu-inc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-inc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 804d8a054
order: 5070
---

apcu_inc

Incrementa un número almacenado

## Descripción

```php
apcu_inc(string $key, [int $step], [bool $success], [int $ttl]): int
```php

Incrementa un número almacenado.

## Parámetros

`key`  
La clave del valor que debe ser incrementado.

`step`  
El paso de incrementación o el valor a añadir.

`success`  
Opcional, pasa el valor booleano éxito o fallo a la variable referenciada.

`ttl`  
Duración de vida a utilizar si la función inserta una nueva variable (en lugar de incrementar una variable existente).

## Valores devueltos

Devuelve el valor actual asociado a la clave `key` en caso de éxito, o `false` si ocurre un error

## Ejemplos

Un ejemplo con `apcu_inc`

```
<?php
echo "Hagamos algo con éxito", PHP_EOL;

apcu_store('anumber', 42);

echo apcu_fetch('anumber'), PHP_EOL;

echo apcu_inc('anumber'), PHP_EOL;
echo apcu_inc('anumber', 10), PHP_EOL;
echo apcu_inc('anumber', 10, $success), PHP_EOL;

var_dump($success);

echo "Ahora, hagamos que falle", PHP_EOL, PHP_EOL;

apcu_store('astring', 'foo');

$ret = apcu_inc('astring', 1, $fail);

var_dump($ret);
var_dump($fail);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Hagamos algo con éxito
    42
    43
    53
    63
    bool(true)
    Ahora, hagamos que falle

    bool(false)
    bool(false)

## Véase también

apcu_dec
