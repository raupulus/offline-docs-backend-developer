---
title: imap_expunge
description: Elimina todos los mensajes marcados para su eliminación
source_url: https://www.php.net/manual/es/function.imap-expunge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-expunge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 673d373ed
order: 38070
---

imap_expunge

Elimina todos los mensajes marcados para su eliminación

## Descripción

```php
imap_expunge(IMAP\Connection $imap): true
```php

Elimina todos los mensajes marcados para su eliminación por `imap_delete`, `imap_mail_move`, o `imap_setflag_full`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
