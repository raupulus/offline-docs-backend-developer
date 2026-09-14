---
title: arsort
description: Ordena un array en orden descendente y conserva la asociación de los
  índices
source_url: https://www.php.net/manual/es/function.arsort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/arsort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2ca090342
order: 5740
---

arsort

Ordena un array en orden descendente y conserva la asociación de los índices

## Descripción

```php
arsort(array $array, [int $flags]): true
```php

Ordena `array` en el lugar en orden descendente, de tal manera que la correlación entre las claves y los valores se conserve.

El uso principal es cuando se ordenan arrays asociativos donde el orden de los elementos es importante.

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

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `arsort`

```
<?php
$fruits = array("d" => "lemon", "a" => "orange", "b" => "banana", "c" => "apple");
arsort($fruits);
foreach ($fruits as $key => $val) {
    echo "$key = $val\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    a = orange
    d = lemon
    b = banana
    c = apple

        

Las frutas han sido ordenadas en orden alfabético inverso, y sus índices respectivos han sido conservados.

## Véase también

sort

asort

Las funciones de

ordenación de arrays
