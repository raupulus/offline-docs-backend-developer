---
title: snmprealwalk
description: Devuelve todos los objetos, incluyendo los identificadores respectivos
  incluidos en el objeto
source_url: https://www.php.net/manual/es/function.snmprealwalk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmprealwalk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74880
---

snmprealwalk

Devuelve todos los objetos, incluyendo los identificadores respectivos incluidos en el objeto

## Descripción

```php
snmprealwalk(string $hostname, string $community, array $object_id, [int $timeout], [int $retries]): array
```php

La función `snmprealwalk` se utiliza para recorrer objetos SNMP, comenzando en el objeto identificado por `object_id` y devuelve no solo los valores sino también los identificadores de los objetos.

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
El número de intentos en caso de que ocurra el tiempo límite.

## Valores devueltos

Devuelve un array asociativo de identificadores de objetos SNMP así como sus valores en caso de éxito o `false` si ocurre un error. En caso de error, se emitirá una alerta de tipo E_WARNING.

## Ejemplos

Ejemplo con `snmprealwalk`

```
<?php
 print_r(snmprealwalk("localhost", "public", "IF-MIB::ifName"));
?>

   
```php

El código anterior producirá una salida similar a: Array ( \[IF-MIB::ifName.1\] =\> STRING: lo \[IF-MIB::ifName.2\] =\> STRING: eth0 \[IF-MIB::ifName.3\] =\> STRING: eth2 \[IF-MIB::ifName.4\] =\> STRING: sit0 \[IF-MIB::ifName.5\] =\> STRING: sixxs )

## Véase también

snmpwalk
