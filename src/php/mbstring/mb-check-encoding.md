---
title: mb_check_encoding
description: Verifica si las cadenas son válidas para el encodage especificado
source_url: https://www.php.net/manual/es/function.mb-check-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-check-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: d2ff0abe1
order: 44960
---

mb_check_encoding

Verifica si las cadenas son válidas para el encodage especificado

## Descripción

```php
mb_check_encoding([array $value], [string $encoding]): bool
```php

Verifica si el flujo de octetos es válido para el encodage específico. Si `value` es de tipo `array`, todas las claves y los valores son validados de manera recursiva. Es útil para prever lo que se conoce como « ataque por encodage inválido ».

## Parámetros

`value`  
El flujo de octetos o `array` a verificar. Si es omitido, esta función verifica todas las entradas desde el inicio de la petición.

> [!WARNING]
> A partir de PHP 8.1.0, la omisión de este argumento o el paso de `null` está obsoleto.

`encoding`  
Encodage esperado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | La llamada a esta función con `null` como `value` o sin argumento está obsoleta. |
| 8.0.0 | `value` y `encoding` ahora son nullable. |
| 7.2.0 | Esta función ahora también acepta un `array` como valor de `value`. Anteriormente, solo las `string` eran soportadas. |
