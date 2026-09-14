---
title: mqseries_inq
description: MQSeries MQINQ
source_url: https://www.php.net/manual/es/function.mqseries-inq.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-inq.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51900
---

mqseries_inq

MQSeries MQINQ

## Descripción

```php
mqseries_inq(resource $hconn, resource $hobj, int $selectorCount, array $selectors, int $intAttrCount, resource $intAttr, int $charAttrLength, resource $charAttr, resource $compCode, resource $reason): void
```php

`mqseries_inq` devuelve un array de enteros y un conjunto de strings que representan un objeto.

## Parámetros

`hConn`  
Gestor de conexión.

Este recurso representa la conexión al gestor de colas.

`hObj`  
Gestor de objeto.

Este recurso representa el objeto a utilizar.

`selectorCount`  
Número de selectores.

`selectors`  
Array de atributos de selectores.

`intAttrLength`  
Número de atributos enteros.

`intAttr`  
Array de atributos enteros.

`charAttrLength`  
Tamaño del buffer de atributos de carácter.

`charAttr`  
Atributo de carácter.

`compCode`  
Código de finalización.

`reason`  
La razón que califica el compCode.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `mqseries_inq`

```
<?php
    $int_attr = array();
    $char_attr = "";

    mqseries_inq($conn, $obj, 1, array(MQSERIES_MQCA_Q_MGR_NAME), 0, $int_attr, 48, $char_attr, $comp_code, $reason);

    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("INQ CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
    } else {
        echo "INQ QManager name result ".$char_attr."<br>\n";
    }
?>

   
```php

## Véase también

mqseries_conn

mqseries_connx

mqseries_open
