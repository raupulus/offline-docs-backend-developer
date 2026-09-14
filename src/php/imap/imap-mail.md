---
title: imap_mail
description: Envía un mensaje de correo electrónico
source_url: https://www.php.net/manual/es/function.imap-mail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-mail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 38330
---

imap_mail

Envía un mensaje de correo electrónico

## Descripción

```php
imap_mail(string $to, string $subject, string $message, [string $additional_headers], [string $cc], [string $bcc], [string $return_path]): bool
```php

`imap_mail` permite enviar correos electrónicos con una gestión correcta de los destinatarios Cc y Bcc.

Los parámetros `to`, `cc` y `bcc` son todos strings y son analizados como listas de direcciones [RFC822](https://datatracker.ietf.org/doc/html/rfc822).

## Parámetros

`to`  
El destinatario

`subject`  
El asunto del correo

`message`  
El cuerpo del correo; ver la función `imap_mail_compose`.

`additional_headers`  
Un string conteniendo los encabezados adicionales a enviar con el correo

`cc`  

`bcc`  
Los destinatarios especificados en el `bcc` recibirán el correo pero son excluidos de los encabezados.

`return_path`  
Utilizar este parámetro para especificar el camino de retorno en caso de fallo en la entrega del correo. Es útil cuando se utiliza PHP como cliente de correo para varios usuarios.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `additional_headers`, `cc`, `bcc`, y `return_path` son ahora nullable. |

## Véase también

`mail`, `imap_mail_compose`
