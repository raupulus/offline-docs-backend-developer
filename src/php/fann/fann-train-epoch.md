---
title: fann_train_epoch
description: Entrenar una época con un conjunto de datos de entrenamiento
source_url: https://www.php.net/manual/es/function.fann-train-epoch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-train-epoch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 22270
---

fann_train_epoch

Entrenar una época con un conjunto de datos de entrenamiento

## Descripción

```php
fann_train_epoch(resource $ann, resource $data): float
```php

Entrena una época con los datos de entrenamiento almacenados en data. Una época es donde todos los datos de entrenamiento son considerados exactamente una vez.

Esta función devuelve el ECM tal como es calculado antes o durante el entrenamiento real. No es el ECM real después de la época de entrenamiento, pero como calcularlo requeriría atravesar el conjunto de entrenamiento completo una vez más, el empleo de este valor durante el entrenamiento es más que adecuado.

El algoritmo de entrenaiento empleado por esta función se elige mediante la función `fann_set_training_algorithm`.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`data`  
Un `resource` de datos de entrenamiento de red neuronal.

## Valores devueltos

El ECM, o `false` en caso de error.

## Véase también

`fann_train_on_data`, `fann_test_data`, `fann_get_MSE`, `fann_set_training_algorithm`
