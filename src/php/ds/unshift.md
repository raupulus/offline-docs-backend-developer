---
title: Ds\Deque::unshift
description: Añade valores al inicio del deque
source_url: https://www.php.net/manual/es/ds-deque.unshift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/unshift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14780
---

Ds\Deque::unshift

Añade valores al inicio del deque

## Descripción

```php
public Ds\Deque::unshift([mixed $values]): void
```php

Añade los valores al inicio del deque, desplazando todos los valores actuales hacia adelante para hacer espacio para los nuevos valores.

## Parámetros

`values`  
Los valores a añadir al inicio del deque.

> [!NOTE]
> Los valores serán añadidos en el mismo orden en que son pasados.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Deque::unshift`

```
<?php
$deque = new \Ds\Deque([1, 2, 3]);

$deque->unshift("a");
$deque->unshift("b", "c");

print_r($deque);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Deque Object
    (
        [0] => b
        [1] => c
        [2] => a
        [3] => 1
        [4] => 2
        [5] => 3
    )
