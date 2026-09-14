---
title: curl_close
description: Cierra una sesión CURL
source_url: https://www.php.net/manual/es/function.curl-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: 86c8ebd19
order: 9830
---

curl_close

Cierra una sesión CURL

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] curl_close(CurlHandle $handle): void
```php

> [!NOTE]
> Esta función no tiene ningún efecto. Anterior a PHP 8.0.0, esta función era utilizada para cerrar un recurso.

Cierra una sesión cURL y libera todos los recursos. El identificador cURL, `handle`, también es borrado.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Esta función ha sido declarada obsoleta. |
| 8.0.0 | Esta función es ahora una NOP. |
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Inicializa una sesión cURL y recupera una página web

```
<?php
// creación de un nuevo recurso cURL
$ch = curl_init();

// configuración de la URL y otras opciones
curl_setopt($ch, CURLOPT_URL, "http://www.example.com/");
curl_setopt($ch, CURLOPT_HEADER, 0);

// recuperación de la URL y visualización en el navegador
curl_exec($ch);

// cierre de la sesión cURL
curl_close($ch);
?>

    
```php

## Véase también

`curl_init`, `curl_multi_close`
