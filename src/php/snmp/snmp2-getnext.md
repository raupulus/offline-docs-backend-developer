---
title: snmp2_getnext
description: Recupera el objeto SNMP que sigue inmediatamente al identificador del
  objeto proporcionado
source_url: https://www.php.net/manual/es/function.snmp2-getnext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp2-getnext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74770
---

snmp2_getnext

Recupera el objeto

SNMP

que sigue inmediatamente al identificador del objeto proporcionado

## Descripción

```php
snmp2_getnext(string $hostname, string $community, array $object_id, [int $timeout], [int $retries]): mixed
```php

La función `snmp2_get_next` se utiliza para leer el valor del objeto SNMP que sigue inmediatamente al objeto `object_id` especificado.

## Parámetros

`hostname`  
El nombre de host del agente SNMP (servidor).

`community`  
La comunidad de lectura.

`object_id`  
El identificador del objeto SNMP que precede al deseado.

`timeout`  
El número de microsegundos antes del primer tiempo límite.

`retries`  
El número de intentos en caso de que ocurra un tiempo límite.

## Valores devueltos

Devuelve el valor del objeto SNMP en caso de éxito, o `false` si ocurre un error. En caso de error, se emitirá una alerta de tipo E_WARNING.

## Ejemplos

Ejemplo con `snmp2_get_next`

```
<?php
$nameOfSecondInterface = snmp2_get_next('localhost', 'public', 'IF-MIB::ifName.1');
?>

   
```php

## Véase también

snmp2_get

snmp2_walk
