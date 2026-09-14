---
title: snmp_set_oid_output_format
description: Define el formato de salida OID
source_url: https://www.php.net/manual/es/function.snmp-set-oid-output-format.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp-set-oid-output-format.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74730
---

snmp_set_oid_output_format

Define el formato de salida OID

## Descripción

```php
snmp_set_oid_output_format(int $format): true
```php

`snmp_set_oid_output_format` define el formato de salida para que sea completo o numérico.

## Parámetros

`format`  
|  |  |
|----|----|
| `SNMP_OID_OUTPUT_FULL` | .iso.org.dod.internet.mgmt.mib-2.system.sysUpTime.sysUpTimeInstance |
| `SNMP_OID_OUTPUT_NUMERIC` | .1.3.6.1.2.1.1.3.0 |
| `SNMP_OID_OUTPUT_MODULE` | DISMAN-EVENT-MIB::sysUpTimeInstance |
| `SNMP_OID_OUTPUT_SUFFIX` | sysUpTimeInstance |
| `SNMP_OID_OUTPUT_UCD` | system.sysUpTime.sysUpTimeInstance |
| `SNMP_OID_OUTPUT_NONE` | Undefined |

Representación OID .1.3.6.1.2.1.1.3.0 para varios valores de `format`

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `snmprealwalk`

```
<?php

 snmp_read_mib("/usr/share/mibs/netsnmp/NET-SNMP-TC");

 // por omisión o SNMP_OID_OUTPUT_MODULE
 print_r( snmprealwalk('localhost', 'public', 'RFC1213-MIB::sysObjectID') );

 snmp_set_oid_output_format(SNMP_OID_OUTPUT_NUMERIC);
 print_r( snmprealwalk('localhost', 'public', 'RFC1213-MIB::sysObjectID') );

 snmp_set_oid_output_format(SNMP_OID_OUTPUT_FULL);
 print_r( snmprealwalk('localhost', 'public', 'RFC1213-MIB::sysObjectID') );
?>

   
```php

El ejemplo anterior mostrará: Array ( \[RFC1213-MIB::sysObjectID.0\] =\> OID: NET-SNMP-TC::linux ) Array ( \[.1.3.6.1.2.1.1.2.0\] =\> OID: .1.3.6.1.4.1.8072.3.2.10 ) Array ( \[.iso.org.dod.internet.mgmt.mib-2.system.sysObjectID.0\] =\> OID: .iso.org.dod.internet.private.enterprises.netSnmp.netSnmpEnumerations.netSnmpAgentOIDs.linux )
