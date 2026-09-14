---
title: SNMP::getError
description: Obtiene el último mensaje de error
source_url: https://www.php.net/manual/es/snmp.geterror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp/geterror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_revision: '409067254'
order: 74970
---

SNMP::getError

Obtiene el último mensaje de error

## Descripción

```php
public SNMP::getError(): string
```php

Devuelve un string con el error de la última solicitud SNMP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

String que describe el error de la última solicitud SNMP.

## Ejemplos

Ejemplo de SNMP::getError

```
<?php
$session = new SNMP(SNMP::VERSION_2c, '127.0.0.1', 'boguscommunity');
var_dump(@$session->get('.1.3.6.1.2.1.1.1.0'));
var_dump($session->getError());
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    string(26) "No response from 127.0.0.1"

## Véase también

SNMP::getErrno
