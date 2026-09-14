---
title: stream_context_set_option
description: Configura una opción para un flujo/gestor/contexto
source_url: https://www.php.net/manual/es/function.stream-context-set-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-context-set-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: e2d1e1f44
order: 87870
---

stream_context_set_option

Configura una opción para un flujo/gestor/contexto

## Descripción

```php
stream_context_set_option(resource $stream_or_context, string $wrapper, string $option_name, mixed $value): bool
```php

La firma alternativa siguiente está obsoleta a partir de PHP 8.4.0, utilice `stream_context_set_options` en su lugar.

```php
stream_context_set_option(resource $stream_or_context, array $options): bool
```

`stream_context_set_option` define una opción para el contexto especificado. El valor `value` se define para la `option` para el contexto `wrapper`.

## Parámetros

`stream_or_context`  
El flujo o el recurso de contexto al que se aplica la opción.

`wrapper`  
El nombre del gestor (que puede ser diferente del protocolo). Consulte la sección sobre los [contextos](#context) para conocer la lista de parámetros estándar de flujo.

`option_name`  
El nombre de la opción.

`value`  
El valor de la opción.

`options`  
La opción a definir para el parámetro `stream_or_context`.

> [!NOTE]
> El parámetro `options` debe ser un array asociativo de arrays asociativos, en el formato `$arr['wrapper']['option'] = $value`.
>
> Consulte la sección sobre los [contextos](#context) para conocer la lista de parámetros estándar de flujo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | La firma alternativa con 2 parámetros está ahora obsoleta. Utilice `stream_context_set_options` en su lugar. |
