---
title: ArrayAccess::offsetGet
description: Offset para recuperar
source_url: https://www.php.net/manual/es/arrayaccess.offsetget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/arrayaccess/offsetget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: ed312486f
order: 2830
---

ArrayAccess::offsetGet

Offset para recuperar

## Descripción

```php
public ArrayAccess::offsetGet(mixed $offset): mixed
```php

Devuelve el valor correspondiente a desplazamiento especificado.

Este método se ejecuta para comprobar si el desplazamiento es `empty`.

## Parámetros

`offset`  
El desplazamiento va a recuperar.

## Valores devueltos

Puede devolver todos los tipos de valor.

## Notas

> [!NOTE]
> Es posible para las implementaciones de este método para devolver por referencia. Esto hace que las modificaciones indirectas a las dimensiones de los arreglos sobrecargados de objetos `ArrayAccess` posibles.
>
> Una modificación directa es aquella que reemplaza completamente el valor de la dimensión de el arreglo, como en `$obj[6] = 7`. Una modificación indirecta, por el contrario, sólo una parte los cambios de la dimensión, o los intentos de asignar la dimensión en función de otra variable, como en `$obj[6][7] = 7` o `$var =& $obj[6]`. Con incrementos `++` y disminye con `--` también se aplican de una manera que requiere la modificación indirecta.
>
> Si bien la modificación directa desencadena una llamada a `ArrayAccess::offsetSet`, modificación indirecta provoca una llamada a `ArrayAccess::offsetGet`. En ese caso, la aplicación de `ArrayAccess::offsetGet` debe ser capaz de volver por la referencia, de lo contrario un `E_NOTICE` mensaje es elevado..

## Véase también

ArrayAccess::offsetExists
