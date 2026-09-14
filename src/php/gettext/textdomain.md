---
title: textdomain
description: Define el dominio por defecto
source_url: https://www.php.net/manual/es/function.textdomain.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gettext/functions/textdomain.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gettext
translation_status: ready
translation_reviewed: false
translation_revision: 679cf93fa
order: 26410
---

textdomain

Define el dominio por defecto

## Descripción

```php
textdomain([string $domain]): string
```php

Esta función define el dominio de búsqueda a utilizar durante las llamadas a `gettext`. Este dominio depende generalmente de la aplicación.

## Parámetros

`domain`  
El nuevo dominio de mensajes, o `null` para recuperar la configuración actual sin modificaciones.

## Valores devueltos

Esta función devuelve el mensaje actual del dominio en caso de éxito, después de una posible modificación.

## Errores/Excepciones

Genera una ValueError si `domain` es un `string` vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Genera ahora una ValueError si `domain` es un `string` vacío. |
| 8.4.0 | `domain` ahora es opcional. Anteriormente, este argumento debía especificarse siempre. |

## Notas

> [!NOTE]
> La información de `textdomain` se mantiene por proceso, y no por hilo.
