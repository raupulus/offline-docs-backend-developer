---
title: snmp_set_enum_print
description: Devuelve todos los valores que son enumeraciones con su valor de enumeración
  en lugar del entero
source_url: https://www.php.net/manual/es/function.snmp-set-enum-print.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp-set-enum-print.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74710
---

snmp_set_enum_print

Devuelve todos los valores que son enumeraciones con su valor de enumeración en lugar del entero

## Descripción

```php
snmp_set_enum_print(bool $enable): true
```php

Esta función permite alternar si snmpwalk/snmpget etc. debe buscar automáticamente los valores enumerados en el MIB y los devuelve con su string legible por humanos.

## Parámetros

`enable`  
Dado que el valor es interpretado como un bool por la biblioteca Net-SNMP, puede valer "0" o "1".

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `snmp_set_enum_print`

```
<?php
 snmp_set_enum_print(0);
 echo snmpget('localhost', 'public', 'IF-MIB::ifOperStatus.3') . "\n";
 snmp_set_enum_print(1);
 echo snmpget('localhost', 'public', 'IF-MIB::ifOperStatus.3') . "\n";
?>

   
```php

El ejemplo anterior mostrará: INTEGER: up(1) INTEGER: 1
