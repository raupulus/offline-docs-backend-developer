---
title: bind_textdomain_codeset
description: Especifica o recupera el juego de caracteres utilizado para los mensajes
  del dominio DOMAIN
source_url: https://www.php.net/manual/es/function.bind-textdomain-codeset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gettext/functions/bind-textdomain-codeset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gettext
translation_status: ready
translation_reviewed: false
translation_revision: 679cf93fa
order: 26330
---

bind_textdomain_codeset

Especifica o recupera el juego de caracteres utilizado para los mensajes del dominio DOMAIN

## Descripción

```php
bind_textdomain_codeset(string $domain, [string $codeset]): string
```php

`bind_textdomain_codeset` permite recuperar o definir la codificación en la cual los mensajes de `domain` serán devueltos por `gettext` y funciones similares.

## Parámetros

`domain`  
El dominio.

`codeset`  
El juego de caracteres. Si `null`, la codificación actualmente definida es devuelta.

## Valores devueltos

Una `string` en caso de éxito.

## Errores/Excepciones

Lanza una ValueError si `domain` es una `string` vacía.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Lanza ahora una ValueError si `domain` es una `string` vacía. |
| 8.4.0 | `codeset` es ahora opcional. Anteriormente, este parámetro debía siempre ser especificado. |
| 8.0.3 | `codeset` es ahora nullable. Anteriormente, no era posible recuperar la codificación actualmente definida. |

## Notas

> [!NOTE]
> La información `bind_textdomain_codeset` es mantenida por proceso, y no por hilo.
