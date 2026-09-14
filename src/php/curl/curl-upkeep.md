---
title: curl_upkeep
description: Realiza los controles de mantenimiento de la conexión
source_url: https://www.php.net/manual/es/function.curl_upkeep.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-upkeep.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 10140
---

curl_upkeep

Realiza los controles de mantenimiento de la conexión

## Descripción

```php
curl_upkeep(CurlHandle $handle): bool
```php

Disponible si construido con libcurl \>= 7.62.0.

Algunos protocolos tienen mecanismos de "mantenimiento de la conexión". Estos mecanismos generalmente envían tráfico sobre las conexiones existentes para mantenerlas vivas; Esto permite, por ejemplo, evitar que las conexiones sean cerradas debido a firewalls demasiado celosos.

El mantenimiento de la conexión está actualmente disponible solo para las conexiones HTTP/2. Una pequeña cantidad de tráfico es generalmente enviada para mantener una conexión viva. HTTP/2 mantiene su conexión enviando una trama HTTP/2 PING.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `curl_upkeep`

```
<?php
$url = "https://example.com";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTP_VERSION,CURL_HTTP_VERSION_2_0);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_UPKEEP_INTERVAL_MS, 200);
if (curl_exec($ch)) {
    usleep(300);
    var_dump(curl_upkeep($ch));
}
?>

    
```php

## Véase también

`curl_init`
