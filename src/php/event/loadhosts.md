---
title: EventDnsBase::loadHosts
description: Carga un fichero hosts (en el mismo formato que /etc/hosts)
source_url: https://www.php.net/manual/es/eventdnsbase.loadhosts.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventdnsbase/loadhosts.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19790
---

EventDnsBase::loadHosts

Carga un fichero hosts (en el mismo formato que /etc/hosts)

## Descripción

```php
public EventDnsBase::loadHosts(string $hosts): bool
```php

Carga un fichero hosts (en el mismo formato que /etc/hosts).

## Parámetros

`hosts`  
Ruta de acceso al fichero hosts.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
