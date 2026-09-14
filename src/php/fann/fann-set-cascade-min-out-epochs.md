---
title: fann_set_cascade_min_out_epochs
description: Establece el mínimo de épocas de salida
source_url: https://www.php.net/manual/es/function.fann-set-cascade-min-out-epochs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-min-out-epochs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 242efce0d
order: 21960
---

fann_set_cascade_min_out_epochs

Establece el mínimo de épocas de salida

## Descripción

```php
fann_set_cascade_min_out_epochs(resource $ann, int $cascade_min_out_epochs): bool
```php

Establece el mínimo de épocas de salida.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_min_out_epochs`  
El mínimo de épocas de salida.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_get_cascade_min_out_epochs`
