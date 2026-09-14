---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/curl.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: ee972f53e
order: 9600
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Las descripciones así como los usos de estas constantes se describen en la documentación de las funciones `curl_setopt`, `curl_multi_setopt` y `curl_getinfo`.

`CURLALTSVC_H1` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.64.1.

`CURLALTSVC_H2` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.64.1.

`CURLALTSVC_H3` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.64.1.

`CURLALTSVC_READONLYFILE` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.64.1.

`CURLAUTH_ANY` (`int`)  

`CURLAUTH_ANYSAFE` (`int`)  

`CURLAUTH_AWS_SIGV4` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.75.0.

`CURLAUTH_BASIC` (`int`)  

`CURLAUTH_BEARER` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.61.0.

`CURLAUTH_DIGEST` (`int`)  

`CURLAUTH_DIGEST_IE` (`int`)  
Utilizar la autenticación HTTP Digest con un navegador IE. Disponible a partir de cURL 7.19.3.

`CURLAUTH_GSSAPI` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.54.1

`CURLAUTH_GSSNEGOTIATE` (`int`)  

`CURLAUTH_NEGOTIATE` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.61.0.

`CURLAUTH_NONE` (`int`)  
Disponible a partir de cURL 7.10.6.

`CURLAUTH_NTLM` (`int`)  

`CURLAUTH_NTLM_WB` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.22.0

`CURLAUTH_ONLY` (`int`)  
Este es un símbolo meta. Colocar este valor CON un solo valor de autenticación específico para forzar a libcurl a verificar la autenticación no restringida y si no, solo este algoritmo de autenticación es aceptable. Disponible a partir de cURL 7.21.3.

`CURLFOLLOW_ALL` (`int`)  
Valor para `CURLOPT_FOLLOWLOCATION` que activa el seguimiento de las redirecciones y mantiene en uso un método de solicitud personalizado definido con `CURLOPT_CUSTOMREQUEST` para todas las solicitudes, incluso después de las redirecciones. Disponible a partir de PHP 8.5.0 y cURL 8.13.0.

`CURLFOLLOW_OBEYCODE` (`int`)  
Valor para `CURLOPT_FOLLOWLOCATION` que activa el seguimiento de las redirecciones respetando el código de respuesta HTTP: un método de solicitud personalizado definido con `CURLOPT_CUSTOMREQUEST` se mantiene, salvo que se cambia a `GET` en los códigos de estado de redirección que lo requieren (como 301, 302 y 303). Disponible a partir de PHP 8.5.0 y cURL 8.13.0.

`CURLFOLLOW_FIRSTONLY` (`int`)  
Valor para `CURLOPT_FOLLOWLOCATION` que activa el seguimiento de las redirecciones pero utiliza un método de solicitud personalizado definido con `CURLOPT_CUSTOMREQUEST` solo para la primera solicitud; las solicitudes siguientes siguen el método dictado por el código de respuesta de redirección. Disponible a partir de PHP 8.5.0 y cURL 8.13.0.

`CURLFTPAUTH_DEFAULT` (`int`)  

`CURLFTPAUTH_SSL` (`int`)  

`CURLFTPAUTH_TLS` (`int`)  

`CURLFTPMETHOD_DEFAULT` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.15.3.

`CURLFTPMETHOD_MULTICWD` (`int`)  
Realiza una sola operación `CWD` para cada parte del camino en la URL dada. Disponible a partir de cURL 7.15.3.

`CURLFTPMETHOD_NOCWD` (`int`)  
libcurl no realiza `CWD` en absoluto. libcurl realiza `SIZE`, `RETR`, `STOR` etc. y devuelve un camino completo al servidor para todas estas comandas. Disponible a partir de cURL 7.15.3.

`CURLFTPMETHOD_SINGLECWD` (`int`)  
libcurl realiza un `CWD` con el directorio objetivo completo luego opera sobre el fichero como en el caso multicwd. Disponible a partir de cURL 7.15.3.

`CURLFTPSSL_ALL` (`int`)  

`CURLFTPSSL_CCC_ACTIVE` (`int`)  
Inicia el cierre de la conexión y espera una respuesta. Disponible a partir de cURL 7.16.2.

`CURLFTPSSL_CCC_NONE` (`int`)  
No intenta usar CCC (Clear Command Channel). Disponible a partir de cURL 7.16.2.

