---
title: imap_fetchbody
description: Devuelve una sección extraída del cuerpo de un mensaje
source_url: https://www.php.net/manual/es/function.imap-fetchbody.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-fetchbody.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38090
---

imap_fetchbody

Devuelve una sección extraída del cuerpo de un mensaje

## Descripción

```php
imap_fetchbody(IMAP\Connection $imap, int $message_num, string $section, [int $flags]): string
```php

Recupera una sección particular del cuerpo de los mensajes especificados. Las partes del cuerpo no son decodificadas por esta función.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_num`  
El número del mensaje

`section`  
El número de la sección. Es una cadena de enteros, delimitados por una coma que corresponden a los índices en la lista de las secciones del mensaje, tal como se prevé en la especificación IMAP4.

`flags`  
La opción `imap_fetchbody` es una máscara que puede contener los siguientes valores:

- `FT_UID` - `message_num` es un UID

- `FT_PEEK` - No levantar el flag \Seen (Mensaje leído) si no está ya levantado.

- `FT_INTERNAL` - La cadena devuelta está en formato interno, y no va a canonizar los CRLF.

## Valores devueltos

Devuelve una sección particular del cuerpo de los mensajes especificados, en forma de una `string`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_savebody`, `imap_fetchstructure`
