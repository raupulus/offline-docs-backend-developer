---
title: Nuevas constantes globales
source_url: https://www.php.net/manual/es/migration72.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration72/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 28f0dc949
order: 530
---

## Nuevas constantes globales

## Constantes predefinidas

- [`PHP_FLOAT_DIG`](#constant.php-float-dig)

- [`PHP_FLOAT_EPSILON`](#constant.php-float-epsilon)

- [`PHP_FLOAT_MIN`](#constant.php-float-min)

- [`PHP_FLOAT_MAX`](#constant.php-float-max)

- [`PHP_OS_FAMILY`](#constant.php-os-family)

## [Información sobre los ficheros](#book.fileinfo)

- [`FILEINFO_EXTENSION`](#constant.fileinfo-extension)

## [JSON](#book.json)

- `JSON_INVALID_UTF8_IGNORE`

- `JSON_INVALID_UTF8_SUBSTITUTE`

## [GD](#book.image)

- [`IMG_EFFECT_MULTIPLY`](#constant.img-effect-multiply)

- [`IMG_BMP`](#constant.img-bmp)

## [LDAP](#book.ldap)

- [`LDAP_EXOP_START_TLS`](#constant.ldap-exop-start-tls)

- [`LDAP_EXOP_MODIFY_PASSWD`](#constant.ldap-exop-modify-passwd)

- [`LDAP_EXOP_REFRESH`](#constant.ldap-exop-refresh)

- [`LDAP_EXOP_WHO_AM_I`](#constant.ldap-exop-who-am-i)

- [`LDAP_EXOP_TURN`](#constant.ldap-exop-turn)

## [Tabla de hash de contraseña](#book.password)

- [`PASSWORD_ARGON2I`](#constant.password-argon2i)

- [`PASSWORD_ARGON2_DEFAULT_MEMORY_COST`](#constant.password-argon2-default-memory-cost)

- [`PASSWORD_ARGON2_DEFAULT_TIME_COST`](#constant.password-argon2-default-time-cost)

- [`PASSWORD_ARGON2_DEFAULT_THREADS`](#constant.password-argon2-default-threads)

## [PCRE](#book.pcre)

- `PREG_UNMATCHED_AS_NULL`

## [PDO](#book.pdo)

- [`PDO::PARAM_STR_NATL`](#pdo.constants.param-str-natl)

- [`PDO::PARAM_STR_CHAR`](#pdo.constants.param-str-char)

- [`PDO::ATTR_DEFAULT_STR_PARAM`](#pdo.constants.attr-default-str-param)

## [Sodium](#book.sodium)

- [`SODIUM_LIBRARY_VERSION`](#constant.sodium-library-version)

- [`SODIUM_LIBRARY_MAJOR_VERSION`](#constant.sodium-library-major-version)

- [`SODIUM_LIBRARY_MINOR_VERSION`](#constant.sodium-library-minor-version)

- [`SODIUM_CRYPTO_AEAD_AES256GCM_KEYBYTES`](#constant.sodium-crypto-aead-aes256gcm-keybytes)

- [`SODIUM_CRYPTO_AEAD_AES256GCM_NSECBYTES`](#constant.sodium-crypto-aead-aes256gcm-nsecbytes)

- [`SODIUM_CRYPTO_AEAD_AES256GCM_NPUBBYTES`](#constant.sodium-crypto-aead-aes256gcm-npubbytes)

- [`SODIUM_CRYPTO_AEAD_AES256GCM_ABYTES`](#constant.sodium-crypto-aead-aes256gcm-abytes)

- [`SODIUM_CRYPTO_AEAD_CHACHA20POLY1305_KEYBYTES`](#constant.sodium-crypto-aead-chacha20poly1305-keybytes)

- [`SODIUM_CRYPTO_AEAD_CHACHA20POLY1305_NSECBYTES`](#constant.sodium-crypto-aead-chacha20poly1305-nsecbytes)

- [`SODIUM_CRYPTO_AEAD_CHACHA20POLY1305_NPUBBYTES`](#constant.sodium-crypto-aead-chacha20poly1305-npubbytes)

- [`SODIUM_CRYPTO_AEAD_CHACHA20POLY1305_ABYTES`](#constant.sodium-crypto-aead-chacha20poly1305-abytes)

- [`SODIUM_CRYPTO_AEAD_CHACHA20POLY1305_IETF_KEYBYTES`](#constant.sodium-crypto-aead-chacha20poly1305-ietf-keybytes)

- [`SODIUM_CRYPTO_AEAD_CHACHA20POLY1305_IETF_NSECBYTES`](#constant.sodium-crypto-aead-chacha20poly1305-ietf-nsecbytes)

- [`SODIUM_CRYPTO_AEAD_CHACHA20POLY1305_IETF_NPUBBYTES`](#constant.sodium-crypto-aead-chacha20poly1305-ietf-npubbytes)

- [`SODIUM_CRYPTO_AEAD_CHACHA20POLY1305_IETF_ABYTES`](#constant.sodium-crypto-aead-chacha20poly1305-ietf-abytes)

- [`SODIUM_CRYPTO_AUTH_BYTES`](#constant.sodium-crypto-auth-bytes)

- [`SODIUM_CRYPTO_AUTH_KEYBYTES`](#constant.sodium-crypto-auth-keybytes)

- [`SODIUM_CRYPTO_BOX_SEALBYTES`](#constant.sodium-crypto-box-sealbytes)

- [`SODIUM_CRYPTO_BOX_SECRETKEYBYTES`](#constant.sodium-crypto-box-secretkeybytes)

- [`SODIUM_CRYPTO_BOX_PUBLICKEYBYTES`](#constant.sodium-crypto-box-publickeybytes)

- [`SODIUM_CRYPTO_BOX_KEYPAIRBYTES`](#constant.sodium-crypto-box-keypairbytes)

- [`SODIUM_CRYPTO_BOX_MACBYTES`](#constant.sodium-crypto-box-macbytes)

- [`SODIUM_CRYPTO_BOX_NONCEBYTES`](#constant.sodium-crypto-box-noncebytes)

- [`SODIUM_CRYPTO_BOX_SEEDBYTES`](#constant.sodium-crypto-box-seedbytes)

- [`SODIUM_CRYPTO_KDF_BYTES_MIN`](#constant.sodium-crypto-kdf-bytes-min)

- [`SODIUM_CRYPTO_KDF_BYTES_MAX`](#constant.sodium-crypto-kdf-bytes-max)

- [`SODIUM_CRYPTO_KDF_CONTEXTBYTES`](#constant.sodium-crypto-kdf-contextbytes)

- [`SODIUM_CRYPTO_KDF_KEYBYTES`](#constant.sodium-crypto-kdf-keybytes)

- [`SODIUM_CRYPTO_KX_SEEDBYTES`](#constant.sodium-crypto-kx-seedbytes)

- [`SODIUM_CRYPTO_KX_SESSIONKEYBYTES`](#constant.sodium-crypto-kx-sessionkeybytes)

- [`SODIUM_CRYPTO_KX_PUBLICKEYBYTES`](#constant.sodium-crypto-kx-publickeybytes)

- [`SODIUM_CRYPTO_KX_SECRETKEYBYTES`](#constant.sodium-crypto-kx-secretkeybytes)

- [`SODIUM_CRYPTO_KX_KEYPAIRBYTES`](#constant.sodium-crypto-kx-keypairbytes)

- [`SODIUM_CRYPTO_GENERICHASH_BYTES`](#constant.sodium-crypto-generichash-bytes)

- [`SODIUM_CRYPTO_GENERICHASH_BYTES_MIN`](#constant.sodium-crypto-generichash-bytes-min)

- [`SODIUM_CRYPTO_GENERICHASH_BYTES_MAX`](#constant.sodium-crypto-generichash-bytes-max)

- [`SODIUM_CRYPTO_GENERICHASH_KEYBYTES`](#constant.sodium-crypto-generichash-keybytes)

- [`SODIUM_CRYPTO_GENERICHASH_KEYBYTES_MIN`](#constant.sodium-crypto-generichash-keybytes-min)

- [`SODIUM_CRYPTO_GENERICHASH_KEYBYTES_MAX`](#constant.sodium-crypto-generichash-keybytes-max)

- [`SODIUM_CRYPTO_PWHASH_ALG_ARGON2I13`](#constant.sodium-crypto-pwhash-alg-argon2i13)

- [`SODIUM_CRYPTO_PWHASH_ALG_DEFAULT`](#constant.sodium-crypto-pwhash-alg-default)

- [`SODIUM_CRYPTO_PWHASH_SALTBYTES`](#constant.sodium-crypto-pwhash-saltbytes)

- [`SODIUM_CRYPTO_PWHASH_STRPREFIX`](#constant.sodium-crypto-pwhash-strprefix)

- [`SODIUM_CRYPTO_PWHASH_OPSLIMIT_INTERACTIVE`](#constant.sodium-crypto-pwhash-opslimit-interactive)

- [`SODIUM_CRYPTO_PWHASH_MEMLIMIT_INTERACTIVE`](#constant.sodium-crypto-pwhash-memlimit-interactive)

- [`SODIUM_CRYPTO_PWHASH_OPSLIMIT_MODERATE`](#constant.sodium-crypto-pwhash-opslimit-moderate)

- [`SODIUM_CRYPTO_PWHASH_MEMLIMIT_MODERATE`](#constant.sodium-crypto-pwhash-memlimit-moderate)

- [`SODIUM_CRYPTO_PWHASH_OPSLIMIT_SENSITIVE`](#constant.sodium-crypto-pwhash-opslimit-sensitive)

- [`SODIUM_CRYPTO_PWHASH_MEMLIMIT_SENSITIVE`](#constant.sodium-crypto-pwhash-memlimit-sensitive)

- [`SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_SALTBYTES`](#constant.sodium-crypto-pwhash-scryptsalsa208sha256-saltbytes)

- [`SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_STRPREFIX`](#constant.sodium-crypto-pwhash-scryptsalsa208sha256-strprefix)

- [`SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_OPSLIMIT_INTERACTIVE`](#constant.sodium-crypto-pwhash-scryptsalsa208sha256-opslimit-interactive)

- [`SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_MEMLIMIT_INTERACTIVE`](#constant.sodium-crypto-pwhash-scryptsalsa208sha256-memlimit-interactive)

- [`SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_OPSLIMIT_SENSITIVE`](#constant.sodium-crypto-pwhash-scryptsalsa208sha256-opslimit-sensitive)

- [`SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_MEMLIMIT_SENSITIVE`](#constant.sodium-crypto-pwhash-scryptsalsa208sha256-memlimit-sensitive)

- [`SODIUM_CRYPTO_SCALARMULT_BYTES`](#constant.sodium-crypto-scalarmult-bytes)

- [`SODIUM_CRYPTO_SCALARMULT_SCALARBYTES`](#constant.sodium-crypto-scalarmult-scalarbytes)

- [`SODIUM_CRYPTO_SHORTHASH_BYTES`](#constant.sodium-crypto-shorthash-bytes)

- [`SODIUM_CRYPTO_SHORTHASH_KEYBYTES`](#constant.sodium-crypto-shorthash-keybytes)

- [`SODIUM_CRYPTO_SECRETBOX_KEYBYTES`](#constant.sodium-crypto-secretbox-keybytes)

- [`SODIUM_CRYPTO_SECRETBOX_MACBYTES`](#constant.sodium-crypto-secretbox-macbytes)

- [`SODIUM_CRYPTO_SECRETBOX_NONCEBYTES`](#constant.sodium-crypto-secretbox-noncebytes)

- [`SODIUM_CRYPTO_SIGN_BYTES`](#constant.sodium-crypto-sign-bytes)

- [`SODIUM_CRYPTO_SIGN_SEEDBYTES`](#constant.sodium-crypto-sign-seedbytes)

- [`SODIUM_CRYPTO_SIGN_PUBLICKEYBYTES`](#constant.sodium-crypto-sign-publickeybytes)

- [`SODIUM_CRYPTO_SIGN_SECRETKEYBYTES`](#constant.sodium-crypto-sign-secretkeybytes)

- [`SODIUM_CRYPTO_SIGN_KEYPAIRBYTES`](#constant.sodium-crypto-sign-keypairbytes)

- [`SODIUM_CRYPTO_STREAM_NONCEBYTES`](#constant.sodium-crypto-stream-noncebytes)

- [`SODIUM_CRYPTO_STREAM_KEYBYTES`](#constant.sodium-crypto-stream-keybytes)

## [Zip](#book.zip)

- [`ZipArchive::EM_NONE`](#ziparchive.constants.em-none)

- [`ZipArchive::EM_AES_128`](#ziparchive.constants.em-aes-128)

- [`ZipArchive::EM_AES_192`](#ziparchive.constants.em-aes-192)

- [`ZipArchive::EM_AES_256`](#ziparchive.constants.em-aes-256)
