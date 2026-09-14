---
title: Ds\Deque::set
description: Actualiza un valor en un índice dado
source_url: https://www.php.net/manual/es/ds-deque.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14710
---

Ds\Deque::set

Actualiza un valor en un índice dado

## Descripción

```php
public Ds\Deque::set(int $index, mixed $value): void
```php

Actualiza un valor en un índice dado.

## Parámetros

`index`  
El índice del valor a actualizar.

`value`  
El nuevo valor.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

`OutOfRangeException` si el índice no es válido.

## Ejemplos

Ejemplo de `Ds\Deque::set`

```
<?php
$deque = new \Ds\Deque(["a", "b", "c"]);

$deque->set(1, "_");
print_r($deque);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Deque Object
    (
        [0] => a
        [1] => _
        [2] => c
    )

Ejemplo de `Ds\Deque::set` utilizando la sintaxis de array

```
<?php
$deque = new \Ds\Deque(["a", "b", "c"]);

$deque[1] = "_";
print_r($deque);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Deque Object
    (
        [0] => a
        [1] => _
        [2] => c
    )
