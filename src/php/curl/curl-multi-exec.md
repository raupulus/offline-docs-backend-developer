---
title: curl_multi_exec
description: Ejecuta las subpeticiones de la sesión cURL
source_url: https://www.php.net/manual/es/function.curl-multi-exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 2ebb9660d
order: 9940
---

curl_multi_exec

Ejecuta las subpeticiones de la sesión cURL

## Descripción

```php
curl_multi_exec(CurlMultiHandle $multi_handle, int $still_running): int
```php

Ejecuta cada gestor de la pila. Este método puede ser llamado incluso si un gestor necesita leer o escribir datos.

## Parámetros

`multi_handle`  
Un gestor múltiple cURL devuelto por `curl_multi_init`.

`still_running`  
Una referencia a un flag, que indica si las operaciones están aún en curso.

## Valores devueltos

Un código cURL, definido en las [constantes predefinidas](#curl.constants) de cURL.

> [!NOTE]
> Esta función solo retorna errores relacionados con la pila. Problemas pueden ocurrir en transferencias individuales incluso cuando esta función retorna `CURLM_OK`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `multi_handle` ahora espera una instancia de `CurlMultiHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `curl_multi_exec`

Este ejemplo creará gestores cURL para una lista de URLs, los añadirá a un gestor múltiple, y los ejecutará de forma asíncrona.

```
<?php
$urls = [
    "https://www.php.net/",
    "https://www.example.com/",
];

$mh = curl_multi_init();
$map = new WeakMap();

foreach ($urls as $url) {
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_multi_add_handle($mh, $ch);
    $map[$ch] = $url;
}

do {
    $status = curl_multi_exec($mh, $unfinishedHandles);
    if ($status !== CURLM_OK) {
        throw new \Exception(curl_multi_strerror(curl_multi_errno($mh)));
    }

    while (($info = curl_multi_info_read($mh)) !== false) {
        if ($info['msg'] === CURLMSG_DONE) {
            $handle = $info['handle'];
            curl_multi_remove_handle($mh, $handle);
            $url = $map[$handle];

            if ($info['result'] === CURLE_OK) {
                $statusCode = curl_getinfo($handle, CURLINFO_HTTP_CODE);

                echo "La petición a {$url} ha terminado con el estado HTTP {$statusCode} :", PHP_EOL;
                echo curl_multi_getcontent($handle);
                echo PHP_EOL, PHP_EOL;
            } else {
                echo "La petición a {$url} ha fallado con el error : ", PHP_EOL;
                echo curl_strerror($info['result']);
                echo PHP_EOL, PHP_EOL;
            }
        }
    }

    if ($unfinishedHandles) {
        if (($updatedHandles = curl_multi_select($mh)) === -1) {
            throw new \Exception(curl_multi_strerror(curl_multi_errno($mh)));
        }
    }
} while ($unfinishedHandles);

curl_multi_close($mh);

?>

    
```php

## Véase también

`curl_multi_init`, `curl_multi_select`, `curl_exec`
