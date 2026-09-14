---
title: GearmanTask::recvData
description: Lee el trabajo o los datos devueltos por una tarea en un buffer
source_url: https://www.php.net/manual/es/gearmantask.recvdata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmantask/recvdata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25670
---

GearmanTask::recvData

Lee el trabajo o los datos devueltos por una tarea en un buffer

## Descripción

```php
public GearmanTask::recvData(int $data_len): false
```php

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Parámetros

`data_len`  
Longitud de los datos a leer.

## Valores devueltos

Un array cuyo primer elemento es la longitud de los datos leídos, y el segundo, el buffer de datos. Devuelve `false` si la lectura falla.

## Véase también

GearmanTask::sendData
