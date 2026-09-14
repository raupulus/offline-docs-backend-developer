---
title: fann_copy
description: Crea una copia de una estructura fann
source_url: https://www.php.net/manual/es/function.fann-copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 20930
---

fann_copy

Crea una copia de una estructura fann

## Descripción

```php
fann_copy(resource $ann): resource
```php

Crea una copia de una estructura fann.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

Devuelve una copia de un recurso de red neuronal en caso de éxito, o `false` en caso de error.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_test`
