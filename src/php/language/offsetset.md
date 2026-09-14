---
title: ArrayAccess::offsetSet
description: Asignar un valor al índice esepecificado
source_url: https://www.php.net/manual/es/arrayaccess.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/arrayaccess/offsetset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: ed312486f
order: 2840
---

ArrayAccess::offsetSet

Asignar un valor al índice esepecificado

## Descripción

```php
public ArrayAccess::offsetSet(mixed $offset, mixed $value): void
```php

Asigna un valor a un offset determinado.

## Parámetros

`offset`  
El offset al que se asigna el valor.

`value`  
El valor a asignar.

## Valores devueltos

No se retorna ningún valor.

## Notas

> [!NOTE]
> El parámetro `offset` será inicializado a `null` si otro valor no está disponible, como en el siguiente ejemplo.
>
> <div class="informalexample">
>
> ```
> <?php
> $arrayaccess[] = "primer valor";
> $arrayaccess[] = "segundo valor";
> print_r($arrayaccess);
> ?>
>
>      
> ```
>
> El ejemplo anterior mostrará:
>
>     Array
>     (
>         [0] => primer valor
>         [1] => segundo valor
>     )
>
>          
>
> </div>

> [!NOTE]
> Esta función no es invocada al realizar asignaciones por referencias y por tanto en los cambios de dimensiones en arrays sobrecargados con `ArrayAccess` (indirecto en el sentido de que no se hace cambiando la dimensión directamente, sino cambiando una sub-dimensión o sub-propiedad o asignando la dimensión del array por referencia en otra variable). En su lugar, se llama a `ArrayAccess::offsetGet`. La operación tendrá éxito si devuelve el valor por referencia.
