---
title: curl_multi_setopt
source_url: https://www.php.net/manual/es/constant.curl-multi-setopt.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/constants_curl_multi_setopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 141b05e57
order: 9640
---

`CURLMOPT_CHUNK_LENGTH_PENALTY_SIZE` (`int`)  
Especifica el umbral de longitud de fragmento para el pipelining en bytes. Disponible a partir de PHP 7.0.7 y cURL 7.30.0

`CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE` (`int`)  
Especifica el umbral de tamaño de penalización de pipelining en bytes. Disponible a partir de PHP 7.0.7 y cURL 7.30.0

`CURLMOPT_MAXCONNECTS` (`int`)  
Especifica la cantidad máxima de conexiones abiertas simultáneamente que libcurl puede almacenar en caché. Por omisión, el tamaño se ampliará para contener cuatro veces el número de gestores añadidos a través de `curl_multi_add_handle`. Cuando la caché está llena, cURL cierra la más antigua en la caché para evitar que el número de conexiones abiertas aumente. Disponible a partir de cURL 7.16.3.

`CURLMOPT_MAX_CONCURRENT_STREAMS` (`int`)  
Especifica el número máximo de streams simultáneos para las conexiones que cURL debería soportar en conexiones que utilizan HTTP/2. Los valores válidos van de `1` a `2147483647` (`2^31 - 1`). El valor pasado aquí será respetado en función de otras propiedades de los recursos del sistema. Por omisión, es `100`. Disponible a partir de PHP 8.2.0 y cURL 7.67.0.

`CURLMOPT_MAX_HOST_CONNECTIONS` (`int`)  
Especifica el número máximo de conexiones a un solo host. Disponible a partir de PHP 7.0.7 y cURL 7.30.0

`CURLMOPT_MAX_PIPELINE_LENGTH` (`int`)  
Especifica el número máximo de solicitudes en un pipeline. Disponible a partir de PHP 7.0.7 y cURL 7.30.0

`CURLMOPT_MAX_TOTAL_CONNECTIONS` (`int`)  
Especifica el número máximo de conexiones abiertas simultáneamente. Disponible a partir de PHP 7.0.7 y cURL 7.30.0

`CURLMOPT_PIPELINING` (`int`)  
Pasar 1 para activar o 0 para desactivar. Activar el pipelining en un gestor múltiple hará que intente realizar el pipelining HTTP tanto como sea posible para las transferencias que utilizan este gestor. Esto significa que añadir una segunda solicitud que puede utilizar una conexión ya existente "pipe" la segunda solicitud en la misma conexión. A partir de cURL 7.43.0, el valor es una máscara de bits, y pasar 2 intentará multiplexar el nuevo transferencia en una conexión HTTP/2 existente. Pasar 3 indica a cURL solicitar el pipelining y el multiplexado independientemente uno del otro. A partir de cURL 7.62.0, establecer el bit de pipelining no tiene ningún efecto. En lugar de literales enteros, las constantes CURLPIPE\_\* también pueden ser utilizadas. Disponible a partir de cURL 7.16.0.

`CURLMOPT_PUSHFUNCTION` (`int`)  
Pasar una `Closure` que será registrada para gestionar las inserciones del servidor y debe tener la siguiente firma:

```php
pushfunction(resource $parent_ch, resource $pushed_ch, array $headers): int
```php

`parent_ch`  
El gestor parental cURL (la solicitud que el cliente ha hecho).

`pushed_ch`  
Un nuevo gestor cURL para la solicitud insertada.

`headers`  
Los encabezados de la promesa de inserción.

La función push debe devolver ya sea `CURL_PUSH_OK` si puede gestionar la inserción, o `CURL_PUSH_DENY` para rechazarla. Disponible a partir de PHP 7.1.0 y cURL 7.44.0
