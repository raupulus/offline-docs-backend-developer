---
title: imap_undelete
description: Elimina la marca de eliminación de un mensaje
source_url: https://www.php.net/manual/es/function.imap-undelete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-undelete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 673d373ed
order: 38620
---

imap_undelete

Elimina la marca de eliminación de un mensaje

## Descripción

```php
imap_undelete(IMAP\Connection $imap, string $message_nums, [int $flags]): true
```php

Elimina la marca de eliminación del mensaje `message_nums`, colocada con `imap_delete` o `imap_mail_move`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_nums`  
Un `string` que representa uno o más mensajes en un formato de secuencia IMAP4 (`"n"`, `"n:m"`, o una combinación de estos, delimitados por comas).

`flags`  

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_delete`, `imap_mail_move`
