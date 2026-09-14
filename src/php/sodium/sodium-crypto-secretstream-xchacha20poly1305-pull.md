---
title: sodium_crypto_secretstream_xchacha20poly1305_pull
description: Desencripta un fragmento de datos de un flujo cifrado
source_url: https://www.php.net/manual/es/function.sodium-crypto-secretstream-xchacha20poly1305-pull.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-secretstream-xchacha20poly1305-pull.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76760
---

sodium_crypto_secretstream_xchacha20poly1305_pull

Desencripta un fragmento de datos de un flujo cifrado

## Descripción

```php
sodium_crypto_secretstream_xchacha20poly1305_pull(string $state, string $ciphertext, [string $additional_data]): array
```php

Desencripta un fragmento de datos de un flujo cifrado.

## Parámetros

`state`  
Ver `sodium_crypto_secretstream_xchacha20poly1305_init_pull` y `sodium_crypto_secretstream_xchacha20poly1305_init_push`

`ciphertext`  
El fragmento de texto cifrado a desencriptar.

`additional_data`  
Opcional de datos adicionales a incluir en la etiqueta de autenticación.

## Valores devueltos

Un array con dos valores:

- `string`; el fragmento de texto desencriptado.

- `int`; Una etiqueta opcional (si se proporciona al enviar). Valores posibles: `SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_MESSAGE`: la etiqueta más común, que no añade información sobre la naturaleza del mensaje., `SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_FINAL`: indica que el mensaje marca el final del flujo, y borra la clave secreta utilizada para cifrar la secuencia anterior., `SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_PUSH`: indica que el mensaje marca el final de un conjunto de mensajes, pero no el final del flujo. Por ejemplo, una enorme cadena JSON enviada en varios fragmentos puede utilizar esta etiqueta para indicar a la aplicación que la cadena está completa y que puede ser decodificada. Pero el flujo mismo no está cerrado, y otros datos pueden seguir., `SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_REKEY`: "olvidar" la clave utilizada para cifrar este mensaje y los anteriores, y derivar una nueva clave secreta.
