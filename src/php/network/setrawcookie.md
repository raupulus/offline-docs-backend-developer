---
title: setrawcookie
description: Envía un cookie sin codificar su valor en URL
source_url: https://www.php.net/manual/es/function.setrawcookie.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/setrawcookie.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: d829c7d11
order: 56540
---

setrawcookie

Envía un cookie sin codificar su valor en URL

## Descripción

```php
setrawcookie(string $name, [string $value], [int $expires_or_options], [string $path], [string $domain], [bool $secure], [bool $httponly]): bool
```php

Firma alternativa disponible a partir de PHP 7.3.0 (no soportado con argumentos nombrados):

```php
setrawcookie(string $name, [string $value], [array $options]): bool
```

`setrawcookie` es idéntica a `setcookie` excepto que el valor del cookie no será automáticamente codificado en URL al enviarlo al navegador.

## Parámetros

Para más información, consúltese la documentación de la función `setcookie`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.0 | Se ha añadido una firma alternativa que soporta un array de `options`. Esta firma permite definir el atributo SameSite del cookie. |

## Véase también

`setcookie`
