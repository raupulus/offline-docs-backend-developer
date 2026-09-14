---
title: snmp_get_quick_print
description: Lee el valor actual de la opción quick_print de la biblioteca NET-SNMP
source_url: https://www.php.net/manual/es/function.snmp-get-quick-print.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp-get-quick-print.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74680
---

snmp_get_quick_print

Lee el valor actual de la opción quick_print de la biblioteca NET-SNMP

## Descripción

```php
snmp_get_quick_print(): bool
```php

`snmp_get_quick_print` devuelve el valor actual, almacenado en la biblioteca NET-SNMP, de la opción quick_print. Por omisión, quick_print está desactivada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si quick_print está activa, `false` en caso contrario.

## Ejemplos

Ejemplo con `snmp_get_quick_print`

```
<?php
$quickprint = snmp_get_quick_print();
?>

   
```php

## Véase también

snmp_set_quick_print

para una descripción completa sobre lo que hace quick_print.
