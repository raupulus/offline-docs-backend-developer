---
title: mb_send_mail
description: Envía un correo electrónico codificado
source_url: https://www.php.net/manual/es/function.mb-send-mail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-send-mail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45380
---

mb_send_mail

Envía un correo electrónico codificado

## Descripción

```php
mb_send_mail(string $to, string $subject, string $message, [array $additional_headers], [string $additional_params]): bool
```php

Envía un correo electrónico. Los encabezados y el cuerpo del mensaje son convertidos y codificados de acuerdo con `mb_language`. `mb_send_mail` es una versión adaptada de `mail`. Consulte la función `mail` para más detalles.

## Parámetros

`to`  
`to` es la dirección de destino del correo. Las direcciones múltiples pueden especificarse separándolas con comas. Este parámetro no es codificado automáticamente.

`subject`  
El asunto del correo.

`message`  
El mensaje del correo.

`additional_headers` (opcional)  
`string` o `array` a insertar al final del encabezado del correo.

Este parámetro se utiliza típicamente para añadir encabezados adicionales (From, Cc, y Bcc). Los diferentes añadidos deben separarse con un CRLF (\r\n). Este parámetro debe ser validado para evitar la inyección de encabezados no deseados por personas malintencionadas.

Si se proporciona un `array`, sus claves son los nombres de los encabezados y sus valores son los valores respectivos de los encabezados.

> [!NOTE]
> Al enviar un correo, *debe* contener un encabezado `From`. Puede ser definido mediante el parámetro `additional_headers` o como valor por defecto en el `php.ini`.
>
> Si no se hace, se emitirá un error similar a: `Warning: mail(): "sendmail_from" not set in php.ini or custom "From:" header missing`. El encabezado `From` también define `Return-Path` en Windows.

> [!NOTE]
> Si los mensajes no son recibidos, intente utilizar únicamente un LF (\n). Algunos agentes de transferencia de correos Unix (en particular [qmail](http://cr.yp.to/qmail.html)) reemplazan un LF por un CRLF automáticamente (lo que resulta en un doble CR si se utiliza CRLF). Debe intentar esta corrección en último lugar, sabiendo que no cumple con la [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822).

`additional_params`  
`additional_params` es una línea de parámetros MTA. Es práctico cuando se quiere definir un `Return-Path` correcto cuando se utiliza `sendmail`.

Este parámetro es escapado por la función `escapeshellcmd` internamente para prevenir la ejecución de comandos. La función `escapeshellcmd` previene la ejecución de comandos, pero permite parámetros adicionales. Por razones de seguridad, este parámetro debe ser validado.

Dado que la función `escapeshellcmd` se aplica automáticamente internamente, algunos caracteres permitidos en las direcciones de correo por los RFCs de Internet ya no pueden ser utilizados. Los programas que necesiten utilizar estos caracteres, la función `mail` ya no puede ser utilizada.

El usuario que ejecuta el servidor web debe ser añadido como usuario de confianza en la configuración de envío de correos para evitar la adición de un encabezado 'X-Warning' en el mensaje cuando el remitente de la envelope (-f) es definido utilizando este método. Para los usuarios de sendmail, este archivo se encuentra utilizando la ruta `/etc/mail/trusted-users`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                                |
|---------|------------------------------------------------------------|
| 8.0.0   | `additional_params` ahora es nullable.                     |
| 7.2.0   | El parámetro `additional_headers` ahora acepta un `array`. |

## Véase también

`mail`, `mb_encode_mimeheader`, `mb_language`
