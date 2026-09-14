---
title: GearmanClient::echo
description: Envía datos a todos los servidores de trabajo para ver si retornan [obsoleto]
source_url: https://www.php.net/manual/es/gearmanclient.echo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/echo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25120
---

GearmanClient::echo

Envía datos a todos los servidores de trabajo para ver si retornan \[obsoleto\]

## Descripción

```php
public GearmanClient::echo(string $workload): bool
```php

El método GearmanClient::echo es obsoleto desde pecl/gearman 1.0.0. Use GearmanClient::ping.

## Parámetros

`workload`  
Datos arbitrarios serializados a ser retornados

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
