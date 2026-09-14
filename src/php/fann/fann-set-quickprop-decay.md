---
title: fann_set_quickprop_decay
description: Establece el factor de decadencia de quickprop
source_url: https://www.php.net/manual/es/function.fann-set-quickprop-decay.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-quickprop-decay.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22060
---

fann_set_quickprop_decay

Establece el factor de decadencia de quickprop

## Descripción

```php
fann_set_quickprop_decay(resource $ann, float $quickprop_decay): bool
```php

Establece el factor de decadencia de quickprop.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`quickprop_decay`  
El factor de decadencia de quickprop.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_quickprop_decay`
