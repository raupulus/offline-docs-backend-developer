---
title: EventBuffer::searchEol
description: Busca en el búfer una ocurrencia de fin de línea
source_url: https://www.php.net/manual/es/eventbuffer.searcheol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/searcheol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19320
---

EventBuffer::searchEol

Busca en el búfer una ocurrencia de fin de línea

## Descripción

```php
public EventBuffer::searchEol([int $start], [int $eol_style]): mixed
```php

Busca en el búfer una ocurrencia de fin de línea especificada por el argumento `eol_style`. El método devuelve la posición numérica del string, o `false` si el string no ha sido encontrado.

Si el argumento `start` es proporcionado, representa la posición donde la búsqueda comenzará; de lo contrario, la búsqueda se realizará desde el inicio del string. Si el argumento `end` es proporcionado, la búsqueda se realizará entre las posiciones de inicio y fin del búfer.

## Parámetros

`start`  
Posición de inicio de la búsqueda.

`eol_style`  
Una constante [EventBuffer:EOL\_\*](#eventbuffer.constants).

## Valores devueltos

Devuelve la posición numérica de la primera ocurrencia del símbolo de fin de línea en el búfer, o bien `false` si no ha sido encontrado.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Véase también

EventBuffer::search
