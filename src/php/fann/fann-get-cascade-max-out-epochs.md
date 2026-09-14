---
title: fann_get_cascade_max_out_epochs
description: Devuelve el máximo de épocas de salida
source_url: https://www.php.net/manual/es/function.fann-get-cascade-max-out-epochs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-max-out-epochs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21220
---

fann_get_cascade_max_out_epochs

Devuelve el máximo de épocas de salida

## Descripción

```php
fann_get_cascade_max_out_epochs(resource $ann): int
```php

El máximo de épocas de salida determina el número máximo de épocas que podrían ser entrenadas las conexiones de salida después de añadir una nueva neurona candidata.

El máximo de épocas de salida predterminado es 150.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El máximo de épocas de salida, o `false` en caso de error.

## Véase también

`fann_set_cascade_max_out_epochs`
