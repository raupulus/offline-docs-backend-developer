---
title: Ds\Queue::__construct
description: Crear una nueva instancia
source_url: https://www.php.net/manual/es/ds-queue.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/queue/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15400
---

Ds\Queue::\_\_construct

Crear una nueva instancia

## Descripción

```php
public Ds\Queue::__construct([mixed $values])
```php

Crear una nueva instancia utilizando un objeto `traversable` o un `array` para los `values` iniciales.

## Parámetros

`values`  
Un objeto traversable o un `array` para los valores iniciales.

## Ejemplos

Ejemplo de `Ds\Queue::__construct`

```
<?php
$queue = new \Ds\Queue();
var_dump($queue);

$queue = new \Ds\Queue([1, 2, 3]);
var_dump($queue);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Queue)#2 (0) {
    }
    object(Ds\Queue)#2 (3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
