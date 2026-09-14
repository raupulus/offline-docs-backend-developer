---
title: imap_fetchstructure
description: Lee la estructura de un mensaje
source_url: https://www.php.net/manual/es/function.imap-fetchstructure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-fetchstructure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38120
---

imap_fetchstructure

Lee la estructura de un mensaje

## Descripción

```php
imap_fetchstructure(IMAP\Connection $imap, int $message_num, [int $flags]): stdClass
```php

`imap_fetchstructure` lee la estructura del mensaje `msg_number`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_num`  
El número del mensaje

`flags`  
Este parámetro opcional tiene una sola opción, `FT_UID`, que solicita a la función tratar el argumento `message_num` como un `UID`.

## Valores devueltos

Devuelve un objeto cuyas propiedades se listan en la tabla siguiente, o `false` si ocurre un error.

|  |  |
|----|----|
| type | Tipo primario de cuerpo |
| encoding | Codificación de transferencia del cuerpo |
| ifsubtype | `true` si hay una cadena de subtipo |
| subtype | subtipo MIME |
| ifdescription | `true` si hay una cadena de descripción |
| description | Cadena de descripción del contenido |
| ifid | `true` si hay una cadena de identificación |
| id | Cadena de identificación |
| lines | Número de líneas |
| bytes | Número de bytes |
| ifdisposition | `true` si hay una cadena de disposición |
| disposition | Cadena de disposición |
| ifdparameters | `true` si hay un array de parámetros `dparameters` |
| dparameters | array de objetos donde cada objeto tiene una propiedad `"attribute"` y una propiedad `"value"` correspondiente a los parámetros de encabezado `Content-disposition` MIME. |
| ifparameters | `true` si el array de parámetros existe |
| parameters | Array de objetos donde cada uno tiene una propiedad `"attribute"` y una propiedad `"value"`. |
| parts | Array de objetos que describen cada parte MIME del mensaje |

Objeto devuelto por `imap_fetchstructure`

| Valor | Tipo       | Constante       |
|-------|------------|-----------------|
| 0     | texto      | TYPETEXT        |
| 1     | multipart  | TYPEMULTIPART   |
| 2     | mensaje    | TYPEMESSAGE     |
| 3     | aplicación | TYPEAPPLICATION |
| 4     | audio      | TYPEAUDIO       |
| 5     | imagen     | TYPEIMAGE       |
| 6     | video      | TYPEVIDEO       |
| 7     | modelo     | TYPEMODEL       |
| 8     | otro       | TYPEOTHER       |

Tipo primario de cuerpo (puede variar según la biblioteca utilizada)

| Valor | Tipo              | Constante          |
|-------|-------------------|--------------------|
| 0     | 7 bit             | ENC7BIT            |
| 1     | 8 bit             | ENC8BIT            |
| 2     | Binario           | ENCBINARY          |
| 3     | Base 64           | ENCBASE64          |
| 4     | Citado imprimible | ENCQUOTEDPRINTABLE |
| 5     | Otro              | ENCOTHER           |

Codificación de transferencia (puede variar según la biblioteca utilizada)

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_fetchbody`, `imap_bodystruct`
