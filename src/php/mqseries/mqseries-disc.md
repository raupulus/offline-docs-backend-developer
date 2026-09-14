---
title: mqseries_disc
description: MQSeries MQDISC
source_url: https://www.php.net/manual/es/function.mqseries-disc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-disc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51880
---

mqseries_disc

MQSeries MQDISC

## Descripción

```php
mqseries_disc(resource $hconn, resource $compCode, resource $reason): void
```php

`mqseries_disc` cierra la conexión entre el gestor de colas y la aplicación. Es lo opuesto a `mqseries_conn` y `mqseries_connx`.

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

Ejemplo con `mqseries_disc`

```
<?php
    mqseries_disc($conn, $comp_code, $reason);
    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("disc CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
    }
?>

   
```php

## Véase también

mqseries_conn

mqseries_connx
