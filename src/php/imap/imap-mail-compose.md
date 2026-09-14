---
title: imap_mail_compose
description: Crea un mensaje MIME
source_url: https://www.php.net/manual/es/function.imap-mail-compose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-mail-compose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 38300
---

imap_mail_compose

Crea un mensaje MIME

## Descripción

```php
imap_mail_compose(array $envelope, array $bodies): string
```php

Crea un mensaje MIME basado en el sobre `envelope` y las secciones `bodies`.

## Parámetros

`envelope`  
Un array asociativo que contiene los campos de los encabezados. Las claves válidas son: `"remail"`, `"return_path"`, `"date"`, `"from"`, `"reply_to"`, `"in_reply_to"`, `"subject"`, `"to"`, `"cc"`, `"bcc"` y `"message_id"`, que definen los encabezados respectivos al `string` dado. Para definir encabezados adicionales, la clave `"custom_headers"` es soportada, que espera un array de estos encabezados, por ejemplo `["User-Agent: My Mail Client"]`.

`bodies`  
Un array indexado de los cuerpos. El primer cuerpo es el cuerpo principal del mensaje; solo si es del tipo `TYPEMULTIPART`, los cuerpos siguientes serán tratados; estos cuerpos constituyen los cuerpos de las partes.

| Clave | Tipo | Descripción |
|----|----|----|
| `type` | `int` | El tipo MIME. Uno de `TYPETEXT` (por omisión), `TYPEMULTIPART`, `TYPEMESSAGE`, `TYPEAPPLICATION`, `TYPEAUDIO`, `TYPEIMAGE`, `TYPEMODEL` o `TYPEOTHER`. |
| `encoding` | `int` | El `Content-Transfer-Encoding`. Uno de `ENC7BIT` (por omisión), `ENC8BIT`, `ENCBINARY`, `ENCBASE64`, `ENCQUOTEDPRINTABLE` o `ENCOTHER`. |
| `charset` | `string` | El juego de caracteres del parámetro del tipo MIME. |
| `type.parameters` | `array` | Un array asociativo de nombre de parámetro `Content-Type` y sus valores. |
| `subtype` | `string` | El subtipo MIME, e.g. `'jpeg'` para `TYPEIMAGE`. |
| `id` | `string` | El `Content-ID`. |
| `description` | `string` | El `Content-Description`. |
| `disposition.type` | `string` | El `Content-Disposition`, e.g. `'attachment'`. |
| `disposition` | `array` | Un array asociativo de nombre de parámetro `Content-Disposition` y sus valores. |
| `contents.data` | `string` | La carga útil. |
| `lines` | `int` | El tamaño de la carga útil en líneas. |
| `bytes` | `int` | El tamaño de la carga útil en bytes. |
| `md5` | `string` | La checksum MD5 de la carga útil. |

Estructura de un Array de un Cuerpo

## Valores devueltos

Devuelve el mensaje MIME como un `string`, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `imap_mail_compose`

```
<?php

$envelope["from"]= "joe@example.com";
$envelope["to"]  = "foo@example.com";
$envelope["cc"]  = "bar@example.com";

$part1["type"] = TYPEMULTIPART;
$part1["subtype"] = "mixed";

$filename = "/tmp/imap.c.gz";
$fp = fopen($filename, "r");
$contents = fread($fp, filesize($filename));
fclose($fp);

$part2["type"] = TYPEAPPLICATION;
$part2["encoding"] = ENCBINARY;
$part2["subtype"] = "octet-stream";
$part2["description"] = basename($filename);
$part2["contents.data"] = $contents;

$part3["type"] = TYPETEXT;
$part3["subtype"] = "plain";
$part3["description"] = "description3";
$part3["contents.data"] = "contents.data3\n\n\n\t";

$body[1] = $part1;
$body[2] = $part2;
$body[3] = $part3;

echo nl2br(imap_mail_compose($envelope, $body));

?>

    
```php
