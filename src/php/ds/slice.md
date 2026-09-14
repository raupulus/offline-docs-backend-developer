---
title: Ds\Deque::slice
description: Devuelve un sub-deque de un rango dado
source_url: https://www.php.net/manual/es/ds-deque.slice.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/slice.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14730
---

Ds\Deque::slice

Devuelve un sub-deque de un rango dado

## Descripción

```php
public Ds\Deque::slice(int $index, [int $length]): Ds\Deque
```php

Crear un sub-deque de un rango dado.

## Parámetros

`index`  
El índice en el que comienza el sub-deque.

Si es positivo, el sub-deque comenzará en este índice en el deque. Si es negativo, el sub-deque comenzará a esta distancia del final.

`length`  
Si se proporciona una longitud y es positiva, el sub-deque resultante tendrá hasta ese número de valores. Si la longitud provoca un desbordamiento, solo se incluirán los valores hasta el final del deque. Si se proporciona una longitud y es negativa, el sub-deque se detendrá a esa cantidad de valores del final. Si no se proporciona una longitud, el sub-deque contendrá todos los valores entre el índice y el final del deque.

## Valores devueltos

Un sub-deque del rango dado.

## Ejemplos

Ejemplo de `Ds\Deque::slice`

```
<?php
$deque = new \Ds\Deque(["a", "b", "c", "d", "e"]);

// Recorte a partir de 2
print_r($deque->slice(2));

// Recorte a partir de 1, para una longitud de 3
print_r($deque->slice(1, 3));

// Recorte a partir de 1 en adelante
print_r($deque->slice(1));

// Recorte a partir de 2 hacia atrás
print_r($deque->slice(-2));

// Recorte de 1 a 1 del final
print_r($deque->slice(1, -1));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Deque Object
    (
        [0] => c
        [1] => d
        [2] => e
    )
    Ds\Deque Object
    (
        [0] => b
        [1] => c
        [2] => d
    )
    Ds\Deque Object
    (
        [0] => b
        [1] => c
        [2] => d
        [3] => e
    )
    Ds\Deque Object
    (
        [0] => d
        [1] => e
    )
    Ds\Deque Object
    (
        [0] => b
        [1] => c
        [2] => d
    )
