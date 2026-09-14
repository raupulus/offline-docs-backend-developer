---
title: SVM::crossvalidate
description: Prueba los argumentos de entrenamiento en los subconjuntos de datos de
  entrenamiento
source_url: https://www.php.net/manual/es/svm.crossvalidate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svm/crossvalidate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 89690
---

SVM::crossvalidate

Prueba los argumentos de entrenamiento en los subconjuntos de datos de entrenamiento

## Descripción

```php
public svm::crossvalidate(array $problem, int $number_of_folds): float
```php

Puede ser utilizado para probar la efectividad del conjunto de argumentos actual en los subconjuntos de datos de entrenamiento. Al proporcionar un problema así como n "plis", la función separará el conjunto del problema en n subconjuntos, y comenzará entrenamientos sucesivos en los subconjuntos. Aunque la precisión sea generalmente más baja que la de un SVM entrenado con los conjuntos de datos proporcionados, el porcentaje correcto retornado debería ser suficientemente útil para probar diferentes argumentos de entrenamiento.

## Parámetros

`problem`  
Los datos del problema. Puede estar en forma de array, de una URL hacia un archivo SVMLight, o de un flujo hacia un recurso de datos SVMLight abierto.

`number_of_folds`  
El número de conjuntos en los que los datos deben ser divididos y probados. Un número alto significa que los conjuntos de entrenamiento serán más pequeños y menos fiables. 5 es un buen comienzo.

## Valores devueltos

El porcentaje correcto, expresado como un número de punto flotante en el intervalo 0-1. En el caso de un núcleo NU_SVC o EPSILON_SVR, el error cuadrático medio será retornado.

## Véase también

SVM::train
