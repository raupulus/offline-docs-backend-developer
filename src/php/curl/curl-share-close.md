---
title: curl_share_close
description: Cierra un manejador compartido cURL
source_url: https://www.php.net/manual/es/function.curl-share-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-share-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: 29c3d1398
order: 10060
---

curl_share_close

Cierra un manejador compartido cURL

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] curl_share_close(CurlShareHandle $share_handle): void
```php

> [!NOTE]
> Esta función no tiene ningún efecto. Anterior a PHP 8.0.0, esta función era utilizada para cerrar un recurso.

Cierra un manejador compartido cURL y libera todos los recursos.

## Parámetros

`share_handle`  
Un gestor compartido cURL devuelto por `curl_share_init`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Esta función ha sido declarada obsoleta. |
| 8.0.0 | Esta función es ahora una NOP. |
| 8.0.0 | `share_handle` ahora espera una instancia de `CurlShareHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `curl_share_setopt`

Este ejemplo crea un manejador compartido cURL, añade dos manejadores cURL, y luego los ejecuta con cookies de datos compartidos.

```
<?php
// Crea un manejador compartido cURL, y lo define para compartir cookies de datos
$sh = curl_share_init();
curl_share_setopt($sh, CURLSHOPT_SHARE, CURL_LOCK_DATA_COOKIE);

// Inicializa el primer manejador cURL, y le asigna el manejador compartido
$ch1 = curl_init("http://example.com/");
curl_setopt($ch1, CURLOPT_SHARE, $sh);

// Ejecuta el primer manejador cURL
curl_exec($ch1);

// Inicializa el segundo manejador cURL, y le asigna el manejador compartido
$ch2 = curl_init("http://php.net/");
curl_setopt($ch2, CURLOPT_SHARE, $sh);

// Ejecuta el segundo manejador cURL.
// Todas las cookies del manejador $ch1 son compartidas con el manejador $ch2.
curl_exec($ch2);

// Cierra el manejador compartido cURL
curl_share_close($sh);
?>

    
```php

## Véase también

`curl_share_init`
