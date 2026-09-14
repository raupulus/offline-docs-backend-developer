---
title: php_user_filter::filter
description: Llamado cuando se aplica un filtro
source_url: https://www.php.net/manual/es/php-user-filter.filter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/php_user_filter/filter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 4f6742c6e
order: 88260
---

php_user_filter::filter

Llamado cuando se aplica un filtro

## Descripción

```php
public php_user_filter::filter(resource $in, resource $out, int $consumed, bool $closing): int
```php

Este método es llamado siempre que los datos son leídos desde o escritos en el flujo adjunto (como con `fread` o `fwrite`).

## Parámetros

`in`  
`in` es un recurso que apunta a una `cadena de recipientes` que contiene uno o más objetos `recipiente` que contienen información que va a ser filtrada.

`out`  
`out` es un recurso que apunta a una segunda `cadena de recipientes` dentro de la cual se deberían ubicar los recipientes modificados.

`consumed`  
`consumed`, el cual *siempre* debe ser declarado por referencia, debería ser incrementado por la longitud de la información que el filtro lee y altera. En la mayoría de los casos esto significa que se incrementará `consumed` por `$recipiente->datalen` para cada `$recipiente`.

`closing`  
Si el flujo está en el proceso de cierre (y por lo tanto éste es el último pase a través de la cadena de filtros), el parámetro `closing` será establecido a `true`.

## Valores devueltos

El método filter debe devolver uno de estos tres valores cuando se complete.

| Valor Devuelto | Significado |
|----|----|
| `PSFS_PASS_ON` | El filtró se procesó con éxito con información disponible en la `cadena de recipientes` `out`. |
| `PSFS_FEED_ME` | El filtró se procesó con éxito, sin embargo no había información disponible que devolver. Se requiere más información del flujo o del filtro previo. |
| `PSFS_ERR_FATAL` (predeterminado) | El filtro experimentó un error irrecuperable y no puede continuar. |
