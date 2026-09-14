---
title: Modos de cifrado Mcrypt
source_url: https://www.php.net/manual/es/mcrypt.ciphers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/ciphers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45670
---

## Modos de cifrado Mcrypt

A continuación se presenta una lista no exhaustiva de los modos de cifrado de la extensión mcrypt. Para disponer de una lista completa de los cifrados soportados, consulte las definiciones en el fichero `mcrypt.h`. La regla general con la API mcrypt-2.2.x es que se puede acceder al modo de cifrado desde PHP con la constante MCRYPT_ciphername. Con la biblioteca libmcrypt-2.4.x y libmcrypt-2.5.x, estas constantes funcionan siempre, pero es posible especificar el nombre del cifrado en una cadena, al llamar a `mcrypt_module_open`.

- MCRYPT_3DES

- MCRYPT_ARCFOUR_IV (libmcrypt \> 2.4.x únicamente)

- MCRYPT_ARCFOUR (libmcrypt \> 2.4.x únicamente)

- MCRYPT_BLOWFISH

- MCRYPT_CAST_128

- MCRYPT_CAST_256

- MCRYPT_CRYPT

- MCRYPT_DES

- MCRYPT_DES_COMPAT (libmcrypt 2.2.x únicamente)

- MCRYPT_ENIGMA (libmcrypt \> 2.4.x únicamente, alias de MCRYPT_CRYPT)

- MCRYPT_GOST

- MCRYPT_IDEA (no libre)

- MCRYPT_LOKI97 (libmcrypt \> 2.4.x únicamente)

- MCRYPT_MARS (libmcrypt \> 2.4.x únicamente, no libre)

- MCRYPT_PANAMA (libmcrypt \> 2.4.x únicamente)

- MCRYPT_RIJNDAEL_128 (libmcrypt \> 2.4.x únicamente)

- MCRYPT_RIJNDAEL_192 (libmcrypt \> 2.4.x únicamente)

- MCRYPT_RIJNDAEL_256 (libmcrypt \> 2.4.x únicamente)

- MCRYPT_RC2

- MCRYPT_RC4 (libmcrypt 2.2.x únicamente)

- MCRYPT_RC6 (libmcrypt \> 2.4.x únicamente)

- MCRYPT_RC6_128 (libmcrypt 2.2.x únicamente)

- MCRYPT_RC6_192 (libmcrypt 2.2.x únicamente)

- MCRYPT_RC6_256 (libmcrypt 2.2.x únicamente)

- MCRYPT_SAFER64

- MCRYPT_SAFER128

- MCRYPT_SAFERPLUS (libmcrypt \> 2.4.x únicamente)

- MCRYPT_SERPENT(libmcrypt \> 2.4.x únicamente)

- MCRYPT_SERPENT_128 (libmcrypt 2.2.x únicamente)

- MCRYPT_SERPENT_192 (libmcrypt 2.2.x únicamente)

- MCRYPT_SERPENT_256 (libmcrypt 2.2.x únicamente)

- MCRYPT_SKIPJACK (libmcrypt \> 2.4.x únicamente)

- MCRYPT_TEAN (libmcrypt 2.2.x únicamente)

- MCRYPT_THREEWAY

- MCRYPT_TRIPLEDES (libmcrypt \> 2.4.x únicamente)

- MCRYPT_TWOFISH (para las versiones antiguas de mcrypt 2.x o mcrypt \> 2.4.x )

- MCRYPT_TWOFISH128 (TWOFISHxxx está disponible en las nuevas versiones 2.x, pero no en las versiones 2.4.x)

- MCRYPT_TWOFISH192

- MCRYPT_TWOFISH256

- MCRYPT_WAKE (libmcrypt \> 2.4.x únicamente)

- MCRYPT_XTEA (libmcrypt \> 2.4.x únicamente)

Se debe (modo `CFB` y `OFB`) o puede (modo `CBC`) proporcionar un vector de inicialización (IV) para estos modos de cifrado. IV debe ser único, y tener el mismo valor en el cifrado y en el descifrado. Para datos que serán almacenados después del cifrado, se puede tomar el resultado de una función como MD5, aplicada al nombre del fichero. De lo contrario, se puede enviar IV con los datos cifrados, (consulte el capítulo 9.3 de Applied Cryptography by Schneier (ISBN 0-471-11709-9) de Schneier (ISBN 0-471-11709-9) para más detalles sobre el tema).