`CURLFTPSSL_CCC_PASSIVE` (`int`)  
No inicia el cierre de la conexión, pero espera que el servidor lo haga. No envía respuesta. Disponible a partir de cURL 7.16.2.

`CURLFTPSSL_CONTROL` (`int`)  

`CURLFTPSSL_NONE` (`int`)  

`CURLFTPSSL_TRY` (`int`)  

`CURLFTP_CREATE_DIR` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.19.3

`CURLFTP_CREATE_DIR_NONE` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.19.3

`CURLFTP_CREATE_DIR_RETRY` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.19.3

`CURLGSSAPI_DELEGATION_FLAG` (`int`)  
Permite la delegación incondicional de las credenciales GSSAPI. Disponible a partir de cURL 7.22.0.

`CURLGSSAPI_DELEGATION_POLICY_FLAG` (`int`)  
Delega únicamente si el flag `OK-AS-DELEGATE` está definido en el ticket de servicio si esta funcionalidad es soportada por la implementación GSS-API y que la definición de `GSS_C_DELEG_POLICY_FLAG` estaba disponible en la compilación. Disponible a partir de cURL 7.22.0.

`CURLHEADER_SEPARATE` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.37.0.

`CURLHEADER_UNIFIED` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.37.0.

`CURLHSTS_ENABLE` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.74.0

`CURLHSTS_READONLYFILE` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.74.0

`CURLKHMATCH_LAST` (`int`)  
Disponible a partir de PHP 8.3.0 y cURL 7.19.6

`CURLKHMATCH_MISMATCH` (`int`)  
Disponible a partir de PHP 8.3.0 y cURL 7.19.6

`CURLKHMATCH_MISSING` (`int`)  
Disponible a partir de PHP 8.3.0 y cURL 7.19.6

`CURLKHMATCH_OK` (`int`)  
Disponible a partir de PHP 8.3.0 y cURL 7.19.6

`CURLMIMEOPT_FORMESCAPE` (`int`)  
Disponible a partir de PHP 8.3.0 y cURL 7.81.0

`CURLMSG_DONE` (`int`)  

`CURLPIPE_HTTP1` (`int`)  
Disponible a partir de cURL 7.43.0.

`CURLPIPE_MULTIPLEX` (`int`)  
Disponible a partir de cURL 7.43.0.

`CURLPIPE_NOTHING` (`int`)  
Disponible a partir de cURL 7.43.0.

`CURLPROXY_HTTP` (`int`)  
Disponible a partir de cURL 7.10.

`CURLPROXY_HTTPS` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.52.0

`CURLPROXY_HTTP_1_0` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.19.3

`CURLPROXY_SOCKS4` (`int`)  
Disponible a partir de cURL 7.10.

`CURLPROXY_SOCKS4A` (`int`)  
Disponible a partir de cURL 7.18.0.

`CURLPROXY_SOCKS5` (`int`)  
Disponible a partir de cURL 7.10.

`CURLPROXY_SOCKS5_HOSTNAME` (`int`)  
Disponible a partir de cURL 7.18.0.

`CURLPX_BAD_ADDRESS_TYPE` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_BAD_VERSION` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_CLOSED` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_GSSAPI` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_GSSAPI_PERMSG` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_GSSAPI_PROTECTION` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_IDENTD` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_IDENTD_DIFFER` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_LONG_HOSTNAME` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_LONG_PASSWD` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_LONG_USER` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_NO_AUTH` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_OK` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_RECV_ADDRESS` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_RECV_AUTH` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_RECV_CONNECT` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_RECV_REQACK` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REPLY_ADDRESS_TYPE_NOT_SUPPORTED` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REPLY_COMMAND_NOT_SUPPORTED` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REPLY_CONNECTION_REFUSED` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REPLY_GENERAL_SERVER_FAILURE` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REPLY_HOST_UNREACHABLE` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REPLY_NETWORK_UNREACHABLE` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REPLY_NOT_ALLOWED` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REPLY_TTL_EXPIRED` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REPLY_UNASSIGNED` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_REQUEST_FAILED` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_RESOLVE_HOST` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_SEND_AUTH` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_SEND_CONNECT` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_SEND_REQUEST` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_UNKNOWN_FAIL` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_UNKNOWN_MODE` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLPX_USER_REJECTED` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLSSH_AUTH_AGENT` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.28.0

`CURLSSH_AUTH_ANY` (`int`)  

`CURLSSH_AUTH_DEFAULT` (`int`)  

