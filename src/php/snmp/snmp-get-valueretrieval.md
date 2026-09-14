---
title: snmp_get_valueretrieval
description: Devuelve el método con el cual los valores SNMP serán devueltos
source_url: https://www.php.net/manual/es/function.snmp-get-valueretrieval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp-get-valueretrieval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74690
---

snmp_get_valueretrieval

Devuelve el método con el cual los valores SNMP serán devueltos

## Descripción

```php
snmp_get_valueretrieval(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una combinación de constantes ( `SNMP_VALUE_LIBRARY` o `SNMP_VALUE_PLAIN` ) con eventualmente una definición de SNMP_VALUE_OBJECT.

## Ejemplos

Ejemplo con `snmp_get_valueretrieval`

```
<?php
 $ret = snmpget('localhost', 'public', 'IF-MIB::ifName.1');
 if (snmp_get_valueretrieval() & SNMP_VALUE_OBJECT) {
   echo $ret->value;
 } else {
   echo $ret;
 }
?>

   
```php

## Véase también

snmp_set_valueretrieval
