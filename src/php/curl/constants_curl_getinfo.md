---
title: curl_getinfo
source_url: https://www.php.net/manual/es/constant.curl-getinfo.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/constants_curl_getinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: ee972f53e
order: 9620
---

`CURLINFO_APPCONNECT_TIME` (`int`)  
El tiempo en segundos que ha sido necesario para establecer la conexión SSL/SSH con el host remoto.

`CURLINFO_APPCONNECT_TIME_T` (`int`)  
El tiempo en microsegundos que ha sido necesario para establecer la conexión SSL/SSH con el host remoto. Disponible a partir de PHP 7.3.0 y cURL 7.61.0

`CURLINFO_CAINFO` (`int`)  
Ruta nativa del certificado CA. Disponible a partir de PHP 8.3.0 y cURL 7.84.0

`CURLINFO_CAPATH` (`int`)  
Ruta nativa del CA. Disponible a partir de PHP 8.3.0 y cURL 7.84.0

`CURLINFO_CERTINFO` (`int`)  
La cadena del certificado TLS.

`CURLINFO_CONDITION_UNMET` (`int`)  
Información sobre la condición temporal no cumplida.

`CURLINFO_CONN_ID` (`int`)  
El ID de la última conexión utilizada por la transferencia. El ID de conexión es único entre todas las conexiones que usan la misma caché de conexiones y resulta útil para distinguir la reutilización de conexiones. Disponible a partir de PHP 8.5.0 y cURL 8.2.0.

`CURLINFO_CONNECT_TIME` (`int`)  
El tiempo en segundos que ha sido necesario para establecer la conexión.

`CURLINFO_CONNECT_TIME_T` (`int`)  
El tiempo total, en microsegundos, desde el inicio hasta que la conexión con el host remoto (o el proxy) se haya completado. Disponible a partir de PHP 7.3.0 y cURL 7.61.0

`CURLINFO_CONTENT_LENGTH_DOWNLOAD` (`int`)  
La longitud del contenido descargado, leída desde el campo Content-Length:

`CURLINFO_CONTENT_LENGTH_DOWNLOAD_T` (`int`)  
El contenido de la longitud de la descarga. Es el valor leído desde el campo Content-Length:. -1 si el tamaño no es conocido. Disponible a partir de PHP 7.3.0 y cURL 7.55.0

`CURLINFO_CONTENT_LENGTH_UPLOAD` (`int`)  
El tamaño especificado del envío.

`CURLINFO_CONTENT_LENGTH_UPLOAD_T` (`int`)  
El tamaño especificado del envío. -1 si el tamaño no es conocido. Disponible a partir de PHP 7.3.0 y cURL 7.55.0

`CURLINFO_CONTENT_TYPE` (`int`)  
El `Content-Type`: del documento solicitado. NULL indica que el servidor no ha enviado un encabezado `Content-Type`: válido.

`CURLINFO_COOKIELIST` (`int`)  
Las cookies conocidas.

`CURLINFO_EFFECTIVE_METHOD` (`int`)  
Devuelve el último método HTTP utilizado.

`CURLINFO_EFFECTIVE_URL` (`int`)  
La última URL efectiva.

`CURLINFO_FILETIME` (`int`)  
El tiempo remoto del documento recuperado, con `CURLOPT_FILETIME` activado; si -1 es devuelto, el tiempo del documento es desconocido.

`CURLINFO_FILETIME_T` (`int`)  
El tiempo remoto del documento recuperado (como un timestamp Unix), una alternativa a `CURLINFO_FILETIME` para permitir a los sistemas con variables largas de 32 bits extraer fechas fuera del rango de tiempo de 32 bits. Disponible a partir de PHP 7.3.0 y cURL 7.59.0

`CURLINFO_FTP_ENTRY_PATH` (`int`)  
La ruta de entrada en el servidor FTP.

`CURLINFO_HEADER_OUT` (`int`)  
La cadena de solicitud enviada. Para que esto funcione, añada la opción `CURLINFO_HEADER_OUT` al manejador llamando a `curl_setopt`.

`CURLINFO_HEADER_SIZE` (`int`)  
El tamaño total de todos los encabezados recibidos.

`CURLINFO_HTTPAUTH_AVAIL` (`int`)  
La máscara de bits que indica el método de autenticación disponible(s) según la respuesta anterior.

`CURLINFO_HTTPAUTH_USED` (`int`)  
Máscara de bits que indica el o los métodos de autenticación HTTP realmente utilizados en la solicitud anterior. Disponible a partir de PHP 8.5.0 y cURL 8.12.0.

`CURLINFO_HTTP_CODE` (`int`)  
El último código de respuesta. A partir de cURL 7.10.8, es un alias heredado de `CURLINFO_RESPONSE_CODE`.