`CURLSSH_AUTH_GSSAPI` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.58.0

`CURLSSH_AUTH_HOST` (`int`)  

`CURLSSH_AUTH_KEYBOARD` (`int`)  

`CURLSSH_AUTH_NONE` (`int`)  

`CURLSSH_AUTH_PASSWORD` (`int`)  

`CURLSSH_AUTH_PUBLICKEY` (`int`)  

`CURLSSLOPT_ALLOW_BEAST` (`int`)  
Disponible a partir de cURL 7.25.0

`CURLSSLOPT_AUTO_CLIENT_CERT` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.77.0

`CURLSSLOPT_NATIVE_CA` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.71.0

`CURLSSLOPT_NO_PARTIALCHAIN` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.68.0

`CURLSSLOPT_NO_REVOKE` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.44.0

`CURLSSLOPT_REVOKE_BEST_EFFORT` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.70.0

`CURLUSESSL_ALL` (`int`)  
Requiere SSL para todas las comunicaciones o falla con `CURLE_USE_SSL_FAILED`. Disponible a partir de cURL 7.17.0.

`CURLUSESSL_CONTROL` (`int`)  
Requiere SSL para la conexión de control o falla con `CURLE_USE_SSL_FAILED`. Disponible a partir de cURL 7.17.0.

`CURLUSESSL_NONE` (`int`)  
No intenta usar SSL. Disponible a partir de cURL 7.17.0.

`CURLUSESSL_TRY` (`int`)  
Intenta usar SSL, sino continúa normalmente. Es de notar que el servidor puede cerrar la conexión si la negociación falla. Disponible a partir de cURL 7.17.0.

`CURLVERSION_NOW` (`int`)  

`CURLWS_RAW_MODE` (`int`)  
Disponible a partir de PHP 8.3.0 y cURL 7.86.0

`CURL_FNMATCHFUNC_FAIL` (`int`)  
Devolvido por la función de devolución de llamada de coincidencia de caracteres genéricos si una error ha ocurrido. Disponible a partir de cURL 7.21.0.

`CURL_FNMATCHFUNC_MATCH` (`int`)  
Devolvido por la función de devolución de llamada de coincidencia de caracteres genéricos si el patrón coincide con la cadena. Disponible a partir de cURL 7.21.0.

`CURL_FNMATCHFUNC_NOMATCH` (`int`)  
Devolvido por la función de devolución de llamada de coincidencia de caracteres genéricos si el patrón no coincide con la cadena. Disponible a partir de cURL 7.21.0.

`CURL_HTTP_VERSION_1_0` (`int`)  

`CURL_HTTP_VERSION_1_1` (`int`)  

`CURL_HTTP_VERSION_2` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.43.0

`CURL_HTTP_VERSION_2TLS` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.47.0

`CURL_HTTP_VERSION_2_0` (`int`)  
Disponible a partir de cURL 7.33.0

`CURL_HTTP_VERSION_2_PRIOR_KNOWLEDGE` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.49.0

`CURL_HTTP_VERSION_3` (`int`)  
Disponible a partir de PHP 8.4.0 y cURL 7.66.0.

`CURL_HTTP_VERSION_3ONLY` (`int`)  
Disponible a partir de PHP 8.4.0 y cURL 7.88.0.

`CURL_HTTP_VERSION_NONE` (`int`)  

`CURL_IPRESOLVE_V4` (`int`)  
Utilizar únicamente direcciones IPv4 al establecer una conexión o al elegir una del pool de conexiones. Disponible a partir de cURL 7.10.8.

`CURL_IPRESOLVE_V6` (`int`)  
Utilizar únicamente direcciones IPv6 al establecer una conexión o al elegir una del pool de conexiones. Disponible a partir de cURL 7.10.8.

`CURL_IPRESOLVE_WHATEVER` (`int`)  
Utilizar direcciones de todas las versiones IP permitidas por el sistema. Disponible a partir de cURL 7.10.8.

`CURL_MAX_READ_SIZE` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.53.0

`CURL_NETRC_IGNORED` (`int`)  

`CURL_NETRC_OPTIONAL` (`int`)  

`CURL_NETRC_REQUIRED` (`int`)  

`CURL_PUSH_DENY` (`int`)  
Disponible a partir de PHP 7.1.0 y cURL 7.44.0

`CURL_PUSH_OK` (`int`)  
Disponible a partir de PHP 7.1.0 y cURL 7.44.0

