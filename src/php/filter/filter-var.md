---
title: filter_var
description: Filtra una variable con el filtro que se indique
source_url: https://www.php.net/manual/es/function.filter-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/functions/filter-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_reviewed: false
translation_revision: c938838be
order: 24230
---

filter_var

Filtra una variable con el filtro que se indique

## Descripción

```php
filter_var(mixed $value, [int $filter], [array $options]): mixed
```php

Filtra una variable usando un filtro de validación `FILTER_VALIDATE_*`, un filtro de saneamiento `FILTER_SANITIZE_*`, o un filtro definido por el usuario.

## Parámetros

`value`  
Valor a filtrar.

> [!WARNING]
> Valores escalares son [convertidos a string](#language.types.string.casting) internamente antes de ser filtrados.

`filter`  
El filtro a aplicar. Puede ser un filtro de validación usando una de las constantes `FILTER_VALIDATE_*`, un filtro de saneamiento usando una de las constantes `FILTER_SANITIZE_*` o `FILTER_UNSAFE_RAW`, o un filtro personalizado usando `FILTER_CALLBACK`.

> [!NOTE]
> Por omisión es `FILTER_DEFAULT`, que es un alias de `FILTER_UNSAFE_RAW`. Esto resultará en que no se aplique ningún filtro por omisión.

`options`  
O bien un `array` asociativo de opciones, o bien una máscara de bits de constantes de indicadores de filtro `FILTER_FLAG_*`.

Si el `filter` acepta opciones, los indicadores pueden ser proporcionados usando el campo `"flags"` del array.

## Valores devueltos

En caso de éxito devuelve la variable filtrada. En caso de fallo se devuelve `false`, a menos que se use el flag `FILTER_NULL_ON_FAILURE`, en cuyo caso se devuelve `null`.

## Ejemplos

Ejemplo de `filter_var`

```
<?php
var_dump(filter_var('bob@example.com', FILTER_VALIDATE_EMAIL));
var_dump(filter_var('https://example.com', FILTER_VALIDATE_URL, FILTER_FLAG_PATH_REQUIRED));
?>

   
```php

El ejemplo anterior mostrará:

    string(15) "bob@example.com"
    bool(false)

Ejemplo validando entradas de un array

```
<?php
$emails = [
    "bob@example.com",
    "test@example.local",
    "invalidemail"
];

var_dump(filter_var($emails, FILTER_VALIDATE_EMAIL, FILTER_REQUIRE_ARRAY));
?>

   
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      string(15) "bob@example.com"
      [1]=>
      string(18) "test@example.local"
      [2]=>
      bool(false)
    }

Ejemplo de pasar un array para `options`

```
<?php

$options = [
    'options' => [
        'min_range' => 10,
    ],
    'flags' => FILTER_FLAG_ALLOW_OCTAL,
];

var_dump(filter_var('0755', FILTER_VALIDATE_INT, $options));
var_dump(filter_var('011', FILTER_VALIDATE_INT, $options));

?>

   
```php

El ejemplo anterior mostrará:

    int(493)
    bool(false)

Proporcionar flags directamente o vía un `array`

```
<?php

$str = 'string';

var_dump(filter_var($str, FILTER_VALIDATE_BOOLEAN, FILTER_NULL_ON_FAILURE));
var_dump(filter_var($str, FILTER_VALIDATE_BOOLEAN, ['flags' => FILTER_NULL_ON_FAILURE]));

?>

   
```php

El ejemplo anterior mostrará:

    NULL
    NULL

## Véase también

filter_var_array

filter_input

filter_input_array

Filtros de validación

FILTER_VALIDATE\_

\*

Filtros de saneación

FILTER_SANITIZE\_

\*
