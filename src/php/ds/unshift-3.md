---
title: Ds\Vector::unshift
description: Añade valores al inicio del vector
source_url: https://www.php.net/manual/es/ds-vector.unshift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/unshift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16510
---

Ds\Vector::unshift

Añade valores al inicio del vector

## Descripción

```php
public Ds\Vector::unshift([mixed $values]): void
```php

Añade valores al inicio del vector, desplazando todos los valores actuales hacia adelante para hacer espacio para los nuevos valores.

## Parámetros

`values`  
Los valores a añadir al inicio del vector.

> [!NOTE]
> Múltiples valores pueden ser añadidos en el mismo orden en que son pasados.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Vector::unshift`

```
<?php
$vector = new \Ds\Vector([1, 2, 3]);

$vector->unshift("a");
$vector->unshift("b", "c");

print_r($vector);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => b
        [1] => c
        [2] => a
        [3] => 1
        [4] => 2
        [5] => 3
    )
