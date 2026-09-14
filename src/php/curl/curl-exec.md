---
title: curl_exec
description: Ejecuta una sesión cURL
source_url: https://www.php.net/manual/es/function.curl-exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 9880
---

curl_exec

Ejecuta una sesión cURL

## Descripción

```php
curl_exec(CurlHandle $handle): string
```php

Ejecuta la sesión cURL proporcionada.

Esta función debe llamarse después de inicializar una sesión cURL y de que todas las opciones de la sesión estén configuradas.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

En caso de éxito, esta función vacía el resultado directamente en `stdout` y devuelve `true`, o `false` si ocurre un error. Sin embargo, si `CURLOPT_RETURNTRANSFER` está [definida](#function.curl-setopt), la función devolverá el resultado en caso de éxito, y `false` en caso de fallo.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

> [!NOTE]
> Tenga en cuenta que los códigos de estado de una respuesta que indican errores (como `404 Not found`) no se consideran fallos. `curl_getinfo` puede ser utilizado para verificar estos casos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Recupera el contenido de una página web

```
<?php
// Creación de un nuevo recurso cURL
$ch = curl_init();

// Configuración de la URL y otras opciones
curl_setopt($ch, CURLOPT_URL, "http://www.example.com/");
curl_setopt($ch, CURLOPT_HEADER, 0);

// Recuperación de la URL y visualización en el navegador
curl_exec($ch);
?>

    
```php

## Véase también

`curl_multi_exec`
