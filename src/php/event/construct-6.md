---
title: EventDnsBase::__construct
description: Construye un objeto EventDnsBase
source_url: https://www.php.net/manual/es/eventdnsbase.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventdnsbase/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 19770
---

EventDnsBase::\_\_construct

Construye un objeto EventDnsBase

## Descripción

```php
public EventDnsBase::__construct(EventBase $base, int $initialize)
```php

Construye un objeto EventDnsBase.

## Parámetros

`base`  
Evento de base.

`initialize`  
Si `initialize` es `true`, intenta utilizar los parámetros por defecto del sistema operativo subyacente para configurar adecuadamente la base DNS. Si es `false`, la base DNS se deja sin configurar, sin servidores de nombres ni opciones definidas. En este último caso, la base DNS debe ser configurada manualmente, por ejemplo con el método EventDnsBase::parseResolvConf.

Si `initialize` es un entero, debe ser uno de los siguientes flags:

| Flag | Descripción |
|----|----|
| `EventDnsBase::DISABLE_WHEN_INACTIVE` | No impide que el bucle de eventos de libevent termine cuando no haya solicitudes DNS activas. |
| `EventDnsBase::INITIALIZE_NAMESERVERS` | Procesar el fichero `resolv.conf`. |
| `EventDnsBase::NAMESERVERS_NO_DEFAULT` | No añadir servidores de nombres por defecto si no hay servidores de nombres en el fichero `resolv.conf`. |

## Errores/Excepciones

Si `initialize` tiene un tipo distinto de `intbool`, se lanza una TypeError.

Si el valor de `initialize` es inválido, se lanza una EventException.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL event 3.1.3 | Si `initialize` tiene un tipo distinto de `intbool`, se lanza una TypeError. |
| PECL event 3.1.0RC1 | El tipo del parámetro `initialize` ha sido cambiado de `bool` a `mixed`. El valor puede ser `bool` (preservando el significado anterior) o una de las siguientes constantes: `EventDnsBase::DISABLE_WHEN_INACTIVE`, `EventDnsBase::INITIALIZE_NAMESERVERS`, o `EventDnsBase::NAMESERVERS_NO_DEFAULT`. |
