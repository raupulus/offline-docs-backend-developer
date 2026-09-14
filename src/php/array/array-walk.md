---
title: array_walk
description: Ejecuta una función proporcionada por el usuario en cada uno de los elementos
  de un array
source_url: https://www.php.net/manual/es/function.array-walk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-walk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 4ca7cdeae
order: 5720
---

array_walk

Ejecuta una función proporcionada por el usuario en cada uno de los elementos de un array

## Descripción

```php
array_walk(array $array, callable $callback, [mixed $arg]): true
```php

Ejecuta la función `callback` definida por el usuario en cada elemento del array `array`.

`array_walk` no es afectado por el puntero interno del array `array`. `array_walk` recorrerá el array en su totalidad sin tener en cuenta la posición del puntero.

## Parámetros

`array`  
El array de entrada.

`callback`  
Típicamente, `callback` toma dos parámetros. El valor del parámetro `array` siendo el primero y la clave/índice, el segundo.

> [!NOTE]
> Si `callback` debe trabajar con los verdaderos valores del array, especifique que el primer parámetro de `callback` debe ser pasado por [referencia](#language.references). Entonces, los elementos serán directamente modificados en el array.

> [!NOTE]
> Varias funciones internas (por ejemplo, `strtolower`) emiten una alerta si más argumentos que los esperados son pasados a la función y no son utilizables directamente como `callback`.

Solo los valores del `array` pueden ser modificados; su estructura no puede ser modificada, es decir, no se pueden añadir, eliminar o reordenar elementos. Si la función de callback no respeta esta regla, el comportamiento se volverá indefinido e impredecible.

`arg`  
Si el parámetro opcional `arg` es proporcionado, será pasado como tercer parámetro a la función definida por el usuario `callback`.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

A partir de PHP 7.1.0, un `ArgumentCountError` será lanzado si la función `callback` requiere más de 2 parámetros (el valor y la clave del elemento del array), o más de 3 si `arg` también es proporcionado. Anteriormente, en este caso un error de nivel [E_WARNING](#errorfunc.constants) habría sido generado cada vez que la función `array_walk` llama a `callback`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El tipo de retorno es ahora `true`, anteriormente era `bool`. |
| 8.0.0 | Si `callback` espera que el segundo o tercer parámetro sea pasado por referencia, esta función ahora emite una `E_WARNING`. |

## Ejemplos

Ejemplo con `array_walk`

```
<?php
$fruits = array("d" => "lemon", "a" => "orange", "b" => "banana", "c" => "apple");

function test_alter(&$item1, $key, $prefix)
{
    $item1 = "$prefix: $item1";
}

function test_print($item2, $key)
{
    echo "$key. $item2\n";
}

echo "Antes ...:\n";
array_walk($fruits, 'test_print');

array_walk($fruits, 'test_alter', 'fruit');
echo "... y después :\n";

array_walk($fruits, 'test_print');
?>

    
```php

El ejemplo anterior mostrará:

```
Antes ...:
d. lemon
a. orange
b. banana
c. apple
... y después :
d. fruit: lemon
a. fruit: orange
b. fruit: banana
c. fruit: apple

    
```php

Ejemplo de `array_walk` con el uso de una función anónima

```
<?php
$elements = ['a', 'b', 'c'];

array_walk($elements, function ($value, $key) {
  echo "{$key} => {$value}\n";
});

?>

    
```php

El ejemplo anterior mostrará:

```
0 => a
1 => b
2 => c

    
```php

## Véase también

`array_walk_recursive`, `iterator_apply`, `list`, `each`, `call_user_func_array`, `array_map`, [`foreach`](#control-structures.foreach)
