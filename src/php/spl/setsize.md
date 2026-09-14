---
title: SplFixedArray::setSize
description: Cambia el tamaño de un array de tamaño fijo
source_url: https://www.php.net/manual/es/splfixedarray.setsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/setsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: eb39dbdba
order: 84800
---

SplFixedArray::setSize

Cambia el tamaño de un array de tamaño fijo

## Descripción

```php
public SplFixedArray::setSize(int $size): true
```php

Cambia el tamaño de un array a un tamaño fijo `size`. Si `size` es inferior al tamaño actual del array, todos los valores después del nuevo tamaño serán ignorados. Si `size` es mayor que el tamaño actual del array, el array será completado con valores de tipo `null`.

## Parámetros

`size`  
El nuevo tamaño del array. Debe ser un valor entre `0` y `PHP_INT_MAX`.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Levanta una excepción ValueError cuando `size` es inferior a cero.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | SplFixedArray::setSize ahora tiene un retorno provisional de `true`. |

## Ejemplos

Ejemplo con `SplFixedArray::setSize`

```
<?php
   $array = new SplFixedArray(5);
   echo $array->getSize()."\n";
   $array->setSize(10);
   echo $array->getSize()."\n";
?>

    
```php

El ejemplo anterior mostrará:

    5
    10
