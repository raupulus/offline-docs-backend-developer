---
title: mqseries_put
description: MQSeries MQPUT
source_url: https://www.php.net/manual/es/function.mqseries-put.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-put.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51920
---

mqseries_put

MQSeries MQPUT

## Descripción

```php
mqseries_put(resource $hConn, resource $hObj, array $md, array $pmo, string $message, resource $compCode, resource $reason): void
```php

`mqseries_put` añade un mensaje a una cola o a una lista de distribución. La cola o la lista de distribución deben estar abiertas.

## Parámetros

`hConn`  
Gestor de conexión.

Esta referencia representa la conexión al gestor de colas.

`hObj`  
Gestor de objeto.

Esta referencia representa el objeto a utilizar.

`md`  
Recurso de mensaje (MQMD).

`pmo`  
Opción de adición de mensaje.

`message`  
El mensaje a colocar en la cola.

`compCode`  
Código de finalización.

`reason`  
La razón que califica el compCode.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `mqseries_put`

```
<?php
// Abre una conexión hacia el gestor de colas
    mqseries_conn('WMQ1', $conn, $comp_code, $reason);
// $conn contiene ahora la referencia a la conexión al gestor de colas.

// Abre la conexión hacia la cola testq
    mqseries_open(
                $conn,
                array('ObjectName' => 'TESTQ'),
                MQSERIES_MQOO_INPUT_AS_Q_DEF | MQSERIES_MQOO_FAIL_IF_QUIESCING | MQSERIES_MQOO_OUTPUT,
                $obj,
                $comp_code,
                $reason);
// $obj contiene ahora la referencia al objeto (TESTQ)

// Define el array de descripción del mensaje. Verifica manualmente las referencias a MQSeries.
    $md = array(
                'Version' => MQSERIES_MQMD_VERSION_1,
                'Expiry' => MQSERIES_MQEI_UNLIMITED,
                'Report' => MQSERIES_MQRO_NONE,
                'MsgType' => MQSERIES_MQMT_DATAGRAM,
                'Format' => MQSERIES_MQFMT_STRING,
                'Priority' => 1,
                'Persistence' => MQSERIES_MQPER_PERSISTENT);

// Define las opciones de transmisión de mensajes.
    $pmo = array('Options' => MQSERIES_MQPMO_NEW_MSG_ID|MQSERIES_MQPMO_SYNCPOINT);

// Coloca el mensaje 'Ping' en la cola.
    mqseries_put($conn, $obj, $md, $pmo, 'Ping', $comp_code, $reason);

    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("put CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
    }

// Cierra la referencia al objeto $obj
    mqseries_close($conn, $obj, MQSERIES_MQCO_NONE, $comp_code, $reason);

// Desconecta el gestor de colas.
    mqseries_disc($conn, $comp_code, $reason);

?>

   
```php

## Véase también

mqseries_conn

mqseries_connx

mqseries_open

mqseries_get
