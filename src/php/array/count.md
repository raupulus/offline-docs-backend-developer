---
title: count
description: Cuenta todos los elementos de un array o en un objeto Countable
source_url: https://www.php.net/manual/es/function.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5770
---

count

Cuenta todos los elementos de un array o en un objeto

Countable

## Descripción

```php
count(Countable $value, [int $mode]): int
```php

Cuenta todos los elementos en un array cuando se utiliza con un `array`. Cuando se utiliza con un objeto que implementa la interfaz Countable, esto devuelve el valor de la método Countable::count.

## Parámetros

`value`  
Un array o un objeto Countable.

`mode`  
Si el parámetro opcional `mode` vale `COUNT_RECURSIVE` (o 1), `count` va contar recursivamente los arrays. Esto es particularmente útil para contar el número de elementos de un array.

> [!CAUTION]
> La función `count` puede detectar las recursiones para evitar bucles infinitos, pero emitirá una advertencia de tipo `E_WARNING` cada vez que ocurra un bucle infinito (en el caso de que un array contenga más de un bucle infinito) y devolverá un contador mayor que el esperado.

## Valores devueltos

Devuelve el número de elementos en `value`. Anterior a PHP 8.0.0, si el parámetro no era ni un `array`, ni un `object` que implementara la interfaz Countable, `1` era devuelto, excepto si `value` era `null`, en cuyo caso `0` era devuelto.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `count` ahora lanza una `TypeError` para tipos contables inválidos pasados al parámetro `value`. |
| 7.2.0 | `count` ahora genera una advertencia para tipos contables inválidos pasados al parámetro `value`. |

## Ejemplos

Ejemplo con `count`

```
<?php
$a[0] = 1;
$a[1] = 3;
$a[2] = 5;
var_dump(count($a));

$b[0]  = 7;
$b[5]  = 9;
$b[10] = 11;
var_dump(count($b));
?>

    
```php

El ejemplo anterior mostrará:

```
int(3)
int(3)

    
```php

Ejemplo de `count` con un argumento no Countable\|array (contraejemplo - no hacer esto)

```
<?php
$b[0]  = 7;
$b[5]  = 9;
$b[10] = 11;
var_dump(count($b));

var_dump(count(null));

var_dump(count(false));
?>

    
```php

El ejemplo anterior mostrará:

```
int(3)

Fatal error: Uncaught TypeError: count(): Argument #1 ($var) must be of type Countable .. on line 12

    
```php

Ejemplo de recursividad con `count`

```
<?php
$food = array('fruits' => array('orange', 'banana', 'apple'),
              'veggie' => array('carrot', 'collard', 'pea'));

// count recursivo
var_dump(count($food, COUNT_RECURSIVE));

// count normal
var_dump(count($food));

?>

    
```php

El ejemplo anterior mostrará:

```
int(8)
int(2)

    
```php

Objeto Countable

```
<?php
class CountOfMethods implements Countable
{
    private function someMethod()
    {
    }
    public function count(): int
    {
        return count(get_class_methods($this));
    }
}
$obj = new CountOfMethods();
var_dump(count($obj));
?>

    
```php

El ejemplo anterior mostrará:

```
int(2)

    
```php

## Véase también

`is_array`, `isset`, `empty`, `strlen`, `is_countable`, [Los arrays](#language.types.array)
