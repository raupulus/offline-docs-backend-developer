---
title: SNMP::getErrno
description: Obtiene el último código de error
source_url: https://www.php.net/manual/es/snmp.geterrno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp/geterrno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_revision: '409067254'
order: 74960
---

SNMP::getErrno

Obtiene el último código de error

## Descripción

```php
public SNMP::getErrno(): int
```php

Devuelve código de error de la última solicitud SNMP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve uno de los valores de error que se describe en el capítulo constantes.

## Ejemplos

Ejemplo de SNMP::getErrno

```
<?php
$session = new SNMP(SNMP::VERSION_2c, '127.0.0.1', 'boguscommunity');
var_dump(@$session->get('.1.3.6.1.2.1.1.1.0'));
var_dump($session->getErrno() == SNMP::ERRNO_TIMEOUT);
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

SNMP::getError
