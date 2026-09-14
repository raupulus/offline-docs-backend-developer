---
title: mysqli::thread_safe
description: Indica si el soporte de hilos está activado o no
source_url: https://www.php.net/manual/es/mysqli.thread-safe.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/thread-safe.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55430
---

mysqli::thread_safe

mysqli_thread_safe

Indica si el soporte de hilos está activado o no

## Descripción

Estilo orientado a objetos

```php
public mysqli::thread_safe(): bool
```php

Estilo procedimental

```php
mysqli_thread_safe(): bool
```

Indica si la biblioteca cliente está compilada con seguridad para hilos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la biblioteca cliente es thread-safe, `false` en caso contrario.
