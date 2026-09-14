---
title: snmpwalk
description: Recibe todos los objetos SNMP de un agente
source_url: https://www.php.net/manual/es/function.snmpwalk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmpwalk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74900
---

snmpwalk

Recibe todos los objetos

SNMP

de un agente

## Descripción

```php
snmpwalk(string $hostname, string $community, array $object_id, [int $timeout], [int $retries]): array
```php

`snmpwalk` se utiliza para leer todos los valores de un agente SNMP especificado por `hostname`.

## Parámetros

`hostname`  
El agente SNMP (servidor).

`community`  
La comunidad de lectura.

`object_id`  
Si `null`, `object_id` se toma como raíz de los objetos SNMP y todos los objetos de este árbol se devuelven en forma de array.

Si `object_id` está especificado, todos los objetos SNMP que siguen a este `object_id` se devuelven.

`timeout`  
El número de microsegundos desde el primer timeout.

`retries`  
El número de intentos en caso de que ocurra el tiempo límite.

## Valores devueltos

Devuelve un array de valores del objeto SNMP, comenzando por `object_id` o `false` si ocurre un error.

## Ejemplos

Ejemplo con `snmpwalk`

```
<?php
$a = snmpwalk("127.0.0.1", "public", "");

foreach ($a as $val) {
    echo "$val\n";
}

?>

   
```php

La llamada a la función anterior devolverá todos los objetos SNMP desde el agente SNMP ejecutado en el host local. Se recorren los valores mediante un bucle.

## Véase también

snmprealwalk
