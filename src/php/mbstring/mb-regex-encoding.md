---
title: mb_regex_encoding
description: Define/Recupera la codificación de caracteres para las expresiones regulares
  multioctetos
source_url: https://www.php.net/manual/es/function.mb-regex-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-regex-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 8cdc6621f
order: 45340
---

mb_regex_encoding

Define/Recupera la codificación de caracteres para las expresiones regulares multioctetos

## Descripción

```php
mb_regex_encoding([string $encoding]): string
```php

Define/Recupera la codificación de caracteres para las expresiones regulares multioctetos.

## Parámetros

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Si `encoding` está definido, entonces Esta función retorna `true` en caso de éxito o `false` si ocurre un error.. En este caso, la codificación de caracteres interna no es modificada. Si el argumento `encoding` es omitido, entonces el nombre de la codificación de caracteres actual para las expresiones regulares multioctetos será devuelto.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `encoding` ahora acepta `null`. |

## Véase también

`mb_internal_encoding`, `mb_ereg`
