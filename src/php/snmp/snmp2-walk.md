---
title: snmp2_walk
description: Recupera todos los objetos SNMP desde un agente
source_url: https://www.php.net/manual/es/function.snmp2-walk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp2-walk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74800
---

snmp2_walk

Recupera todos los objetos

SNMP

desde un agente

## Descripción

```php
snmp2_walk(string $hostname, string $community, array $object_id, [int $timeout], [int $retries]): array
```php

La función `snmp2_walk` se utiliza para leer todos los valores desde un agente SNMP especificado por el parámetro `hostname`.

## Parámetros

`hostname`  
El agente SNMP (servidor).

`community`  
La comunidad de lectura.

`object_id`  
Si `null`, `object_id` será la raíz del árbol de objetos SNMP y todos los objetos de este árbol serán devueltos en forma de un array.

Si `object_id` está especificado, todos los objetos SNMP bajo este `object_id` serán devueltos.

`timeout`  
El número de microsegundos antes del primer tiempo límite.

`retries`  
El número de intentos en caso de que ocurra un tiempo límite.

## Valores devueltos

Devuelve un array de valores de objeto SNMP comenzando por el objeto `object_id` o `false` si ocurre un error.

## Ejemplos

Ejemplo con `snmp2_walk`

```
<?php
$a = snmp2_walk("127.0.0.1", "public", "");

foreach ($a as $val) {
    echo "$val\n";
}

?>

   
```php

La función anterior debería devolver todos los objetos SNMP desde el agente SNMP funcionando localmente. Un paso siguiente recorre los valores con un bucle.

## Véase también

snmp2_real_walk
