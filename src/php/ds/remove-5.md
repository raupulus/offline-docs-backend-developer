---
title: Ds\Vector::remove
description: Elimina y devuelve un valor por índice
source_url: https://www.php.net/manual/es/ds-vector.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16400
---

Ds\Vector::remove

Elimina y devuelve un valor por índice

## Descripción

```php
public Ds\Vector::remove(int $index): mixed
```php

Elimina y devuelve un valor por índice.

## Parámetros

`index`  
El índice del valor a eliminar.

## Valores devueltos

El valor que ha sido eliminado.

## Errores/Excepciones

`OutOfRangeException` si el índice no es válido.

## Ejemplos

Ejemplo de `Ds\Vector::remove`

```
<?php
$vector = new \Ds\Vector(["a", "b", "c"]);

var_dump($vector->remove(1));
var_dump($vector->remove(0));
var_dump($vector->remove(0));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "b"
    string(1) "a"
    string(1) "c"
