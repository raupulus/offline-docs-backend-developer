---
title: Ds\Queue::push
description: Añade un elemento a la cola
source_url: https://www.php.net/manual/es/ds-queue.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/queue/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_revision: 9e0f03ac3
order: 15470
---

Ds\Queue::push

Añade un elemento a la cola

## Descripción

```php
public Ds\Queue::push(mixed ...$values): void
```php

Añade `valores` en la cola.

## Parámetros

`values`  
Los valores a añadir a la cola.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Queue::push`

```
<?php
$queue = new \Ds\Queue();

$queue->push("a");
$queue->push("b");
$queue->push("c", "d");
$queue->push(...["e", "f"]);

print_r($queue);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Queue Object
    (
        [0] => a
        [1] => b
        [2] => c
        [3] => d
        [4] => e
        [5] => f
    )
