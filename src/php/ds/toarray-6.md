---
title: Ds\Queue::toArray
description: Convierte la cola en un array
source_url: https://www.php.net/manual/es/ds-queue.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/queue/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_revision: dd07341fa
order: 15480
---

Ds\Queue::toArray

Convierte la cola en un

array

## Descripción

```php
public Ds\Queue::toArray(): array
```php

Convierte la cola en un `array`.

> [!NOTE]
> Un casting a un `array` no se soporta todavía.

> [!NOTE]
> Este método no es destructivo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` conteniendo todos los elementos en el mismo orden que la cola.

## Ejemplos

Ejemplo de `Ds\Queue::toArray`

```
<?php
$queue = new \Ds\Queue([1, 2, 3]);

var_dump($queue->toArray());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
