---
title: ksort
description: Ordena un array según las claves en orden ascendente
source_url: https://www.php.net/manual/es/function.ksort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/ksort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 4acad9b77
order: 5860
---

ksort

Ordena un array según las claves en orden ascendente

## Descripción

```php
ksort(array $array, [int $flags]): true
```php

Ordena `array` en su lugar según las claves en orden ascendente.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

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

| Versión | Descripción |
|----|----|
| 8.2.0 | El tipo de retorno es ahora `true`, anteriormente era `bool`. |
| 8.2.0 | Esta función realiza ahora una comparación de strings numéricos bajo `SORT_REGULAR` utilizando las reglas estándar de PHP 8. |

## Ejemplos

Ejemplo con `ksort`

```
<?php
$fruits = array("d"=>"lemon", "a"=>"orange", "b"=>"banana", "c"=>"apple");
ksort($fruits);
foreach ($fruits as $key => $val) {
    echo "$key = $val\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    a = orange
    b = banana
    c = apple
    d = lemon

`ksort` con claves `int`

```
<?php
$a = [0 => 'First', 2 => 'Last', 1 => 'Middle'];
var_dump($a);
ksort($a);
var_dump($a);
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      string(5) "First"
      [2]=>
      string(4) "Last"
      [1]=>
      string(6) "Middle"
    }
    array(3) {
      [0]=>
      string(5) "First"
      [1]=>
      string(6) "Middle"
      [2]=>
      string(4) "Last"
    }

## Véase también

sort

krsort

Las funciones de

ordenación de arrays
