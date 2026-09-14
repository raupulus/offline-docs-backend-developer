---
title: iconv_mime_decode
description: Decodifica un campo de encabezado MIME
source_url: https://www.php.net/manual/es/function.iconv-mime-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv-mime-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: ab9a7d2e3
order: 31190
---

iconv_mime_decode

Decodifica un campo de encabezado MIME

## Descripción

```php
iconv_mime_decode(string $string, [int $mode], [string $encoding]): string
```php

`iconv_mime_decode` decodifica un campo de encabezado MIME.

## Parámetros

`string`  
El encabezado codificado, en forma de `string`.

`mode`  
`mode` determina una alternativa en caso de que `iconv_mime_decode` encuentre un campo de encabezado `MIME` mal formado.

| Valor | Constante | Descripción |
|----|----|----|
| 1 | ICONV_MIME_DECODE_STRICT | Si está definido, el encabezado correspondiente será decodificado siguiendo estrictamente el estándar [RFC2047](https://datatracker.ietf.org/doc/html/rfc2047). Esta opción está desactivada por omisión, ya que existen muchos `clientes de correo` que no siguen este estándar y por lo tanto, producen malos encabezados `MIME`. |
| 2 | ICONV_MIME_DECODE_CONTINUE_ON_ERROR | Si está definido, `iconv_mime_decode` intenta continuar decodificando el encabezado pasado, incluso si aparecen errores. |

Máscaras aceptables para la función `iconv_mime_decode`

`encoding`  
El parámetro por omisión `encoding` especifica el juego de caracteres a utilizar para representar el resultado. Si se omite, [iconv.internal_encoding](#iconv.configuration) será utilizado.

## Valores devueltos

Devuelve un campo `MIME` en caso de éxito, o `false` si ocurre un error durante la decodificación.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `encoding` ahora es nullable. |

## Ejemplos

Ejemplo con `iconv_mime_decode`

```
<?php
// Esto mostrará: "Subject: Prüfung Prüfung"
echo iconv_mime_decode("Subject: =?UTF-8?B?UHLDvGZ1bmcgUHLDvGZ1bmc=?=",
                       0, "ISO-8859-1");
?>

    
```php

## Véase también

`iconv_mime_decode_headers`, `mb_decode_mimeheader`, `imap_mime_header_decode`, `imap_base64`, `imap_qprint`
