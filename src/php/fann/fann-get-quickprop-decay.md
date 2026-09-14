---
title: fann_get_quickprop_decay
description: Devuelve la decadencia, que es un factor por el que los pesos deberían
  decrementar en cada iteración durante un entrenamiento quickprop
source_url: https://www.php.net/manual/es/function.fann-get-quickprop-decay.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-quickprop-decay.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21420
---

fann_get_quickprop_decay

Devuelve la decadencia, que es un factor por el que los pesos deberían decrementar en cada iteración durante un entrenamiento quickprop

## Descripción

```php
fann_get_quickprop_decay(resource $ann): float
```php

La decadencia es un número pequeño negativo que es un factor por el que los pesos deberían decrementar en cada iteración durante un entrenamiento quickprop. Se emplea para asegurarse de que los pesos no sean demasiado altos durante el entrenamiento.

La decadencia predeterminada es -0.0001.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

The decay, or `false` on error.

## Véase también

`fann_set_quickprop_decay`
