---
title: curl_pause
description: Pone en pausa, o saca de la pausa una conexión
source_url: https://www.php.net/manual/es/function.curl-pause.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-pause.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 10020
---

curl_pause

Pone en pausa, o saca de la pausa una conexión

## Descripción

```php
curl_pause(CurlHandle $handle, int $flags): int
```php

Pone en pausa o reanuda una sesión cURL. Una sesión puede ser pausada mientras se realiza una transferencia, en las direcciones de lectura, escritura o ambas, llamando a esta función desde una función de devolución de llamada registrada con la función `curl_setopt`.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

`flags`  
Una constante entre `CURLPAUSE_*`.

## Valores devueltos

Devuelve un código de error (`CURLE_OK` corresponde a ninguna error).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |
