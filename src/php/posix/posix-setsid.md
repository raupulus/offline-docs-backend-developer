---
title: posix_setsid
description: Hacer del proceso actual un líder de sesión
source_url: https://www.php.net/manual/es/function.posix-setsid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-setsid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65440
---

posix_setsid

Hacer del proceso actual un líder de sesión

## Descripción

```php
posix_setsid(): int
```php

Hace del proceso actual un líder de sesión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un id de sesión, o -1 si ocurrió algún error.

## Véase también

Las páginas del manual POSIX.1 y setsid(2) del sistema POSIX para más información sobre los grupos de procesos y el control de trabajo.
