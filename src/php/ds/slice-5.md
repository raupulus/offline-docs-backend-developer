---
title: Ds\Vector::slice
description: Devuelve un sub-vector de un rango dado
source_url: https://www.php.net/manual/es/ds-vector.slice.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/slice.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16460
---

Ds\Vector::slice

Devuelve un sub-vector de un rango dado

## Descripción

```php
public Ds\Vector::slice(int $index, [int $length]): Ds\Vector
```php

Crea un sub-vector de un rango dado.

## Parámetros

`index`  
El índice en el que comienza el sub-vector.

Si es positivo, el sub-vector comenzará en este índice en el vector. Si es negativo, el sub-vector comenzará a esta distancia del final.

`length`  
Si se proporciona una longitud y es positiva, el sub-vector resultante tendrá hasta ese número de valores. Si la longitud provoca un desbordamiento, solo los valores hasta el final del vector serán incluidos. Si se proporciona una longitud y es negativa, el sub-vector se detendrá a ese número de valores del final. Si no se proporciona una longitud, el sub-vector contendrá todos los valores entre el índice y el final del vector.

## Valores devueltos

Un sub-vector del rango dado.

## Ejemplos

Ejemplo de `Ds\Vector::slice`

```
<?php
$vector = new \Ds\Vector(["a", "b", "c", "d", "e"]);

// Recorte a partir de 2
print_r($vector->slice(2));

// Recorte a partir de 1, para una longitud de 3
print_r($vector->slice(1, 3));

// Recorte a partir de 1 en adelante
print_r($vector->slice(1));

// Recorte a partir de 2 hacia atrás
print_r($vector->slice(-2));

// Recorte de 1 a 1 del final
print_r($vector->slice(1, -1));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => c
        [1] => d
        [2] => e
    )
    Ds\Vector Object
    (
        [0] => b
        [1] => c
        [2] => d
    )
    Ds\Vector Object
    (
        [0] => b
        [1] => c
        [2] => d
        [3] => e
    )
    Ds\Vector Object
    (
        [0] => d
        [1] => e
    )
    Ds\Vector Object
    (
        [0] => b
        [1] => c
        [2] => d
    )
