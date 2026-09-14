---
title: imap_num_msg
description: Devuelve el número de mensajes en el buzón de correo actual
source_url: https://www.php.net/manual/es/function.imap-num-msg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-num-msg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38380
---

imap_num_msg

Devuelve el número de mensajes en el buzón de correo actual

## Descripción

```php
imap_num_msg(IMAP\Connection $imap): int
```php

Devuelve el número de mensajes en el buzón de correo actual.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

## Valores devueltos

Devuelve el número de mensajes en el buzón de correo actual, en forma de un `int`, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_num_recent`, `imap_status`
