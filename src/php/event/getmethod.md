---
title: EventBase::getMethod
description: Devuelve el método de evento utilizado
source_url: https://www.php.net/manual/es/eventbase.getmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/getmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_revision: e26545dca
order: 19060
---

EventBase::getMethod

Devuelve el método de evento utilizado

## Descripción

```php
public EventBase::getMethod(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

String que representa el método de evento utilizado (backend).

## Ejemplos

Ejemplo con `EventBase::getMethod`

```
<?php
$cfg = new EventConfig();
if ($cfg->avoidMethod("select")) {
    echo "Método `select' evitado\n";
}

// Crear un evento base asociado con el config
$base = new EventBase($cfg);
echo "Método de evento utilizado: ", $base->getMethod(), PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    método `select' evitado
    Método de evento utilizado: epoll

## Véase también

EventBase::getFeatures
