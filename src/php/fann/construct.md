---
title: FANNConnection::__construct
description: El constructor de la conexión
source_url: https://www.php.net/manual/es/fannconnection.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/fannconnection/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: c44e9cb68
order: 20840
---

FANNConnection::\_\_construct

El constructor de la conexión

## Descripción

```php
public FANNConnection::__construct(int $from_neuron, int $to_neuron, float $weight)
```php

Crea una nueva conexión e inicializa sus parámetros. Después de crear la conexión, solamente se puede cambiar el peso.

## Parámetros

`from_neuron`  
El número de posición de la neurona inicial.

`to_neuron`  
El número de posición de la neurona terminal.

`weight`  
El valor del peso de la conexión.
