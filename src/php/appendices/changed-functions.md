---
title: Funciones modificadas
source_url: https://www.php.net/manual/es/migration56.changed-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration56/changed-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: da75c15e0
order: 160
---

## Funciones modificadas

## Núcleo de PHP

- `crypt` ahora lanza un error `E_NOTICE` si se omite el parámetro `salt`.

- `substr_compare` ahora acepta `0` para su parámetro `length`.

- `unserialize` ahora fallará si los datos serializados proporcionados se han manipulado para instanciar un objeto sin llamar a su constructor.

## [cURL](#book.curl)

- El envío de archivos usando la sintaxis `@file` ahora solo se admite si la opción `CURLOPT_SAFE_UPLOAD` está definida como `false`. Se debería usar `CURLFile` en su lugar.

## [Mcrypt](#book.mcrypt)

- El parámetro `source` de `mcrypt_create_iv` ahora tiene como valor predeterminado `MCRYPT_DEV_URANDOM` en lugar de `MCRYPT_DEV_RANDOM`.

## [OpenSSL](#book.openssl)

- `stream_socket_enable_crypto` ahora permite que el parámetro `crypto_type` sea opcional si el contexto SSL del flujo incluye la nueva opción `crypto_type`.

## [PostgreSQL](#book.pgsql)

- `pg_insert`, `pg_select`, `pg_update` y `pg_delete` ya no están en estado experimental.

- `pg_send_execute`, `pg_send_prepare`, `pg_send_query` y `pg_send_query_params` ya no bloquearán la ejecución hasta que finalice la escritura de la consulta si el flujo del socket subyacente para la conexión a la base de datos está establecido en modo no bloqueante.

## [Reflection](#book.reflection)

- ReflectionClass::newInstanceWithoutConstructor ahora permite que las clases internas no finales sean instanciadas.

## [XMLReader](#book.xmlreader)

- XMLReader::getAttributeNs y XMLReader::getAttributeNo ahora devuelven `null` si el atributo no puede ser encontrado, como XMLReader::getAttribute.
