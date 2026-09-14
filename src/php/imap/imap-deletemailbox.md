---
title: imap_deletemailbox
description: Borra una boîte aux lettres
source_url: https://www.php.net/manual/es/function.imap-deletemailbox.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-deletemailbox.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38050
---

imap_deletemailbox

Borra una boîte aux lettres

## Descripción

```php
imap_deletemailbox(IMAP\Connection $imap, string $mailbox): bool
```php

Borra la boîte aux lettres especificada.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`mailbox`  
El nombre de la boîte aux lettres, ver la documentación sobre la función `imap_open` para más detalles

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_createmailbox`, `imap_renamemailbox`, `imap_open` para el formato `mbox`
