---
title: Ds\Sequence::filter
description: Crear una nueva secuencia utilizando un callable para determinar qué
  valores incluir
source_url: https://www.php.net/manual/es/ds-sequence.filter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/filter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15530
---

Ds\Sequence::filter

Crear una nueva secuencia utilizando un

callable

para determinar qué valores incluir

## Descripción

```php
abstract public Ds\Sequence::filter([callable $callback]): Ds\Sequence
```php

Crear una nueva secuencia utilizando un `callable` para determinar qué valores incluir.

## Parámetros

`callback`  
```php
callback(mixed $value): bool
```

Un `callable` opcional que devuelve `true` si el par debe ser incluido, `false` en caso contrario.

Si no se proporciona ninguna función de retrollamada, solo se incluirán los valores que son `true` (ver [conversión en booléen](#language.types.boolean.casting)).

## Valores devueltos

Una nueva secuencia que contiene todos los pares para los cuales el `callback` ha devuelto `true`, o todos los valores que se convierten en `true` si no se ha proporcionado un `callback`.

## Ejemplos

Ejemplo de `Ds\Sequence::filter` utilizando una función de retrollamada

```php
<?php
$sequence = new \Ds\Vector([1, 2, 3, 4, 5]);

var_dump($sequence->filter(function($value) {
    return $value % 2 == 0;
}));
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Ds\Vector)#3 (2) {
      [0]=>
      int(2)
      [1]=>
      int(4)
    }

Ejemplo de `Ds\Sequence::filter` sin función de retrollamada

```php
<?php
$sequence = new \Ds\Vector([0, 1, 'a', true, false]);

var_dump($sequence->filter());
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Ds\Vector)#2 (3) {
      [0]=>
      int(1)
      [1]=>
      string(1) "a"
      [2]=>
      bool(true)
    }
