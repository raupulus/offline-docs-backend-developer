---
title: imap_fetchmime
description: Recupera los encabezados MIME para una sección particular del mensaje
source_url: https://www.php.net/manual/es/function.imap-fetchmime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-fetchmime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38110
---

imap_fetchmime

Recupera los encabezados MIME para una sección particular del mensaje

## Descripción

```php
imap_fetchmime(IMAP\Connection $imap, int $message_num, string $section, [int $flags]): string
```php

Recupera los encabezados MIME para una sección particular del cuerpo de un mensaje específico.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_num`  
El número del mensaje.

`section`  
El número de la sección. Es una cadena de enteros delimitados por una coma que representa el índice de la lista de secciones del cuerpo del mensaje, tal como se especifica en IMAP4.

`flags`  
Una máscara de una o varias opciones siguientes:

- `FT_UID` - El parámetro `message_num` es un UID.

- `FT_PEEK` - No colocar la bandera \Seen si no está ya definida.

- `FT_INTERNAL` - La cadena devuelta está en un formato interno, y no será canonizada en CRLF.

## Valores devueltos

Devuelve los encabezados MIME de una sección particular del cuerpo del mensaje especificado, en forma de un `string`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_fetchbody`, `imap_fetchstructure`, `imap_fetchheader`
