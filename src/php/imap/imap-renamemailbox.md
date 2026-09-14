---
title: imap_renamemailbox
description: Renombra un buzón de correo
source_url: https://www.php.net/manual/es/function.imap-renamemailbox.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-renamemailbox.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38440
---

imap_renamemailbox

Renombra un buzón de correo

## Descripción

```php
imap_renamemailbox(IMAP\Connection $imap, string $from, string $to): bool
```php

`imap_renamemailbox` renombra el buzón de correo `from` a `to` (ver la función `imap_open` para el formato de los nombres `mbox`).

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`from`  
El antiguo nombre del buzón de correo, ver la documentación de la función `imap_open` para más detalles

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`to`  
El nuevo nombre del buzón de correo, ver la documentación de la función `imap_open` para más detalles

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_createmailbox`, `imap_deletemailbox`
