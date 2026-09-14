---
title: ArrayObject::uksort
description: Ordena los elementos por clave con una función utilitaria
source_url: https://www.php.net/manual/es/arrayobject.uksort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/uksort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 2226ad08f
order: 81550
---

ArrayObject::uksort

Ordena los elementos por clave con una función utilitaria

## Descripción

```php
public ArrayObject::uksort(callable $callback): true
```php

Esta función ordena las claves de los elementos utilizando una función utilitaria de comparación. La correlación entre las claves y los elementos se conserva.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

## Parámetros

`callback`  
La función de comparación debe retornar un entero menor que, igual a, o mayor que 0 si el primer argumento es considerado, respectivamente, menor que, igual a, o mayor que el segundo.

```php
callback(mixed $a, mixed $b): int
```

> [!CAUTION]
> Devolver valores *no enteros* (como `float`) desde la función de comparación resultará en una conversión interna del valor de retorno de la retrollamada a `int`. Así, valores como `0.99` y `0.1` serán convertidos ambos al valor entero `0`, por lo que se compararán como iguales.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `ArrayObject::uksort`

```php
<?php
function cmp($a, $b) {
    $a = preg_replace('@^(le|la|les|un|une|des) @', '', $a);
    $b = preg_replace('@^(le|la|les|un|une|des) @', '', $b);
    return strcasecmp($a, $b);
}

$array = array("Jean" => 1, "la Terre" => 2, "une pomme" => 3, "une banane" => 4);
$arrayObject = new ArrayObject($array);
$arrayObject->uksort('cmp');

foreach ($arrayObject as $key => $value) {
    echo "$key: $value\n";
}
?>

    
```

El ejemplo anterior mostrará:

    une banane: 4
    Jean: 1
    une pomme: 3
    la Terre: 2

## Véase también

ArrayObject::asort, ArrayObject::ksort, ArrayObject::natsort, ArrayObject::natcasesort, ArrayObject::uasort, `uksort`
