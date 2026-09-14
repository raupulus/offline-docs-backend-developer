---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/openssl.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 6eadfc433
order: 58980
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

## Opciones de validación general

`X509_PURPOSE_SSL_CLIENT` (`int`)  

`X509_PURPOSE_SSL_SERVER` (`int`)  

`X509_PURPOSE_NS_SSL_SERVER` (`int`)  

`X509_PURPOSE_SMIME_SIGN` (`int`)  

`X509_PURPOSE_SMIME_ENCRYPT` (`int`)  

`X509_PURPOSE_CRL_SIGN` (`int`)  

`X509_PURPOSE_ANY` (`int`)  

`X509_PURPOSE_OCSP_HELPER` (`int`)  
Verifica el certificado para su uso como ayudante de respondedor OCSP. Disponible a partir de PHP 8.4.0.

`X509_PURPOSE_TIMESTAMP_SIGN` (`int`)  
Verifica el certificado para su uso como firmante de marcas de tiempo de confianza. Disponible a partir de PHP 8.4.0.

## Opciones de relleno (`Padding`) para el cifrado asimétrico

`OPENSSL_PKCS1_PADDING` (`int`)  

`OPENSSL_SSLV23_PADDING` (`int`)  

`OPENSSL_NO_PADDING` (`int`)  

`OPENSSL_PKCS1_OAEP_PADDING` (`int`)  

`OPENSSL_PKCS1_PSS_PADDING` (`int`)  
Relleno RSA-PSS. Disponible a partir de PHP 8.5.0.

## Tipos de clave

`OPENSSL_KEYTYPE_RSA` (`int`)  
Tipo de clave RSA.

`OPENSSL_KEYTYPE_DSA` (`int`)  
Tipo de clave DSA.

`OPENSSL_KEYTYPE_DH` (`int`)  
Tipo de clave DH (Diffie-Hellman).

`OPENSSL_KEYTYPE_EC` (`int`)  
Tipo de clave de curva elíptica.

`OPENSSL_KEYTYPE_X25519` (`int`)  
Tipo de clave de curva X25519. Esta constante solo está disponible cuando PHP se compila con OpenSSL 3.0+.

`OPENSSL_KEYTYPE_ED25519` (`int`)  
Tipo de clave de curva Ed25519. Esta constante solo está disponible cuando PHP se compila con OpenSSL 3.0+.

`OPENSSL_KEYTYPE_X448` (`int`)  
Tipo de clave de curva X448. Esta constante solo está disponible cuando PHP se compila con OpenSSL 3.0+.

`OPENSSL_KEYTYPE_ED448` (`int`)  
Tipo de clave de curva Ed448. Esta constante solo está disponible cuando PHP se compila con OpenSSL 3.0+.

## Constantes/opciones PKCS7

Las funciones S/MIME utilizan opciones que se especifican mediante un campo de bits. Los valores válidos son:

