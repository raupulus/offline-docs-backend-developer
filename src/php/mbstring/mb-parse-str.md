---
title: mb_parse_str
description: Analiza los datos HTTP GET/POST/COOKIE y asigna las variables globales
source_url: https://www.php.net/manual/es/function.mb-parse-str.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-parse-str.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45320
---

mb_parse_str

Analiza los datos HTTP GET/POST/COOKIE y asigna las variables globales

## Descripción

```php
mb_parse_str(string $string, array $result): bool
```php

Analiza los datos de entrada HTTP GET/POST/COOKIE y asigna las variables globales. Dado que PHP no proporciona valores brutos de POST/COOKIE, esta función solo es utilizable con los datos en método GET. `mb_parse_str` toma los datos de la URL llamante, detecta el juego de caracteres, convierte los datos al juego de caracteres interno, y asigna los valores al array de variables globales.

## Parámetros

`string`  
Los datos codificados en URL.

`result`  
Un array que contiene los valores decodificados y los nombres de los juegos de caracteres.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El segundo argumento ya no es opcional. |
| 7.2.0 | Una llamada a la función `mb_parse_str` sin el segundo argumento se ha vuelto obsoleta. |

## Véase también

`mb_detect_order`, `mb_internal_encoding`
