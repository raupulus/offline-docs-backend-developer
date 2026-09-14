---
title: fann_set_quickprop_mu
description: Establece el factor mu de quickprop
source_url: https://www.php.net/manual/es/function.fann-set-quickprop-mu.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-quickprop-mu.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22070
---

fann_set_quickprop_mu

Establece el factor mu de quickprop

## Descripción

```php
fann_set_quickprop_mu(resource $ann, float $quickprop_mu): bool
```php

Establece el factor mu de quickprop.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`quickprop_mu`  
El factor mu.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_quickprop_mu`
