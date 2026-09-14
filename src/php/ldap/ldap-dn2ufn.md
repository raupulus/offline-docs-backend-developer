---
title: ldap_dn2ufn
description: Convierte un DN en formato UFN (User Friendly Naming)
source_url: https://www.php.net/manual/es/function.ldap-dn2ufn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-dn2ufn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 76f8c0151
order: 43110
---

ldap_dn2ufn

Convierte un DN en formato UFN (User Friendly Naming)

## Descripción

```php
ldap_dn2ufn(string $dn): string
```php

Convierte el DN `dn` a un formato más legible para humanos, eliminando los tipos de nombres.

## Parámetros

`dn`  
El DN de la entrada LDAP.

## Valores devueltos

Devuelve el UFN, o `false` si ocurre un error.
