---
title: array_udiff
description: Calcula la diferencia entre dos arrays utilizando una función de retrollamada
source_url: https://www.php.net/manual/es/function.array-udiff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-udiff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 56509d07a
order: 5640
---

array_udiff

Calcula la diferencia entre dos arrays utilizando una función de retrollamada

## Descripción

```php
array_udiff(array $array, array ...$arrays, callable $value_compare_func): array
```php

Calcula la diferencia entre dos arrays utilizando una función de retrollamada. Esta función actúa como la función `array_diff` que utiliza una función interna para comparar los datos.

## Parámetros

`array`  
El primer array.

`arrays`  
Arrays a comparar contra

`value_compare_func`  
La función de comparación.

La función de comparación debe retornar un entero menor que, igual a, o mayor que 0 si el primer argumento es considerado, respectivamente, menor que, igual a, o mayor que el segundo.

```php
callback(mixed $a, mixed $b): int
```

> [!CAUTION]
> Devolver valores *no enteros* (como `float`) desde la función de comparación resultará en una conversión interna del valor de retorno de la retrollamada a `int`. Así, valores como `0.99` y `0.1` serán convertidos ambos al valor entero `0`, por lo que se compararán como iguales.

> [!CAUTION]
> La función de callback de ordenación debe tratar cualquier valor de cualquier array en cualquier orden, independientemente del orden en el que fueron proporcionados inicialmente. Esto se debe a que cada array individual es ordenado primero antes de ser comparado con otros arrays. Por ejemplo:
>
> ```
> <?php
> $arrayA = ["string", 1];
> $arrayB = [["value" => 1]];
> // $item1 y $item2 pueden ser cualquiera de los siguientes valores : "cadena", 1 o
> ["value" => 1] $compareFunc = static function ($item1,
>     $item2) { $value1 = is_string($item1) ? strlen($item1) : (is_array($item1) ? $item1["value"] :
>     $item1); $value2 = is_string($item2) ? strlen($item2) : (is_array($item2) ? $item2["value"] : $item2);
>     return $value1 <=> $value2;
> };
> ?>
>
>   
> ```

## Valores devueltos

Retorna un array que contiene todas las valores del array `array` que no están presentes en ningún otro argumento.

## Ejemplos

Ejemplo con `array_udiff` utilizando objetos stdClass

```php
<?php
// Arrays a comparar
$array1 = array(new stdClass, new stdClass,
                new stdClass, new stdClass,
               );

$array2 = array(
                new stdClass, new stdClass,
               );

// Define algunas propiedades para cada objeto
$array1[0]->width = 11; $array1[0]->height = 3;
$array1[1]->width = 7;  $array1[1]->height = 1;
$array1[2]->width = 2;  $array1[2]->height = 9;
$array1[3]->width = 5;  $array1[3]->height = 7;

$array2[0]->width = 7;  $array2[0]->height = 5;
$array2[1]->width = 9;  $array2[1]->height = 2;

function compare_by_area($a, $b) {
    $areaA = $a->width * $a->height;
    $areaB = $b->width * $b->height;

    if ($areaA < $areaB) {
        return -1;
    } elseif ($areaA > $areaB) {
        return 1;
    } else {
        return 0;
    }
}

print_r(array_udiff($array1, $array2, 'compare_by_area'));
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => stdClass Object
            (
                [width] => 11
                [height] => 3
            )

        [1] => stdClass Object
            (
                [width] => 7
                [height] => 1
            )

    )

Ejemplo con `array_udiff` utilizando objetos DateTime

```php
<?php
class MyCalendar {
    public $free = array();
    public $booked = array();

    public function __construct($week = 'now') {
        $start = new DateTime($week);
        $start->modify('Monday this week midnight');
        $end = clone $start;
        $end->modify('Friday this week midnight');
        $interval = new DateInterval('P1D');
        foreach (new DatePeriod($start, $interval, $end) as $freeTime) {
            $this->free[] = $freeTime;
        }
    }

    public function bookAppointment(DateTime $date, $note) {
        $this->booked[] = array('date' => $date->modify('midnight'), 'note' => $note);
    }

    public function checkAvailability() {
        return array_udiff($this->free, $this->booked, array($this, 'customCompare'));
    }

    public function customCompare($free, $booked) {
        if (is_array($free)) $a = $free['date'];
        else $a = $free;
        if (is_array($booked)) $b = $booked['date'];
        else $b = $booked;
        if ($a == $b) {
            return 0;
        } elseif ($a > $b) {
            return 1;
        } else {
            return -1;
        }
    }
}

// Crea un calendario para las citas semanales
$myCalendar = new MyCalendar;

// Registra algunas citas para esta semana
$myCalendar->bookAppointment(new DateTime('Monday this week'), "Limpiar el apartamento de GoogleGuy.");
$myCalendar->bookAppointment(new DateTime('Wednesday this week'), "Ir a un viaje de snowboard.");
$myCalendar->bookAppointment(new DateTime('Friday this week'), "Arreglar código con errores.");

// Verifica la disponibilidad en días, comparando las fechas $booked con las fechas $free
echo "Estoy disponible en los siguientes días esta semana...\n\n";
foreach ($myCalendar->checkAvailability() as $free) {
    echo $free->format('l'), "\n";
}
echo "\n\n";
echo "Estoy ocupado en los siguientes días esta semana...\n\n";
foreach ($myCalendar->booked as $booked) {
    echo $booked['date']->format('l'), ": ", $booked['note'], "\n";
}
?>

    
```

El ejemplo anterior mostrará:

    Estoy disponible en los siguientes días esta semana...

    Tuesday
    Thursday

    Estoy ocupado en los siguientes días esta semana...

    Monday: Limpiar el apartamento de GoogleGuy.
    Wednesday: Ir a un viaje de snowboard.
    Friday: Arreglar código con errores.

## Notas

> [!NOTE]
> Tenga en cuenta que esta función solo verifica una dimensión de un array multidimensional. Por supuesto, se puede probar una dimensión particular utilizando, por ejemplo, `array_udiff($array1[0], $array2[0], "data_compare_func");`.

## Véase también

`array_diff`, `array_diff_assoc`, `array_diff_uassoc`, `array_udiff_assoc`, `array_udiff_uassoc`, `array_intersect`, `array_intersect_assoc`, `array_uintersect`, `array_uintersect_assoc`, `array_uintersect_uassoc`
