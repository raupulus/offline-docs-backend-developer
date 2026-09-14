---
title: fann_get_total_neurons
description: Obtener el número total de neuronas de la red completa
source_url: https://www.php.net/manual/es/function.fann-get-total-neurons.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-total-neurons.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21540
---

fann_get_total_neurons

Obtener el número total de neuronas de la red completa

## Descripción

```php
fann_get_total_neurons(resource $ann): int
```php

Obtener el número total de neuronas de la red completa. Este número también incluye las neuronas de tendencia, por lo que una red 2-4-2 posee 2+4+2 +2(tendencias) = 10 neuronas.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El número total de neuronas de la red completa, o `false` en caso de error.
