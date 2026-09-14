---
title: foreach
source_url: https://www.php.net/manual/es/control-structures.foreach.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/foreach.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: ba7093cf7
order: 2160
---

## foreach

La estructura `foreach` proporciona una forma sencilla de iterar sobre `array`s y objetos Traversable. `foreach` generará un error cuando se utilice con una variable que contenga un tipo de dato diferente o con una variable no inicializada.

`foreach` puede obtener opcionalmente la `key` de cada elemento:

    foreach (iterable_expression as $value) {
        statement_list
    }

    foreach (iterable_expression as $key => $value) {
        statement_list
    }

La primera forma recorre el iterable dado por `iterable_expression`. En cada iteración, el valor del elemento actual se asigna a `$value`.

La segunda forma asignará adicionalmente la clave del elemento actual a la variable `$key` en cada iteración.

Tenga en cuenta que `foreach` no modifica el puntero interno del array, que es utilizado por funciones como `current` y `key`.

Es posible [personalizar la iteración de objetos](#language.oop5.iterations).

Usos comunes de `foreach`

```php
<?php

/* Ejemplo: solo valor */
$array = [1, 2, 3, 17];

foreach ($array as $value) {
    echo "Elemento actual de \$array: $value.\n";
}

/* Ejemplo: clave y valor */
$array = [
    "one" => 1,
    "two" => 2,
    "three" => 3,
    "seventeen" => 17
];

foreach ($array as $key => $value) {
    echo "Clave: $key => Valor: $value\n";
}

/* Ejemplo: arrays multidimensionales clave-valor */
$grid = [];
$grid[0][0] = "a";
$grid[0][1] = "b";
$grid[1][0] = "y";
$grid[1][1] = "z";

foreach ($grid as $y => $row) {
    foreach ($row as $x => $value) {
        echo "Valor en posición x=$x y y=$y: $value\n";
    }
}

/* Ejemplo: arrays dinámicos */
foreach (range(1, 5) as $value) {
    echo "$value\n";
}
?>

  
```

> [!NOTE]
> `foreach` no admite la capacidad de suprimir mensajes de error utilizando [`@`](#language.operators.errorcontrol).

## Desempaquetar arrays anidados

Es posible iterar sobre un array de arrays y desempaquetar el array anidado en variables de bucle utilizando ya sea [destructuración de arrays](#language.types.array.syntax.destructuring) mediante `[]` o utilizando la estructura de lenguaje `list` como valor.

> [!NOTE]
> Tenga en cuenta que [destructuración de arrays](#language.types.array.syntax.destructuring) mediante `[]` solo es posible a partir de PHP 7.1.0

En ambos ejemplos siguientes, `$a` se establecerá con el primer elemento del array anidado y `$b` contendrá el segundo elemento:

```php
<?php
$array = [
    [1, 2],
    [3, 4],
];

foreach ($array as [$a, $b]) {
    echo "A: $a; B: $b\n";
}

foreach ($array as list($a, $b)) {
    echo "A: $a; B: $b\n";
}
?>

    
```

El ejemplo anterior mostrará:

    A: 1; B: 2
    A: 3; B: 4

Cuando se proporcionan menos variables que elementos en el array, los elementos restantes serán ignorados. De manera similar, los elementos pueden omitirse utilizando una coma:

```php
<?php
$array = [
    [1, 2, 5],
    [3, 4, 6],
];

foreach ($array as [$a, $b]) {
    // Note que no hay $c aquí.
    echo "$a $b\n";
}

foreach ($array as [, , $c]) {
    // Omitiendo $a y $b
    echo "$c\n";
}
?>

    
```

El ejemplo anterior mostrará:

    1 2
    3 4
    5
    6

Se generará un aviso si no hay suficientes elementos en el array para llenar el `list`:

```php
<?php
$array = [
    [1, 2],
    [3, 4],
];

foreach ($array as [$a, $b, $c]) {
    echo "A: $a; B: $b; C: $c\n";
}
?>

    
```

El ejemplo anterior mostrará:

    Notice: Undefined offset: 2 in example.php on line 7
    A: 1; B: 2; C:

    Notice: Undefined offset: 2 in example.php on line 7
    A: 3; B: 4; C:

## foreach y referencias

Es posible modificar directamente elementos de array dentro de un bucle precediendo `$value` con `&`. En ese caso el valor será asignado por [referencia](#language.references).

```php
<?php
$arr = [1, 2, 3, 4];
foreach ($arr as &$value) {
    $value = $value * 2;
}
// $arr es ahora [2, 4, 6, 8]
unset($value); // romper la referencia con el último elemento
?>

    
```

> [!WARNING]
> La referencia a un `$value` del último elemento del array permanece incluso después del bucle `foreach`. Se recomienda destruir estas referencias utilizando `unset`. De lo contrario, ocurrirá el siguiente comportamiento:
>
> <div class="informalexample">
>
> ```
> <?php
> $arr = [1, 2, 3, 4];
> foreach ($arr as &$value) {
>     $value = $value * 2;
> }
> // $arr es ahora [2, 4, 6, 8]
>
> // sin un unset($value), $value sigue siendo una referencia al último elemento: $arr[3]
>
> foreach ($arr as $key => $value) {
>     // $arr[3] se actualizará con cada valor de $arr...
>     echo "{$key} => {$value} ";
>     print_r($arr);
> }
> // ...hasta que finalmente el penúltimo valor se copie sobre el último valor
> ?>
>
>     
> ```
>
> El ejemplo anterior mostrará:
>
>     0 => 2 Array ( [0] => 2, [1] => 4, [2] => 6, [3] => 2 )
>     1 => 4 Array ( [0] => 2, [1] => 4, [2] => 6, [3] => 4 )
>     2 => 6 Array ( [0] => 2, [1] => 4, [2] => 6, [3] => 6 )
>     3 => 6 Array ( [0] => 2, [1] => 4, [2] => 6, [3] => 6 )
>
>         
>
> </div>

Iterar los valores de un array constante por referencia

```php
<?php
foreach ([1, 2, 3, 4] as &$value) {
    $value = $value * 2;
}
?>

   
```

## Véase también

array

Traversable

iterable

list
