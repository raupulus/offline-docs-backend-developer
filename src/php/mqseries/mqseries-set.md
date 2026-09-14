---
title: mqseries_set
description: MQSeries MQSET
source_url: https://www.php.net/manual/es/function.mqseries-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: true
translation_revision: b5efbef2d
order: 51940
---

mqseries_set

MQSeries MQSET

## Descripción

```php
mqseries_set(resource $hConn, resource $hObj, int $selectorCount, array $selectors, int $intAttrCount, array $intAttrs, int $charAttrLength, array $charAttrs, resource $compCode, resource $reason): void
```php

La llamada a `mqseries_set` (MQSET) se utiliza para modificar los atributos de un objeto representado por un manejador. El objeto debe ser una cola.

## Parámetros

`hConn`  
Manejador de conexión.

Este manejador representa la conexión al gestor de colas.

`hObj`  
Manejador de objeto.

Este manejador representa el objeto a utilizar.

`selectorCount`  
Conteo de selectores.

`selectors`  
Array de atributos de los selectores.

`intAttrCount`  
Conteo de atributos enteros.

`intAttrs`  
Array de atributos enteros.

`charAttrLength`  
Longitud del búfer de atributos de caracteres.

`charAttrs`  
Atributos de caracteres.

`compCode`  
Código de finalización.

`reason`  
La razón que califica el compCode.

## Valores devueltos

No se retorna ningún valor.

## Véase también

mqseries_inq
