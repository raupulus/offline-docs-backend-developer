---
title: QuickHashIntSet::__construct
description: Crear un nuevo objeto QuickHashIntSet
source_url: https://www.php.net/manual/es/quickhashintset.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintset/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67150
---

QuickHashIntSet::\_\_construct

Crear un nuevo objeto QuickHashIntSet

## Descripción

```php
public QuickHashIntSet::__construct(int $size, [int $options])
```php

Este constructor crea un nuevo `QuickHashIntSet`. El tamaño es el número de listas de cubos a crear. Cuantas más listas haya, menos colisiones habrá. Las opciones también son soportadas.

## Parámetros

`size`  
La cantidad de listas de cubos a configurar. El número que se pasa será automáticamente redondeado a la siguiente potencia de dos. También se limita automáticamente de `4` a `4194304`.

`options`  
Las opciones que se pueden pasar son: `QuickHashIntSet::CHECK_FOR_DUPES`, que asegura que ninguna entrada duplicada sea añadida al conjunto; `QuickHashIntSet::DO_NOT_USE_ZEND_ALLOC` para no utilizar el gestor de memoria interno de PHP así como una de las `QuickHashIntSet::HASHER_NO_HASH`, `QuickHashIntSet::HASHER_JENKINS1` o `QuickHashIntSet::HASHER_JENKINS2`. Estas tres últimas configuran el algoritmo de hash a utilizar. Todas las opciones pueden ser combinadas utilizando máscaras de bits.

## Valores devueltos

Devuelve un nuevo objeto `QuickHashIntSet`.

## Ejemplos

Ejemplo de `QuickHashIntSet::__construct`

```
<?php
var_dump( new QuickHashIntSet( 1024 ) );
var_dump( new QuickHashIntSet( 1024, QuickHashIntSet::CHECK_FOR_DUPES ) );
var_dump(
    new QuickHashIntSet(
        1024,
        QuickHashIntSet::DO_NOT_USE_ZEND_ALLOC | QuickHashIntSet::HASHER_JENKINS2
    )
);
?>

   
```php
