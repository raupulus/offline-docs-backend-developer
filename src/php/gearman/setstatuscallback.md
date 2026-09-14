---
title: GearmanClient::setStatusCallback
description: Define una función de retorno para recolectar los estados de una tarea
source_url: https://www.php.net/manual/es/gearmanclient.setstatuscallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/setstatuscallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25290
---

GearmanClient::setStatusCallback

Define una función de retorno para recolectar los estados de una tarea

## Descripción

```php
public GearmanClient::setStatusCallback(callable $callback): bool
```php

Define una función de retorno para utilizar al recuperar las informaciones de estado actualizadas desde el agente.

> [!NOTE]
> El callback solo será disparado para las tareas que son añadidas (por ejemplo llamando a GearmanClient::addTask) después de la llamada a este método.

## Parámetros

`callback`  
Una función o método a llamar. Debe retornar un valor válido [de retorno Gearman](#gearman.constants).

Si no se proporciona una instrucción de retorno, el valor predeterminado será `GEARMAN_SUCCESS`.

```php
callback(GearmanTask $task, mixed $context): int
```

`task`  
La tarea para la cual se llama este callback.

`context`  
Todo lo que se pasó a GearmanClient::addTask (o método equivalente) como `context`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanClient::setDataCallback

GearmanClient::setCompleteCallback

GearmanClient::setCreatedCallback

GearmanClient::setExceptionCallback

GearmanClient::setFailCallback

GearmanClient::setWarningCallback

GearmanClient::setWorkloadCallback
