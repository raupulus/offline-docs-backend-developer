---
title: iconv_mime_decode_headers
description: Decodifica múltiples encabezados MIME
source_url: https://www.php.net/manual/es/function.iconv-mime-decode-headers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv-mime-decode-headers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: false
translation_revision: 16a1bdfd1
order: 31180
---

iconv_mime_decode_headers

Decodifica múltiples encabezados

MIME

## Descripción

```php
iconv_mime_decode_headers(string $headers, [int $mode], [string $encoding]): array
```php

`iconv_mime_decode_headers` decodifica múltiples encabezados `MIME`.

## Parámetros

`headers`  
Los encabezados codificados, en forma de `string`.

`mode`  
`mode` determina el comportamiento de la función, si `iconv_mime_decode_headers` encuentra un encabezado `MIME` malformado.

| Valor | Constante | Descripción |
|----|----|----|
| 1 | ICONV_MIME_DECODE_STRICT | Si se utiliza, los encabezados son decodificados respetando estrictamente el estándar de la [RFC2047](https://datatracker.ietf.org/doc/html/rfc2047). Esta opción está desactivada por omisión, ya que existen numerosos clientes de correo que no siguen estas especificaciones y que no producen encabezados `MIME` correctos. |
| 2 | ICONV_MIME_DECODE_CONTINUE_ON_ERROR | Si esta opción está activada, `iconv_mime_decode_headers` intenta ignorar los errores de sintaxis y continúa procesando el encabezado dado. |

Mascara aceptada por la función `iconv_mime_decode_headers`

`encoding`  
El parámetro opcional `encoding` especifica el juego de caracteres utilizado para representar el resultado. Si se omite, se utiliza el juego definido en el archivo `php.ini` [iconv.internal_encoding](#iconv.configuration).

## Valores devueltos

Devuelve un array asociativo que contiene los encabezados `MIME` especificados por el parámetro `headers`, o bien `false` si ocurre un error durante el decodificado.

Cada clave del array devuelto contiene un nombre de encabezado distinto, y su valor correspondiente. Si varios campos tienen el mismo nombre, `iconv_mime_decode_headers` convierte ese campo en un array indexado, con los valores en su orden de aparición. Cabe señalar que los nombres de los encabezados no son *insensibles a mayúsculas/minúsculas*.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `encoding` ahora es nullable. |

## Ejemplos

Ejemplo con `iconv_mime_decode_headers`

```
<?php
$headers_string = <<<EOF
Subject: =?UTF-8?B?UHLDvGZ1bmcgUHLDvGZ1bmc=?=
To: example@example.com
Date: Thu, 1 Jan 1970 00:00:00 +0000
Message-Id: <example@example.com>
Received: from localhost (localhost [127.0.0.1]) by localhost
    with SMTP id example for <example@example.com>;
    Thu, 1 Jan 1970 00:00:00 +0000 (UTC)
    (envelope-from example-return-0000-example=example.com@example.com)
Received: (qmail 0 invoked by uid 65534); 1 Thu 2003 00:00:00 +0000

EOF;

$headers =  iconv_mime_decode_headers($headers_string, 0, "ISO-8859-1");
print_r($headers);
?>

     
```php

El ejemplo anterior mostrará:

    Array
    (
        [Subject] => Prüfung Prüfung
        [To] => example@example.com
        [Date] => Thu, 1 Jan 1970 00:00:00 +0000
        [Message-Id] => <example@example.com>
        [Received] => Array
            (
                [0] => from localhost (localhost [127.0.0.1]) by localhost with SMTP id example for <example@example.com>; Thu, 1 Jan 1970 00:00:00 +0000 (UTC) (envelope-from example-return-0000-example=example.com@example.com)
                [1] => (qmail 0 invoked by uid 65534); 1 Thu 2003 00:00:00 +0000
            )

    )

## Véase también

`iconv_mime_decode`, `mb_decode_mimeheader`, `imap_mime_header_decode`, `imap_base64`, `imap_qprint`
