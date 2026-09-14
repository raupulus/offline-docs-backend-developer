---
title: fann_descale_input
description: Escalar datos en un vector de entrada después de obtenerlo de una RNA
  basada en parámetros previamente calculados
source_url: https://www.php.net/manual/es/function.fann-descale-input.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-descale-input.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21030
---

fann_descale_input

Escalar datos en un vector de entrada después de obtenerlo de una RNA basada en parámetros previamente calculados

## Descripción

```php
fann_descale_input(resource $ann, array $input_vector): bool
```php

Escalar datos en un vector de entrada después de obtenerlo de una RNA basada en parámetros previamente calculados.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`input_vector`  
El vector de entrada a desescalar

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_scale_input`, `fann_descale_output`
