---
title: rawurlencode
description: Codificar estilo URL de acuerdo al RFC 3986
source_url: https://www.php.net/manual/es/function.rawurlencode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/rawurlencode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_reviewed: false
translation_revision: f9c4a68ef
order: 100260
---

rawurlencode

Codificar estilo URL de acuerdo al RFC 3986

## Descripción

```php
rawurlencode(string $string): string
```php

Codifica la cadena dada de acuerdo al [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986).

## Parámetros

`string`  
La URL a ser codificada.

## Valores devueltos

Devuelve una cadena en donde todos los caracteres no-alfanuméricos, excepto `-_.~`, son reemplazados con un signo de porcentaje (`%`) seguido de dos dígitos hexadecimales. Este es el tipo de codificación descrito en el [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986) para evitar que caracteres literales sean interpretados como delimitadores de URL especiales, y para evitar que las URLs sean modificadas por medios de transmisión con conversiones de caracteres (como algunos sistemas de correo electrónico).

## Ejemplos

Inclusión de una contraseña en una URL FTP

```
<?php
echo '<a href="ftp://user:', rawurlencode('foo @+%/'),
     '@ftp.example.com/x.txt">';
?>

    
```php

El ejemplo anterior mostrará:

```
<a href="ftp://user:foo%20%40%2B%25%2F@ftp.example.com/x.txt">

    
```php

O, si pasa información en un componente PATH_INFO de la URL:

Ejemplo 2 de `rawurlencode`

```
<?php
echo '<a href="http://example.com/department_list_script/',
    rawurlencode('sales and marketing/Miami'), '">';
?>

    
```php

El ejemplo anterior mostrará:

```
<a href="http://example.com/department_list_script/sales%20and%20marketing%2FMiami">

    
```php

## Véase también

`rawurldecode`, `urldecode`, `urlencode`, [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)