`CURLINFO_HTTP_CONNECTCODE` (`int`)  
El código de respuesta CONNECT.

`CURLINFO_HTTP_VERSION` (`int`)  
La versión utilizada en la última conexión HTTP. El valor de retorno será una de las constantes `CURL_HTTP_VERSION_*` definidas o 0 si la versión no puede ser determinada. Disponible a partir de PHP 7.3.0 y cURL 7.50.0

`CURLINFO_LASTONE` (`int`)  
El último valor de enumeración en la enumeración `CURLINFO` subyacente en `libcurl`.

`CURLINFO_LOCAL_IP` (`int`)  
La dirección IP local (fuente) de la última conexión.

`CURLINFO_LOCAL_PORT` (`int`)  
El puerto local (fuente) de la última conexión.

`CURLINFO_NAMELOOKUP_TIME` (`int`)  
El tiempo en segundos hasta que la resolución del nombre esté completa.

`CURLINFO_NAMELOOKUP_TIME_T` (`int`)  
El tiempo en microsegundos hasta que la resolución del nombre esté completa. Disponible a partir de PHP 7.3.0 y cURL 7.61.0

`CURLINFO_NUM_CONNECTS` (`int`)  
El número de conexiones que curl ha tenido que crear para realizar la transferencia anterior.

`CURLINFO_OS_ERRNO` (`int`)  
El número de error del fallo de conexión. El número es específico del sistema operativo y del sistema.

`CURLINFO_PRETRANSFER_TIME` (`int`)  
El tiempo en segundos desde el inicio hasta justo antes de que la transferencia de fichero comience.

`CURLINFO_PRETRANSFER_TIME_T` (`int`)  
El tiempo transcurrido desde el inicio hasta que la transferencia de fichero comience, en microsegundos. Disponible a partir de PHP 7.3.0 y cURL 7.61.0

`CURLINFO_PRIMARY_IP` (`int`)  
La dirección IP de la última conexión.

`CURLINFO_PRIMARY_PORT` (`int`)  
El puerto de destino de la última conexión.

`CURLINFO_PRIVATE` (`int`)  
Los datos privados asociados a esta conexión cURL, previamente definidos con la opción `CURLOPT_PRIVATE` de `curl_setopt`.

`CURLINFO_PROTOCOL` (`int`)  
El protocolo utilizado en la última conexión HTTP. El valor de retorno será exactamente uno de los valores `CURLPROTO_*`. Disponible a partir de PHP 7.3.0 y cURL 7.52.0

`CURLINFO_PROXYAUTH_AVAIL` (`int`)  
La máscara de bits que indica el método de autenticación de proxy disponible según la respuesta anterior.

`CURLINFO_PROXYAUTH_USED` (`int`)  
Máscara de bits que indica el o los métodos de autenticación del proxy realmente utilizados en la solicitud anterior. Disponible a partir de PHP 8.5.0 y cURL 8.12.0.

