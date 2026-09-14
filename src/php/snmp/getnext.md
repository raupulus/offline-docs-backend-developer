---
title: SNMP::getnext
description: Recupera un objeto SNMP que sigue al identificador de objeto proporcionado
source_url: https://www.php.net/manual/es/snmp.getnext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp/getnext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 74980
---

SNMP::getnext

Recupera un objeto

SNMP

que sigue al identificador de objeto proporcionado

## Descripción

```php
public SNMP::getnext(array $objectId): mixed
```php

Recupera un objeto SNMP que sigue al objeto especificado por el argumento `objectId`.

## Parámetros

Si `objectId` es una `string`, entonces SNMP::getnext devolverá un objeto SNMP en forma de `string`. Si `objectId` es un array, todos los objetos SNMP solicitados serán devueltos en forma de un array asociativo de identificadores de objetos SNMP así como sus valores.

`objectId`  
El o los objetos SNMP (OID).

## Valores devueltos

Devuelve los objetos SNMP solicitados en forma de una `string` o de un array, según el tipo del argumento `objectId` o `false` si ocurre un error.

## Errores/Excepciones

Este método no lanza excepciones por defecto. Para activar el lanzamiento de excepciones SNMPException cuando ocurren errores de la biblioteca, el parámetro de la clase SNMP `exceptions_enabled` ebe ser definido al valor correspondiente. Ver las [ explicaciones sobre `SNMP::$exceptions_enabled`](#snmp.props.exceptions-enabled) para más detalles.

## Ejemplos

Un solo objeto SNMP

Un solo objeto SNMP puede ser solicitado de 2 maneras: como una cadena, devolviendo así un valor en forma de cadena, o como un array que contiene solo un elemento, devolviendo así un array asociativo.

```
<?php
  $session = new SNMP(SNMP_VERSION_1, "127.0.0.1", "public");
  $nsysdescr = $session->getnext("sysDescr.0");
  echo "$nsysdescr\n";
  $nsysdescr = $session->getnext(array("sysDescr.0"));
  print_r($nsysdescr);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    OID: NET-SNMP-MIB::netSnmpAgentOIDs.8
    Array
    (
        [SNMPv2-MIB::sysObjectID.0] => OID: NET-SNMP-MIB::netSnmpAgentOIDs.8
    )

Varios objetos SNMP

```
<?php
  $session = new SNMP(SNMP_VERSION_1, "127.0.0.1", "public");
  $results = $session->getnext(array("sysDescr.0", "sysName.0"));
  print_r($results);
  $session->close();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [SNMPv2-MIB::sysObjectID.0] => OID: NET-SNMP-MIB::netSnmpAgentOIDs.8
        [SNMPv2-MIB::sysLocation.0] => STRING: Nowhere
    )

## Véase también

SNMP::getErrno

SNMP::getError
