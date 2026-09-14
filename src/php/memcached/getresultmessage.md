---
title: Memcached::getResultMessage
description: Devuelve un mensaje que describe el resultado de la última operación
source_url: https://www.php.net/manual/es/memcached.getresultmessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getresultmessage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46610
---

Memcached::getResultMessage

Devuelve un mensaje que describe el resultado de la última operación

## Descripción

```php
public Memcached::getResultMessage(): string
```php

`Memcached::getResultMessage` devuelve un string que describe el código de resultado de la última operación Memcached ejecutada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Mensaje que describe el resultado de la última operación Memcached.

## Ejemplos

Ejemplo con `Memcached::getResultMessage`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$m->add('foo', 'bar'); // Éxito la primera vez
$m->add('foo', 'bar');
echo $m->getResultMessage(),"\n";
?>

    
```php

El ejemplo anterior mostrará:

    NOT STORED
