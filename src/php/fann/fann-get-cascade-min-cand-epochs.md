---
title: fann_get_cascade_min_cand_epochs
description: Devuelve el mínimo de épocas de candidatas
source_url: https://www.php.net/manual/es/function.fann-get-cascade-min-cand-epochs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-min-cand-epochs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21230
---

fann_get_cascade_min_cand_epochs

Devuelve el mínimo de épocas de candidatas

## Descripción

```php
fann_get_cascade_min_cand_epochs(resource $ann): int
```php

El mínimo de épocas de cadidatas determina el número máximo de épocas que podrían ser entrenadas las conexiones de entrada a las candidatas antes de añadir una nueva neurona candidata.

El mínimo de épocas de candidatas predterminado es 150.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El mínimo de épocas de candidtas, o `false` en caso de error.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_set_cascade_min_cand_epochs`
