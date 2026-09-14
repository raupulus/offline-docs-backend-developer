---
title: imap_alerts
description: Devuelve todas las alertas
source_url: https://www.php.net/manual/es/function.imap-alerts.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-alerts.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 4a9963bc4
order: 37930
---

imap_alerts

Devuelve todas las alertas

## Descripción

```php
imap_alerts(): array
```php

Devuelve un array de todos los mensajes de alerta IMAP generados desde la última llamada a `imap_alerts` o desde el inicio de la página.

Cuando `imap_alerts` es llamada, la pila de alertas es vaciada. Las especificaciones IMAP requieren que estos mensajes sean pasados al usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array que contiene todos los mensajes de alerta IMAP generados o `false` si no hay mensajes de alerta disponibles.

## Véase también

`imap_errors`
