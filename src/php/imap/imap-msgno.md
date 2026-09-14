---
title: imap_msgno
description: Devuelve el número de secuencia del mensaje para un UID dado
source_url: https://www.php.net/manual/es/function.imap-msgno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-msgno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38360
---

imap_msgno

Devuelve el número de secuencia del mensaje para un UID dado

## Descripción

```php
imap_msgno(IMAP\Connection $imap, int $message_uid): int
```php

Devuelve el número de secuencia del mensaje para el UID `message_uid`.

Esta función es el inverso de la función `imap_uid`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_uid`  
El UID del mensaje

## Valores devueltos

Devuelve el número de secuencia del mensaje para el UID `message_uid`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_uid`
