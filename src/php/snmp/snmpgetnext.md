---
title: snmpgetnext
description: Recupera un objeto SNMP que sigue inmediatamente al objeto proporcionado
source_url: https://www.php.net/manual/es/function.snmpgetnext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmpgetnext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 74870
---

snmpgetnext

Recupera un objeto

SNMP

que sigue inmediatamente al objeto proporcionado

## Descripción

```php
snmpgetnext(string $hostname, string $community, array $object_id, [int $timeout], [int $retries]): mixed
```php

La función `snmpgetnext` se utiliza para leer el valor de un objeto SNMP que sigue inmediatamente al objeto cuyo identificador es especificado por el parámetro `object_id`.

## Parámetros

`hostname`  
El nombre del host del agente SNMP (servidor).

`community`  
La comunidad de lectura.

`object_id`  
El identificador del objeto SNMP que precede al deseado.

`timeout`  
El número de microsegundos antes del primer tiempo límite.

`retries`  
El número de intentos en caso de que ocurra un tiempo límite.

## Valores devueltos

Devuelve el valor del objeto SNMP en caso de éxito o `false` si ocurre un error. En caso de error, se emitirá una alerta de tipo E_WARNING.

## Ejemplos

Ejemplo con `snmpgetnext`

```
<?php
$nameOfSecondInterface = snmpgetnext('localhost', 'public', 'IF-MIB::ifName.1');
?>

   
```php

## Véase también

snmpget

snmpwalk
