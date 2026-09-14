---
title: fann_get_sarprop_weight_decay_shift
description: Devuelve el desplazamiento de decadencia del peso de sarprop
source_url: https://www.php.net/manual/es/function.fann-get-sarprop-weight-decay-shift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-sarprop-weight-decay-shift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21520
---

fann_get_sarprop_weight_decay_shift

Devuelve el desplazamiento de decadencia del peso de sarprop

## Descripción

```php
fann_get_sarprop_weight_decay_shift(resource $ann): float
```php

Devuelve el desplazamiento de decadencia del peso de sarprop.

El valor de delta máximo es -6.644.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El desplazamiento de decadencia del peso de sarprop, o `false` en caso de error.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_set_sarprop_weight_decay_shift`
