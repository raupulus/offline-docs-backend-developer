---
title: snmp2_get
description: Recupera un objeto SNMP
source_url: https://www.php.net/manual/es/function.snmp2-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp2-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: dd22c7821
order: 74760
---

snmp2_get

Recupera un objeto

SNMP

## Descripción

```php
snmp2_get(string $hostname, string $community, array $object_id, [int $timeout], [int $retries]): mixed
```php

La función `snmp2_get` se utiliza para leer el valor de un objeto SNMP especificado por el parámetro `object_id`.

## Parámetros

`hostname`  
El agente SNMP.

`community`  
La comunidad de lectura.

`object_id`  
El identificador del objeto SNMP.

`timeout`  
El número de microsegundos antes del primer tiempo límite.

`retries`  
El número de intentos en caso de que ocurra el tiempo límite.

## Valores devueltos

Devuelve el valor del objeto SNMP en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza un ValueError cuando la longitud del nombre de host es igual o mayor a 128 bytes, cuando el puerto es negativo o mayor que 65535, o cuando los valores de timeout o reintentos son menores a -1 o demasiado grandes. |

## Ejemplos

Ejemplo con `snmp2_get`

```
<?php
$syscontact = snmp2_get("127.0.0.1", "public", "system.SysContact.0");
?>

   
```php

## Véase también

snmp2_set
