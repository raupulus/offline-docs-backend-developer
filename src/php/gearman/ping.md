---
title: GearmanClient::ping
description: Envío de datos a todos los servidores de tareas para verificar que siguen
  en funcionamiento
source_url: https://www.php.net/manual/es/gearmanclient.ping.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/ping.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25160
---

GearmanClient::ping

Envío de datos a todos los servidores de tareas para verificar que siguen en funcionamiento

## Descripción

```php
public GearmanClient::ping(string $workload): bool
```php

Envío de datos arbitrarios a todos los servidores de tareas para verificar que siguen en funcionamiento. Los datos enviados no son utilizados ni analizados en ningún caso. La utilidad principal de esta función es durante las pruebas y la depuración.

## Parámetros

`workload`  
Algunos datos arbitrarios que serán devueltos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
