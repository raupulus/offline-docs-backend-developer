---
title: EventDnsBase::countNameservers
description: Recupera el número de servidores de nombres configurados
source_url: https://www.php.net/manual/es/eventdnsbase.countnameservers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventdnsbase/countnameservers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 8e173d4fe
order: 19780
---

EventDnsBase::countNameservers

Recupera el número de servidores de nombres configurados

## Descripción

```php
public EventDnsBase::countNameservers(): int
```php

Recupera el número de servidores de nombres configurados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de servidores de nombres configurados (no necesariamente el número de servidores de nombres en funcionamiento). Esto es útil para verificar si las llamadas a las diversas funciones de configuración de los servidores de nombres han tenido éxito o no.
