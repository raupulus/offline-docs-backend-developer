---
title: curl_getinfo
description: Obtiene información sobre una transferencia específica
source_url: https://www.php.net/manual/es/function.curl-getinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-getinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 9890
---

curl_getinfo

Obtiene información sobre una transferencia específica

## Descripción

```php
curl_getinfo(CurlHandle $handle, [int $option]): mixed
```php

Obtiene información sobre la última transferencia.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

`option`  
Una de las constantes `CURLINFO_*`.

## Valores devueltos

Si `option` es proporcionado, el valor será devuelto. De lo contrario, será un array asociativo conteniendo los siguientes elementos (que corresponden a `option`), o `false` si ocurre un error:

- "url"

- "content_type"

- "http_code"

- "header_size"

- "request_size"

- "filetime"

- "ssl_verify_result"

- "redirect_count"

- "total_time"

- "namelookup_time"

- "connect_time"

- "pretransfer_time"

- "size_upload"

- "size_download"

- "speed_download"

- "speed_upload"

- "download_content_length"

- "upload_content_length"

- "starttransfer_time"

- "redirect_time"

- "certinfo"

- "primary_ip"

- "primary_port"

- "local_ip"

- "local_port"

- "redirect_url"

- "request_header" (Solo existe si `CURLINFO_HEADER_OUT` es utilizado mediante una llamada a `curl_setopt`)

- "posttransfer_time_us" (Disponible a partir de PHP 8.4.0 y cURL 8.10.0)

Tenga en cuenta que los datos privados no están incluidos en el array asociativo y deben ser recuperados individualmente con la opción `CURLINFO_PRIVATE`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Introducción de la constante `CURLINFO_POSTTRANSFER_TIME_T` y de `posttransfer_time_us` (cURL 8.10.0 o versión posterior). |
| 8.3.0 | Introdujo `CURLINFO_CAINFO` y `CURLINFO_CAPATH`. |
| 8.2.0 | Introducción de las nuevas constantes `CURLINFO_PROXY_ERROR`, `CURLINFO_REFERER`, `CURLINFO_RETRY_AFTER`. |
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `option` ahora es nullable; anteriormente, el valor por omisión era `0`. |
| 7.3.0 | Añadido `CURLINFO_CONTENT_LENGTH_DOWNLOAD_T`, `CURLINFO_CONTENT_LENGTH_UPLOAD_T`, `CURLINFO_HTTP_VERSION`, `CURLINFO_PROTOCOL`, `CURLINFO_PROXY_SSL_VERIFYRESULT`, `CURLINFO_SCHEME`, `CURLINFO_SIZE_DOWNLOAD_T`, `CURLINFO_SIZE_UPLOAD_T`, `CURLINFO_SPEED_DOWNLOAD_T`, `CURLINFO_SPEED_UPLOAD_T`, `CURLINFO_APPCONNECT_TIME_T`, `CURLINFO_CONNECT_TIME_T`, `CURLINFO_FILETIME_T`, `CURLINFO_NAMELOOKUP_TIME_T`, `CURLINFO_PRETRANSFER_TIME_T`, `CURLINFO_REDIRECT_TIME_T`, `CURLINFO_STARTTRANSFER_TIME_T`, `CURLINFO_TOTAL_TIME_T`. |

## Ejemplos

Ejemplo con `curl_getinfo`

```
<?php
// Creación de un manejador cURL
$ch = curl_init('http://www.example.com/');

// Ejecución
curl_exec($ch);

// Verificación si ocurrió un error
if(!curl_errno($ch))
{
 $info = curl_getinfo($ch);

 echo 'La petición tardó ' . $info['total_time'] . ' segundos en ser enviada a ' . $info['url'];
}
?>

    
```php

Ejemplo de `curl_getinfo` con el parámetro `option`

```
<?php
// Creación de un manejador cURL
$ch = curl_init('http://www.example.com/');

// Ejecución
curl_exec($ch);

// Verificación del código de estado HTTP
if (!curl_errno($ch)) {
  switch ($http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE)) {
    case 200:  # OK
      break;
    default:
      echo 'Código HTTP inesperado: ', $http_code, "\n";
  }
}
?>

    
```php

## Notas

> [!NOTE]
> Las informaciones proporcionadas por esta función se conservan si la conexión es reutilizada. Los datos previamente utilizados son por lo tanto devueltos a menos que sean sobrescritos internamente entre tanto.
