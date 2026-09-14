---
title: strcoll
description: Comparación de strings localizadas
source_url: https://www.php.net/manual/es/function.strcoll.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strcoll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: e095023e4
order: 89270
---

strcoll

Comparación de strings localizadas

## Descripción

```php
strcoll(string $string1, string $string2): int
```php

Se debe tener en cuenta que esta comparación distingue entre mayúsculas y minúsculas, y que, a diferencia de `strcmp`, no es compatible con strings binarios.

`strcoll` utiliza la configuración local/regional actual para realizar la comparación. Si la configuración local/regional actual es C o POSIX, esta función es entonces equivalente a la función `strcmp`.

## Parámetros

`string1`  
El primer string.

`string2`  
El segundo string.

## Valores devueltos

Devuelve \< 0 si `string1` es menor que `string2`; \> 0 si `string1` es mayor que `string2`, y 0 si los dos strings son iguales.

## Véase también

`preg_match`, `strcmp`, `strcasecmp`, `substr`, `stristr`, `strncasecmp`, `strncmp`, `strstr`, `setlocale`
