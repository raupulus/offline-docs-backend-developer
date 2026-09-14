---
title: dngettext
description: Versión plural de dgettext
source_url: https://www.php.net/manual/es/function.dngettext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gettext/functions/dngettext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gettext
translation_status: ready
translation_reviewed: false
translation_revision: a4fd6e61b
order: 26380
---

dngettext

Versión plural de dgettext

## Descripción

```php
dngettext(string $domain, string $singular, string $plural, int $count): string
```php

`dngettext` permite reemplazar el dominio actual `domain` para una búsqueda simple en plural de un mensaje.

## Parámetros

`domain`  
El dominio

`singular`  

`plural`  

`count`  

## Valores devueltos

Un `string` en caso de éxito.

## Errores/Excepciones

Genera una ValueError si `domain` es un `string` vacío.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.4.0   | Genera ahora una ValueError si `domain` es un `string` vacío. |

## Véase también

`ngettext`
