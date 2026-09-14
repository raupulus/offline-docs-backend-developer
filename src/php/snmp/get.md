---
title: SNMP::get
description: Recupera un objeto SNMP
source_url: https://www.php.net/manual/es/snmp.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 74950
---

SNMP::get

Recupera un objeto

SNMP

## Descripción

```php
public SNMP::get(array $objectId, [bool $preserveKeys]): mixed
```php

Recupera un objeto SNMP especificado por el identificador `objectId` utilizando una solicitud GET.

## Parámetros

Si `objectId` es una `string`, entonces SNMP::get devolverá un objeto SNMP en forma de `string`. Si `objectId` es un array, todos los objetos SNMP solicitados serán devueltos en forma de array asociativo de identificadores de objetos SNMP y sus valores.

`objectId`  
El o los objetos SNMP (OID)

`preserve_keys`  
Cuando `objectId` es un array, y el parámetro `preserve_keys` está definido a `true`, las claves en el resultado serán tomadas exactamente del objeto `objectId`, de lo contrario, la propiedad `SNMP::oid_output_format` será utilizada para determinar el formato de las claves.

## Valores devueltos

Devuelve los objetos SNMP solicitados, en forma de strings o arrays, según el tipo del parámetro `objectId`, o `false` si ocurre un error.

## Errores/Excepciones

Este método no lanza excepciones por defecto. Para activar el lanzamiento de excepciones SNMPException cuando ocurren errores de la biblioteca, el parámetro de la clase SNMP `exceptions_enabled` ebe ser definido al valor correspondiente. Ver las [ explicaciones sobre `SNMP::$exceptions_enabled`](#snmp.props.exceptions-enabled) para más detalles.

## Ejemplos

Un solo objeto SNMP

Un solo objeto SNMP puede ser solicitado de 2 maneras: en forma de `string`, devolviendo así un valor en forma de `string` también, o un array conteniendo un solo elemento, devolviendo así un array asociativo.

```
<?php
  $session = new SNMP(SNMP_VERSION_1, "127.0.0.1", "public");
  $sysdescr = $session->get("sysDescr.0");
  echo "$sysdescr\n";
  $sysdescr = $session->get(array("sysDescr.0"));
  print_r($sysdescr);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    STRING: Test server
    Array
    (
        [SNMPv2-MIB::sysDescr.0] => STRING: Test server
    )

Varios objetos SNMP

```
  $session = new SNMP(SNMP_VERSION_1, "127.0.0.1", "public");
  $results = $session->get(array("sysDescr.0", "sysName.0"));
  print_r($results);
  $session->close();

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [SNMPv2-MIB::sysDescr.0] => STRING: Test server
        [SNMPv2-MIB::sysName.0] => STRING: myhost.nodomain
    )

## Véase también

SNMP::getErrno

SNMP::getError
