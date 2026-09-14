---
title: imap_fetchheader
description: Devuelve el encabezado de un mensaje
source_url: https://www.php.net/manual/es/function.imap-fetchheader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-fetchheader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38100
---

imap_fetchheader

Devuelve el encabezado de un mensaje

## Descripción

```php
imap_fetchheader(IMAP\Connection $imap, int $message_num, [int $flags]): string
```php

`imap_fetchheader` devuelve el encabezado RFC2822 crudo y completo del mensaje `msgno`, en forma de string.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_num`  
El número del mensaje

`flags`  
Las opciones posibles son:

- `FT_UID` - `message_num` es un UID

- `FT_INTERNAL` - La string devuelta está en formato "internal", es decir, sin canonización de los CRLF

- `FT_PREFETCHTEXT` - RFC822.TEXT debe ser pre descargado junto con el encabezado. Esto reduce el RTT en una conexión IMAP, si se desea el mensaje completo. (e.g. en una operación de guardado en un fichero).

## Valores devueltos

Devuelve el encabezado del mensaje especificado, en forma de string, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_fetch_overview`
