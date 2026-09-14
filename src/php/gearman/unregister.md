---
title: GearmanWorker::unregister
description: Elimina una función de los servidores de trabajos
source_url: https://www.php.net/manual/es/gearmanworker.unregister.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/unregister.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25930
---

GearmanWorker::unregister

Elimina una función de los servidores de trabajos

## Descripción

```php
public GearmanWorker::unregister(string $function_name): bool
```php

Elimina una función de los servidores de trabajos, haciendo que ningún trabajo sea enviado al agente para esta función.

## Parámetros

`function_name`  
El nombre de una función a eliminar del servidor de trabajos.

## Valores devueltos

Un valor de retorno estándar de Gearman.

## Véase también

GearmanWorker::register

GearmanWorker::unregisterAll
