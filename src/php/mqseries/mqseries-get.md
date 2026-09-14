---
title: mqseries_get
description: MQSeries MQGET
source_url: https://www.php.net/manual/es/function.mqseries-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51890
---

mqseries_get

MQSeries MQGET

## Descripción

```php
mqseries_get(resource $hConn, resource $hObj, array $md, array $gmo, int $bufferLength, string $msg, int $data_length, resource $compCode, resource $reason): void
```php

`mqseries_get` lee un mensaje de una cola local, que ha sido abierta con la función `mqseries_open`.

## Parámetros

`hConn`  
Gestor de conexión.

Este recurso representa la conexión al gestor de colas.

`hObj`  
Gestor de objeto.

Este recurso representa el objeto a utilizar.

`md`  
Recurso de mensaje (MQMD).

`gmo`  
Opciones de mensaje

`bufferLength`  
Tamaño esperado del buffer de resultado

`msg`  
Buffer que contiene el mensaje leído desde el objeto.

`data_length`  
Tamaño real del buffer

`compCode`  
Código de finalización.

`reason`  
La razón que califica el compCode.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `mqseries_get`

```
<?php
// Abre la conexión hacia el gestor de colas
    mqseries_conn('WMQ1', $conn, $comp_code, $reason);
// $conn contiene ahora la referencia a la conexión al gestor de colas.

// Abre la conexión hacia la cola de prueba testq
    mqseries_open(
                $conn,
                array('ObjectName' => 'TESTQ'),
                MQSERIES_MQOO_INPUT_AS_Q_DEF | MQSERIES_MQOO_FAIL_IF_QUIESCING | MQSERIES_MQOO_OUTPUT,
                $obj,
                $comp_code,
                $reason);
// $obj contiene ahora la referencia al objeto (TESTQ)

// Define un descriptor de mensaje vacío.
    $mdg = array();
// Define las opciones de recuperación de mensajes
    $gmo = array('Options' => MQSERIES_MQGMO_FAIL_IF_QUIESCING | MQSERIES_MQGMO_WAIT, 'WaitInterval' => 3000);

// Recupera los mensajes desde la cola
    mqseries_get($conn, $obj, $mdg, $gmo, 255, $msg, $data_length, $comp_code, $reason);
    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("GET CompCode:%d Reason:%d Text:%s<br>", $comp_code, $reason, mqseries_strerror($reason));
    }

// Cierra la referencia al objeto $obj
    mqseries_close($conn, $obj, MQSERIES_MQCO_NONE, $comp_code, $reason);

// Desconecta del gestor de colas
    mqseries_disc($conn, $comp_code, $reason);

?>

   
```php

## Véase también

mqseries_conn

mqseries_connx

mqseries_open

mqseries_put
