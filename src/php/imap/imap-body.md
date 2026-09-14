---
title: imap_body
description: Lee el cuerpo de un mensaje
source_url: https://www.php.net/manual/es/function.imap-body.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-body.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 37970
---

imap_body

Lee el cuerpo de un mensaje

## Descripción

```php
imap_body(IMAP\Connection $imap, int $message_num, [int $flags]): string
```php

`imap_body` devuelve el cuerpo del mensaje número `message_num` del buzón actual.

`imap_body` devolverá una copia sin tratar del cuerpo del mensaje. Para extraer las subpartes MIME del mensaje, utilice `imap_fetchstructure` para analizar la estructura, y `imap_fetchbody` para extraer una copia de una de las subpartes.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_num`  
El número del mensaje

`flags`  
El parámetro `flags` opcional es una máscara que puede contener los siguientes valores:

- `FT_UID` - `message_num` es un UID

- `FT_PEEK` - No levantar el flag \Seen (Mensaje leído) si no está ya levantado.

- `FT_INTERNAL` - La string devuelta está en formato interno, y no va a canonizar los CRLF.

## Valores devueltos

Devuelve el cuerpo del mensaje especificado, en forma de `string`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
