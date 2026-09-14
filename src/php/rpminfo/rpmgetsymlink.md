---
title: rpmgetsymlink
description: Devuelve el destino de un enlace simbólico
source_url: https://www.php.net/manual/es/function.rpmgetsymlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/functions/rpmgetsymlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1d4f5d151
order: 72490
---

rpmgetsymlink

Devuelve el destino de un enlace simbólico

## Descripción

```php
rpmgetsymlink(string $path, string $name): string
```php

Devuelve el destino de un enlace simbólico.

## Parámetros

`path`  
La ruta de acceso del fichero RPM.

`name`  
El nombre del fichero enlace simbólico.

## Valores devueltos

Un `string` con el destino del enlace simbólico, `null` en caso de error, o una cadena vacía si no es un enlace simbólico.
