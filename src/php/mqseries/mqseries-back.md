---
title: mqseries_back
description: MQSeries MQBACK
source_url: https://www.php.net/manual/es/function.mqseries-back.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-back.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51820
---

mqseries_back

MQSeries MQBACK

## Descripción

```php
mqseries_back(resource $hconn, resource $compCode, resource $reason): void
```php

`mqseries_back` indica al gestor de colas que todos los mensajes leídos y escritos desde el último punto de sincronización deben ser anulados. Los mensajes que forman parte de una unidad de trabajo serán eliminados. Los mensajes leídos como unidad de trabajo serán reinsertados en la cola.

El uso de `mqseries_back` funciona asimismo en conjunción con `mqseries_begin` y únicamente al conectarse directamente al gestor de colas: no funciona a través de la interfaz mqclient.

## Parámetros

`hConn`  
Gestor de conexión.

Este recurso representa la conexión al gestor de colas.

`compCode`  
Código de finalización.

`reason`  
La razón que califica el compCode.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `mqseries_back`

```
<?php
    mqseries_back($conn, $comp_code, $reason);

    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
    }
?>

   
```php

## Notas

> [!NOTE]
> `mqseries_back` no funciona cuando un cliente MQSeries Client se conecta al gestor de colas.

## Véase también

mqseries_conn

mqseries_connx

mqseries_begin
