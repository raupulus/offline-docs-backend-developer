---
title: snmp2_real_walk
description: Devuelve todos los objetos incluyendo los identificadores de sus respectivos
  objetos
source_url: https://www.php.net/manual/es/function.snmp2-real-walk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp2-real-walk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74780
---

snmp2_real_walk

Devuelve todos los objetos incluyendo los identificadores de sus respectivos objetos

## Descripción

```php
snmp2_real_walk(string $hostname, string $community, array $object_id, [int $timeout], [int $retries]): array
```php

La función `snmp2_real_walk` se utiliza para recorrer un número de objetos SNMP comenzando por el objeto identificado por `object_id` y devuelve no solo sus valores, sino también los identificadores de sus objetos.

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
El número de intentos en caso de que el tiempo límite ocurra.

## Valores devueltos

Devuelve un array asociativo de identificadores de objetos SNMP así como sus valores en caso de éxito o `false` si ocurre un error. En caso de error, se emitirá una alerta de tipo E_WARNING.

## Ejemplos

Ejemplo con `snmp2_real_walk`

```
<?php
 print_r(snmp2_real_walk("localhost", "public", "IF-MIB::ifName"));
?>

   
```php

El ejemplo anterior mostrará algo como: Array ( \[IF-MIB::ifName.1\] =\> STRING: lo \[IF-MIB::ifName.2\] =\> STRING: eth0 \[IF-MIB::ifName.3\] =\> STRING: eth2 \[IF-MIB::ifName.4\] =\> STRING: sit0 \[IF-MIB::ifName.5\] =\> STRING: sixxs )

## Véase también

snmp2_walk
