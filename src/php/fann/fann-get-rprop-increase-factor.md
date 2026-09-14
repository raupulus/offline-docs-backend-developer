---
title: fann_get_rprop_increase_factor
description: Devuelve el factor de aumento empleado durante un entrenamiento RPROP
source_url: https://www.php.net/manual/es/function.fann-get-rprop-increase-factor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-rprop-increase-factor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21480
---

fann_get_rprop_increase_factor

Devuelve el factor de aumento empleado durante un entrenamiento RPROP

## Descripción

```php
fann_get_rprop_increase_factor(resource $ann): float
```php

El factor de aumento es un valor mayor que 1, el cual se emplea para aumentar el tamaño del paso durante un entrenamiento RPROP.

El factor de aumento predeterminado es 1.2.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El factor de aumento, o `false` en caso de error.

## Véase también

`fann_set_rprop_increase_factor`
