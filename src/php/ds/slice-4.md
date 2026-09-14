---
title: Ds\Set::slice
description: Devuelve un subconjunto de un rango dado
source_url: https://www.php.net/manual/es/ds-set.slice.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/slice.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15990
---

Ds\Set::slice

Devuelve un subconjunto de un rango dado

## Descripción

```php
public Ds\Set::slice(int $index, [int $length]): Ds\Set
```php

Crea un subconjunto de un rango dado.

## Parámetros

`index`  
El índice en el que comienza la subsecuencia.

Si es positivo, la subsecuencia comenzará en este índice en la secuencia. Si es negativo, la subsecuencia comenzará a esta distancia del final.

`length`  
Si se proporciona una longitud y es positiva, la subsecuencia resultante tendrá hasta tantos valores. Si la longitud provoca un desbordamiento, solo los valores hasta el final del conjunto serán incluidos. Si se proporciona una longitud y es negativa, la subsecuencia se detendrá a tantos valores del final. Si no se proporciona una longitud, la subsecuencia contendrá todos los valores entre el índice y el final de la secuencia.

## Valores devueltos

Un subconjunto del conjunto dado.

## Ejemplos

Ejemplo de `Ds\Set::slice`

```
<?php
$set = new \Ds\Set(["a", "b", "c", "d", "e"]);

// Corte a partir de 2
print_r($set->slice(2));

// Corte a partir de 1, para una longitud de 3
print_r($set->slice(1, 3));

// Corte a partir de 1 en adelante
print_r($set->slice(1));

// Corte a partir de 2 hacia atrás
print_r($set->slice(-2));

// Corte de 1 a 1 del final
print_r($set->slice(1, -1));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Set Object
    (
        [0] => c
        [1] => d
        [2] => e
    )
    Ds\Set Object
    (
        [0] => b
        [1] => c
        [2] => d
    )
    Ds\Set Object
    (
        [0] => b
        [1] => c
        [2] => d
        [3] => e
    )
    Ds\Set Object
    (
        [0] => d
        [1] => e
    )
    Ds\Set Object
    (
        [0] => b
        [1] => c
        [2] => d
    )
