---
title: QuickHashIntHash::__construct
description: Crear un nuevo objeto QuickHashIntHash
source_url: https://www.php.net/manual/es/quickhashinthash.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67020
---

QuickHashIntHash::\_\_construct

Crear un nuevo objeto QuickHashIntHash

## Descripción

```php
public QuickHashIntHash::__construct(int $size, [int $options])
```php

Este constructor crea un nuevo objeto `QuickHashIntHash`. El tamaño es el número de listas de cubos a crear. Cuantas más listas haya, menos colisiones se tendrán. Las opciones también son soportadas.

## Parámetros

`size`  
La cantidad de listas de cubos a configurar. El número que se pase será automáticamente redondeado a la siguiente potencia de dos. También se limita automáticamente de `64` a `4194304`.

`options`  
Las opciones que se pueden pasar son: `QuickHashIntHash::CHECK_FOR_DUPES`, que asegura que ninguna entrada duplicada sea añadida al hash; `QuickHashIntHash::DO_NOT_USE_ZEND_ALLOC` para no utilizar el gestor de memoria interno de PHP así como una de las `QuickHashIntHash::HASHER_NO_HASH`, `QuickHashIntHash::HASHER_JENKINS1` o `QuickHashIntHash::HASHER_JENKINS2`. Estas tres últimas configuran el algoritmo de hash a utilizar. Todas las opciones pueden ser combinadas utilizando máscaras de bits.

## Valores devueltos

Devuelve un nuevo objeto `QuickHashIntHash`.

## Ejemplos

Ejemplo de `QuickHashIntHash::__construct`

```
<?php
var_dump( new QuickHashIntHash( 1024 ) );
var_dump( new QuickHashIntHash( 1024, QuickHashIntHash::CHECK_FOR_DUPES ) );
var_dump(
    new QuickHashIntHash(
        1024,
        QuickHashIntHash::DO_NOT_USE_ZEND_ALLOC | QuickHashIntHash::HASHER_JENKINS2
    )
);
?>

   
```php
