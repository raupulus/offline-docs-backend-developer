---
title: imap_mail_move
description: Mueve mensajes a una caja de correo
source_url: https://www.php.net/manual/es/function.imap-mail-move.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-mail-move.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 91a4618df
order: 38320
---

imap_mail_move

Mueve mensajes a una caja de correo

## Descripción

```php
imap_mail_move(IMAP\Connection $imap, string $message_nums, string $mailbox, [int $flags]): bool
```php

`imap_mail_move` mueve los mensajes especificados por `message_nums` a la caja de correo `mailbox`. Es importante destacar que los mensajes son en realidad *copiados* a la caja de correo `mailbox`, y los mensajes originales son marcados para ser eliminados. Esto implica que los mensajes en `mailbox` son asignados nuevos UIDs.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_nums`  
`message_nums` es un intervalo, y no solo una lista de mensajes (como se describe en la [RFC2060](https://datatracker.ietf.org/doc/html/rfc2060)).

`mailbox`  
El nombre de la caja de correo, ver la documentación de la función `imap_open` para más detalles

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`flags`  
`flags` es un campo de bits y puede contener un solo valor:

- `CP_UID` - La secuencia de números contiene UIDs

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Notas

> [!NOTE]
> `imap_mail_move` marcará el correo electrónico original con un marcador de eliminación, para eliminarlo efectivamente, se requiere una llamada a `imap_expunge`.

## Véase también

`imap_mail_copy`
