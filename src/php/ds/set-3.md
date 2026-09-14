---
title: Ds\Vector::set
description: Cambia un valor en un índice dado
source_url: https://www.php.net/manual/es/ds-vector.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16440
---

Ds\Vector::set

Cambia un valor en un índice dado

## Descripción

```php
public Ds\Vector::set(int $index, mixed $value): void
```php

Cambia un valor en un índice dado.

## Parámetros

`index`  
El índice del valor a actualizar.

`value`  
El nuevo valor.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

`OutOfRangeException` si el índice no es válido.

## Ejemplos

Ejemplo de `Ds\Vector::set`

```
<?php
$vector = new \Ds\Vector(["a", "b", "c"]);

$vector->set(1, "_");
print_r($vector);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => a
        [1] => _
        [2] => c
    )

Ejemplo de `Ds\Vector::set` utilizando la sintaxis de array

```
<?php
$vector = new \Ds\Vector(["a", "b", "c"]);

$vector[1] = "_";
print_r($vector);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => a
        [1] => _
        [2] => c
    )
