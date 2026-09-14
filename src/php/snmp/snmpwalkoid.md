---
title: snmpwalkoid
description: Solicitud de información de árbol sobre una entidad de la red
source_url: https://www.php.net/manual/es/function.snmpwalkoid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmpwalkoid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74910
---

snmpwalkoid

Solicitud de información de árbol sobre una entidad de la red

## Descripción

```php
snmpwalkoid(string $hostname, string $community, array $object_id, [int $timeout], [int $retries]): array
```php

`snmpwalkoid` se utiliza para leer todos los identificadores de objetos así como sus valores respectivos desde el agente SNMP especificado por `hostname`.

La existencia de `snmpwalkoid` y `snmpwalk` tiene razones históricas. Ambas funciones proporcionan compatibilidades ascendentes. Utilice en su lugar la función `snmprealwalk`.

## Parámetros

`hostname`  
El agente SNMP.

`community`  
La comunidad de lectura.

`object_id`  
Si `null`, `object_id` se toma como raíz de los objetos SNMP y todos los objetos de este árbol se devuelven en forma de array.

Si `object_id` se especifica, todos los objetos SNMP siguientes a este `object_id` se devuelven.

`timeout`  
El número de microsegundos desde el primer timeout.

`retries`  
El número de intentos en caso de que ocurra el tiempo límite máximo.

## Valores devueltos

Devuelve un array asociativo que contiene los identificadores de los objetos así como sus valores respectivos, a partir de `object_id`, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `snmpwalkoid`

```
<?php
$a = snmpwalkoid("127.0.0.1", "public", "");
for (reset($a); $i = key($a); next($a)) {
    echo "$i: $a[$i]<br />\n";
}
?>

   
```php

La llamada a la función anterior devolverá todos los objetos SNMP desde el agente SNMP ejecutado en el host local. Se recorren los valores mediante un bucle.

## Véase también

snmpwalk
