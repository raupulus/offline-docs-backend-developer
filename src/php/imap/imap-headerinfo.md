---
title: imap_headerinfo
description: Lee la cabecera del mensaje
source_url: https://www.php.net/manual/es/function.imap-headerinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-headerinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_revision: 4e69a9f2b
order: 38210
---

imap_headerinfo

Lee la cabecera del mensaje

## Descripción

```php
imap_headerinfo(IMAP\Connection $imap, int $message_num, [int $from_length], [int $subject_length]): stdClass
```php

Recupera la información sobre un número de mensaje dado leyendo sus cabeceras.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_num`  
El número del mensaje

`from_length`  
Número de caracteres para la propiedad `fetchfrom`. Debe ser mayor o igual a `0`.

`subject_length`  
Número de caracteres para la propiedad `fetchsubject`. Debe ser mayor o igual a `0`.

## Valores devueltos

Devuelve `false` en caso de errores o, en caso de éxito, la información en un objeto que contiene las siguientes propiedades:

- `"toaddress"` : toda la línea de cabecera to: hasta 1024 caracteres

- `"to"` : un array de objetos de la línea to: con las siguientes propiedades: `personal`, `adl`, `mailbox`, y `host`

- `"fromaddress"` : toda la línea de cabecera from: hasta 1024 caracteres

- `"from"` : un array de objetos de la línea From: con las siguientes propiedades: `personal`, `adl`, `mailbox`, y `host`

- `"ccaddress"` : toda la línea de cabecera cc: hasta 1024 caracteres

- `"cc"` : un array de objetos de la línea cc: con las siguientes propiedades: `personal`, `adl`, `mailbox`, y `host`

- `"bccaddress"` : toda la línea de cabecera bcc: hasta 1024 caracteres

- `"bcc"` : un array de objetos de la línea Bcc: con las siguientes propiedades: `personal`, `adl`, `mailbox`, y `host`

- `"reply_toaddress"` : toda la línea de cabecera Reply_to: hasta 1024 caracteres

- `"reply_to"` : un array de objetos de la línea Reply_to: con las siguientes propiedades: `personal`, `adl`, `mailbox`, y `host`

- `"senderaddress"` : toda la línea de cabecera Sender: hasta 1024 caracteres

- `"sender"` : un array de objetos de la línea Sender: con las siguientes propiedades: `personal`, `adl`, `mailbox`, y `host`

- `"return_pathaddress"` : toda la línea de cabecera Return-path: hasta 1024 caracteres

- `"return_path"` : un array de objetos de la línea Return-path: con las siguientes propiedades: `personal`, `adl`, `mailbox`, y `host`

- remail -

- `"date"` : La fecha del mensaje, tal como se encuentra en las cabeceras

- `"Date"` : Idéntico a `"date"`

- `"subject"` : El asunto del mensaje

- `"Subject"` : Idéntico a `"subject"`

- `"in_reply_to"` :

- `"message_id"` :

- `"newsgroups"` :

- `"followup_to"` :

- `"references"` :

- `"Recent"` : `R` si el mensaje es reciente y leído, `N` si el mensaje es reciente y no leído, `" "` si el mensaje no es reciente.

- `"Unseen"` : `U` si el mensaje es no leído Y no reciente, `" "` si el mensaje es no leído y reciente

- `"Flagged"` : `F` si el mensaje contiene un flag, `" "` en caso contrario

- `"Answered"` : `A` si se ha respondido a este mensaje, `" "` en caso contrario

- `"Deleted"` : `D` si el mensaje está eliminado, `" "` en caso contrario

- `"Draft"` : `X` si el mensaje es un borrador, `" "` en caso contrario

- `"Msgno"` : El número del mensaje

- `"MailDate"` :

- `"Size"` : El tamaño del mensaje

- `"udate"` : Fecha de envío del mensaje, en forma de fecha Unix

- `"fetchfrom"` : Línea `"from"` formateada para caber en `from_length` caracteres

- `"fetchsubject"` : Línea `"subject"` formateada para caber en `subject_length` caracteres

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
| 8.0.0 | El parámetro `defaulthost` sin uso ha sido eliminado. |

## Véase también

`imap_fetch_overview`
