---
title: curl_setopt_array
description: Establece múltiples opciones para una transferencia cURL
source_url: https://www.php.net/manual/es/function.curl-setopt-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-setopt-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 10040
---

curl_setopt_array

Establece múltiples opciones para una transferencia cURL

## Descripción

```php
curl_setopt_array(CurlHandle $handle, array $options): bool
```php

Establece múltiples opciones para una sesión cURL. Esta función es útil para configurar un gran número de opciones cURL sin llamar a cada vez `curl_setopt`.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

`options`  
Un `array` que especifica qué opciones establecer con sus valores. Las claves deberían ser constantes válidas de `curl_setopt` o sus enteros equivalentes.

## Valores devueltos

Devuelve `true` si todas las opciones se establecieron correctamente. Si una opción no puede ser establecida correctamente, `false` es devuelto inmediatamente, ignorando todas las opciones futuras en el array `options`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Inicialización de una nueva sesión cURL y recuperación de una página web

```
<?php
// crea un nuevo recurso cURL
$ch = curl_init();

// establece la URL y otras opciones apropiadas
$options = array(CURLOPT_URL => 'http://www.example.com/',
                 CURLOPT_HEADER => false
                );

curl_setopt_array($ch, $options);

// captura la URL y la pasa al navegador
curl_exec($ch);
?>

    
```php

## Notas

> [!NOTE]
> Con la función `curl_setopt`, el hecho de pasar un array como valor de la constante `CURLOPT_POST` hará que los datos sean codificados como *multipart/form-data*, mientras que el hecho de pasar una string codificada URL hará que los datos sean codificados como *application/x-www-form-urlencoded*.

## Véase también

`curl_setopt`