| Constante | Descripción |
|----|----|
| `PKCS7_TEXT` (`int`) | Añade el texto en claro en los encabezados del mensaje firmado/cifrado. Al descifrar o verificar, se eliminan simplemente estos datos. Si el mensaje cifrado o firmado no es del tipo MIME, se producirá un error. |
| `PKCS7_BINARY` (`int`) | Normalmente, el mensaje se convierte al formato canónico que utiliza efectivamente `CR` y `LF` como fin de línea, como se solicita en las especificaciones de S/MIME. Cuando esta opción está activada, el mensaje no se convertirá. Esto es útil cuando se manipulan datos binarios que no están en formato MIME. |
| `PKCS7_NOINTERN` (`int`) | Al verificar un mensaje, los certificados (si los hay) incluidos en el mensaje se utilizan normalmente para buscar el certificado de firma. Con esta opción, solo se utiliza el certificado especificado por el argumento `untrusted_certificates_filename` de la función `openssl_pkcs7_verify`. Los certificados proporcionados pueden seguir utilizándose, con un nivel de confianza reducido. |
| `PKCS7_NOVERIFY` (`int`) | No verifica los certificados de los firmantes de un mensaje firmado. |
| `PKCS7_NOCHAIN` (`int`) | No encadena las verificaciones de los certificados de los firmantes. Es decir, no utiliza los certificados contenidos en el mensaje. |
| `PKCS7_NOCERTS` (`int`) | Al firmar un mensaje, el certificado del firmante se incluye normalmente. Con esta opción, esto se desactiva. Esto reducirá el tamaño del mensaje, pero el verificador deberá tener una copia local del certificado del firmante (pasado al argumento `untrusted_certificates_filename`, con la función `openssl_pkcs7_verify`). |
| `PKCS7_NOATTR` (`int`) | Normalmente, cuando se firma un mensaje, se incluye un conjunto de atributos que contiene la hora de firma y el algoritmo simétrico soportado, en el mensaje. Con esta opción, no se incluye. |
| `PKCS7_DETACHED` (`int`) | Al firmar un mensaje, se utiliza la firma en texto claro, con el tipo MIME `"multipart/signed"`. Este es el valor por defecto del argumento `flags` para la función `openssl_pkcs7_sign`. Si se anula esta opción, el mensaje se firmará de manera opaca, lo que resiste mejor a la traducción de los relés de correo (algunos antiguos servidores de correo corrompen los mensajes), pero impide la lectura por los clientes de correo que no conocen S/MIME. |
| `PKCS7_NOSIGS` (`int`) | No verifica las firmas de un mensaje |
| `PKCS7_NOOLDMIMETYPE` (`int`) | Disponible a partir de PHP 8.3.0. Establece el encabezado HTTP Content-Type en `application/pkcs7-mime` en lugar de `application/x-pkcs7-mime` para cifrar un mensaje. |
| `PKCS7_NOSMIMECAP` (`int`) | Disponible a partir de PHP 8.5.0. No incluye las capacidades S/MIME (SMIMECapabilities) en la firma. |
| `PKCS7_CRLFEOL` (`int`) | Disponible a partir de PHP 8.5.0. Utiliza `CRLF` como fin de línea en la salida. |
| `PKCS7_NOCRL` (`int`) | Disponible a partir de PHP 8.5.0. No incluye las CRL en la estructura PKCS7. |
| `PKCS7_NO_DUAL_CONTENT` (`int`) | Disponible a partir de PHP 8.5.0. No incluye el contenido duplicado, evitando la duplicación del contenido firmado. |

Constantes PKCS7

## Bandera/Constantes CMS

Las funciones CMS utilizan banderas que se especifican utilizando una máscara de bits que incluye una o más de las siguientes opciones:

| Constantes | Descripción |
|----|----|
| `OPENSSL_CMS_TEXT` (`int`) | Añade el encabezado content type `text/plain` al mensaje cifrado/firmado. Al descifrar/verificar, estos encabezados se eliminan de la salida, si el mensaje descifrado o verificado no es del tipo MIME `text/plain` entonces se producirá un error. |
| `OPENSSL_CMS_BINARY` (`int`) | Normalmente el mensaje de entrada se convierte a su forma "canónica" que en realidad utiliza `CR` y `LF` como fin de línea: tal como se requiere por la especificación CMS. Cuando esta opción está presente, ninguna traducción se realiza. Esto es útil al manejar datos binarios que pueden no estar en formato CMS. |
| `OPENSSL_CMS_NOINTERN` (`int`) | Al verificar un mensaje, los certificados (si los hay) incluidos en el mensaje se utilizan normalmente para buscar el certificado de firma. Con esta opción, solo se utilizan los certificados especificados en el argumento `untrusted_certificates_filename` de `openssl_cms_verify`. Los certificados proporcionados pueden seguir utilizándose como autoridades de certificación no fiables. |
| `OPENSSL_CMS_NOVERIFY` (`int`) | No verifica el certificado del firmante de un mensaje firmado. |
| `OPENSSL_CMS_NOCERTS` (`int`) | Al firmar un mensaje el certificado del firmante se incluye normalmente, con esta opción se excluye. Esto reducirá el tamaño del mensaje firmado pero el verificador debe tener una copia del certificado del firmante disponible localmente (pasado utilizando `untrusted_certificates_filename` de `openssl_cms_verify` por ejemplo). |
| `OPENSSL_CMS_NOATTR` (`int`) | Normalmente cuando un mensaje es firmado, se incluyen un conjunto de atributos que incluyen la hora de firma y los algoritmos simétricos soportados. Con esta opción no se incluyen. |
| `OPENSSL_CMS_DETACHED` (`int`) | Al firmar un mensaje, se utiliza la firma en texto claro con el tipo MIME `"multipart/signed"`. Este es el comportamiento por defecto, si no se especifica ningún `flags` a `openssl_cms_sign`. Si se desactiva esta opción, el mensaje se firmará utilizando una firma opaca, que es más resistente a la traducción por los relés de correo pero no puede ser leída por los agentes de correo que no soportan S/MIME. |
| `OPENSSL_CMS_NOSIGS` (`int`) | No intenta verificar las firmas de un mensaje |
| `OPENSSL_CMS_OLDMIMETYPE` (`int`) | Disponible a partir de PHP 8.3.0. Establece el encabezado HTTP Content-Type en `application/x-pkcs7-mime` en lugar de `application/pkcs7-mime` para cifrar un mensaje. |

