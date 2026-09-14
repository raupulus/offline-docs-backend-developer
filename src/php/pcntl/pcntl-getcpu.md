---
title: pcntl_getcpu
description: Obtiene el número de CPU en la que el proceso llamante se ejecutó por
  última vez
source_url: https://www.php.net/manual/es/function.pcntl-getcpu.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-getcpu.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_revision: acb474ea9
order: 61250
---

pcntl_getcpu

Obtiene el número de CPU en la que el proceso llamante se ejecutó por última vez

## Descripción

```php
pcntl_getcpu(): int
```php

`pcntl_getcpu` devuelve el número de la CPU en la que el proceso llamante se ejecutó por última vez. Esta función utiliza la llamada al sistema `sched_getcpu(3)` disponible en Linux.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de CPU como un `int`.

## Véase también

pcntl_getcpuaffinity

pcntl_setcpuaffinity
