---
title: imap_mail_copy
description: Copia los mensajes especificados en un buzón de correo
source_url: https://www.php.net/manual/es/function.imap-mail-copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-mail-copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 91a4618df
order: 38310
---

imap_mail_copy

Copia los mensajes especificados en un buzón de correo

## Descripción

```php
imap_mail_copy(IMAP\Connection $imap, string $message_nums, string $mailbox, [int $flags]): bool
```php

Copia los mensajes de correo electrónico especificados por `message_nums` en el buzón de correo especificado.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_nums`  
`message_nums` es un intervalo, y no solo una lista de números de mensaje (como se describe en la [RFC2060](https://datatracker.ietf.org/doc/html/rfc2060)).

`mailbox`  
El nombre del buzón de correo, ver la documentación de la función `imap_open` para más detalles

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`flags`  
`flags` es una máscara, que puede contener uno o varios de los siguientes valores:

- `CP_UID` - la secuencia de números contiene UIDS

- `CP_MOVE` - Borra los mensajes después de la copia. Si este flag está definido, la función se comporta de manera idéntica a `imap_mail_move`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_mail_move`
