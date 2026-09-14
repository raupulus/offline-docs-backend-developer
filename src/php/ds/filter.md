---
title: Ds\Deque::filter
description: Crear un nuevo deque utilizando un callable para determinar qué valores
  incluir
source_url: https://www.php.net/manual/es/ds-deque.filter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/filter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14530
---

Ds\Deque::filter

Crear un nuevo deque utilizando un

callable

para determinar qué valores incluir

## Descripción

```php
public Ds\Deque::filter([callable $callback]): Ds\Deque
```php

Crear un nuevo deque utilizando un `callable` para determinar qué valores incluir.

## Parámetros

`callback`  
```php
callback(mixed $value): bool
```

Un `callable` opcional que devuelve `true` si el valor debe ser incluido, `false` en caso contrario.

Si no se proporciona ninguna función de retrollamada, solo se incluirán los valores que sean `true` (ver [conversión en booléen](#language.types.boolean.casting)).

## Valores devueltos

Un nuevo deque que contiene todos los valores para los cuales el `callback` ha devuelto `true`, o todos los valores que se convierten en `true` si no se ha proporcionado un `callback`.

## Ejemplos

Ejemplo de `Ds\Deque::filter` con una función de retrollamada

```php
<?php
$deque = new \Ds\Deque([1, 2, 3, 4, 5]);

var_dump($deque->filter(function($value) {
    return $value % 2 == 0;
}));
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Ds\Deque)#3 (2) {
      [0]=>
      int(2)
      [1]=>
      int(4)
    }

Ejemplo de `Ds\Deque::filter` sin una función de retrollamada

```php
<?php
$deque = new \Ds\Deque([0, 1, 'a', true, false]);

var_dump($deque->filter());
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Ds\Deque)#2 (3) {
      [0]=>
      int(1)
      [1]=>
      string(1) "a"
      [2]=>
      bool(true)
    }
