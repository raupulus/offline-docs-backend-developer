---
title: SVMModel::predict
description: Predice un valor para datos anteriores no vistos
source_url: https://www.php.net/manual/es/svmmodel.predict.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svmmodel/predict.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 1ca2d4af9
order: 89830
---

SVMModel::predict

Predice un valor para datos anteriores no vistos

## Descripción

```php
public SVMModel::predict(array $data): float
```php

Esta función acepta un array de datos y trata de predecir el valor de la clase o de la regresión, según el modelo extraído desde los datos previamente entrenados.

## Parámetros

`data`  
El array a clasificar. Esto puede ser una serie de pares clave =\> valor en orden creciente de las claves, pero no necesariamente continuo.

## Valores devueltos

Devuelve el valor predicho. Esto puede ser una etiqueta de clase en el caso de una clasificación, un valor real en el caso de una regresión. Lanza una excepción SVMException en caso de error.

## Véase también

SVM::train
