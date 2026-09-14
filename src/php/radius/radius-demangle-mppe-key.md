---
title: radius_demangle_mppe_key
description: Deriva las claves mppe desde datos
source_url: https://www.php.net/manual/es/function.radius-demangle-mppe-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-demangle-mppe-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67630
---

radius_demangle_mppe_key

Deriva las claves mppe desde datos

## Descripción

```php
radius_demangle_mppe_key(resource $radius_handle, string $mangled): string
```php

Al utilizar MPPE con MS-CHAPv2, las claves recibidas y enviadas son "secadas" (ver la [RFC 2548](https://datatracker.ietf.org/doc/html/rfc2548)), sin embargo, esta función es útil, ya que no se sabe si existe o no una implementación de PPTP-MPPE en PHP.

## Parámetros

`radius_handle`  
El recurso RADIUS.

`mangled`  
Los datos deformados a descifrar

## Valores devueltos

Devuelve el string o `false` si ocurre un error.
