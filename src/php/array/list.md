---
title: list
description: Asigna variables como si fueran un array
source_url: https://www.php.net/manual/es/function.list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: eaec4ab10
order: 5870
---

list

Asigna variables como si fueran un array

## Descripción

```php
list(mixed $var, [mixed ...$vars]): array
```php

Al igual que `array`, esto no es realmente una función, sino una construcción del lenguaje. `list` se utiliza para asignar una lista de variables en una sola operación. Solo se pueden desempaquetar arrays y objetos que implementen [ArrayAccess](#class.arrayaccess). Las expresiones `list` no pueden estar completamente vacías.

> [!NOTE]
> Antes de PHP 7.1.0, `list` solo funcionaba con arrays numéricos y asumía que los índices numéricos comenzaban en 0.

A partir de PHP 7.1.0, `list` también puede contener claves explícitas, permitiendo la desestructuración de arrays con claves no enteras o no secuenciales. Para más detalles sobre la desestructuración de arrays, consulte la [sección de desestructuración de arrays](#language.types.array.syntax.destructuring).

> [!NOTE]
> Intentar acceder a una clave de array que no ha sido definida es lo mismo que acceder a cualquier otra variable no definida: se emitirá un mensaje de error de nivel `E_WARNING` (nivel `E_NOTICE` antes de PHP 8.0.0) y el resultado será `null`.
>
> Intentar desempaquetar un escalar asigna `null` a todas las variables. Intentar desempaquetar un objeto que no implementa ArrayAccess es un error fatal.

## Parámetros

`var`  
Una variable.

<!-- -->

`vars`  
Variables adicionales.

## Valores devueltos

Devuelve el array asignado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.0 | Se añadió soporte para asignaciones por referencia en la desestructuración de arrays. |
| 7.1.0 | Ahora es posible especificar claves en `list`. Esto permite la desestructuración de arrays con claves no enteras o no secuenciales. |

## Ejemplos

Ejemplos de `list`

```
<?php

$info = array('coffee', 'brown', 'caffeine');

// Listando todas las variables
list($drink, $color, $power) = $info;
echo "$drink es $color y $power lo hace especial.\n";

// Listando algunas de ellas
list($drink, , $power) = $info;
echo "$drink tiene $power.\n";

// O saltemos solo a la tercera
list( , , $power) = $info;
echo "¡Necesito $power!\n";

// list() no funciona con strings
list($bar) = "abcde";
var_dump($bar); // NULL
?>

    
```php

Un ejemplo de uso de `list`

```
<?php
$result = $pdo->query("SELECT id, name FROM employees");
while (list($id, $name) = $result->fetch(PDO::FETCH_NUM)) {
    echo "id: $id, name: $name\n";
}
?>

    
```php

Uso de `list` anidado

```
<?php

list($a, list($b, $c)) = array(1, array(2, 3));

var_dump($a, $b, $c);

?>

    
```php

El ejemplo anterior mostrará:

    int(1)
    int(2)
    int(3)

El orden en el que se definen los índices del array a ser consumido por `list` es irrelevante.

`list` y el orden de las definiciones de índices

```
<?php
$foo = array(2 => 'a', 'foo' => 'b', 0 => 'c');
$foo[1] = 'd';
list($x, $y, $z) = $foo;
var_dump($foo, $x, $y, $z);

    
```php

Produce la siguiente salida (note el orden de los elementos comparado con el orden en que fueron escritos en la sintaxis `list`):

    array(4) {
      [2]=>
      string(1) "a"
      ["foo"]=>
      string(1) "b"
      [0]=>
      string(1) "c"
      [1]=>
      string(1) "d"
    }
    string(1) "c"
    string(1) "d"
    string(1) "a"

`list` con claves

A partir de PHP 7.1.0 `list` ahora también puede contener claves explícitas, que pueden ser dadas como expresiones arbitrarias. Se permite mezclar claves enteras y string; sin embargo, no se pueden mezclar elementos con y sin claves.

```
<?php
$data = [
    ["id" => 1, "name" => 'Tom'],
    ["id" => 2, "name" => 'Fred'],
];
foreach ($data as ["id" => $id, "name" => $name]) {
    echo "id: $id, name: $name\n";
}
echo PHP_EOL;
list(1 => $second, 3 => $fourth) = [1, 2, 3, 4];
echo "$second, $fourth\n";

    
```php

El ejemplo anterior mostrará:

    id: 1, name: Tom
    id: 2, name: Fred

    2, 4

## Véase también

`each`, `array`, `extract`
