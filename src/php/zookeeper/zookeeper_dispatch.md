---
title: zookeeper_dispatch
description: Llama a las funciones de devolución de llamada para las operaciones pendientes
source_url: https://www.php.net/manual/es/function.zookeeper-dispatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/functions/zookeeper_dispatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 62a954a6f
order: 109520
---

zookeeper_dispatch

Llama a las funciones de devolución de llamada para las operaciones pendientes

## Descripción

```php
zookeeper_dispatch(): void
```php

La función `zookeeper_dispatch` llama a las funciones de devolución de llamada pasadas por las operaciones como Zookeeper::get o Zookeeper::exists.

> [!CAUTION]
> Desde la versión 0.4.0, esta función debe ser llamada manualmente para realizar operaciones asíncronas. Si desea que esto se haga automáticamente, también puede declarar ticks al inicio de su programa.

Después de PHP 7.1, puede ignorar esta función. Esta extensión usa EG(vm_interrupt) para implementar la distribución asíncrona.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Este método emite una alerta PHP cuando la función de devolución de llamada no puede ser invocada.

## Ejemplos

Ejemplo de zookeeper_dispatch \#1

Distribuir manualmente las funciones de devolución de llamada.

```
<?php
$client = new Zookeeper();
$client->connect('localhost:2181');
$client->get('/zookeeper', function() {
    echo "Callback was called".PHP_EOL;
});
while(true) {
    sleep(1);
    zookeeper_dispatch();
}
?>

   
```php

Ejemplo de zookeeper_dispatch \#2

Declarar ticks.

```
<?php
declare(ticks=1);

$client = new Zookeeper();
$client->connect('localhost:2181');
$client->get('/zookeeper', function() {
    echo "Callback was called".PHP_EOL;
});
while(true) {
    sleep(1);
}
?>

   
```php

## Véase también

Zookeeper::addAuth, Zookeeper::connect, Zookeeper::\_\_construct, Zookeeper::exists, Zookeeper::get, Zookeeper::getChildren, Zookeeper::setWatcher
