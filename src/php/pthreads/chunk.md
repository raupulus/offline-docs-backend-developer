---
title: Threaded::chunk
description: Manipulación
source_url: https://www.php.net/manual/es/threaded.chunk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/chunk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66780
---

Threaded::chunk

Manipulación

## Descripción

```php
public Threaded::chunk(int $size, bool $preserve): array
```php

Recorre una parte de la tabla de propiedades de los objetos preservando, opcionalmente, las claves.

## Parámetros

`size`  
El número de elementos a recorrer

`preserve`  
Preserva las claves de los miembros; por omisión, vale `false`

## Valores devueltos

Un array de elementos desde la tabla de propiedades de los objetos.

## Ejemplos

Recorrido de una parte de la tabla de propiedades

```
<?php
$safe = new Threaded();

while (count($safe) < 10) {
    $safe[] = count($safe);
}

var_dump($safe->chunk(5));
?>

   
```php

El ejemplo anterior mostrará:

    array(5) {
      [0]=>
      int(0)
      [1]=>
      int(1)
      [2]=>
      int(2)
      [3]=>
      int(3)
      [4]=>
      int(4)
    }
