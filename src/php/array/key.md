---
title: key
description: Devuelve una clave de un array asociativo
source_url: https://www.php.net/manual/es/function.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 0a192fcd9
order: 5840
---

key

Devuelve una clave de un array asociativo

## Descripción

```php
key(array $array): int
```php

`key` devuelve la clave actual en el array `array`.

## Parámetros

`array`  
El array.

## Valores devueltos

La función `key` devuelve simplemente la clave del elemento del array que es actualmente apuntado por el puntero interno. Esta función no modifica en ningún caso la posición de este puntero. Si el puntero interno apunta un elemento situado después del final de la lista de elementos, o bien si el array está vacío, la función `key` devolverá `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | O bien convertir el `object` en un `array` utilizando `get_mangled_object_vars` primero, o utilizar los métodos proporcionados por una clase que implemente Iterator, tal como `ArrayIterator`. |
| 7.4.0 | A partir de PHP 7.4.0, las instancias de clases [SPL](#book.spl) son tratadas como objetos vacíos sin propiedades en lugar de llamar al método Iterator con el mismo nombre que esta función. |

## Ejemplos

Ejemplo con `key`

```
<?php
$array = array(
    'fruit1' => 'apple',
    'fruit2' => 'orange',
    'fruit3' => 'grape',
    'fruit4' => 'apple',
    'fruit5' => 'apple');

// Este ciclo muestra todas las claves
// cuyo valor es "apple"
while ($fruit_name = current($array)) {
    if ($fruit_name == 'apple') {
        echo key($array), "\n";
    }
    next($array);
}
?>

    
```php

El ejemplo anterior mostrará:

    fruit1
    fruit4
    fruit5

## Véase también

`current`, `next`, `array_key_first`, [foreach](#control-structures.foreach)
