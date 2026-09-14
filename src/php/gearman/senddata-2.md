---
title: GearmanTask::sendData
description: Envía datos para una tarea (deprecado)
source_url: https://www.php.net/manual/es/gearmantask.senddata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmantask/senddata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25690
---

GearmanTask::sendData

Envía datos para una tarea (deprecado)

## Descripción

```php
public GearmanTask::sendData(string $data): int
```php

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Parámetros

`data`  
Datos a enviar al agente.

## Valores devueltos

La longitud de los datos enviados, o `false` si el envío ha fallado.

## Véase también

GearmanTask::recvData
