---
title: imap_uid
description: Devuelve el UID de un mensaje
source_url: https://www.php.net/manual/es/function.imap-uid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-uid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38610
---

imap_uid

Devuelve el UID de un mensaje

## Descripción

```php
imap_uid(IMAP\Connection $imap, int $message_num): int
```php

`imap_uid` devuelve el UID para el mensaje `msgno`. Un UID es un identificador único que nunca cambia, mientras que el número del mensaje en la lista de mensajes puede cambiar con cualquier modificación del buzón de correo.

Es la función inversa de `imap_msgno`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_num`  
El número del mensaje.

## Valores devueltos

El UID de un mensaje dado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Notas

> [!NOTE]
> Esta funcionalidad no es soportada por los buzones de correo POP3.

## Véase también

`imap_msgno`
