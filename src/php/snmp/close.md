---
title: SNMP::close
description: Cerrar sesión SNMP
source_url: https://www.php.net/manual/es/snmp.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74930
---

SNMP::close

Cerrar sesión

SNMP

## Descripción

```php
public SNMP::close(): bool
```php

Libera previamente asignado un objeto de sesión SNMP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de SNMP::close

```
<?php
  $session = new SNMP(SNMP::VERSION_1, "127.0.0.1", "public");
  # ...
  # get, walk, etc va aquí
  # ...
  $session->close();
?>

   
```php

## Véase también

SNMP::\_\_construct
