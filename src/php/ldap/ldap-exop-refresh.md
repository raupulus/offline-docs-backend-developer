---
title: ldap_exop_refresh
description: Actualiza la ayuda de la operación extendida
source_url: https://www.php.net/manual/es/function.ldap-exop-refresh.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-exop-refresh.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43170
---

ldap_exop_refresh

Actualiza la ayuda de la operación extendida

## Descripción

```php
ldap_exop_refresh(LDAP\Connection $ldap, string $dn, int $ttl): int
```php

Realiza una operación extendida de actualización y devuelve los datos.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`dn`  
dn de la entrada a actualizar.

`ttl`  
El tiempo en segundos (entre 1 y 31557600) que el cliente solicita que la entrada exista en el directorio antes de ser eliminada automáticamente.

## Valores devueltos

Según la RFC: El campo responseTtl es el tiempo en segundos que el servidor elige como campo de tiempo de vida para esta entrada. No debe ser menor que el solicitado por el cliente, y puede ser mayor. Sin embargo, para permitir a los servidores mantener un directorio relativamente preciso, y para evitar que los clientes abusen de las extensiones dinámicas, los servidores están autorizados a acortar un valor de tiempo de vida solicitado por el cliente, hasta un mínimo de 86400 segundos (un día). `false` será devuelto en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |

## Véase también

`ldap_exop`
