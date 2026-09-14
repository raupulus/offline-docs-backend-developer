---
title: dgettext
description: Reemplaza el dominio actual
source_url: https://www.php.net/manual/es/function.dgettext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gettext/functions/dgettext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gettext
translation_status: ready
translation_reviewed: false
translation_revision: a4fd6e61b
order: 26370
---

dgettext

Reemplaza el dominio actual

## Descripción

```php
dgettext(string $domain, string $message): string
```php

`dgettext` reemplaza el dominio actual `domain` para una búsqueda simple en `message`.

## Parámetros

`domain`  
El dominio

`message`  
El mensaje

## Valores devueltos

Un string en caso de éxito.

## Errores/Excepciones

Lanza una ValueError si `domain` es un string vacío.

## Historial de cambios

| Versión | Descripción                                                |
|---------|------------------------------------------------------------|
| 8.4.0   | Ahora lanza una ValueError si `domain` es un string vacío. |

## Véase también

`gettext`
