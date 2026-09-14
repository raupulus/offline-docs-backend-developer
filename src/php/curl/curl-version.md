---
title: curl_version
description: Devuelve la versión actual de cURL
source_url: https://www.php.net/manual/es/function.curl-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: true
translation_revision: fd45557ea
order: 10150
---

curl_version

Devuelve la versión actual de cURL

## Descripción

```php
curl_version(): array
```php

Devuelve información sobre la versión de cURL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array asociativo que contiene los siguientes elementos:

| Clave | Descripción del valor |
|----|----|
| version_number | número de versión de cURL de 24 bits |
| version | número de versión de cURL, en forma de string |
| ssl_version_number | número de versión de OpenSSL de 24 bits |
| ssl_version | número de versión de OpenSSL, en forma de string |
| libz_version | número de versión de zlib, en forma de string |
| host | Información sobre el host en el que se construyó cURL |
| age |  |
| features | Una máscara de constantes `CURL_VERSION_*` |
| protocols | Un array de nombres de protocolos soportados por cURL |
| feature_list | Un array asociativo de todas las funcionalidades de cURL conocidas, y si son soportadas (`true`) o no (`false`). |

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `features_list` añadido. |
| 8.0.0 | El argumento opcional `age` ha sido eliminado. |
| 7.4.0 | El argumento opcional `age` está deprecado; si se proporciona un valor, es ignorado. |

## Ejemplos

Ejemplo con `curl_version`

Este ejemplo analiza las funcionalidades disponibles en la versión actual de cURL utilizando la máscara `'features'` devuelta por la función `curl_version`.

```
<?php
// Obtiene la versión de cURL, en forma de array
$version = curl_version();

// Estos son los campos que pueden ser utilizados
// para verificar las funcionalidades presentes en cURL
$bitfields = Array(
             'CURL_VERSION_IPV6',
             'CURL_VERSION_KERBEROS4',
             'CURL_VERSION_SSL',
             'CURL_VERSION_LIBZ'
             );

foreach($bitfields as $feature)
{
    echo $feature . ($version['features'] & constant($feature) ? ' presente' : ' ausente');
    echo PHP_EOL;
}
?>

    
```php
