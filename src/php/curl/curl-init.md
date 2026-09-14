---
title: curl_init
description: Inicializa una sesión cURL
source_url: https://www.php.net/manual/es/function.curl-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 61f65786e
order: 9900
---

curl_init

Inicializa una sesión cURL

## Descripción

```php
curl_init([string $url]): CurlHandle
```php

Inicializa una nueva sesión y devuelve un manejador cURL.

## Parámetros

`url`  
Si se proporciona, entonces `CURLOPT_URL` tomará este valor. Esto puede ser configurado manualmente utilizando la función `curl_setopt`.

> [!NOTE]
> El protocolo `file` está desactivado por cURL si [open_basedir](#ini.open-basedir) está definido.

## Valores devueltos

Devuelve una sesión cURL en caso de éxito, `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función devuelve ahora una instancia de `CurlHandle`; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `url` ahora es nullable. |

## Ejemplos

Inicializar una sesión cURL y recuperar una página web

```
<?php

// Inicializa una nueva sesión cURL
$ch = curl_init();

// Definir la URL y otras opciones apropiadas
curl_setopt($ch, CURLOPT_URL, "http://www.example.com/");
curl_setopt($ch, CURLOPT_HEADER, 0);

// Recuperar la URL y pasarla al navegador
curl_exec($ch);

?>

    
```php

## Véase también

`curl_multi_init`
