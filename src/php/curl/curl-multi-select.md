---
title: curl_multi_select
description: Espera hasta que la lectura o la escritura sea posible para cualquier
  conexión de gestor cURL multi
source_url: https://www.php.net/manual/es/function.curl-multi-select.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-select.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: f414967c2
order: 9990
---

curl_multi_select

Espera hasta que la lectura o la escritura sea posible para cualquier conexión de gestor cURL multi

## Descripción

```php
curl_multi_select(CurlMultiHandle $multi_handle, [float $timeout]): int
```php

Bloquea la ejecución del script hasta que un gestor cURL asociado al gestor cURL multi pueda progresar durante la próxima llamada a `curl_multi_exec` o hasta que expire el tiempo de espera (según lo que ocurra primero).

## Parámetros

`multi_handle`  
Un gestor múltiple cURL devuelto por `curl_multi_init`.

`timeout`  
Duración máxima, en segundos, para esperar una respuesta de las conexiones activas del gestor cURL multi.

## Valores devueltos

En caso de éxito, devuelve el número de descriptores activos contenidos en los conjuntos de descriptores. Esto puede ser `0` si no ha habido actividad en ninguno de los descriptores. En caso de error, esta función devolverá `-1` en caso de fallo de selección (de la llamada al sistema `select()` subyacente).

## Errores/Excepciones

Genera una ValueError si `timeout` es inferior a `0` o superior a `PHP_INT_MAX`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Genera ahora una ValueError si `timeout` es inferior a `0` o superior a `PHP_INT_MAX`. |
| 8.0.0 | `multi_handle` ahora espera una instancia de `CurlMultiHandle` ; anteriormente, se esperaba un `resource`. |

## Véase también

`curl_multi_init`
