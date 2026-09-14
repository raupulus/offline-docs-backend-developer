---
title: OAuth::fetch
description: Lee un recurso protegido por OAuth
source_url: https://www.php.net/manual/es/oauth.fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: true
translation_revision: bdee7e8c1
order: 56730
---

OAuth::fetch

Lee un recurso protegido por OAuth

## Descripción

```php
public OAuth::fetch(string $protected_resource_url, [array $extra_parameters], [string $http_method], [array $http_headers]): mixed
```php

Lee un recurso protegido por OAuth.

## Parámetros

`protected_resource_url`  
URL del recurso protegido por OAuth.

`extra_parameters`  
Argumentos adicionales a enviar con la petición, al recurso.

`http_method`  
Una de las constantes `OAUTH_HTTP_METHOD_*` OAUTH, incluyendo GET, POST, PUT, HEAD, o DELETE.

HEAD (`OAUTH_HTTP_METHOD_HEAD`) puede ser útil para descubrir información antes de la petición (si las autorizaciones OAuth están en el encabezado `Authorization`).

`http_headers`  
Los encabezados HTTP del cliente (tales como `User-Agent`, `Accept`, etc.)

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL oauth 1.0.0 | Antes de esta versión, `null` era devuelto en lugar de `false`. |
| PECL oauth 0.99.5 | Se añadió el argumento `http_method` |
| PECL oauth 0.99.8 | Se añadió el argumento `http_headers` |

## Ejemplos

Ejemplo con `OAuth::fetch`

```
<?php
try {
    $oauth = new OAuth("consumer_key","consumer_secret",OAUTH_SIG_METHOD_HMACSHA1,OAUTH_AUTH_TYPE_AUTHORIZATION);
    $oauth->setToken("access_token","access_token_secret");

    $oauth->fetch("http://photos.example.net/photo?file=vacation.jpg");

    $response_info = $oauth->getLastResponseInfo();
    header("Content-Type: {$response_info["content_type"]}");
    echo $oauth->getLastResponse();
} catch(OAuthException $E) {
    echo "Exception caught!\n";
    echo "Response: ". $E->lastResponse . "\n";
}
?>

   
```php

## Véase también

OAuth::getLastResponse

OAuth::getLastResponseInfo

OAuth::setToken
