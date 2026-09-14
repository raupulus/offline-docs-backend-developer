---
title: QuickHashStringIntHash::__construct
description: Crear un nuevo objeto QuickHashStringIntHash
source_url: https://www.php.net/manual/es/quickhashstringinthash.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67380
---

QuickHashStringIntHash::\_\_construct

Crear un nuevo objeto QuickHashStringIntHash

## Descripción

```php
public QuickHashStringIntHash::__construct(int $size, [int $options])
```php

Este constructor crea un nuevo objeto `QuickHashStringIntHash`. El tamaño es el número de listas de cubos a crear. Cuantas más listas haya, menos colisiones habrá. Las opciones también son soportadas.

## Parámetros

`size`  
La cantidad de listas de cubos a configurar. El número que se pasa será automáticamente redondeado a la siguiente potencia de dos. También se limita automáticamente de `64` a `4194304`.

`options`  
Las opciones que se pueden pasar son: `QuickHashStringIntHash::CHECK_FOR_DUPES`, que verifica que ninguna entrada duplicada se añade al hash y `QuickHashStringIntHash::DO_NOT_USE_ZEND_ALLOC` para no utilizar el gestor de memoria interno de PHP.

## Valores devueltos

Devuelve un nuevo objeto `QuickHashStringIntHash`.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::__construct`

```
<?php
var_dump( new QuickHashStringIntHash( 1024 ) );
var_dump( new QuickHashStringIntHash( 1024, QuickHashStringIntHash::CHECK_FOR_DUPES ) );
?>

   
```php
