---
title: mqseries_put1
description: MQSeries MQPUT1
source_url: https://www.php.net/manual/es/function.mqseries-put1.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-put1.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: true
translation_revision: b5efbef2d
order: 51930
---

mqseries_put1

MQSeries MQPUT1

## Descripción

```php
mqseries_put1(resource $hconn, resource $objDesc, resource $msgDesc, resource $pmo, string $buffer, resource $compCode, resource $reason): void
```php

La llamada a `mqseries_put1` (MQPUT1) añade un mensaje a una cola. La cola no necesita estar abierta.

Se pueden utilizar tanto llamadas a `mqseries_put` como a `mqseries_put1` para añadir mensajes a una cola; qué llamada utilizar depende de las circunstancias. Utilizar la llamada a `mqseries_put` (MQPUT) para añadir varios mensajes a la misma cola. Utilizar la llamada a `mqseries_put1` (MQPUT1) para añadir un solo mensaje a una cola. Esta llamada engloba las llamadas a MQOPEN, MQPUT y MQCLOSE en una sola llamada, minimizando el número de llamadas a emitir.

## Parámetros

`hConn`  
Gestor de conexión.

Este gestor representa la conexión al gestor de colas.

`objDesc`  
Descriptor del objeto (MQOD).

Esta estructura identifica la cola en la que se añadirá el mensaje.

`msgDesc`  
Descriptor del mensaje (MQMD).

`pmo`  
Opciones de adición del mensaje (MQPMO).

`compCode`  
Código de finalización.

`reason`  
La razón que califica el compCode.

## Valores devueltos

No se retorna ningún valor.

## Véase también

mqseries_conn

mqseries_connx

mqseries_open

mqseries_get
