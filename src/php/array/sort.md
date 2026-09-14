---
title: sort
description: Ordena un array en orden creciente
source_url: https://www.php.net/manual/es/function.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2ca090342
order: 5980
---

sort

Ordena un array en orden creciente

## Descripción

```php
sort(array $array, [int $flags]): true
```php

Ordena `array` en su lugar siguiendo los valores en orden creciente.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

> [!NOTE]
> Esta función asigna nuevas claves a los elementos en `array`. Eliminará todas las claves existentes que hayan podido ser asignadas, en lugar de reordenar las claves.

> [!NOTE]
> Reinicia el puntero interno del array al primer elemento.

## Parámetros

`array`  
El array de entrada.

`flags`  
El segundo parámetro opcional `flags` puede ser utilizado para modificar el comportamiento de ordenación utilizando estos valores:

Tipo de banderas de ordenación:

- `SORT_REGULAR` - compara los elementos normalmente; los detalles son descritos en la sección de los [operadores de comparación](#language.operators.comparison)

- `SORT_NUMERIC` - compara los elementos numéricamente

- `SORT_STRING` - compara los elementos como strings

- `SORT_LOCALE_STRING` - compara los elementos como strings, basado en la configuración regional actual. Esto utiliza la configuración regional, que puede ser cambiada utilizando `setlocale`

- `SORT_NATURAL` - compara los elementos como strings utilizando el "orden natural" como `natsort`

- `SORT_FLAG_CASE` - puede ser combinado (OR a nivel de bits) con `SORT_STRING` o `SORT_NATURAL` para ordenar strings sin tener en cuenta la mayúscula/minúscula

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `sort`

```
<?php

$fruits = array("lemon", "orange", "banana", "apple");
sort($fruits);
foreach ($fruits as $key => $val) {
    echo "fruits[" . $key . "] = " . $val . "\n";
}

?>

    
```php

El ejemplo anterior mostrará:

    fruits[0] = apple
    fruits[1] = banana
    fruits[2] = lemon
    fruits[3] = orange

Las frutas han sido ordenadas en orden alfabético.

Ejemplo con `sort` utilizando el orden natural sin tener en cuenta la casilla

```
<?php

$fruits = array(
    "Orange1", "orange2", "Orange3", "orange20"
);
sort($fruits, SORT_NATURAL | SORT_FLAG_CASE);
foreach ($fruits as $key => $val) {
    echo "fruits[" . $key . "] = " . $val . "\n";
}

?>

    
```php

El ejemplo anterior mostrará:

    fruits[0] = Orange1
    fruits[1] = orange2
    fruits[2] = Orange3
    fruits[3] = orange20

Las frutas han sido ordenadas como lo habrían sido con la función `natcasesort`.

## Notas

> [!NOTE]
> Al igual que la mayoría de las funciones de ordenación de PHP, `sort` utiliza una implementación de [Quicksort](http://en.wikipedia.org/wiki/Quicksort). El pivote es elegido en el medio de la partición, resultando así en una optimización del tiempo para los arrays ya ordenados. Pero esto no es más que un detalle de la implementación, sin tener ningún impacto.

> [!WARNING]
> Prestar atención al ordenar arrays con valores de tipos diferentes ya que `sort` puede producir resultados impredecibles cuando `flags` es `SORT_REGULAR`.

## Véase también

rsort

Las funciones de

ordenación de arrays
