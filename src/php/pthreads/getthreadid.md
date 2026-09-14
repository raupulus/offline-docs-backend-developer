---
title: Thread::getThreadId
description: Identificación
source_url: https://www.php.net/manual/es/thread.getthreadid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/thread/getthreadid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66720
---

Thread::getThreadId

Identificación

## Descripción

```php
public Thread::getThreadId(): int
```php

Se devuelve la identidad del Thread referenciado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una identidad numérica.

## Ejemplos

Se devuelve la identidad del Thread referenciado

```
<?php
class My extends Thread {
    public function run() {
        printf("%s es el Thread #%lu\n", __CLASS__, $this->getThreadId());
    }
}
$my = new My();
$my->start();
?>

   
```php

El ejemplo anterior mostrará:

    My es el Thread #123456778899
