---
title: Contextos de Flujos
source_url: https://www.php.net/manual/es/stream.contexts.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/contexts.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 96c9d88ba
order: 87740
---

## Contextos de Flujos

Un `contexto` es un conjunto de `parámetros` y `opciones` específicas de envolturas que modifican o mejoran el comportamiento de un flujo. Los `contextos` se crean usando `stream_context_create` y se pueden pasar a la mayoría de las funciones de creación de flujos relacionados con sistemas de archivos (esto es, `fopen`, `file`, `file_get_contents`, etc...).

Se pueden especificar `opciones` cuando se llama a `stream_context_create`, o después, usando `stream_context_set_option`. Una lista de `opciones` específicas de envolturas se puede encontrar en el capítulo [???](#context).

Se pueden especificar `parámetros` para los `contextos` usando la función `stream_context_set_params`.
