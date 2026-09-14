---
title: mqseries_close
description: MQSeries MQCLOSE
source_url: https://www.php.net/manual/es/function.mqseries-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51840
---

mqseries_close

MQSeries MQCLOSE

## Descripción

```php
mqseries_close(resource $hconn, resource $hobj, int $options, resource $compCode, resource $reason): void
```php

`mqseries_close` libera el acceso a un objeto y es la operación inversa de la función `mqseries_open`.

## Parámetros

`hConn`  
Gestor de conexión.

Este recurso representa la conexión al gestor de colas.

`hObj`  
Gestor de objeto.

Este recurso representa el objeto a utilizar.

`options`  

`compCode`  
Código de finalización.

`reason`  
La razón que califica el compCode.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `mqseries_close`

```
<?php
    mqseries_close($conn, $obj, MQSERIES_MQCO_NONE, $comp_code, $reason);
    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("close CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
    }
?>

   
```php

## Véase también

mqseries_open

mqseries_conn

mqseries_connx
