---
title: La clase streamWrapper
source_url: https://www.php.net/manual/es/class.streamwrapper.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 88560
---

## Introducción

Permite implementar sus propios gestores de protocolo y flujos para usarlos con las demás funciones de sistemas de archivos (como `fopen`, `fread` etc.).

> [!NOTE]
> Esta *NO* es una clase real, sólo es un prototipo de cómo debería ser una clase que define su propio protocolo.

> [!NOTE]
> Implementar los métodos de distinta forma que la descrita aquí puede conducir a un comportamiento indefinido.

Una instancia de esta clase se inicializa tan pronto como una función de flujo intente acceder al protocolo al que está asociado.

## Sinopsis de la clase

streamWrapper

streamWrapper

Propiedades

public

resource

context

Métodos

## Propiedades

recurso de `context`  
El [contexto](#context) actual, o `null` si no se pasó ningún contexto a la función que realizó la llamada.

Use la función `stream_context_get_options` para analizar el contexto.

> [!NOTE]
> Esta propiedad *debe* ser pública para que PHP pueda rellenarla con el recurso de contexto real.

## Véase también

[???](#stream.streamwrapper.example-1), `stream_wrapper_register`, `stream_wrapper_unregister`, `stream_wrapper_restore`
