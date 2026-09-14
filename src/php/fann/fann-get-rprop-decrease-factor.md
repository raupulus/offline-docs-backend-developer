---
title: fann_get_rprop_decrease_factor
description: Devuelve el factor de disminución empleado durante un entrenamiento RPROP
source_url: https://www.php.net/manual/es/function.fann-get-rprop-decrease-factor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-rprop-decrease-factor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 21440
---

fann_get_rprop_decrease_factor

Devuelve el factor de disminución empleado durante un entrenamiento RPROP

## Descripción

```php
fann_get_rprop_decrease_factor(resource $ann): float
```php

El factor de disminución es un valor menor que 1, el cual se emplea para disminuir el tamaño del paso durante un entrenamiento RPROP.

El factor de disminución predeterminado es 0.5.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El factor de disminución, o `false` en caso de error.

## Véase también

`fann_set_rprop_decrease_factor`
