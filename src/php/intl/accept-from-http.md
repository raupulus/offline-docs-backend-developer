---
title: Locale::acceptFromHttp
description: Determina la mejor configuración local a partir del encabezado HTTP "Accept-Language"
source_url: https://www.php.net/manual/es/locale.acceptfromhttp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/accept-from-http.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41820
---

Locale::acceptFromHttp

locale_accept_from_http

Determina la mejor configuración local a partir del encabezado HTTP

"Accept-Language"

## Descripción

Estilo orientado a objetos

```php
public static Locale::acceptFromHttp(string $header): string
```php

Estilo procedimental

```php
locale_accept_from_http(string $header): string
```

Intenta encontrar una configuración local que pueda satisfacer la lista de idiomas solicitada por el encabezado HTTP `"Accept-Language"`.

## Parámetros

`header`  
La cadena que contiene el encabezado `"Accept-Language"`, en el formato de la RFC 2616.

## Valores devueltos

El identificador de configuración local correspondiente.

Devuelve `false` cuando la longitud de `header` excede `INTL_MAX_LOCALE_LEN`.

## Ejemplos

Ejemplo con `locale_accept_from_http`, procedimental

```php
<?php
$locale = locale_accept_from_http($_SERVER['HTTP_ACCEPT_LANGUAGE']);
echo $locale;
?>

   
```

Ejemplo con `locale_accept_from_http`, POO

```php
<?php
$locale = Locale::acceptFromHttp($_SERVER['HTTP_ACCEPT_LANGUAGE']);
echo $locale;
?>

   
```

El ejemplo anterior mostrará:

    en_US

      

## Véase también

`locale_lookup`
