---
title: fann_set_sarprop_weight_decay_shift
description: Establece el desplazamiento de decadencia del peso de sarprop
source_url: https://www.php.net/manual/es/function.fann-set-sarprop-weight-decay-shift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-sarprop-weight-decay-shift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 242efce0d
order: 22160
---

fann_set_sarprop_weight_decay_shift

Establece el desplazamiento de decadencia del peso de sarprop

## Descripción

```php
fann_set_sarprop_weight_decay_shift(resource $ann, float $sarprop_weight_decay_shift): bool
```php

Establece el desplazamiento de decadencia del peso de sarprop.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`sarprop_weight_decay_shift`  
El desplazamiento de decadencia del peso de sarprop.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_get_sarprop_weight_decay_shift`
