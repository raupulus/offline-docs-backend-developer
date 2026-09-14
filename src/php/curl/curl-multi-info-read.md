---
title: curl_multi_info_read
description: Lee las informaciones sobre las transferencias actuales
source_url: https://www.php.net/manual/es/function.curl-multi-info-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-info-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 9960
---

curl_multi_info_read

Lee las informaciones sobre las transferencias actuales

## Descripción

```php
curl_multi_info_read(CurlMultiHandle $multi_handle, [int $queued_messages]): array
```php

Invoca el gestor múltiple si existen mensajes o informaciones provenientes de las transferencias individuales. Los mensajes pueden incluir informaciones como un código de error de la transferencia, o simplemente el hecho de que la transferencia ha finalizado.

Las llamadas repetidas a esta función devolverán un nuevo resultado cada vez, hasta que `false` no sea devuelto, indicando que no hay nada más que recuperar en este momento. El entero presente en el argumento `queued_messages` representa el número de mensajes restantes una vez llamada esta función.

> [!WARNING]
> Los datos apuntados por el recurso devuelto, no sobrevivirán a la llamada de la función `curl_multi_remove_handle`.

## Parámetros

`multi_handle`  
Un gestor múltiple cURL devuelto por `curl_multi_init`.

`queued_messages`  
Número de mensajes aún presentes en la cola

## Valores devueltos

Devuelve un array asociativo que contiene el mensaje en caso de éxito, `false` si ocurre un error.

| Clave: | Valor: |
|----|----|
| `msg` | La constante `CURLMSG_DONE`. Las demás valores devueltos no están actualmente disponibles. |
| `result` | Una de las constantes `CURLE_*`. Si todo ha transcurrido correctamente, se devolverá la constante `CURLE_OK`. |
| `handle` | Recurso de tipo curl que indica el gestor concernido. |

Contenido del array devuelto

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `multi_handle` ahora espera una instancia de `CurlMultiHandle` ; anteriormente, se esperaba un `resource`. |

## Véase también

`curl_multi_init`
