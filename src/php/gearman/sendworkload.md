---
title: GearmanTask::sendWorkload
description: Envía los datos para una tarea
source_url: https://www.php.net/manual/es/gearmantask.sendworkload.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmantask/sendworkload.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25700
---

GearmanTask::sendWorkload

Envía los datos para una tarea

## Descripción

```php
public GearmanTask::sendWorkload(string $data): int
```php

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Parámetros

`data`  
Datos a enviar al agente.

## Valores devueltos

La longitud de los datos a enviar, o `false` si el envío falla.

## Véase también

GearmanTask::recvData
