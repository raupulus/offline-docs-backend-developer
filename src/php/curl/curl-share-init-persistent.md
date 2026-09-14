---
title: curl_share_init_persistent
description: Inicializa un gestor cURL "share" persistente
source_url: https://www.php.net/manual/es/function.curl-share-init-persistent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-share-init-persistent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 9e08f606a
order: 10080
---

curl_share_init_persistent

Inicializa un gestor cURL "share"

persistente

## Descripción

```php
curl_share_init_persistent(array $share_options): CurlSharePersistentHandle
```php

Inicializa un gestor cURL "share" **persistente** con las opciones de compartición dadas. A diferencia de `curl_share_init`, los gestores creados por esta función no serán destruidos al final de la petición PHP. Si se encuentra un gestor de compartición persistente con el mismo conjunto de `share_options`, será reutilizado.

## Parámetros

`share_options`  
Un array no vacío de constantes `CURL_LOCK_DATA_*`.

> [!NOTE]
> `CURL_LOCK_DATA_COOKIE` no está permitido y, si se especifica, esta función lanzará una ValueError. La compartición de cookies entre las peticiones PHP puede llevar a una mezcla involuntaria de cookies sensibles entre los usuarios.

## Valores devueltos

Devuelve un `CurlSharePersistentHandle`.

## Errores/Excepciones

- Si `share_options` está vacío, esta función lanza una ValueError.

- Si `share_options` contiene un valor que no corresponde a una `CURL_LOCK_DATA_*`, esta función lanza una `ValueError`.

- Si `share_options` contiene `CURL_LOCK_DATA_COOKIE`, esta función lanza una ValueError.

- Si `share_options` contiene un valor no entero, esta función lanza una TypeError.

## Ejemplos

Ejemplo de `curl_share_init_persistent`

Este ejemplo creará un gestor cURL "share" persistente y demostrará la compartición de conexiones entre ellos. Si se ejecuta en un SAPI PHP de larga duración, `$sh` sobrevivirá entre las peticiones SAPI.

```
    
<?php
// Crear o recuperar un gestor cURL "share" persistente configurado para compartir las búsquedas DNS y las conexiones
$sh = curl_share_init_persistent([CURL_LOCK_DATA_DNS, CURL_LOCK_DATA_CONNECT]);

// Inicializa el primer gestor cURL y le asigna el gestor de partage
$ch1 = curl_init("http://example.com/");
curl_setopt($ch1, CURLOPT_SHARE, $sh);

// Ejecuta el primer gestor cURL. Esto puede reutilizar la conexión de una petición SAPI anterior
curl_exec($ch1);

// Inicializa el segundo gestor cURL y le asigna el gestor de partage
$ch2 = curl_init("http://example.com/");
curl_setopt($ch2, CURLOPT_SHARE, $sh);

// Ejecuta el segundo gestor cURL. Esto puede reutilizar la conexión de $ch1
curl_exec($ch2);

?>

    
   
```php

## Véase también

curl_setopt

curl_share_init
