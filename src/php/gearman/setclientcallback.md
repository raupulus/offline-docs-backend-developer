---
title: GearmanClient::setClientCallback
description: Define una función de retrollamada cuando se recibe un paquete de datos
  para una tarea (obsoleto)
source_url: https://www.php.net/manual/es/gearmanclient.setclientcallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/setclientcallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25200
---

GearmanClient::setClientCallback

Define una función de retrollamada cuando se recibe un paquete de datos para una tarea (obsoleto)

## Descripción

```php
public GearmanClient::setClientCallback(callable $callback): void
```php

Define una función de retrollamada cuando se recibe un paquete de datos para una tarea.

> [!NOTE]
> Este método ha sido reemplazado por el método GearmanClient::setDataCallback desde la versión 0.6.0 de la extensión Gearman.

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

GearmanClient::setCompleteCallback

GearmanClient::setCreatedCallback

GearmanClient::setDataCallback

GearmanClient::setExceptionCallback

GearmanClient::setFailCallback

GearmanClient::setStatusCallback

GearmanClient::setWarningCallback

GearmanClient::setWorkloadCallback
