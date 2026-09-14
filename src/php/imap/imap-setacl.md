---
title: imap_setacl
description: Modifica el ACL de la bandeja de entrada
source_url: https://www.php.net/manual/es/function.imap-setacl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-setacl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38540
---

imap_setacl

Modifica el ACL de la bandeja de entrada

## Descripción

```php
imap_setacl(IMAP\Connection $imap, string $mailbox, string $user_id, string $rights): bool
```php

Define el ACL para la bandeja de entrada dada.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`mailbox`  
El nombre de la bandeja de entrada, ver la documentación de la función `imap_open` para más detalles

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`user_id`  
El identificador del usuario cuyos derechos se desean definir.

`rights`  
Los derechos a otorgar al usuario. Pasar una cadena vacía borrará el ACL.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Notas

Esta función está actualmente disponible solo para los usuarios de la biblioteca `c-client2000` o superior.

## Véase también

`imap_getacl`