`CURLINFO_PROXY_ERROR` (`int`)  
El detalle del código de error (SOCKS) proxy cuando la última transferencia ha devuelto un error `CURLE_PROXY`. El valor devuelto será exactamente uno de los valores `CURLPX_*`. El código de error será `CURLPX_OK` si ningún código de respuesta estaba disponible. Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLINFO_PROXY_SSL_VERIFYRESULT` (`int`)  
El resultado de la verificación del certificado que ha sido solicitada (usando la opción `CURLOPT_PROXY_SSL_VERIFYPEER`). Utilizado únicamente para proxies HTTPS. Disponible a partir de PHP 7.3.0 y cURL 7.52.0

`CURLINFO_QUEUE_TIME_T` (`int`)  
El tiempo, en microsegundos, durante el cual la transferencia estuvo retenida en una cola de espera antes de comenzar, debido a los límites establecidos con `CURLMOPT_MAX_TOTAL_CONNECTIONS` u opciones similares. Disponible a partir de PHP 8.5.0 y cURL 8.6.0.

`CURLINFO_REDIRECT_COUNT` (`int`)  
El número de redirecciones, con la opción `CURLOPT_FOLLOWLOCATION` activada.

`CURLINFO_REDIRECT_TIME` (`int`)  
El tiempo en segundos de todas las etapas de redirección antes de que la transacción final comience, con la opción `CURLOPT_FOLLOWLOCATION` activada.

`CURLINFO_REDIRECT_TIME_T` (`int`)  
El tiempo total, en microsegundos, que ha sido necesario para todas las etapas de redirección, incluyendo la resolución de nombre, la conexión, el pre-transferencia y la transferencia antes de que la transacción final comience. Disponible a partir de PHP 7.3.0 y cURL 7.61.0

`CURLINFO_REDIRECT_URL` (`int`)  
Con la opción `CURLOPT_FOLLOWLOCATION` desactivada: URL de redirección encontrada en la última transacción, que debería ser solicitada manualmente después. Con la opción `CURLOPT_FOLLOWLOCATION` activada: está vacía. La URL de redirección en este caso está disponible en `CURLINFO_EFFECTIVE_URL`.

`CURLINFO_REFERER` (`int`)  
El encabezado `Referer`. Disponible a partir de PHP 8.2.0 y cURL 7.76.0

`CURLINFO_REQUEST_SIZE` (`int`)  
El tamaño total de las solicitudes emitidas, actualmente únicamente para las solicitudes HTTP.

`CURLINFO_RESPONSE_CODE` (`int`)  
El último código de respuesta. Disponible a partir de cURL 7.10.8

`CURLINFO_RETRY_AFTER` (`int`)  
La información del encabezado `Retry-After`, o cero si no había un encabezado válido. Disponible a partir de PHP 8.2.0 y cURL 7.66.0

`CURLINFO_RTSP_CLIENT_CSEQ` (`int`)  
La próxima secuencia CSeq del cliente RTSP.

`CURLINFO_RTSP_CSEQ_RECV` (`int`)  
La recepción CSeq RTSP reciente.

`CURLINFO_RTSP_SERVER_CSEQ` (`int`)  
La próxima secuencia CSeq del servidor RTSP.

`CURLINFO_RTSP_SESSION_ID` (`int`)  
El ID de sesión RTSP.

`CURLINFO_SCHEME` (`int`)  
El esquema de URL utilizado para la última conexión. Disponible a partir de PHP 7.3.0 y cURL 7.52.0

`CURLINFO_SIZE_DOWNLOAD` (`int`)  
El número total de octetos descargados.

`CURLINFO_SIZE_DOWNLOAD_T` (`int`)  
El número total de octetos descargados. El número es únicamente para la última transferencia y será reiniciado para cada nueva transferencia. Disponible a partir de PHP 7.3.0 y cURL 7.50.0

`CURLINFO_SIZE_UPLOAD` (`int`)  
El número total de octetos subidos.

`CURLINFO_SIZE_UPLOAD_T` (`int`)  
El número total de octetos subidos. Disponible a partir de PHP 7.3.0 y cURL 7.50.0

`CURLINFO_SPEED_DOWNLOAD` (`int`)  
La velocidad media de descarga.

`CURLINFO_SPEED_DOWNLOAD_T` (`int`)  
La velocidad media de descarga en octetos/segundo que curl ha medido para la descarga completa. Disponible a partir de PHP 7.3.0 y cURL 7.50.0

`CURLINFO_SPEED_UPLOAD` (`int`)  
La velocidad media de subida.

`CURLINFO_SPEED_UPLOAD_T` (`int`)  
La velocidad media de subida en octetos/segundo que curl ha medido para la subida completa. Disponible a partir de PHP 7.3.0 y cURL 7.50.0

`CURLINFO_SSL_ENGINES` (`int`)  
Los motores de criptografía OpenSSL soportados.

`CURLINFO_SSL_VERIFYRESULT` (`int`)  
El resultado de la verificación del certificado SSL solicitada definiendo `CURLOPT_SSL_VERIFYPEER`.

`CURLINFO_STARTTRANSFER_TIME` (`int`)  
El tiempo en segundos hasta que el primer octeto esté a punto de ser transferido.

`CURLINFO_STARTTRANSFER_TIME_T` (`int`)  
El tiempo, en microsegundos, que ha sido necesario desde el inicio hasta que el primer octeto sea recibido. Disponible a partir de PHP 7.3.0 y cURL 7.61.0

`CURLINFO_TOTAL_TIME` (`int`)  
El tiempo total en segundos para la última transferencia.

`CURLINFO_TOTAL_TIME_T` (`int`)  
El tiempo total en microsegundos para la última transferencia, incluyendo la resolución de nombre, la conexión TCP, etc. Disponible a partir de PHP 7.3.0 y cURL 7.61.0

`CURLINFO_USED_PROXY` (`int`)  
Indica si la transferencia anterior utilizó un proxy; devuelve `1` si se utilizó un proxy y `0` en caso contrario. Disponible a partir de PHP 8.5.0 y cURL 8.7.0.

`CURLINFO_POSTTRANSFER_TIME_T` (`int`)  
Tiempo transcurrido desde el inicio hasta el envío del último octeto, en microsegundos. Disponible a partir de PHP 8.4.0 y cURL 8.10.0.
