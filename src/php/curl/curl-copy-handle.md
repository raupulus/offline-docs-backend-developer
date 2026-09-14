---
title: curl_copy_handle
description: Copia un recurso cURL con todas sus preferencias
source_url: https://www.php.net/manual/es/function.curl-copy-handle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-copy-handle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 9840
---

curl_copy_handle

Copia un recurso cURL con todas sus preferencias

## Descripción

```php
curl_copy_handle(CurlHandle $handle): CurlHandle
```php

Copia un recurso cURL, devolviendo un nuevo recurso cURL con las mismas preferencias.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

Devuelve un nuevo recurso cURL, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `CurlHandle`; anteriormente se devolvía un`resource`. |

## Ejemplos

Copia de un recurso cURL

```
<?php
// crea un nuevo recurso cURL
$ch = curl_init();

// asigna URL y otras opciones apropiadas
curl_setopt($ch, CURLOPT_URL, 'http://www.example.com/');
curl_setopt($ch, CURLOPT_HEADER, 0);

// copia el recurso
$ch2 = curl_copy_handle($ch);

// captura la URL (http://www.example.com/) y la envía al navegador
curl_exec($ch2);
?>

    
```php
