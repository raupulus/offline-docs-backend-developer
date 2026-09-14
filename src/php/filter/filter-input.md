---
title: filter_input
description: Toma una variable externa concreta por su nombre y opcionalmente la filtra
source_url: https://www.php.net/manual/es/function.filter-input.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/functions/filter-input.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_reviewed: false
translation_revision: f7e68a1a3
order: 24200
---

filter_input

Toma una variable externa concreta por su nombre y opcionalmente la filtra

## Descripción

```php
filter_input(int $type, string $var_name, [int $filter], [array $options]): mixed
```php

## Parámetros

`type`  
Una de las constantes `INPUT_*`.

> [!WARNING]
> El contenido de la superglobal que se está filtrando es el original "sin procesar" proporcionado por SAPI, antes de cualquier modificación del usuario a la superglobal. Para filtrar una superglobal modificada, utilice `filter_var_array` en su lugar.

`var_name`  
Nombre de una variable a filtrar dentro de la superglobal correspondiente `type`.

## Valores devueltos

Valor de la variable solicitada en caso de éxito, `false` si el filtro falla, o `null` si la variable `var_name` no está definida. Si se usa el flag `FILTER_NULL_ON_FAILURE`, devuelve `false` si la variable no está definida y `null` si el filtro falla.

## Ejemplos

Un ejemplo de `filter_input`

```
<?php
$search_html = filter_input(INPUT_GET, 'search', FILTER_SANITIZE_SPECIAL_CHARS);
$search_url = filter_input(INPUT_GET, 'search', FILTER_SANITIZE_ENCODED);
echo "Has buscado $search_html.\n";
echo "<a href='?search=$search_url'>Busca de nuevo.</a>";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Has buscado Me &#38; son.
    <a href='?search=Me%20%26%20son'>Busca de nuevo.</a>

## Véase también

filter_input_array

filter_var

filter_var_array

Filtros de validación

FILTER_VALIDATE\_

\*

Filtros de saneación

FILTER_SANITIZE\_

\*
