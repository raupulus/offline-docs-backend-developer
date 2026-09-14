---
title: oci_register_taf_callback
description: Registra una función de retrollamada definida por el usuario para Oracle
  Database TAF
source_url: https://www.php.net/manual/es/function.oci-register-taf-callback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-register-taf-callback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: ed6de1ae2
order: 57550
---

oci_register_taf_callback

Registra una función de retrollamada definida por el usuario para Oracle Database TAF

## Descripción

```php
oci_register_taf_callback(resource $connection, callable $callback): bool
```php

Se registra una función de retrollamada definida por el usuario para `connection`. Si `connection` falla debido a una falla de instancia o de red, la función de retrollamada registrada será invocada varias veces durante el basculement. Ver [Soporte de basculement de aplicación transparente OCI8 (TAF)](#oci8.taf) para más información.

Cuando `oci_register_taf_callback` es llamada varias veces, cada registro sobrescribe al anterior.

Utilizar `oci_unregister_taf_callback` para cancelar explícitamente un retrollamada definida por el usuario.

Los registros de retrollamada TAF NO serán guardados entre conexiones persistentes, por lo tanto, el retrollamada debe ser re-registrado para una nueva conexión persistente.

## Parámetros

`connection`  
Un identificador de conexión Oracle.

`callback`  
Una función de retrollamada definida por el usuario para registrar TAF Oracle. Puede ser una cadena de nombre de función o una clausura (función anónima).

La interfaz para una función de retrollamada definida por el usuario TAF es la siguiente:

```php
userCallbackFn(resource $connection, int $event, int $type): int
```

Ver la descripción del parámetro y un ejemplo en la página [ Soporte de basculement de aplicación transparente OCI8 (TAF)](#oci8.taf).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`oci_unregister_taf_callback`
