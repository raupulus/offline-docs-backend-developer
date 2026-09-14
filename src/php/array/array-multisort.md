---
title: array_multisort
description: Ordena los arrays multidimensionales
source_url: https://www.php.net/manual/es/function.array-multisort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-multisort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 5b7646656
order: 5470
---

array_multisort

Ordena los arrays multidimensionales

## Descripción

```php
array_multisort(array $array1, [mixed $array1_sort_order], [mixed $array1_sort_flags], mixed ...$rest): true
```php

`array_multisort` sirve para ordenar simultáneamente varios arrays, o bien para ordenar un array multidimensional, siguiendo una u otra de sus dimensiones.

Las claves asociativas (`string`) serán mantenidas, pero las claves numéricas serán reindexadas.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

> [!NOTE]
> Reinicia el puntero interno del array al primer elemento.

## Parámetros

`array1`  
Un `array` a ordenar.

`array1_sort_order`  
El orden utilizado para ordenar el argumento anterior `array`. Puede ser la constante `SORT_ASC` para ordenar de forma ascendente, o la constante `SORT_DESC` para ordenar de forma descendente.

Este argumento puede ser asociado con el parámetro `array1_sort_flags` o simplemente omitido, en cuyo caso, la constante `SORT_ASC` será utilizada.

`array1_sort_flags`  
Opciones de ordenación del argumento `array` anterior:

Tipo de opciones de ordenación:

- `SORT_REGULAR` - compara los elementos normalmente (sin cambio de tipo)

- `SORT_NUMERIC` - compara los elementos numéricamente

- `SORT_STRING` - compara los elementos como strings

- `SORT_LOCALE_STRING` - compara los elementos como strings, basándose en la configuración local actual. La función utiliza las locales, y estas pueden ser modificadas utilizando la función `setlocale`

- `SORT_NATURAL` - compara los elementos como strings, utilizando el "orden natural", como lo hace la función `natsort`

- `SORT_FLAG_CASE` - puede ser combinado (con el operador OR) con `SORT_STRING` o `SORT_NATURAL` para ordenar los strings sin tener en cuenta la casilla

Este argumento puede ser asociado con el parámetro `array1_sort_order` o simplemente omitido, en cuyo caso, la constante `SORT_REGULAR` será utilizada.

`rest`  
Más argumentos, opcionalmente seguidos por formas de ordenar y flags. Solo los elementos equivalentes en los arrays anteriores son comparados. En otras palabras, el ordenamiento es lexicográfico.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                    |
|---------|----------------------------------------------------------------|
| 8.5.0   | El tipo de retorno es ahora `true`; anteriormente, era `bool`. |

## Ejemplos

Ordenar varios arrays

```
<?php
$ar1 = array(10, 100, 100, 0);
$ar2 = array(1, 3, 2, 4);
array_multisort($ar1, $ar2);

var_dump($ar1);
var_dump($ar2);
?>

    
```php

En este ejemplo, después del ordenamiento, el primer array contiene 0, 10, 100, 100. El segundo array contiene 4, 1, 2, 3. Las entradas del segundo array correspondientes a los valores duplicados del primer array (100 y 100), también son ordenadas.

    array(4) {
      [0]=> int(0)
      [1]=> int(10)
      [2]=> int(100)
      [3]=> int(100)
    }
    array(4) {
      [0]=> int(4)
      [1]=> int(1)
      [2]=> int(2)
      [3]=> int(3)
    }

Ordenar un array multidimensional

```
<?php
$ar = array(
       array("10", 11, 100, 100, "a"),
       array(   1,  2, "2",   3,   1)
      );
array_multisort($ar[0], SORT_ASC, SORT_STRING,
                $ar[1], SORT_NUMERIC, SORT_DESC);
var_dump($ar);
?>

    
```php

En este ejemplo, después del ordenamiento, el primer array contiene "10", 100, 100, 11, "a" (orden alfabético, orden ascendente); El segundo array contiene 1, 3, "2", 2, 1 (orden numérico, orden descendente).

    array(2) {
      [0]=> array(5) {
        [0]=> string(2) "10"
        [1]=> int(100)
        [2]=> int(100)
        [3]=> int(11)
        [4]=> string(1) "a"
      }
      [1]=> array(5) {
        [0]=> int(1)
        [1]=> int(3)
        [2]=> string(1) "2"
        [3]=> int(2)
        [4]=> int(1)
      }
    }

Ordenar los resultados de una base de datos

En este ejemplo, cada elemento del array `data` representa una fila de la tabla. Este tipo de datos es típico de un registro de base de datos.

Ejemplo de datos:

    volume | edition
    -------+--------
        67 |       2
        86 |       1
        85 |       6
        98 |       2
        86 |       6
        67 |       7

        

Los datos están en forma de array, llamado `data`. Esto es generalmente el resultado, por ejemplo, de la función `mysqli_fetch_assoc`.

En este ejemplo, vamos a ordenar la columna `volume` en orden descendente, y la columna `edition` en orden ascendente.

Tenemos un array de filas, pero `array_multisort` requiere un array de columnas, por lo tanto utilizamos el siguiente código para obtener las columnas y así realizar el ordenamiento.

```
<?php
// Los datos son creados recorriendo mysqli_fetch_assoc:
$data[] = array('volume' => 67, 'edition' => 2);
$data[] = array('volume' => 86, 'edition' => 1);
$data[] = array('volume' => 85, 'edition' => 6);
$data[] = array('volume' => 98, 'edition' => 2);
$data[] = array('volume' => 86, 'edition' => 6);
$data[] = array('volume' => 67, 'edition' => 7);

// Obtiene una lista de columnas
foreach ($data as $key => $row) {
    $volume[$key]  = $row['volume'];
    $edition[$key] = $row['edition'];
}

// Puede utilizarse array_column() en lugar del código anterior
$volume  = array_column($data, 'volume');
$edition = array_column($data, 'edition');

// Ordena los datos por volume descendente, edition ascendente
// Añade $data como último parámetro, para ordenar por la clave común
array_multisort($volume, SORT_DESC, $edition, SORT_ASC, $data);

// Recorre los datos y muestra los valores ordenados para cada columna
echo 'volume | edition', PHP_EOL;
echo '-------+--------', PHP_EOL;
for ($i = 0; $i < count($data); $i++) {
     printf("%6d | %7d\n", $volume[$i], $edition[$i]);
}
?>

    
```php

El conjunto de registros ahora está ordenado y se ve así:

    volume | edition
    -------+--------
        98 |       2
        86 |       1
        86 |       6
        85 |       6
        67 |       2
        67 |       7

Ordenamiento no sensible a la casilla

`SORT_STRING` y `SORT_REGULAR` son sensibles a la casilla, los strings que comienzan con una letra mayúscula vendrán antes que los strings que comienzan con una letra minúscula.

Para realizar un ordenamiento no sensible a la casilla, realice el ordenamiento sobre una copia en minúsculas de las columnas del array original.

```
<?php
$array = array('Alpha', 'atomic', 'Beta', 'bank');
$array_lowercase = array_map('strtolower', $array);

array_multisort($array_lowercase, SORT_ASC, SORT_STRING, $array);

print_r($array);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Alpha
        [1] => atomic
        [2] => bank
        [3] => Beta
    )

## Véase también

`usort`, Las funciones de [ordenación de arrays](#array.sorting)
