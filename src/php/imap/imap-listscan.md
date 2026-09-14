---
title: imap_listscan
description: Lee la lista de buzones de correo y busca una cadena
source_url: https://www.php.net/manual/es/function.imap-listscan.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-listscan.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38270
---

imap_listscan

Lee la lista de buzones de correo y busca una cadena

## Descripción

```php
imap_listscan(IMAP\Connection $imap, string $reference, string $pattern, string $content): array
```php

Devuelve un array que contiene los nombres de los buzones de correo que contienen el string `content` en su nombre.

Esta función es similar a `imap_listmailbox`, pero también verifica la presencia del string `content` en los mensajes del buzón de correo.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`reference`  
`reference` debe ser solo el servidor en la forma descrita en `imap_open`

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`pattern`  
Especifica en qué parte de la jerarquía del buzón comenzar la búsqueda.

Hay dos caracteres especiales que se pueden pasar como parte del `pattern`: '`*`' y '`%`'. '`*`' significa devolver todos los buzones. Si se pasa `pattern` como '`*`', se obtendrá una lista de toda la jerarquía del buzón. '`%`' significa devolver solo el nivel actual. '`%`' como parámetro `pattern` devolverá solo los buzones de nivel superior; '`~/mail/%`' en `UW_IMAPD` devolverá cada buzón en el directorio `~/mail`, pero ninguno en las subcarpetas de ese directorio.

`content`  
El string buscado

## Valores devueltos

Devuelve un array que contiene los nombres de los buzones de correo que contienen el string `content` en el nombre del buzón de correo, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_listmailbox`, `imap_search`
