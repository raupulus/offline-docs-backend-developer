---
title: Ds\Set::filter
description: Crear un nuevo conjunto utilizando un callable para determinar qué valores
  incluir
source_url: https://www.php.net/manual/es/ds-set.filter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/filter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15850
---

Ds\Set::filter

Crear un nuevo conjunto utilizando un

callable

para determinar qué valores incluir

## Descripción

```php
public Ds\Set::filter([callable $callback]): Ds\Set
```php

Crear un nuevo conjunto utilizando un `callable` para determinar qué valores incluir.

## Parámetros

`callback`  
```php
callback(mixed $value): bool
```

Un `callable` opcional que devuelve `true` si el par debe ser incluido, `false` en caso contrario.

Si no se proporciona ninguna función de retrollamada, solo se incluirán los valores que son `true` (ver [conversión en booléen](#language.types.boolean.casting)).

## Valores devueltos

Un nuevo conjunto que contiene todos los pares para los cuales el `callback` ha devuelto `true`, o todos los valores que se convierten en `true` si no se ha proporcionado un `callback`.

## Ejemplos

Ejemplo de `Ds\Set::filter` utilizando una función de retrollamada

```php
<?php
$set = new \Ds\Set([1, 2, 3, 4, 5]);

var_dump($set->filter(function($value) {
    return $value % 2 == 0;
}));
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#3 (2) {
      [0]=>
      int(2)
      [1]=>
      int(4)
    }

Ejemplo de `Ds\Set::filter` sin función de retrollamada

```php
<?php
$set = new \Ds\Set([0, 1, 'a', true, false]);

var_dump($set->filter());
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#2 (3) {
      [0]=>
      int(1)
      [1]=>
      string(1) "a"
      [2]=>
      bool(true)
    }
