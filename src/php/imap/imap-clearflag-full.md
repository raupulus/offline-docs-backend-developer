---
title: imap_clearflag_full
description: Elimina un flag en un mensaje
source_url: https://www.php.net/manual/es/function.imap-clearflag-full.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-clearflag-full.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 673d373ed
order: 38000
---

imap_clearflag_full

Elimina un flag en un mensaje

## Descripción

```php
imap_clearflag_full(IMAP\Connection $imap, string $sequence, string $flag, [int $options]): true
```php

`imap_clearflag_full` borra el flag `flag` en los mensajes de la secuencia `sequence`, del flujo imap `stream`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`sequence`  
Una secuencia de números de mensajes. Se pueden enumerar los mensajes deseados con la sintaxis `X,Y`, o recuperar todos los mensajes contenidos en un intervalo, con la sintaxis `X:Y`

`flag`  
Los flags `flag` que se pueden borrar son "\\Seen", "\\Answered", "\\Flagged", "\\Deleted" y "\\Draft" (tal como se definen en la [RFC2060](https://datatracker.ietf.org/doc/html/rfc2060))

`options`  
`options` es una máscara de bits, que acepta únicamente el siguiente valor:

- `ST_UID` - la secuencia contiene UID en lugar de números de secuencia

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Lanza una excepción `ValueError` si el argumento `options` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
| 8.0.0 | Una excepción `ValueError` es ahora lanzada para valores inválidos del argumento `options`. Anteriormente, se emitía una advertencia y la función devolvía `false`. |

## Véase también

`imap_setflag_full`
