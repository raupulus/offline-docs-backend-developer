---
title: natcasesort
description: Ordena un array con el algoritmo de "orden natural" insensible a mayúsculas
  y minúsculas
source_url: https://www.php.net/manual/es/function.natcasesort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/natcasesort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: f78180344
order: 5880
---

natcasesort

Ordena un array con el algoritmo de "orden natural" insensible a mayúsculas y minúsculas

## Descripción

```php
natcasesort(array $array): true
```php

`natcasesort` es la versión insensible a mayúsculas y minúsculas de `natsort`.

Esta función implementa un algoritmo de ordenación que trata las cadenas alfanuméricas del array `array` como lo haría un ser humano, manteniendo la relación clave/valor. Esto se conoce como "orden natural".

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

> [!NOTE]
> Reinicia el puntero interno del array al primer elemento.

## Parámetros

`array`  
El array de entrada.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `natcasesort`

```
<?php
$array1 = $array2 = array('IMG0.png', 'img12.png', 'img10.png', 'img2.png', 'img1.png', 'IMG3.png');

sort($array1);
echo "Ordenación estándar\n";
print_r($array1);

natcasesort($array2);
echo "\nOrdenación en orden natural (insensible a mayúsculas y minúsculas)\n";
print_r($array2);
?>

    
```php

El ejemplo anterior mostrará:

    Ordenación estándar
    Array
    (
        [0] => IMG0.png
        [1] => IMG3.png
        [2] => img1.png
        [3] => img10.png
        [4] => img12.png
        [5] => img2.png
    )

    Ordenación en orden natural (insensible a mayúsculas y minúsculas)
    Array
    (
        [0] => IMG0.png
        [4] => img1.png
        [3] => img2.png
        [5] => IMG3.png
        [2] => img10.png
        [1] => img12.png
    )

        

Para más detalles, visite el sitio de Martin Pool sobre [la comparación de cadenas en orden natural](https://github.com/sourcefrog/natsort).

## Véase también

`natsort`, Las funciones de [ordenación de arrays](#array.sorting), `strnatcmp`, `strnatcasecmp`
