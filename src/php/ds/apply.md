---
title: Ds\Deque::apply
description: Actualiza todos los valores aplicando una retrollamada a cada valor
source_url: https://www.php.net/manual/es/ds-deque.apply.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/apply.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14460
---

Ds\Deque::apply

Actualiza todos los valores aplicando una retrollamada a cada valor

## Descripción

```php
public Ds\Deque::apply(callable $callback): void
```php

Actualiza todos los valores aplicando un `callback` a cada valor en la deque.

## Parámetros

`callback`  
```php
callback(mixed $value): mixed
```

Un `callable` a aplicar a cada valor en la deque.

La retrollamada debe aceptar un valor y devolver lo que el valor debe ser reemplazado por.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Deque::apply`

```php
<?php
$deque = new \Ds\Deque([1, 2, 3]);
$deque->apply(function($value) { return $value * 2; });

print_r($deque);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Deque Object
    (
        [0] => 2
        [1] => 4
        [2] => 6
    )
