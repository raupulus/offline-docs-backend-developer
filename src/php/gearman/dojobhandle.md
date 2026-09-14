---
title: GearmanClient::doJobHandle
description: Obtiene el manejador de trabajos para la tarea en curso
source_url: https://www.php.net/manual/es/gearmanclient.dojobhandle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/dojobhandle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25070
---

GearmanClient::doJobHandle

Obtiene el manejador de trabajos para la tarea en curso

## Descripción

```php
public GearmanClient::doJobHandle(): string
```php

Obtiene el manejador de trabajos para la tarea en curso. Puede ser utilizado durante múltiples llamadas al método GearmanClient::doNormal. El manejador de trabajos puede entonces ser utilizado para recuperar las informaciones sobre la tarea.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El manejador de trabajos para la tarea en curso.

## Véase también

GearmanClient::jobStatus
