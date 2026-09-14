---
title: Nuevas constantes globales
source_url: https://www.php.net/manual/es/migration84.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration84/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: d0ac0a55f
order: 1090
---

## Nuevas constantes globales

## Núcleo

PHP_OUTPUT_HANDLER_PROCESSED

PHP_SBINDIR

## cURL

CURL_HTTP_VERSION_3

CURL_HTTP_VERSION_3ONLY

CURLOPT_TCP_KEEPCNT

CURLOPT_PREREQFUNCTION

CURL_PREREQFUNC_OK

CURL_PREREQFUNC_ABORT

CURLOPT_SERVER_RESPONSE_TIMEOUT

CURLOPT_DEBUGFUNCTION

CURLINFO_TEXT

CURLINFO_HEADER_IN

CURLINFO_DATA_IN

CURLINFO_DATA_OUT

CURLINFO_SSL_DATA_OUT

CURLINFO_SSL_DATA_IN

CURLINFO_POSTTRANSFER_TIME_T

## Intl

PATTERN

(

IntlDateFormatter

)

PROPERTY_IDS_UNARY_OPERATOR

(

IntlChar

)

PROPERTY_ID_COMPAT_MATH_START

PROPERTY_ID_COMPAT_MATH_CONTINUE

## LDAP

LDAP_OPT_X_TLS_PROTOCOL_MAX

LDAP_OPT_X_TLS_PROTOCOL_TLS1_3

## libxml

LIBXML_RECOVER

LIBXML_NO_XXE

. Esto se usa en conjunción con

LIBXML_NOENT

cuando la sustitución de entidad debe realizarse, mientras se prohíbe la carga de entidad externa. Esta constante está disponible a partir de libxml2 2.13.

## MySQLi

MYSQLI_TYPE_VECTOR

## OpenSSL

X509_PURPOSE_OCSP_HELPER

X509_PURPOSE_TIMESTAMP_SIGN

## PCNTL

SIGCKPT

(Solo DragonFlyBSD)

SIGCKPTEXIT

(Solo DragonFlyBSD)

WEXITED

WSTOPPED

WNOWAIT

P_ALL

P_PID

P_PGID

P_PIDFD

(Solo Linux)

P_UID

(Solo NetBSD/FreeBSD)

P_GID

(Solo NetBSD/FreeBSD)

P_SID

(Solo NetBSD/FreeBSD)

P_JAILID

(Solo FreeBSD)

## PGSQL

PGSQL_TUPLES_CHUNK

## POSIX

POSIX_SC_CHILD_MAX

POSIX_SC_CLK_TCK

## Sockets

Las siguientes opciones de socket ahora están definidas si son soportadas:

SO_EXCLUSIVEADDRUSE

(Solo Windows)

SOCK_CONN_DGRAM

(Solo NetBSD)

SOCK_DCCP

(Solo NetBSD)

TCP_SYNCNT

(Solo Linux)

SO_EXCLBIND

(Solo Solaris/Illumos)

SO_NOSIGPIPE

(macOS y FreeBSD)

SO_LINGER_SEC

(Solo macOS)

IP_PORTRANGE

(Solo FreeBSD/NetBSD/OpenBSD)

IP_PORTRANGE_DEFAULT

(Solo FreeBSD/NetBSD/OpenBSD)

IP_PORTRANGE_HIGH

(Solo FreeBSD/NetBSD/OpenBSD)

IP_PORTRANGE_LOW

(Solo FreeBSD/NetBSD/OpenBSD)

SOCK_NONBLOCK

SOCK_CLOEXEC

SO_BINDTOIFINDEX

## Sodium

SODIUM_CRYPTO_AEAD_AEGIS128L_KEYBYTES

SODIUM_CRYPTO_AEAD_AEGIS128L_NSECBYTES

SODIUM_CRYPTO_AEAD_AEGIS128L_NPUBBYTES

SODIUM_CRYPTO_AEAD_AEGIS128L_ABYTES

SODIUM_CRYPTO_AEAD_AEGIS256_KEYBYTES

SODIUM_CRYPTO_AEAD_AEGIS256_NSECBYTES

SODIUM_CRYPTO_AEAD_AEGIS256_NPUBBYTES

SODIUM_CRYPTO_AEAD_AEGIS256_ABYTES

## Tokenizer

T_PUBLIC_SET

T_PROTECTED_SET

T_PRIVATE_SET

## XML

XML_OPTION_PARSE_HUGE

que permite analizar grandes archivos con

xml_parse

y

xml_parse_into_struct

.
