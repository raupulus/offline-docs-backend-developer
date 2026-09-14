---
title: fann_get_quickprop_mu
description: Devuelve el factor mu
source_url: https://www.php.net/manual/es/function.fann-get-quickprop-mu.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-quickprop-mu.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21430
---

fann_get_quickprop_mu

Devuelve el factor mu

## Descripción

```php
fann_get_quickprop_mu(resource $ann): float
```php

El factor mu se emplea para aumentar y disminuir el tamaño del paso durante un entrenamiento quickprop. El factor mu debería estar siempre por encima de 1, ya que, de lo contrario, lo disminuiría cuando se suponía que debía de aumentarlo.

El factor mu predeterminado es 1.75.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

Ek factor mu, o `false` en caso de error.

## Véase también

`fann_set_quickprop_mu`
