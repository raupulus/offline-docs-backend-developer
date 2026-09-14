---
title: FANNConnection::setWeight
description: Establece el peso de la conexión
source_url: https://www.php.net/manual/es/fannconnection.setweight.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/fannconnection/setweight.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: dd52a26b7
order: 20880
---

FANNConnection::setWeight

Establece el peso de la conexión

## Descripción

```php
public FANNConnection::setWeight(float $weight): void
```php

Establece el peso de la conexión.

Este método es diferente de `fann_set_weight`. No actualiza el valor del peso de la red. El valor de la red se actualiza solamente después de llamar a `fann_set_weight_array`.

## Parámetros

`weight`  
El peso de la conexión.

## Valores devueltos

No devuelve ningún valor.
