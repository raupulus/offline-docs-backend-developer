---
title: snmpget
description: Recibe un objeto SNMP
source_url: https://www.php.net/manual/es/function.snmpget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmpget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: dd22c7821
order: 74860
---

snmpget

Recibe un objeto

SNMP

## Descripción

```php
snmpget(string $hostname, string $community, array $object_id, [int $timeout], [int $retries]): mixed
```php

`snmpget` se utiliza para leer un valor de un objeto SNMP representado por `object_id`.

## Parámetros

`hostname`  
El agente SNMP.

`community`  
La comunidad de lectura.

`object_id`  
El objeto SNMP.

`timeout`  
El número de microsegundos desde el primer timeout.

`retries`  
El número de intentos cuando ocurre el tiempo límite máximo de espera.

## Valores devueltos

Devuelve el valor del objeto SNMP en caso de éxito, `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza un ValueError cuando la longitud del nombre de host es igual o mayor a 128 bytes, cuando el puerto es negativo o mayor que 65535, o cuando los valores de timeout o reintentos son menores a -1 o demasiado grandes. |

## Ejemplos

Ejemplo con `snmpget`

```
<?php
$syscontact = snmpget("127.0.0.1", "public", "system.SysContact.0");
?>

   
```php

## Véase también

snmpset
