---
title: Opciones de contexto SSL
description: Lista de opciones de contexto SSL
source_url: https://www.php.net/manual/es/context.ssl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/context/ssl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 8bc832a46
order: 2040
---

Opciones de contexto SSL

Lista de opciones de contexto SSL

## Descripción

Opciones de contexto para los protocolos `ssl://` y `tls://`.

## Opciones

`peer_name` `string`  
Nombre de pares a utilizar. Si este valor no está definido, entonces el nombre será adivinado basándose en el nombre de host utilizado al abrir el flujo.

`verify_peer` `bool`  
Requiere una verificación del certificado SSL utilizado.

Por omisión, vale `true`.

`verify_peer_name` `bool`  
Requiere la verificación del nombre de pares.

Por omisión, vale `true`.

`allow_self_signed` `bool`  
Permite los certificados autofirmados. Requiere el parámetro [`verify_peer`](#context.ssl.verify-peer).

Por omisión, vale `false`

`cafile` `string`  
Ubicación del fichero de la autoridad del certificado en el sistema de ficheros local que deberá ser utilizado con la opción de contexto `verify_peer` para identificar el par distante.

`capath` `string`  
Si `cafile` no está especificado o si el certificado no ha sido encontrado, se realizará una búsqueda en el directorio señalado por `capath` para encontrar un certificado válido. `capath` debe ser un directorio de certificados válido.

`local_cert` `string`  
Ruta al certificado local, en el sistema de ficheros. Debe ser un fichero codificado PEM que contiene su certificado y su clave privada. Puede, opcionalmente, contener la cadena de certificación del emisor. La clave privada también puede estar contenida en un fichero separado especificado por `local_pk`.

`local_pk` `string`  
Ruta de acceso al fichero de clave privada local en el sistema de ficheros en el caso de ficheros separados para el certificado (`local_cert`) y la clave privada.

`passphrase` `string`  
La frase de paso con la que su fichero `local_cert` ha sido codificado.

`verify_depth` `int`  
Fallará si la cadena de certificación es demasiado profunda.

Por omisión, no se realiza ninguna verificación.

`ciphers` `string`  
Define la lista de cifrados. El formato de la cadena está descrito en la página [ciphers(1)](https://docs.openssl.org/master/man1/openssl-ciphers/).

Por omisión, vale `DEFAULT`.

`capture_peer_cert` `bool`  
Si se define a `true`, se creará una opción de contexto `peer_certificate` que contendrá el certificado del emisor.

`capture_peer_cert_chain` `bool`  
Si se define a `true`, se creará una opción de contexto `peer_certificate_chain` que contendrá la cadena de certificación.

`SNI_enabled` `bool`  
Si vale `true`, la indicación sobre el nombre del servidor estará activada. Activar SNI permite utilizar múltiples certificados en la misma dirección IP.

`disable_compression` `bool`  
Si se define, la compresión TLS estará desactivada. Esto puede ayudar a mitigar el vector de ataque CRIME.

`peer_fingerprint` `string` \| `array`  
Se detiene cuando el digest del certificado distante no coincide con el hash especificado.

Cuando se utiliza una `string`, la longitud determinará el algoritmo de hachaje utilizado, ya sea "md5" (32) o "sha1" (40).

Cuando se utiliza un `array`, la clave indica el nombre del algoritmo de hachaje, y cada valor correspondiente representa el digest esperado.

`security_level` `int`  
Define el nivel de seguridad. Si no se especifica, se utiliza el nivel de seguridad por omisión. Los niveles de seguridad están descritos en [SSL_CTX_get_security_level(3)](https://docs.openssl.org/master/man3/SSL_CTX_set_security_level/).

Disponible a partir de PHP 7.2.0 y OpenSSL 1.1.0.

## Historial de cambios

| Versión | Descripción                                              |
|---------|----------------------------------------------------------|
| 7.2.0   | Adición de `security_level`. Requiere OpenSSL \>= 1.1.0. |

## Notas

> [!NOTE]
> Dado que `ssl://` es un protocolo subyacente para los gestores [`https://`](#wrappers.http) y [`ftps://`](#wrappers.ftp), todas las opciones de contexto aplicadas a `ssl://` también se aplicarán a `https://` y `ftps://`.

> [!NOTE]
> Para que SNI (Server Name Indication) esté disponible, PHP debe ser compilado con OpenSSL 0.9.8j o superior. Utilice la constante `OPENSSL_TLSEXT_SERVER_NAME` para determinar si SNI es soportado o no.

## Véase también

[???](#context.socket)
