---
title: iconv_mime_encode
description: Construye un encabezado MIME con los campos field_name y field_value
source_url: https://www.php.net/manual/es/function.iconv-mime-encode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv-mime-encode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: ab9a7d2e3
order: 31200
---

iconv_mime_encode

Construye un encabezado MIME con los campos field_name y field_value

## Descripción

```php
iconv_mime_encode(string $field_name, string $field_value, [array $options]): string
```php

`iconv_mime_encode` compone y devuelve una cadena de caracteres que representa un campo encabezado `MIME` similar a:

    Subject: =?ISO-8859-1?Q?Pr=FCfung_f=FCr?= Entwerfen von einer MIME kopfzeile

       

En el ejemplo anterior, `"Subject"` es el nombre del campo y la parte que comienza por `"=?ISO-8859-1?..."` es el valor del campo.

## Parámetros

`field_name`  
El nombre del campo.

`field_value`  
El valor del campo.

`options`  
Puede controlarse el comportamiento de la función `iconv_mime_encode` especificando un array asociativo que contenga la configuración de los elementos en el parámetro `options`. La lista de elementos soportados por `iconv_mime_encode` se muestra a continuación. Tenga en cuenta que los nombres de los elementos son sensibles a mayúsculas/minúsculas.

| Elemento | Tipo | Descripción | Valor por omisión | Ejemplo |
|----|----|----|----|----|
| scheme | `string` | Especifica el método de codificación de un campo. Los valores posibles son `"B"` o `"Q"`, donde `"B"` indica que el esquema de codificación será `base64` y `"Q"`, `quoted-printable`. | B | B |
| input-charset | `string` | Especifica el juego de caracteres para representar el primer parámetro `field_name` y el segundo parámetro `field_value`. Si se omite, `iconv_mime_encode` utilizará la directiva de configuración [iconv.internal_encoding](#iconv.configuration) de su php.ini para representarlos. | [iconv.internal_encoding](#iconv.configuration) | ISO-8859-1 |
| output-charset | `string` | Especifica el juego de caracteres a utilizar para componer el encabezado `MIME`. | [iconv.internal_encoding](#iconv.configuration) | UTF-8 |
| line-length | `int` | Especifica la longitud máxima de cada encabezado. Si el encabezado es mayor que la longitud definida por este parámetro, el encabezado resultante será un encabezado compuesto por varias líneas conforme al estándar [RFC2822 - Internet Message Format](https://datatracker.ietf.org/doc/html/rfc2822). Si se omite, la longitud máxima se establecerá en 76 caracteres. | 76 | 996 |
| line-break-chars | `string` | Especifica los caracteres de fin de línea. Si se omite, el valor por omisión será `"\r\n"` (`CR` `LF`). Tenga en cuenta que este parámetro siempre se representa como una cadena ASCII en relación con el valor del parámetro `input-charset`. | \r\n | \n |

Lista de elementos soportados por `iconv_mime_encode`

## Valores devueltos

Devuelve un campo `MIME` en caso de éxito, o `false` si ocurre un error durante la codificación.

## Ejemplos

Ejemplo con `iconv_mime_encode`

```
<?php
$preferences = array(
    "input-charset" => "ISO-8859-1",
    "output-charset" => "UTF-8",
    "line-length" => 76,
    "line-break-chars" => "\n"
);
$preferences["scheme"] = "Q";
// Esto produce "Subject: =?UTF-8?Q?Pr=C3=BCfung=20Pr=C3=BCfung?="
echo iconv_mime_encode("Subject", "Prüfung Prüfung", $preferences);

$preferences["scheme"] = "B";
// Esto produce "Subject: =?UTF-8?B?UHLDvGZ1bmcgUHLDvGZ1bmc=?="
echo iconv_mime_encode("Subject", "Prüfung Prüfung", $preferences);
?>

    
```php

## Véase también

`imap_binary`, `mb_encode_mimeheader`, `imap_8bit`, `quoted_printable_encode`
