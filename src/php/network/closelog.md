---
title: closelog
description: Cierra la conexión al registro del sistema
source_url: https://www.php.net/manual/es/function.closelog.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/closelog.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: f78180344
order: 56230
---

closelog

Cierra la conexión al registro del sistema

## Descripción

```php
closelog(): true
```php

`closelog` cierra el puntero utilizado para escribir en el registro del sistema. El uso de `closelog` es opcional.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Véase también

`syslog`, `openlog`
