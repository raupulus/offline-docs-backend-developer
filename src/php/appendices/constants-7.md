---
title: Nuevas Constantes Globales
source_url: https://www.php.net/manual/es/migration81.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration81/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: b3e7b1692
order: 840
---

## Nuevas Constantes Globales

## cURL

- `CURLOPT_DOH_URL`

- `CURLOPT_ISSUERCERT_BLOB`

- `CURLOPT_PROXY_ISSUERCERT`

- `CURLOPT_PROXY_ISSUERCERT_BLOB`

- `CURLOPT_PROXY_SSLCERT_BLOB`

- `CURLOPT_PROXY_SSLKEY_BLOB`

- `CURLOPT_SSLCERT_BLOB`

- `CURLOPT_SSLKEY_BLOB`

## GD

- `IMG_AVIF`

- `IMG_WEBP_LOSSLESS`

## MySQLi

- `MYSQLI_REFRESH_REPLICA`

  Esta constante se ha añadido en reemplazo de `MYSQLI_REFRESH_SLAVE`, en consonancia con un cambio en la versión original de MySQL. La constante antigua sigue disponible por razones de compatibilidad ascendente, pero puede ser depreciada/eliminada en el futuro.

## PCNTL

- `PRIO_DARWIN_BG`

- `PRIO_DARWIN_THREAD`

## POSIX

- `POSIX_RLIMIT_KQUEUES`

- `POSIX_RLIMIT_NPTS`

## Sockets

Las siguientes opciones de socket ahora están definidas si son soportadas:

- `SO_ACCEPTFILTER`

- `SO_DONTTRUNC`

- `SO_WANTMORE`

- `SO_MARK`

- `TCP_DEFER_ACCEPT`

## Sodium

- `SODIUM_CRYPTO_STREAM_XCHACHA20_NONCEBYTES`

- `SODIUM_CRYPTO_STREAM_XCHACHA20_KEYBYTES`

- `SODIUM_CRYPTO_SCALARMULT_RISTRETTO255_BYTES`

- `SODIUM_CRYPTO_SCALARMULT_RISTRETTO255_SCALARBYTES`

- `SODIUM_CRYPTO_CORE_RISTRETTO255_BYTES`

- `SODIUM_CRYPTO_CORE_RISTRETTO255_HASHBYTES`

- `SODIUM_CRYPTO_CORE_RISTRETTO255_SCALARBYTES`

- `SODIUM_CRYPTO_CORE_RISTRETTO255_NONREDUCEDSCALARBYTES`

## Estándar

- `IMAGETYPE_AVIF`

## Tokenizer

- `T_READONLY`