`CURL_READFUNC_PAUSE` (`int`)  
Disponible a partir de cURL 7.18.0

`CURL_REDIR_POST_301` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.18.2

`CURL_REDIR_POST_302` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.18.2

`CURL_REDIR_POST_303` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.25.1

`CURL_REDIR_POST_ALL` (`int`)  
Disponible a partir de PHP 7.0.7 y cURL 7.18.2

`CURL_RTSPREQ_ANNOUNCE` (`int`)  
Cuando enviado por un cliente, este método cambia la descripción de la sesión. `ANNOUNCE` actúa como un HTTP PUT o POST así como `CURL_RTSPREQ_SET_PARAMETER`. Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_DESCRIBE` (`int`)  
Utilizado para obtener la descripción de bajo nivel de un flujo. La aplicación debe anotar los formatos que comprende en el encabezado `Accept:`. A menos que esté definido manualmente, libcurl añade automáticamente `Accept: application/sdp`. Los encabezados de condición temporal son añadidos a las peticiones DESCRIBE si la opción `CURLOPT_TIMECONDITION` es utilizada. Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_GET_PARAMETER` (`int`)  
Recupera un parámetro del servidor. Por omisión, libcurl añade un encabezado `Content-Type: text/parameters` a todas las peticiones no vacías a menos que un encabezado personalizado esté definido. `GET_PARAMETER` actúa como un HTTP PUT o POST. Las aplicaciones que deseen enviar un mensaje de latido deben utilizar una petición `GET_PARAMETER` vacía. Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_OPTIONS` (`int`)  
Utilizado para obtener las opciones de la sesión. Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_PAUSE` (`int`)  
Envía un comando `PAUSE` al servidor. Utilizar la opción `CURLOPT_RANGE` con un solo valor para indicar cuándo el flujo debe ser detenido (por ejemplo npt=25). Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_PLAY` (`int`)  
Envía un comando `PLAY` al servidor. Utilizar la opción `CURLOPT_RANGE` para modificar el tiempo de lectura (por ejemplo npt=10-15). Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_RECEIVE` (`int`)  
Define el tipo de petición RTSP para recibir datos RTP entrelazados. Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_RECORD` (`int`)  
Utilizado para decirle al servidor que grabe una sesión. Utilizar la opción `CURLOPT_RANGE` para modificar el tiempo de grabación. Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_SETUP` (`int`)  
Utilizado para inicializar la capa de transporte para la sesión. Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_SET_PARAMETER` (`int`)  
Define un parámetro en el servidor. Disponible a partir de cURL 7.20.0.

`CURL_RTSPREQ_TEARDOWN` (`int`)  
Termina una sesión RTSP. Cerrar simplemente una conexión no termina la sesión RTSP ya que es válido controlar una sesión RTSP en diferentes conexiones. Disponible a partir de cURL 7.20.0.

`CURL_SSLVERSION_DEFAULT` (`int`)  

`CURL_SSLVERSION_MAX_DEFAULT` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.54.0

`CURL_SSLVERSION_MAX_NONE` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.54.0

`CURL_SSLVERSION_MAX_TLSv1_0` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.54.0

`CURL_SSLVERSION_MAX_TLSv1_1` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.54.0

`CURL_SSLVERSION_MAX_TLSv1_2` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.54.0

`CURL_SSLVERSION_MAX_TLSv1_3` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.54.0

`CURL_SSLVERSION_SSLv2` (`int`)  

`CURL_SSLVERSION_SSLv3` (`int`)  

`CURL_SSLVERSION_TLSv1` (`int`)  

`CURL_SSLVERSION_TLSv1_0` (`int`)  

`CURL_SSLVERSION_TLSv1_1` (`int`)  

`CURL_SSLVERSION_TLSv1_2` (`int`)  

`CURL_SSLVERSION_TLSv1_3` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.52.0

`CURL_TIMECOND_IFMODSINCE` (`int`)  

`CURL_TIMECOND_IFUNMODSINCE` (`int`)  

`CURL_TIMECOND_LASTMOD` (`int`)  

`CURL_TIMECOND_NONE` (`int`)  

`CURL_TLSAUTH_SRP` (`int`)  
Disponible a partir de cURL 7.21.4.

`CURL_VERSION_ALTSVC` (`int`)  
Disponible a partir de PHP 7.3.6 y cURL 7.64.1

`CURL_VERSION_ASYNCHDNS` (`int`)  
Resoluciones DNS asíncronas. Disponible a partir de PHP 7.3.0 y cURL 7.10.7

`CURL_VERSION_BROTLI` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.57.0

`CURL_VERSION_CONV` (`int`)  
Conversiones de caracteres soportadas. Disponible a partir de PHP 7.3.0 y cURL 7.15.4

`CURL_VERSION_CURLDEBUG` (`int`)  
Seguimiento de la memoria de depuración soportado. Disponible a partir de PHP 7.3.6 y cURL 7.19.6

`CURL_VERSION_DEBUG` (`int`)  
Construido con capacidades de depuración. Disponible a partir de PHP 7.3.0 y cURL 7.10.6

`CURL_VERSION_GSASL` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.76.0

`CURL_VERSION_GSSAPI` (`int`)  
Construido contra una biblioteca GSS-API. Disponible a partir de PHP 7.3.0 y cURL 7.38.0

`CURL_VERSION_GSSNEGOTIATE` (`int`)  
La autenticación Negotiate es soportada. Disponible a partir de PHP 7.3.0 y cURL 7.10.6 (obsoleto a partir de cURL 7.38.0)

`CURL_VERSION_HSTS` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.74.0

`CURL_VERSION_HTTP2` (`int`)  
Soporte HTTP2 integrado. Disponible a partir de cURL 7.33.0

`CURL_VERSION_HTTP3` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.66.0

`CURL_VERSION_HTTPS_PROXY` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.52.0

`CURL_VERSION_IDN` (`int`)  
Los nombres de dominio internacionalizados son soportados. Disponible a partir de PHP 7.3.0 y cURL 7.12.0

`CURL_VERSION_IPV6` (`int`)  
Soporte IPv6.

`CURL_VERSION_KERBEROS4` (`int`)  
La autenticación Kerberos V4 es soportada.

`CURL_VERSION_KERBEROS5` (`int`)  
La autenticación Kerberos V5 es soportada. Disponible a partir de PHP 7.0.7 y cURL 7.40.0

`CURL_VERSION_LARGEFILE` (`int`)  
Soporte para ficheros de más de 2 Go. Disponible a partir de cURL 7.33.0

`CURL_VERSION_LIBZ` (`int`)  
Las funcionalidades de libz están presentes.

`CURL_VERSION_MULTI_SSL` (`int`)  
Disponible a partir de PHP 7.3.0 y cURL 7.56.0

`CURL_VERSION_NTLM` (`int`)  
La autenticación NTLM es soportada. Disponible a partir de PHP 7.3.0 y cURL 7.10.6

`CURL_VERSION_NTLM_WB` (`int`)  
La delegación NTLM al helper winbind es soportada. Disponible a partir de PHP 7.3.0 y cURL 7.22.0

`CURL_VERSION_PSL` (`int`)  
Lista de sufijos públicos de Mozilla, utilizada para la verificación de dominios de cookies. Disponible a partir de PHP 7.3.6 y cURL 7.47.0

`CURL_VERSION_SPNEGO` (`int`)  
La autenticación SPNEGO es soportada. Disponible a partir de PHP 7.3.0 y cURL 7.10.8

`CURL_VERSION_SSL` (`int`)  
Las opciones SSL están presentes.

`CURL_VERSION_SSPI` (`int`)  
Construido contra Windows SSPI. Disponible a partir de PHP 7.3.0 y cURL 7.13.2

`CURL_VERSION_TLSAUTH_SRP` (`int`)  
La autenticación TLS-SRP es soportada. Disponible a partir de PHP 7.3.0 y cURL 7.21.4

`CURL_VERSION_UNICODE` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.72.0

`CURL_VERSION_UNIX_SOCKETS` (`int`)  
Soporte para sockets de dominio Unix. Disponible a partir de PHP 7.0.7 y cURL 7.40.0

`CURL_VERSION_ZSTD` (`int`)  
Disponible a partir de PHP 8.2.0 y cURL 7.72.0

`CURL_WRITEFUNC_PAUSE` (`int`)  
Disponible a partir de cURL 7.18.0

`CURL_PREREQFUNC_OK` (`int`)  
Disponible a partir de PHP 8.4.0 y cURL 7.80.0.

`CURL_PREREQFUNC_ABORT` (`int`)  
Disponible a partir de PHP 8.4.0 y cURL 7.80.0.
