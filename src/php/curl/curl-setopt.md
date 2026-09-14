---
title: curl_setopt
description: Establece una opción para una transferencia cURL
source_url: https://www.php.net/manual/es/function.curl-setopt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-setopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 10050
---

curl_setopt

Establece una opción para una transferencia cURL

## Descripción

```php
curl_setopt(CurlHandle $handle, int $option, mixed $value): bool
```php

Establece una opción para el gestor de sesión cURL proporcionado.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

`option`  
La opción `CURLOPT_*` a definir.

`value`  
El valor a definir para `option`. Ver la descripción de las constantes `CURLOPT_*` para detalles sobre el tipo de valores esperados por cada constante.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `CURLOPT_DNS_USE_GLOBAL_CACHE` ya no tiene ningún efecto, y la activación de esta opción en las versiones PHP thread-safe ya no genera advertencias. |
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |
| 7.3.15, 7.4.3 | Introducción de la constante `CURLOPT_HTTP09_ALLOWED`. |
| 7.3.0 | Introdujo `CURLOPT_ABSTRACT_UNIX_SOCKET`, `CURLOPT_KEEP_SENDING_ON_ERROR`, `CURLOPT_PRE_PROXY`, `CURLOPT_PROXY_CAINFO`, `CURLOPT_PROXY_CAPATH`, `CURLOPT_PROXY_CRLFILE`, `CURLOPT_PROXY_KEYPASSWD`, `CURLOPT_PROXY_PINNEDPUBLICKEY`, `CURLOPT_PROXY_SSLCERT`, `CURLOPT_PROXY_SSLCERTTYPE`, `CURLOPT_PROXY_SSL_CIPHER_LIST`, `CURLOPT_PROXY_SSLKEY`, `CURLOPT_PROXY_SSLKEYTYPE`, `CURLOPT_PROXY_SSL_OPTIONS`, `CURLOPT_PROXY_SSL_VERIFYHOST`, `CURLOPT_PROXY_SSL_VERIFYPEER`, `CURLOPT_PROXY_SSLVERSION`, `CURLOPT_PROXY_TLSAUTH_PASSWORD`, `CURLOPT_PROXY_TLSAUTH_TYPE`, `CURLOPT_PROXY_TLSAUTH_USERNAME`, `CURLOPT_SOCKS5_AUTH`, `CURLOPT_SUPPRESS_CONNECT_HEADERS`, `CURLOPT_DISALLOW_USERNAME_IN_URL`, `CURLOPT_DNS_SHUFFLE_ADDRESSES`, `CURLOPT_HAPPY_EYEBALLS_TIMEOUT_MS`, `CURLOPT_HAPROXYPROTOCOL`, `CURLOPT_PROXY_TLS13_CIPHERS`, `CURLOPT_SSH_COMPRESSION`, `CURLOPT_TIMEVALUE_LARGE` y `CURLOPT_TLS13_CIPHERS`. |
| 7.0.7 | Introdujo `CURL_HTTP_VERSION_2`, `CURL_HTTP_VERSION_2_PRIOR_KNOWLEDGE`, `CURL_HTTP_VERSION_2TLS`, `CURL_REDIR_POST_301`, `CURL_REDIR_POST_302`, `CURL_REDIR_POST_303`, `CURL_REDIR_POST_ALL`, `CURL_VERSION_KERBEROS5`, `CURL_VERSION_PSL`, `CURL_VERSION_UNIX_SOCKETS`, `CURLAUTH_NEGOTIATE`, `CURLAUTH_NTLM_WB`, `CURLFTP_CREATE_DIR`, `CURLFTP_CREATE_DIR_NONE`, `CURLFTP_CREATE_DIR_RETRY`, `CURLHEADER_SEPARATE`, `CURLHEADER_UNIFIED`, `CURLMOPT_CHUNK_LENGTH_PENALTY_SIZE`, `CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE`, `CURLMOPT_MAX_HOST_CONNECTIONS`, `CURLMOPT_MAX_PIPELINE_LENGTH`, `CURLMOPT_MAX_TOTAL_CONNECTIONS`, `CURLOPT_CONNECT_TO`, `CURLOPT_DEFAULT_PROTOCOL`, `CURLOPT_DNS_INTERFACE`, `CURLOPT_DNS_LOCAL_IP4`, `CURLOPT_DNS_LOCAL_IP6`, `CURLOPT_EXPECT_100_TIMEOUT_MS`, `CURLOPT_HEADEROPT`, `CURLOPT_LOGIN_OPTIONS`, `CURLOPT_PATH_AS_IS`, `CURLOPT_PINNEDPUBLICKEY`, `CURLOPT_PIPEWAIT`, `CURLOPT_PROXY_SERVICE_NAME`, `CURLOPT_PROXYHEADER`, `CURLOPT_SASL_IR`, `CURLOPT_SERVICE_NAME`, `CURLOPT_SSL_ENABLE_ALPN`, `CURLOPT_SSL_ENABLE_NPN`, `CURLOPT_SSL_FALSESTART`, `CURLOPT_SSL_VERIFYSTATUS`, `CURLOPT_STREAM_WEIGHT`, `CURLOPT_TCP_FASTOPEN`, `CURLOPT_TFTP_NO_OPTIONS`, `CURLOPT_UNIX_SOCKET_PATH`, `CURLOPT_XOAUTH2_BEARER`, `CURLPROTO_SMB`, `CURLPROTO_SMBS`, `CURLPROXY_HTTP_1_0`, `CURLSSH_AUTH_AGENT` y `CURLSSLOPT_NO_REVOKE`. |

## Ejemplos

Inicialización de una nueva sesión CURL y búsqueda de una página web

```
<?php
// Creación de un recurso cURL
$ch = curl_init();

// Definición de la URL y otras opciones apropiadas
curl_setopt($ch, CURLOPT_URL, "http://www.example.com/");
curl_setopt($ch, CURLOPT_HEADER, false);

// Recuperación de la URL y paso al navegador
curl_exec($ch);
?>

    
```php

## Notas

> [!NOTE]
> El hecho de pasar un array a la constante `CURLOPT_POSTFIELDS` codificará los datos como *multipart/form-data*, mientras que el hecho de pasar una cadena codificada URL codificará los datos como *application/x-www-form-urlencoded*.

## Véase también

`curl_setopt_array`, `CURLFile`, `CURLStringFile`
