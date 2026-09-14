---
title: mqseries_begin
description: MQseries MQBEGIN
source_url: https://www.php.net/manual/es/function.mqseries-begin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-begin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51830
---

mqseries_begin

MQseries MQBEGIN

## Descripción

```php
mqseries_begin(resource $hconn, array $beginOptions, resource $compCode, resource $reason): void
```php

`mqseries_begin` inicia una unidad de trabajo, coordinada por el gestor de colas, e involucrando finalmente gestores de recursos externos.

Al utilizar `mqseries_begin` se inicia una unidad de trabajo. Finalmente, `mqseries_back` o `mqseries_cmit` terminarán la unidad de trabajo.

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

Ejemplo con `mqseries_begin`

```
<?php
    $mqbo = array();
    mqseries_begin( $conn,
                    $mqbo,
                    $comp_code,
                    $reason);
    if ($comp_code !== MQSERIES_MQCC_OK) {
        /* reason code 2121 es una advertencia, para más información ver el manual de referencia de MQSeries.*/
        if ($reason !== 2121) {
            printf("CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
        }
    }
?>

   
```php

## Notas

> [!NOTE]
> `mqseries_begin` no funciona cuando un cliente MQSeries Client se conecta al gestor de colas.

## Véase también

mqseries_conn

mqseries_connx

mqseries_back

mqseries_cmit
