---
title: extract
description: Importa variables al símbolo actual desde un array
source_url: https://www.php.net/manual/es/function.extract.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/extract.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: f53ab502a
order: 5810
---

extract

Importa variables al símbolo actual desde un array

## Descripción

```php
extract(array $array, [int $flags], [string $prefix]): int
```php

Importa variables desde un array a la tabla de símbolos actual.

Verifica cada clave para determinar si tiene un nombre de variable válido. También verifica colisiones con variables existentes en la tabla de símbolos.

> [!WARNING]
> No utilice `extract` con datos no confiables, como entrada de usuario (ej. `$_GET`, `$_FILES`).

## Parámetros

`array`  
Un array asociativo. Esta función trata las claves como nombres de variables y los valores como valores de variables. Para cada par clave/valor creará una variable en la tabla de símbolos actual, sujeto a los parámetros `flags` y `prefix`.

Debe usar un array asociativo; un array indexado numéricamente no producirá resultados a menos que use `EXTR_PREFIX_ALL` o `EXTR_PREFIX_INVALID`.

`flags`  
La forma en que se tratan las claves inválidas/numéricas y las colisiones se determina por los `flags` de extracción. Puede ser uno de los siguientes valores:

`EXTR_OVERWRITE`  
Si hay una colisión, sobrescribe la variable existente.

`EXTR_SKIP`  
Si hay una colisión, no sobrescribe la variable existente.

`EXTR_PREFIX_SAME`  
Si hay una colisión, antepone el nombre de la variable con `prefix`.

`EXTR_PREFIX_ALL`  
Antepone todos los nombres de variables con `prefix`.

`EXTR_PREFIX_INVALID`  
Solo antepone nombres de variables inválidas/numéricas con `prefix`.

`EXTR_IF_EXISTS`  
Solo sobrescribe la variable si ya existe en la tabla de símbolos actual, de lo contrario no hace nada. Esto es útil para definir una lista de variables válidas y luego extraer solo esas variables que ha definido de `$_REQUEST`, por ejemplo.

`EXTR_PREFIX_IF_EXISTS`  
Solo crea nombres de variables con prefijo si la versión sin prefijo de la misma variable existe en la tabla de símbolos actual.

`EXTR_REFS`  
Extrae variables como referencias. Esto significa efectivamente que los valores de las variables importadas aún hacen referencia a los valores del parámetro `array`. Puede usar este flag por sí solo o combinarlo con cualquier otro flag mediante OR con los `flags`.

Si `flags` no está especificado, se asume que es `EXTR_OVERWRITE`.

`prefix`  
Tenga en cuenta que `prefix` solo es requerido si `flags` es `EXTR_PREFIX_SAME`, `EXTR_PREFIX_ALL`, `EXTR_PREFIX_INVALID` o `EXTR_PREFIX_IF_EXISTS`. Si el resultado con prefijo no es un nombre de variable válido, no se importará a la tabla de símbolos. Los prefijos se separan automáticamente de la clave del array por un carácter de guión bajo.

## Valores devueltos

Devuelve el número de variables importadas con éxito a la tabla de símbolos.

## Ejemplos

Ejemplo de `extract`

```
<?php
$size = "large";
$var_array = array(
    "color" => "blue",
    "size"  => "medium",
    "shape" => "sphere"
);

extract($var_array, EXTR_PREFIX_SAME, "wddx");

echo "$color, $size, $shape, $wddx_size\n";

?>

    
```php

El ejemplo anterior mostrará:

    blue, large, sphere, medium

        

La variable `$size` no fue sobrescrita porque especificamos `EXTR_PREFIX_SAME`, lo que resultó en la creación de `$wddx_size`. Si se hubiera especificado `EXTR_SKIP`, entonces `$wddx_size` ni siquiera se habría creado. `EXTR_OVERWRITE` habría hecho que `$size` tuviera el valor "medium", y `EXTR_PREFIX_ALL` habría resultado en nuevas variables llamadas `$wddx_color`, `$wddx_size`, y `$wddx_shape`.

## Notas

> [!WARNING]
> No utilice `extract` con datos no confiables, como entrada de usuario (ej. `$_GET`, `$_FILES`, etc.). Si lo hace, asegúrese de usar uno de los valores de `flags` que no sobrescriban, como `EXTR_SKIP` y tenga en cuenta que debe extraer en el mismo orden que está definido en [variables_order](#ini.variables-order) dentro del [`php.ini`](#ini).

## Véase también

`compact`, `list`
