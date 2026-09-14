---
title: SVMModel::predict_probability
description: Devuelve las probabilidades para los datos anteriores no presentados
source_url: https://www.php.net/manual/es/svmmodel.predict-probability.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svmmodel/predict-probability.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 1ca2d4af9
order: 89820
---

SVMModel::predict_probability

Devuelve las probabilidades para los datos anteriores no presentados

## Descripción

```php
public SVMModel::predict_probability(array $data): float
```php

Esta función acepta un array de datos y trata de predecir la clase, como con las funciones de predicción. Además, sin embargo, esta función devuelve un array de probabilidades, una por clase del modelo, que representa la probabilidad estimada de que los datos proporcionados sean un miembro de esa clase. Necesita que el modelo a utilizar sea tratado con el parámetro de probabilidad establecido en `true`.

## Parámetros

`data`  
El array a clasificar. Esto debe ser una serie de pares clave=\>valor cuyos índices están en orden creciente, pero no necesariamente continuo.

`probabilities`  
El valor proporcionado será completado con las probabilidades. Esto puede ser `null` en el caso de que el modelo no contenga información de probabilidad, o un array en el que los índices sean los nombres de clase y los valores, las probabilidades.

## Valores devueltos

Devuelve el valor predicho. Esto será una etiqueta de clase en el caso de una clasificación, un valor real en el caso de una regresión. Lanza una excepción de tipo SVMException en caso de error.

## Véase también

SVM::predict
