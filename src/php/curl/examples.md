---
title: Ejemplos
source_url: https://www.php.net/manual/es/curl.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: fc9a0a8b2
order: 9820
---

## Ejemplos

## Ejemplo con curl

Una vez compilado PHP con soporte para cURL, puede empezar a usar las funciones cURL. La idea básica detrás de las funciones cURL es que se inicializa una sesión cURL usando `curl_init`, luego pueden definirse todas las opciones para la transferencia con la función `curl_setopt`, y finalmente, puede ejecutarse la sesión con `curl_exec`. A continuación se muestra un ejemplo que utiliza las funciones cURL para recuperar la página de inicio del sitio example.com en un fichero:

Uso del módulo cURL para recuperar la página de inicio de example.com

```php
<?php

$ch = curl_init("http://www.example.com/");
$fp = fopen("example_homepage.txt", "w");

curl_setopt($ch, CURLOPT_FILE, $fp);
curl_setopt($ch, CURLOPT_HEADER, 0);

curl_exec($ch);
if(curl_error($ch)) {
    fwrite($fp, curl_error($ch));
}
fclose($fp);
?>

    
```
