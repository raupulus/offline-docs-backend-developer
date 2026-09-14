---
title: session_unset
description: Destruye todas las variables de una sesión
source_url: https://www.php.net/manual/es/function.session-unset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-unset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 682510e91
order: 73920
---

session_unset

Destruye todas las variables de una sesión

## Descripción

```php
session_unset(): bool
```php

`session_unset` destruye todas las variables de la sesión actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | El tipo de retorno de esta función es ahora `bool`. Anteriormente, era [void](#language.types.declarations.void). |

## Notas

> [!NOTE]
> Si se utiliza `$_SESSION` utilice `unset` para destruir una variable de sesión, es decir `unset($_SESSION['nomvariable']);`.

> [!CAUTION]
> No se debe destruir `$_SESSION` con `unset($_SESSION)` ya que esto desactivará la posibilidad de almacenar variables de sesión a partir del array superglobal `$_SESSION`.

> [!NOTE]
> Únicamente `session_unset` debe utilizarse para código antiguo que no utiliza `$_SESSION`.
>
> > [!CAUTION]
> > Esta función solo funciona si una sesión está activa. No vaciará el array `$_SESSION` si la sesión no ha sido iniciada o si ya ha sido destruida. Utilice `$_SESSION = []` para eliminar todas las variables de sesión incluso si la sesión no está activa.
