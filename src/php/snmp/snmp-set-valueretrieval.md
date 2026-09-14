---
title: snmp_set_valueretrieval
description: Especifica el método con el cual los valores SNMP serán devueltos
source_url: https://www.php.net/manual/es/function.snmp-set-valueretrieval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp-set-valueretrieval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74750
---

snmp_set_valueretrieval

Especifica el método con el cual los valores SNMP serán devueltos

## Descripción

```php
snmp_set_valueretrieval(int $method): true
```php

## Parámetros

`method`  
|  |  |
|----|----|
| SNMP_VALUE_LIBRARY | Los valores devueltos serán aquellos devueltos por la biblioteca Net-SNMP. |
| SNMP_VALUE_PLAIN | Los valores devueltos serán brutos, sin la información del tipo SNMP. |
| SNMP_VALUE_OBJECT | Los valores devueltos serán objetos con las propiedades `value` y `type`, donde la segunda es una de las constantes `SNMP_OCTET_STR`, `SNMP_COUNTER` etc. La forma en que la `value` es devuelta se basa en el uso de la constante `SNMP_VALUE_LIBRARY` o de la constante `SNMP_VALUE_PLAIN`. |

Tipos

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `snmp_set_valueretrieval`

```
<?php
 snmp_set_valueretrieval(SNMP_VALUE_LIBRARY);
 $ret = snmpget('localhost', 'public', 'IF-MIB::ifName.1');
 // $ret = "STRING: lo"

 snmp_set_valueretrieval(SNMP_VALUE_PLAIN);
 $ret = snmpget('localhost', 'public', 'IF-MIB::ifName.1');
 // $ret = "lo";

 snmp_set_valueretrieval(SNMP_VALUE_OBJECT);
 $ret = snmpget('localhost', 'public', 'IF-MIB::ifName.1');
 // stdClass Object
 // (
 //   [type] => 4        <-- SNMP_OCTET_STR, ver las constantes
 //   [value] => lo
 // )

 snmp_set_valueretrieval(SNMP_VALUE_OBJECT | SNMP_VALUE_PLAIN);
 $ret = snmpget('localhost', 'public', 'IF-MIB::ifName.1');
 // stdClass Object
 // (
 //   [type] => 4        <-- SNMP_OCTET_STR, ver las constantes
 //   [value] => lo
 // )

 snmp_set_valueretrieval(SNMP_VALUE_OBJECT | SNMP_VALUE_LIBRARY);
 $ret = snmpget('localhost', 'public', 'IF-MIB::ifName.1');
 // stdClass Object
 // (
 //   [type] => 4        <-- SNMP_OCTET_STR, ver las constantes
 //   [value] => STRING: lo
 // )

?>

   
```php

## Véase también

snmp_get_valueretrieval
