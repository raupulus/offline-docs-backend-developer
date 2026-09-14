---
title: imap_num_recent
description: Devuelve el número de mensajes recientes en el buzón de correo actual
source_url: https://www.php.net/manual/es/function.imap-num-recent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-num-recent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38390
---

imap_num_recent

Devuelve el número de mensajes recientes en el buzón de correo actual

## Descripción

```php
imap_num_recent(IMAP\Connection $imap): int
```php

Devuelve el número de mensajes recientes en el buzón de correo actual.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

## Valores devueltos

Devuelve el número de mensajes recientes en el buzón de correo actual, en forma de un `int`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_num_msg`, `imap_status`
