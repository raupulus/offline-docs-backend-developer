---
title: sodium_crypto_secretstream_xchacha20poly1305_push
description: Cifra un fragmento de datos para que pueda ser descifrado en una API
  de streaming
source_url: https://www.php.net/manual/es/function.sodium-crypto-secretstream-xchacha20poly1305-push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-secretstream-xchacha20poly1305-push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76770
---

sodium_crypto_secretstream_xchacha20poly1305_push

Cifra un fragmento de datos para que pueda ser descifrado en una API de streaming

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_secretstream_xchacha20poly1305_push(string $state, string $message, [string $additional_data], [int $tag]): string
```php

Cifra un fragmento de datos para que pueda ser descifrado en una API de streaming.

## Parámetros

`state`  
Ver `sodium_crypto_secretstream_xchacha20poly1305_init_pull` y `sodium_crypto_secretstream_xchacha20poly1305_init_push`

`message`  

`additional_data`  

`tag`  
Opcional. Puede ser utilizado para afirmar el comportamiento de descifrado (es decir, el reordenamiento o la indicación del último fragmento en un flujo).

SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_MESSAGE

: la etiqueta más común, que no añade información sobre la naturaleza del mensaje.

SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_FINAL

: indica que el mensaje marca el final del flujo, y borra la clave secreta utilizada para cifrar la secuencia anterior.

SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_PUSH

: indica que el mensaje marca el final de un conjunto de mensajes, pero no el final del flujo. Por ejemplo, una enorme cadena JSON enviada en varios fragmentos puede utilizar esta etiqueta para indicar a la aplicación que la cadena está completa y que puede ser decodificada. Pero el flujo mismo no está cerrado, y otros datos pueden seguir.

SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_REKEY

: "olvidar" la clave utilizada para cifrar este mensaje y los anteriores, y derivar una nueva clave secreta.

## Valores devueltos

Devuelve el fragmento de texto cifrado.
