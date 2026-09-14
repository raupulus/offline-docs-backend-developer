---
title: ob_implicit_flush
description: Activa/desactiva el envío implícito
source_url: https://www.php.net/manual/es/function.ob-implicit-flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-implicit-flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: false
translation_revision: 1cdb6d04a
order: 59840
---

ob_implicit_flush

Activa/desactiva el envío implícito

## Descripción

```php
ob_implicit_flush([bool $enable]): void
```php

`ob_implicit_flush` activa/desactiva el envío implícito. La puesta en memoria intermedia implícita provocará una operación de volcado después de cada bloque de código que produzca una salida, de modo que no serán necesarios los llamados explícitos a `flush`.

> [!NOTE]
> Mostrar strings vacíos o enviar encabezados no se considera una salida y no desencadenará una operación de volcado.

> [!NOTE]
> Esta función no tiene ningún efecto sobre los gestores de salida de nivel usuario, tales como los iniciados por `ob_start` o `output_add_rewrite_var`.

## Parámetros

`enable`  
`true` para activar, `false` en caso contrario.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `enable` ahora espera un valor `bool`; anteriormente, se esperaba un `int`. |

## Véase también

`flush`, `ob_start`, `ob_end_flush`
