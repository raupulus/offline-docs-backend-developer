---
title: oci_unregister_taf_callback
description: Anular el registro de una función callback definida para Oracle Database
  TAF
source_url: https://www.php.net/manual/es/function.oci-unregister-taf-callback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-unregister-taf-callback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: e9366ee45
order: 57690
---

oci_unregister_taf_callback

Anular el registro de una función callback definida para Oracle Database TAF

## Descripción

```php
oci_unregister_taf_callback(resource $connection): bool
```php

Anula el registro de la función callback definida por el usuario registrada en la `conexión` por `oci_register_taf_callback`. Véase [Soporte para 'Transparent Application Failover' (TAF) de OCI8 ](#oci8.taf) para más información.

## Parámetros

`connection`  
Un identificador de conexión de Oracle.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`oci_register_taf_callback`
