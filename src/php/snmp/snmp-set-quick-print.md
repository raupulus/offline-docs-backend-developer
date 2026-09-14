---
title: snmp_set_quick_print
description: Escribe el valor actual de la opción enable de la biblioteca NET-SNMP
source_url: https://www.php.net/manual/es/function.snmp-set-quick-print.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp-set-quick-print.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74740
---

snmp_set_quick_print

Escribe el valor actual de la opción

enable

de la biblioteca NET-

SNMP

## Descripción

```php
snmp_set_quick_print(bool $enable): true
```php

Fija el valor de la opción `enable` de la biblioteca NET-SNMP. Cuando tiene el valor de (1), la biblioteca SNMP devolverá valores 'rápidos'. Esto significa que solo se devolverá el valor. Cuando la opción `enable` no está activada (por omisión), la biblioteca NET-SNMP mostrará otra información (como la dirección IP (IpAddress) o OID). Además, si quick_print no está activada, la biblioteca también mostrará valores hexadecimales adicionales para todas las cadenas de tres caracteres o menos.

Por omisión, NET-SNMP devuelve valores detallados, y quick_print sirve para devolver solo el valor.

Actualmente, las cadenas siempre se devuelven con comillas adicionales. Esto se corregirá posteriormente.

## Parámetros

`enable`  

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Modificar `enable` es más frecuente cuando se utilizan los valores devueltos que cuando se muestran.

Ejemplo con `snmp_set_quick_print`

```
<?php
snmp_set_quick_print(0);
$a = snmpget("127.0.0.1", "public", ".1.3.6.1.2.1.2.2.1.9.1");
echo "$a\n";
snmp_set_quick_print(1);
$a = snmpget("127.0.0.1", "public", ".1.3.6.1.2.1.2.2.1.9.1");
echo "$a\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    'Timeticks: (0) 0:00:00.00'
    '0:00:00.00'

## Véase también

snmp_get_quick_print
