---
title: EventConfig::avoidMethod
description: Solicita a libevent que ignore un método de evento específico
source_url: https://www.php.net/manual/es/eventconfig.avoidmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventconfig/avoidmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19680
---

EventConfig::avoidMethod

Solicita a libevent que ignore un método de evento específico

## Descripción

```php
public EventConfig::avoidMethod(string $method): bool
```php

Solicita a libevent que ignore un método de evento específico. Ver la [creación de un evento de base](http://www.wangafu.net/~nickm/libevent-book/Ref2_eventbase.html#_creating_an_event_base).

## Parámetros

`method`  
El método a ignorar. Ver [las constantes EventConfig](#eventconfig.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventConfig::avoidMethod`

```
<?php
$cfg = new EventConfig();
if ($cfg->avoidMethod("select")) {
    echo "Método 'select' ignorado\n";
}
?>

   
```php

## Véase también

EventBase::\_\_construct
