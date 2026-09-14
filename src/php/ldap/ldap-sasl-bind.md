---
title: ldap_sasl_bind
description: Autenticación en el servidor LDAP utilizando SASL
source_url: https://www.php.net/manual/es/function.ldap-sasl-bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-sasl-bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 5bc68add3
order: 43500
---

ldap_sasl_bind

Autenticación en el servidor LDAP utilizando SASL

## Descripción

```php
#[\SensitiveParameter] ldap_sasl_bind(LDAP\Connection $ldap, [string $dn], [string $password], [string $mech], [string $realm], [string $authc_id], [string $authz_id], [string $props]): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.0.0 | `dn`, `password`, `mech`, `realm`, `authc_id`, `authz_id` y `props` ahora son nulos. |

## Notas

> [!NOTE]
> `ldap_sasl_bind` requiere soporte SASL (`sasl.h`). Asegúrese de que la opción de configuración `--with-ldap-sasl` se utilice durante la compilación de PHP, de lo contrario, esta función no estará definida.
