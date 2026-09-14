---
title: apcu_dec
description: Disminuir un número almacenado
source_url: https://www.php.net/manual/es/function.apcu-dec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-dec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 804d8a054
order: 5010
---

apcu_dec

Disminuir un número almacenado

## Descripción

```php
apcu_dec(string $key, [int $step], [bool $success], [int $ttl]): int
```php

Disminuye un valor entero almacenado.

## Parámetros

`key`  
La clave de el valor a ser disminuido.

`step`  
El paso, o valor a disminuir.

`success`  
Opcionalmente pasa el valor booleano en caso de éxito o en caso de error a esta variable referenciada.

`ttl`  
TTL para usar si la operación inserta un nuevo valor (en lugar de disminuir uno existente).

## Valores devueltos

Devuelve el valor actual del valor de las claves (`key`) en caso de éxito, o `false` si ocurre un error

## Ejemplos

Ejemplo de `apcu_dec`

```
<?php
echo "Hagamos algo con éxito", PHP_EOL;

apcu_store('anumber', 42);

echo apcu_fetch('anumber'), PHP_EOL;

echo apcu_dec('anumber'), PHP_EOL;
echo apcu_dec('anumber', 10), PHP_EOL;
echo apcu_dec('anumber', 10, $success), PHP_EOL;

var_dump($success);

echo "Ahora, hagamos que falle", PHP_EOL, PHP_EOL;

apcu_store('astring', 'foo');

$ret = apcu_dec('astring', 1, $fail);

var_dump($ret);
var_dump($fail);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Hagamos algo con éxito
    42
    41
    31
    21
    bool(true)
    Ahora, hagamos que falle

    bool(false)
    bool(false)

## Véase también

apcu_inc
