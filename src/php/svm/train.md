---
title: SVM::train
description: Crea un modelo SVMModel basado en los datos de entrenamiento
source_url: https://www.php.net/manual/es/svm.train.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svm/train.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 1ca2d4af9
order: 89720
---

SVM::train

Crea un modelo SVMModel basado en los datos de entrenamiento

## Descripción

```php
public svm::train(array $problem, [array $weights]): SVMModel
```php

Entrena una máquina vectorial basada en los datos de entrenamiento proporcionados.

## Parámetros

`problem`  
El problema puede ser proporcionado de 3 maneras. Un array, donde las datos deben comenzar por la etiqueta de la clase (habitualmente 1 o -1), seguido por una serie de datos en forma de pares dimensión/dato. Una URL hacia un archivo que contiene un problema en formato SVM Light, donde cada línea comienza con un nuevo ejemplo de entrenamiento, el inicio de cada línea contiene la clase (1 o -1) seguido de una serie de valores de datos separados por una tabulación en forma clave:valor. Un flujo abierto que apunta hacia una fuente de datos formateada como en el archivo anterior.

`weights`  
Los pesos son conjuntos opcionales de parámetros de ponderación para las diferentes clases, para ayudar en el conteo para conjuntos de entrenamiento desequilibrados. Por ejemplo, si las clases son 1 y -1, y que -1 tiene más ejemplos significativos que el primero, el peso para -1 podría ser de 0.5. Los pesos deben estar en el intervalo 0-1.

## Valores devueltos

Devuelve un modelo SVMModel que puede ser utilizado para clasificar datos previamente no vistos. Lanza una excepción SVMException si ocurre un error.
