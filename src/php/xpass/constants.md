---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/xpass.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xpass/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xpass
translation_status: ready
translation_reviewed: true
translation_revision: 1526b45ee
order: 104010
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

La extensión Xpass proporciona diversos conjuntos de constantes. Métodos de hash (`CRYPT_PREFIX_*`) para el parámetro prefix de `crypt_gensalt`. Códigos de error (`CRYPT_SALT_*`) devueltos por `crypt_checksalt`. Algoritmos de contraseña (`PASSWORD_*`) para el parámetro algo de `password_hash`.

`CRYPT_PREFIX_STD_DES` (`string`)  
El método de hash original de Unix V7, basado en el cifrado por bloques DES. Dado que DES es poco costoso en el hardware moderno, solo hay `4096` salts posibles y 2\*\*56 contraseñas distintas, que se truncan a 8 caracteres, es posible encontrar cualquier contraseña hasheada con este método. No debería usarse excepto para soportar sistemas operativos antiguos que no soportan ningún otro algoritmo de generación de hash, debido a la debilidad de los hashes DES.

`CRYPT_PREFIX_EXT_DES` (`string`)  
Una extensión del DES tradicional, que elimina el límite de longitud, aumenta el tamaño del salt y hace el costo temporal ajustable. Proviene de BSDI BSD/OS y también está disponible en al menos NetBSD, OpenBSD y FreeBSD debido al uso de la biblioteca FreeSec de David Burren. Es mucho mejor que los hashes DES tradicionales y bigcrypt, pero aún no debería usarse para nuevos hashes.

`CRYPT_PREFIX_MD5` (`string`)  
Un hash basado en el algoritmo MD5, desarrollado originalmente por Poul-Henning Kamp para FreeBSD. Soportado en la mayoría de los Unix libres y versiones más recientes de Solaris. No tan débil como los hashes basados en DES, pero MD5 es tan poco costoso en el hardware moderno que no debería usarse para nuevos hashes. El costo de procesamiento no es ajustable.

`CRYPT_PREFIX_BLOWFISH` (`string`)  
Un hash basado en el cifrado por bloques Blowfish, modificado para tener un calendario de claves extra-costoso. Desarrollado originalmente por Niels Provos y David Mazieres para OpenBSD y también soportado en versiones recientes de FreeBSD y NetBSD, en Solaris 10 y más reciente, y en varias distribuciones GNU/\*/Linux.

`CRYPT_PREFIX_SHA256` (`string`)  
Un hash basado en SHA-2 con una salida de 256 bits, desarrollado originalmente por Ulrich Drepper para GNU libc. Soportado en Linux pero no común en otros lugares. Aceptable para nuevos hashes. El parámetro de costo de procesamiento por defecto es `5000`, lo cual es demasiado bajo para el hardware moderno.

`CRYPT_PREFIX_SHA512` (`string`)  
Un hash basado en SHA-2 con una salida de 512 bits, desarrollado originalmente por Ulrich Drepper para GNU libc. Soportado en Linux pero no común en otros lugares. Aceptable para nuevos hashes. El parámetro de costo de procesamiento por defecto es `5000`, lo cual es demasiado bajo para el hardware moderno.

`CRYPT_PREFIX_SCRYPT` (`string`)  
Scrypt es una función de derivación de clave basada en contraseña creada por Colin Percival, originalmente para el servicio de respaldo en línea Tarsnap. El algoritmo fue diseñado específicamente para hacer costosas las ataques de hardware personalizados a gran escala al requerir grandes cantidades de memoria. En 2016, el algoritmo scrypt fue publicado por el IETF como RFC 7914.

`CRYPT_PREFIX_GOST_YESCRYPT` (`string`)  
Gost-yescrypt usa la salida de yescrypt como mensaje de entrada para HMAC con la función de hash GOST R 34.11-2012 (Streebog) con un resumen de 256 bits. Así, las propiedades criptográficas de yescrypt son suplantadas por las de la función de hash GOST. Este método de hash es útil en aplicaciones que requieren un hash de contraseña moderno, pero deben basarse en algoritmos GOST. La función de hash GOST R 34.11-2012 (Streebog) fue publicada por el IETF como RFC 6986. Aceptable para nuevos hashes si es necesario.

