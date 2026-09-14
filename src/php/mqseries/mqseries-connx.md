---
title: mqseries_connx
description: MQSeries MQCONNX
source_url: https://www.php.net/manual/es/function.mqseries-connx.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-connx.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: true
translation_revision: b5efbef2d
order: 51870
---

mqseries_connx

MQSeries MQCONNX

## Descripción

```php
mqseries_connx(string $qManagerName, array $connOptions, resource $hconn, resource $compCode, resource $reason): void
```php

La llamada a `mqseries_connx` (MQCONNX) conecta un programa de aplicación a un gestor de colas. Proporciona un descriptor de conexión del gestor de colas, que es utilizado por la aplicación en llamadas MQ posteriores.

La llamada a `mqseries_connx` es como la llamada a `mqseries_conn` (MQCONN), con la excepción de que MQCONNX permite especificar opciones para controlar el funcionamiento de la llamada.

## Parámetros

`qManagerName`  
Nombre del gestor de colas.

Nombre del gestor de colas con el que la aplicación desea conectarse.

`connOps`  
Opciones que controlan las acciones de la función

Véase también la estructura MQCNO.

`hConn`  
Gestor de conexión.

Este gestor representa la conexión al gestor de colas.

`compCode`  
Código de finalización.

`reason`  
La razón que califica el compCode.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `mqseries_connx`

```
<?php
    $mqcno = array(
        'Version' => MQSERIES_MQCNO_VERSION_2,
        'Options' => MQSERIES_MQCNO_STANDARD_BINDING,
        'MQCD' => array('ChannelName' => 'MQNX9420.CLIENT',
        'ConnectionName' => 'localhost',
        'TransportType' => MQSERIES_MQXPT_TCP)
    );

    mqseries_connx('MQNX9420', $mqcno, $conn, $comp_code,$reason);
    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("Connx CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
        exit;
    }

?>

    
```php

Ejemplo con `mqseries_connx` utilizando una conexión SSL y una URL OCSP Responder

```
<?php
    $mqcno = array(
        'Version' => 4, //MQCNO_VERSION_4
        'Options' => MQSERIES_MQCNO_STANDARD_BINDING,
        'MQCD' => array(
            'Version' => 7, //MQCD_VERSION_7
            'ConnectionName' => 'localhost',
            'TransportType' => MQSERIES_MQXPT_TCP,
            'ChannelName' => 'CONNECTIONCHANNEL',
            'SSLCipherSpec' => 'NULL_SHA'
        ),
        'MQSCO' => array(
            'KeyRepository' => '/var/mqm/qmgrs/QUEUEMGR/ssl/key', //Ruta local donde se puede encontrar la carpeta que contiene la clave SSL
            'MQAIR' => array(
                'Version' => 2, //MQAIR_VERSION_2
                'AuthInfoType' => 2, //MQAIT_OCSP
                'OCSPResponderURL' => 'http://dummy.OCSP.responder'
            )
        )
    );

    mqseries_connx('QUEUEMGR', $mqcno, $conn, $comp_code,$reason);
    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("Connx CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
        exit;
    }

?>

    
```php

## Véase también

mqseries_disc
