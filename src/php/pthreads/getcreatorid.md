---
title: Thread::getCreatorId
description: Identificación
source_url: https://www.php.net/manual/es/thread.getcreatorid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/thread/getcreatorid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66690
---

Thread::getCreatorId

Identificación

## Descripción

```php
public Thread::getCreatorId(): int
```php

Devuelve la identidad del Thread que ha creado el Thread referenciado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una identidad numérica.

## Ejemplos

Devuelve la identidad del Thread o del proceso que ha creado el Thread referenciado

```
<?php
class My extends Thread {
    public function run() {
        printf("%s ha sido creado por el Thread #%lu\n", __CLASS__, $this->getCreatorId());
    }
}
$my = new My();
$my->start();
?>

   
```php

El ejemplo anterior mostrará:

    My ha sido creado por el Thread #123456778899
