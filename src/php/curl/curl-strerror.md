---
title: curl_strerror
description: Devuelve la cadena descriptiva del código de error proporcionado
source_url: https://www.php.net/manual/es/function.curl-strerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-strerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 10120
---

curl_strerror

Devuelve la cadena descriptiva del código de error proporcionado

## Descripción

```php
curl_strerror(int $error_code): string
```php

Devuelve el mensaje de error que describe el código de error proporcionado.

## Parámetros

`error_code`  
Una constante entre las constantes [de los códigos de error cURL](http://curl.haxx.se/libcurl/c/libcurl-errors.html).

## Valores devueltos

Devuelve la descripción del error o `null` para un código de error inválido.

## Ejemplos

Ejemplo con `curl_errno`

```
<?php
// Crea un manejador curl con un error en el protocolo de la URL utilizada
$ch = curl_init("htp://example.com/");

// Envía la petición
curl_exec($ch);

// Verifica los errores y muestra el mensaje de error
if($errno = curl_errno($ch)) {
    $error_message = curl_strerror($errno);
    echo "Error cURL ({$errno}):\n {$error_message}";
}
?>

    
```php

El ejemplo anterior mostrará:

    Error cURL (1):
     Unsupported protocol

## Véase también

`curl_errno`, `curl_error`, [Los códigos de error Curl](http://curl.haxx.se/libcurl/c/libcurl-errors.html)
