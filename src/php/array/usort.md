---
title: usort
description: Ordena un array utilizando una función de comparación
source_url: https://www.php.net/manual/es/function.usort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/usort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 6010
---

usort

Ordena un array utilizando una función de comparación

## Descripción

```php
usort(array $array, callable $callback): true
```php

Ordena `array` en su lugar según los valores utilizando una función de comparación definida por el usuario.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

> [!NOTE]
> Esta función asigna nuevas claves a los elementos en `array`. Eliminará todas las claves existentes que hayan podido ser asignadas, en lugar de reordenar las claves.

## Parámetros

`array`  
El array de entrada.

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

| Versión | Descripción |
|----|----|
| 8.2.0 | El tipo de retorno es ahora `true`, anteriormente era `bool`. |
| 8.0.0 | Si `callback` espera un parámetro a ser pasado por referencia, esta función emite ahora una `E_WARNING`. |

## Ejemplos

Ejemplo con `usort`

```php
<?php
function cmp($a, $b)
{
    if ($a == $b) {
        return 0;
    }
    return ($a < $b) ? -1 : 1;
}

$a = array(3, 2, 5, 6, 1);

usort($a, "cmp");

foreach ($a as $key => $value) {
    echo "$key: $value\n";
}
?>

    
```

El ejemplo anterior mostrará:

    0: 1
    1: 2
    2: 3
    3: 5
    4: 6

        

El operador combinado puede ser utilizado para simplificar la comparación interna.

```php
<?php
function cmp($a, $b)
{
    return $a <=> $b;
}

$a = array(3, 2, 5, 6, 1);

usort($a, "cmp");

foreach ($a as $key => $value) {
    echo "$key: $value\n";
}
?>

    
```

> [!NOTE]
> Evidentemente en este caso trivial, `sort` sería más apropiado.

Ordenación con `usort` sobre un array multidimensional

```php
<?php
function cmp($a, $b)
{
    return strcmp($a["fruit"], $b["fruit"]);
}

$fruits[0]["fruit"] = "lemons";
$fruits[1]["fruit"] = "apples";
$fruits[2]["fruit"] = "grapes";

usort($fruits, "cmp");

foreach ($fruits as $key => $value) {
    echo "\$fruits[$key]: " . $value["fruit"] . "\n";
}
?>

    
```

El ejemplo anterior mostrará:

    $fruits[0]: apples
    $fruits[1]: grapes
    $fruits[2]: lemons

        

Al ordenar arrays multidimensionales, `$a` y `$b` contienen referencias al primer elemento del array.

Ordenación con `usort` sobre un objeto

```php
<?php
class TestObj {
    public string $name;

    function __construct($name)
    {
        $this->name = $name;
    }

    /* Esta es una función de comparación estática */
    static function cmp_obj($a, $b)
    {
        return strtolower($a->name) <=> strtolower($b->name);
    }
}

$a[] = new TestObj("c");
$a[] = new TestObj("b");
$a[] = new TestObj("d");

usort($a, [TestObj::class, "cmp_obj"]);

foreach ($a as $item) {
    echo $item->name . "\n";
}
?>

    
```

El ejemplo anterior mostrará:

    b
    c
    d

Ejemplo con `usort` utilizando una [closure](#functions.anonymous) para ordenar un array multidimensional

```php
<?php
$array[0] = array('key_a' => 'z', 'key_b' => 'c');
$array[1] = array('key_a' => 'x', 'key_b' => 'b');
$array[2] = array('key_a' => 'y', 'key_b' => 'a');

function build_sorter($key) {
    return function ($a, $b) use ($key) {
        return strnatcmp($a[$key], $b[$key]);
    };
}

usort($array, build_sorter('key_b'));

foreach ($array as $item) {
    echo $item['key_a'] . ', ' . $item['key_b'] . "\n";
}
?>

    
```

El ejemplo anterior mostrará:

    y, a
    x, b
    z, c

Ejemplo de uso del operador combinado con `usort`.

El operador combinado permite una comparación directa de valores compuestos sobre múltiples ejes. En el ejemplo siguiente, `$people` se ordena por apellido, luego por nombre si el apellido coincide.

```php
<?php
$people[0] = ['first' => 'Adam', 'last' => 'West'];
$people[1] = ['first' => 'Alec', 'last' => 'Baldwin'];
$people[2] = ['first' => 'Adam', 'last' => 'Baldwin'];

function sorter(array $a, array $b) {
    return [$a['last'], $a['first']] <=> [$b['last'], $b['first']];
}

usort($people, 'sorter');

foreach ($people as $person) {
    print $person['last'] . ', ' . $person['first'] . PHP_EOL;
}
?>

    
```

El ejemplo anterior mostrará:

    Baldwin, Adam
    Baldwin, Alec
    West, Adam

## Véase también

uasort

uksort

Las funciones de

ordenación de arrays
