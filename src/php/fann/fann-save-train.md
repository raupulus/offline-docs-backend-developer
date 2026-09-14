---
title: fann_save_train
description: Guarda la estructura de entrenamiento en un fichero
source_url: https://www.php.net/manual/es/function.fann-save-train.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-save-train.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21700
---

fann_save_train

Guarda la estructura de entrenamiento en un fichero

## Descripción

```php
fann_save_train(resource $data, string $file_name): bool
```php

Guarda la estructura de entrenamiento en un fichero, con el formato especificado en `fann_read_train_from_file`.

## Parámetros

`data`  
Un `resource` de datos de entrenamiento de red neuronal.

`file_name`  
El nombre delfichero donde guardar los datos de entrenamiento.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_read_train_from_file`
