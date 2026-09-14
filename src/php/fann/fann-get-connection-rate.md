---
title: fann_get_connection_rate
description: Obtener el índice de conexión empleado al crear la red
source_url: https://www.php.net/manual/es/function.fann-get-connection-rate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-connection-rate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21310
---

fann_get_connection_rate

Obtener el índice de conexión empleado al crear la red

## Descripción

```php
fann_get_connection_rate(resource $ann): float
```php

Obtener el índice de conexión empleado al crear la red.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El índice de conexión empleado al crear la red, o `false` en caso de error.