`CRYPT_PREFIX_YESCRYPT` (`string`)  
Yescrypt es un esquema de hash de contraseña escalable diseñado por Solar Designer, que se basa en el scrypt de Colin Percival. Aunque la fuerza de yescrypt contra los ataques de adivinación de contraseñas proviene de su diseño de algoritmo, su seguridad criptográfica está garantizada por su uso de SHA-256 en la capa externa. La función de hash SHA-256 fue publicada por el NIST en el FIPS PUB 180-2 (y sus revisiones posteriores como el FIPS PUB 180-4) y por el IETF como RFC 4634 (y posteriormente RFC 6234). Recomendado para nuevos hashes.

`CRYPT_PREFIX_SM3CRYPT` (`string`)  
Un hash basado en la función de hash ShangMi 3 con una salida de 256 bits, que usa el mismo diseño que sha256crypt y/o sha512crypt. Soportado en EulerOS, Kylin, openEuler y openKylin, pero no es común en otros lugares. Aceptable para nuevos hashes si es necesario. El parámetro de costo de procesamiento por defecto es 5000, lo cual es demasiado bajo para el hardware moderno.

Disponible a partir de 1.2.0 con libcxcrypt \>= 4.5.0.

`CRYPT_PREFIX_SM3_YESCRYPT` (`string`)  
Sm3-yescrypt usa la salida de yescrypt como mensaje de entrada para HMAC con la función de hash ShangMi 3 con un resumen de 256 bits. Así, las propiedades criptográficas de yescrypt son suplantadas por las de la función de hash ShangMi 3. Este método de hash es útil en aplicaciones que necesitan un hash de contraseña moderno, pero deben basarse en algoritmos aprobados por la Oficina de Administración de Criptografía Comercial del Estado de China (OSCCA). La función de hash ShangMi 3 ha sido publicada en la Parte 3: "Dedicated hash-functions" de la ISO/IEC 10118-3:2018. Aceptable para nuevos hashes si es necesario.

Disponible a partir de 1.2.0 con libcxcrypt \>= 4.5.0.

<!-- -->

`CRYPT_SALT_OK` (`int`)  
No hay error.

`CRYPT_SALT_INVALID` (`int`)  
Método de hash desconocido o parámetros inválidos.

`CRYPT_SALT_METHOD_DISABLED` (`int`)  
El método de hash ya no está permitido para ser usado.

`CRYPT_SALT_METHOD_LEGACY` (`int`)  
El método de hash ya no se considera lo suficientemente fuerte.

`CRYPT_SALT_TOO_CHEAP` (`int`)  
El costo de los parámetros se considera demasiado bajo.

<!-- -->

`PASSWORD_SHA512` (`string`)  
`PASSWORD_SHA512` se usa para crear nuevos hashes de contraseña usando el algoritmo `CRYPT_PREFIX_SHA512`.

`PASSWORD_YESCRYPT` (`string`)  
`PASSWORD_YESCRYPT` se usa para crear nuevos hashes de contraseña usando el algoritmo `CRYPT_PREFIX_YESCRYPT`.

`PASSWORD_SM3CRYPT` (`string`)  
`PASSWORD_SM3CRYPT` se usa para crear nuevos hashes de contraseña usando el algoritmo `CRYPT_PREFIX_SM3CRYPT`.

Disponible a partir de 1.2.0 con libcxcrypt \>= 4.5.0.

`PASSWORD_SM3_YESCRYPT` (`string`)  
`PASSWORD_SM3_YESCRYPT` se usa para crear nuevos hashes de contraseña usando el algoritmo `CRYPT_PREFIX_SM3_YESCRYPT`.

Disponible a partir de 1.2.0 con libcxcrypt \>= 4.5.0.