Constantes CMS

## Algoritmo de firma

`OPENSSL_ALGO_DSS1` (`int`)  

`OPENSSL_ALGO_SHA1` (`int`)  
Utilizado como algoritmo por defecto para las funciones `openssl_sign` y `openssl_verify`.

`OPENSSL_ALGO_SHA224` (`int`)  

`OPENSSL_ALGO_SHA256` (`int`)  

`OPENSSL_ALGO_SHA384` (`int`)  

`OPENSSL_ALGO_SHA512` (`int`)  

`OPENSSL_ALGO_RMD160` (`int`)  

`OPENSSL_ALGO_MD5` (`int`)  

`OPENSSL_ALGO_MD4` (`int`)  

`OPENSSL_ALGO_MD2` (`int`)  
Esta constante solo está disponible cuando PHP se compila con soporte MD2. Es necesario pasar el CFLAG `-DHAVE_OPENSSL_MD2_H` al compilar PHP y pasar `enable-md2` al compilar OpenSSL 1.0.0+.

## Cifrados

`OPENSSL_DEFAULT_STREAM_CIPHERS` (`string`)  
Lista de cifrados por defecto.

`OPENSSL_CIPHER_RC2_40` (`int`)  

`OPENSSL_CIPHER_RC2_128` (`int`)  

`OPENSSL_CIPHER_RC2_64` (`int`)  

`OPENSSL_CIPHER_DES` (`int`)  

`OPENSSL_CIPHER_3DES` (`int`)  

<!-- -->

`OPENSSL_CIPHER_AES_128_CBC` (`int`)  

`OPENSSL_CIPHER_AES_192_CBC` (`int`)  

`OPENSSL_CIPHER_AES_256_CBC` (`int`)  

## Constantes de versión

`OPENSSL_VERSION_TEXT` (`string`)  

`OPENSSL_VERSION_NUMBER` (`int`)  

## Constantes de identificación del nombre del servidor

`OPENSSL_TLSEXT_SERVER_NAME` (`int`)  
Si el soporte SNI está disponible o no.

> [!NOTE]
> Esta constante solo está disponible cuando PHP se compila con OpenSSL 0.9.8j o posterior

## Otras constantes

`OPENSSL_RAW_DATA` (`int`)  
Si `OPENSSL_RAW_DATA` está definida en `openssl_encrypt` o `openssl_decrypt`, los datos devueltos se devuelven tal cual. Cuando esto no está especificado, los datos devueltos al llamador están codificados en Base64.

`OPENSSL_DONT_ZERO_PAD_KEY` (`int`)  
Impide que `openssl_encrypt` rellene las claves que son más cortas que la longitud de clave por defecto.

`OPENSSL_ZERO_PADDING` (`int`)  
Por defecto, las operaciones de cifrado se completan utilizando bloques estándar y el relleno se verifica y elimina al descifrar. Si la constante `OPENSSL_ZERO_PADDING` está definida en el argumento `options` de la función `openssl_encrypt` o `openssl_decrypt` entonces no se realizará ningún relleno, la cantidad total de datos cifrados deberá ser entonces un múltiplo del tamaño del bloque o bien se producirá un error.

`OPENSSL_ENCODING_SMIME` (`int`)  
Indica que la codificación es S/MIME.

`OPENSSL_ENCODING_DER` (`int`)  
Indica que la codificación es DER (Distinguished Encoding Rules).

`OPENSSL_ENCODING_PEM` (`int`)  
Indica que la codificación es PEM (Privacy-Enhanced Mail).
