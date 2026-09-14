---
title: GearmanClient::wait
description: Espera la actividad de E/S en todas las conexiones de un cliente
source_url: https://www.php.net/manual/es/gearmanclient.wait.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/wait.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: true
translation_revision: cf0a919c1
order: 25340
---

GearmanClient::wait

Espera la actividad de E/S en todas las conexiones de un cliente

## Descripción

```php
public GearmanClient::wait(): bool
```php

Esto espera la actividad de cualquiera de los servidores conectados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` en caso de éxito, `false` en caso de error.

## Véase también

GearmanWorker::wait
