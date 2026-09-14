---
title: GearmanWorker::echo
description: Comprueba la respuesta de un servidor de trabajo
source_url: https://www.php.net/manual/es/gearmanworker.echo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/echo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25820
---

GearmanWorker::echo

Comprueba la respuesta de un servidor de trabajo

## Descripción

```php
public GearmanWorker::echo(string $workload): bool
```php

Envía datos a todos los servidores de trabajo para comprobar si los retornan. Esta es una función de prueba para ver si los servidores de trabajo están respondiendo de forma adecuada.

## Parámetros

`workload`  
Datos arbitrarios serializados

## Valores devueltos

Valor de retorno estándar de Gearman.

## Véase también

GearmanClient::echo
