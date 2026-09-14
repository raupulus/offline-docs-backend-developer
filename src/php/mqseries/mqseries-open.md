---
title: mqseries_open
description: MQSeries MQOPEN
source_url: https://www.php.net/manual/es/function.mqseries-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51910
---

mqseries_open

MQSeries MQOPEN

## Descripción

```php
mqseries_open(resource $hconn, array $objDesc, int $option, resource $hobj, resource $compCode, resource $reason): void
```php

`mqseries_open` establece el acceso a un objeto.

## Parámetros

`hConn`  
Gestor de conexión.

Este recurso representa la conexión al gestor de colas.

`objDesc`  
Recurso de objeto.

`options`  
Opciones que controlan las acciones de la función.

`hObj`  
Gestor de objeto.

Este recurso representa el objeto a utilizar.

`compCode`  
Código de finalización.

`reason`  
La razón que califica el compCode.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `mqseries_open`

```
<?php
    $mqods = array('ObjectName' => 'TESTQ');
    mqseries_open(
                $conn,
                $mqods,
                MQSERIES_MQOO_INPUT_AS_Q_DEF | MQSERIES_MQOO_FAIL_IF_QUIESCING | MQSERIES_MQOO_OUTPUT,
                $obj,
                $comp_code,
                $reason);
    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("open CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
        exit;
    }
?>

   
```php

## Véase también

mqseries_close
