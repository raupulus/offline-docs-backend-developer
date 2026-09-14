---
title: radius_demangle
description: Deshidrata datos
source_url: https://www.php.net/manual/es/function.radius-demangle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-demangle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67640
---

radius_demangle

Deshidrata datos

## Descripción

```php
radius_demangle(resource $radius_handle, string $mangled): string
```php

Algunos datos (contraseñas, claves MS-CHAPv1 MPPE) son "deshidratados" por razones de seguridad y deben ser "deshidratados" antes de poder utilizarlos.

## Parámetros

`radius_handle`  
El recurso RADIUS.

`mangled`  
Los datos deformados a descifrar

## Valores devueltos

Devuelve la cadena "deshidratada" o `false` si ocurre un error.
