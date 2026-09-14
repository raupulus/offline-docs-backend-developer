---
title: Threaded::isTerminated
description: Detección de estado
source_url: https://www.php.net/manual/es/threaded.isterminated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/isterminated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66820
---

Threaded::isTerminated

Detección de estado

## Descripción

```php
public Threaded::isTerminated(): bool
```php

Se verifica si el objeto referenciado ha finalizado durante la ejecución; si ha sufrido un error fatal o ha generado excepciones que no han podido ser capturadas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un valor booleano que indica el estado.

## Ejemplos

Detecta el estado del objeto referenciado

```
<?php
class My extends Thread {
    public function run() {
        i_do_not_exist();
    }
}
$my = new My();
$my->start();
$my->join();
var_dump($my->isTerminated());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
