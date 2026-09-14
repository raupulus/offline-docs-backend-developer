---
title: mqseries_cmit
description: MQSeries MQCMIT
source_url: https://www.php.net/manual/es/function.mqseries-cmit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-cmit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51850
---

mqseries_cmit

MQSeries MQCMIT

## Descripción

```php
mqseries_cmit(resource $hconn, resource $compCode, resource $reason): void
```php

`mqseries_cmit` indica al gestor de colas que la aplicación ha alcanzado un punto de sincronización, y que todos los mensajes que han sido leídos y escritos desde el último punto de sincronización han sido hechos permanentes. Los mensajes colocados en la cola como unidad de trabajo son ahora accesibles a otras aplicaciones. Los mensajes leídos como unidad de trabajo son ahora destruidos.

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

Ejemplo con `mqseries_cmit`

```
<?php
    mqseries_cmit($conn, $comp_code, $reason);
    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("cmit CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
    }
?>

   
```php

## Notas

> [!NOTE]
> `mqseries_back` no funciona cuando un cliente MQSeries Client se conecta al gestor de colas.

## Véase también

mqseries_begin

mqseries_back

mqseries_conn

mqseries_connx
