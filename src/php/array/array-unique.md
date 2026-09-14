---
title: array_unique
description: Elimina los valores duplicados de un array
source_url: https://www.php.net/manual/es/function.array-unique.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-unique.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 651fad6c6
order: 5680
---

array_unique

Elimina los valores duplicados de un array

## Descripción

```php
array_unique(array $array, [int $flags]): array
```php

`array_unique` extrae del array `array` los valores distintos, y elimina todos los duplicados.

Tenga en cuenta que las claves se preservan. Si varios elementos comparados son iguales bajo el `flags` dado, entonces la clave y el valor del primer elemento igual serán conservados.

> [!NOTE]
> Dos elementos se consideran iguales si y solo si `(string) $elem1 === (string) $elem2`, es decir, cuando la representación en string es idéntica.

## Parámetros

`array`  
El array de entrada.

`flags`  
El segundo parámetro opcional `flags` puede ser utilizado para modificar el comportamiento de comparación utilizando los siguientes valores:

Flag de tipo de comparación:

- `SORT_REGULAR` - compara los elementos normalmente (no modifica los tipos)

- `SORT_NUMERIC` - compara los elementos numéricamente

- `SORT_STRING` - compara los elementos como strings

- `SORT_LOCALE_STRING` - compara los elementos como strings, según la configuración local actual.

## Valores devueltos

Devuelve el array filtrado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | Si `flags` es `SORT_STRING`, anteriormente `array` era copiado y los elementos no únicos eran eliminados (sin comprimir el array después), pero ahora se construye un nuevo array añadiendo los elementos únicos. Como consecuencia, el resultado final puede tener índices numéricos diferentes. |

## Ejemplos

Ejemplo con `array_unique`

```
<?php

$input = ["a" => "green", "red", "b" => "green", "blue", "red"];
$result = array_unique($input);
print_r($result);

?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [a] => green
    [0] => red
    [1] => blue
)

    
```php

Ejemplo con `array_unique` y los tipos

```
<?php

$input = [4, "4", "3", 4, 3, "3"];
$result = array_unique($input);
var_dump($result);

?>

    
```php

El ejemplo anterior mostrará:

```
array(2) {
  [0] => int(4)
  [2] => string(1) "3"
}

    
```php

## Notas

> [!NOTE]
> Tenga en cuenta que `array_unique` no funciona con arrays multidimensionales.

## Véase también

`array_count_values`
