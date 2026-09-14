---
title: natsort
description: Ordena un array con el algoritmo de "orden natural"
source_url: https://www.php.net/manual/es/function.natsort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/natsort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: f78180344
order: 5890
---

natsort

Ordena un array con el algoritmo de "orden natural"

## Descripción

```php
natsort(array $array): true
```php

`natsort` implementa un algoritmo de ordenación que trata las cadenas alfanuméricas del array `array` como lo haría un ser humano, conservando la relación clave/valor. Esto se conoce como "orden natural". Un ejemplo de la diferencia de tratamiento entre tal algoritmo y un algoritmo de ordenación de cadenas (como cuando se utiliza `sort`) se ilustra a continuación.

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

Ejemplo de uso básico con `natsort`

```
<?php
$array1 = $array2 = array("img12.png", "img10.png", "img2.png", "img1.png");

asort($array1);
echo "Ordenación estándar\n";
print_r($array1);

natsort($array2);
echo "\nOrdenación en orden natural\n";
print_r($array2);
?>

    
```php

El ejemplo anterior mostrará:

    Ordenación estándar
    Array
    (
        [3] => img1.png
        [1] => img10.png
        [0] => img12.png
        [2] => img2.png
    )

    Ordenación en orden natural
    Array
    (
        [3] => img1.png
        [2] => img2.png
        [1] => img10.png
        [0] => img12.png
    )

        

Para más detalles, visite el sitio de Martin Pool sobre [la comparación de cadenas en orden natural](https://github.com/sourcefrog/natsort).

Ejemplos que muestran las trampas de `natsort`

```
<?php
echo "Números negativos\n";
$negative = array('-5','3','-2','0','-1000','9','1');
print_r($negative);
natsort($negative);
print_r($negative);

echo "Alineación con ceros\n";
$zeros = array('09', '8', '10', '009', '011', '0');
print_r($zeros);
natsort($zeros);
print_r($zeros);
?>

    
```php

El ejemplo anterior mostrará:

    Números negativos
    Array
    (
        [0] => -5
        [1] => 3
        [2] => -2
        [3] => 0
        [4] => -1000
        [5] => 9
        [6] => 1
    )
    Array
    (
        [2] => -2
        [0] => -5
        [4] => -1000
        [3] => 0
        [6] => 1
        [1] => 3
        [5] => 9
    )

    Alineación con ceros
    Array
    (
        [0] => 09
        [1] => 8
        [2] => 10
        [3] => 009
        [4] => 011
        [5] => 0
    )
    Array
    (
        [5] => 0
        [1] => 8
        [3] => 009
        [0] => 09
        [2] => 10
        [4] => 011
    )

## Véase también

`natcasesort`, Las funciones de [ordenación de arrays](#array.sorting), `strnatcmp`, `strnatcasecmp`
