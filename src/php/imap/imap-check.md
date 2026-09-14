---
title: imap_check
description: Verifica el buzón de correo actual
source_url: https://www.php.net/manual/es/function.imap-check.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-check.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 37990
---

imap_check

Verifica el buzón de correo actual

## Descripción

```php
imap_check(IMAP\Connection $imap): stdClass
```php

Verifica la información del buzón de correo actual.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

## Valores devueltos

Devuelve la información en un objeto que contiene las siguientes propiedades:

- `Date` - Fecha de la última modificación del contenido del buzón de correo de acuerdo con la [RFC2822](https://datatracker.ietf.org/doc/html/rfc2822)

- `Driver` - protocolo utilizado para acceder al buzón de correo: POP3, IMAP, NNTP.

- `Mailbox` - nombre del buzón de correo

- `Nmsgs` - número de mensajes en el buzón de correo

- `Recent` - número de mensajes recientes en el buzón de correo

Devuelve `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_check`

```
<?php

$imap = imap_check($imap_stream);
var_dump($imap);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)(5) {
      ["Date"]=>
      string(37) "Wed, 10 Dec 2003 17:56:54 +0100 (CET)"
      ["Driver"]=>
      string(4) "imap"
      ["Mailbox"]=>
      string(54)
      "{www.example.com:143/imap/user="foo@example.com"}INBOX"
      ["Nmsgs"]=>
      int(1)
      ["Recent"]=>
      int(0)
    }
