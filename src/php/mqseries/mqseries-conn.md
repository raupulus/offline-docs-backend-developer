---
title: mqseries_conn
description: MQSeries MQCONN
source_url: https://www.php.net/manual/es/function.mqseries-conn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-conn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51860
---

mqseries_conn

MQSeries MQCONN

## Descripción

```php
mqseries_conn(string $qManagerName, resource $hconn, resource $compCode, resource $reason): void
```php

`mqseries_conn` establece la conexión con el gestor de colas. Proporciona un recurso de conexión, que es utilizado por las demás funciones de la extensión.

## Parámetros

`qManagerName`  
Nombre del gestor de colas.

Nombre del gestor de colas con el que la aplicación desea conectarse.

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

Ejemplo con `mqseries_conn`

```
<?php
    mqseries_conn('WMQ1', $conn, $comp_code, $reason);
    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("conn CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
        exit;
    }
?>

   
```php

## Véase también

mqseries_disc
