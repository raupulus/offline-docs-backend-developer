---
title: QuickHashIntStringHash::__construct
description: Crear un nuevo objeto QuickHashIntStringHash
source_url: https://www.php.net/manual/es/quickhashintstringhash.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintstringhash/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67250
---

QuickHashIntStringHash::\_\_construct

Crear un nuevo objeto QuickHashIntStringHash

## Descripción

```php
public QuickHashIntStringHash::__construct(int $size, [int $options])
```php

Este constructor crea un nuevo objeto `QuickHashIntStringHash`. El tamaño es el número de listas de cubos a crear. Cuantas más listas haya, menos colisiones habrá. Las opciones también son compatibles.

## Parámetros

`size`  
La cantidad de listas de cubos a configurar. El número que se pasa será automáticamente redondeado a la siguiente potencia de dos. También se limita automáticamente de `64` a `4194304`.

`options`  
Las opciones que se pueden pasar son: `QuickHashIntStringHash::CHECK_FOR_DUPES`, que asegura que ninguna entrada duplicada se añada al hash; `QuickHashIntStringHash::DO_NOT_USE_ZEND_ALLOC` para no utilizar el gestor de memoria interno de PHP así como uno de los valores `QuickHashIntStringHash::HASHER_NO_HASH`, `QuickHashIntStringHash::HASHER_JENKINS1` o `QuickHashIntStringHash::HASHER_JENKINS2`. Estas tres últimas configuran el algoritmo de hash a utilizar. Todas las opciones pueden ser combinadas utilizando máscaras de bits.

## Valores devueltos

Devuelve un nuevo objeto `QuickHashIntStringHash`.

## Ejemplos

Ejemplo de `QuickHashIntStringHash::__construct`

```
<?php
var_dump( new QuickHashIntStringHash( 1024 ) );
var_dump( new QuickHashIntStringHash( 1024, QuickHashIntStringHash::CHECK_FOR_DUPES ) );
var_dump(
    new QuickHashIntStringHash(
        1024,
        QuickHashIntStringHash::DO_NOT_USE_ZEND_ALLOC | QuickHashIntStringHash::HASHER_JENKINS2
    )
);
?>

   
```php
