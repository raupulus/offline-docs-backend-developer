---
title: SNMP::walk
description: Recupera el sub-objeto de un objeto SNMP
source_url: https://www.php.net/manual/es/snmp.walk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp/walk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 75010
---

SNMP::walk

Recupera el sub-objeto de un objeto

SNMP

## Descripción

```php
public SNMP::walk(array $objectId, [bool $suffixAsKey], [int $maxRepetitions], [int $nonRepeaters]): array
```php

SNMP::walk se utiliza para leer el sub-objeto SNMP cuya profundidad está especificada por el argumento `object_id`.

## Parámetros

`objectId`  
Raíz del sub-objeto a leer

`suffixAsKey`  
Por omisión, la notación completa del OID se utiliza para las claves en el array resultante. Si se establece en `true`, el prefijo del sub-objeto será eliminado de las claves, dejando solo el sufijo de object_id.

`nonRepeaters`  
Especifica el número de variables proporcionadas que no deben ser repetidas. Por omisión, este valor será utilizado desde el objeto SNMP.

`maxRepetitions`  
Especifica el número máximo de iteraciones sobre las variables repetidas. Por omisión, este valor será utilizado desde el objeto SNMP.

## Valores devueltos

Devuelve un array asociativo de identificadores de objetos SNMP así como sus valores en caso de éxito o `false` si ocurre un error. Cuando ocurre un error SNMP, SNMP::get_errno y SNMP::get_error pueden ser utilizadas para recuperar respectivamente el número del error (específico de la extensión SNMP, ver las constantes de la clase) así como el mensaje de error.

## Errores/Excepciones

Este método no lanza excepciones por defecto. Para activar el lanzamiento de excepciones SNMPException cuando ocurren errores de la biblioteca, el parámetro de la clase SNMP `exceptions_enabled` ebe ser definido al valor correspondiente. Ver las [ explicaciones sobre `SNMP::$exceptions_enabled`](#snmp.props.exceptions-enabled) para más detalles.

## Ejemplos

Ejemplo con SNMP::walk

```
<?php
  $session = new SNMP(SNMP_VERSION_1, "127.0.0.1", "public");
  $fulltree = $session->walk(".");
  print_r($fulltree);
  $session->close();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [SNMPv2-MIB::sysDescr.0] => STRING: Test server
        [SNMPv2-MIB::sysObjectID.0] => OID: NET-SNMP-MIB::netSnmpAgentOIDs.8
        [DISMAN-EVENT-MIB::sysUpTimeInstance] => Timeticks: (1150681750) 133 days, 4:20:17.50
        [SNMPv2-MIB::sysContact.0] => STRING: Nobody
        [SNMPv2-MIB::sysName.0] => STRING: server.localdomain
        ...
    )

Ejemplo con el argumento `suffixAsKey`

El argumento `suffixAsKey` puede ser utilizado al fusionar varios sub-objetos SNMP en uno solo. Este ejemplo enlaza los nombres de interfaces y sus tipos.

```
<?php
  $session = new SNMP(SNMP_VERSION_1, "127.0.0.1", "public");
  $session->valueretrieval = SNMP_VALUE_PLAIN;
  $ifDescr = $session->walk(".1.3.6.1.2.1.2.2.1.2", TRUE);
  $session->valueretrieval = SNMP_VALUE_LIBRARY;
  $ifType = $session->walk(".1.3.6.1.2.1.2.2.1.3", TRUE);
  print_r($ifDescr);
  print_r($ifType);
  $result = array();
  foreach($ifDescr as $i => $n) {
    $result[$n] = $ifType[$i];
  }
  print_r($result);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [1] => igb0
        [2] => igb1
        [3] => ipfw0
        [4] => lo0
        [5] => lagg0
    )
    Array
    (
        [1] => INTEGER: ieee8023adLag(161)
        [2] => INTEGER: ieee8023adLag(161)
        [3] => INTEGER: ethernetCsmacd(6)
        [4] => INTEGER: softwareLoopback(24)
        [5] => INTEGER: ethernetCsmacd(6)
    )
    Array
    (
        [igb0] => INTEGER: ieee8023adLag(161)
        [igb1] => INTEGER: ieee8023adLag(161)
        [ipfw0] => INTEGER: ethernetCsmacd(6)
        [lo0] => INTEGER: softwareLoopback(24)
        [lagg0] => INTEGER: ethernetCsmacd(6)
    )

## Véase también

SNMP::getErrno

SNMP::getError
