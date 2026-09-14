---
title: apcu_exists
description: Verifica si una entrada existe
source_url: https://www.php.net/manual/es/function.apcu-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_reviewed: false
translation_revision: 804d8a054
order: 5050
---

apcu_exists

Verifica si una entrada existe

## Descripción

```php
apcu_exists(string $keys): bool
```php

Verifica si una o varias entradas APCu existen.

## Parámetros

`keys`  
Un `string` o un `array` de strings que contiene las claves.

## Valores devueltos

Devuelve el valor `true` si la clave existe, o `false` en caso contrario. O bien, si un `array` ha sido pasado a `keys`, entonces el valor devuelto es un array conteniendo todas las claves existentes, o un array vacío si ninguna existe.

## Ejemplos

Un ejemplo con `apcu_exists`

```
<?php
$fruit  = 'apple';
$veggie = 'carrot';

apcu_store('foo', $fruit);
apcu_store('bar', $veggie);

if (apcu_exists('foo')) {
    echo "Foo existe: ";
    echo apcu_fetch('foo');
} else {
    echo "Foo no existe";
}

echo PHP_EOL;
if (apcu_exists('baz')) {
    echo "Baz existe.";
} else {
    echo "Baz no existe";
}

echo PHP_EOL;

$ret = apcu_exists(array('foo', 'donotexist', 'bar'));
var_dump($ret);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Foo existe: apple
    Baz no existe
    array(2) {
      ["foo"]=>
      bool(true)
      ["bar"]=>
      bool(true)
    }

## Véase también

apcu_cache_info

apcu_fetch
