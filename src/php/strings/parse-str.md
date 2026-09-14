---
title: parse_str
description: Analiza una string como una cadena de consulta URL
source_url: https://www.php.net/manual/es/function.parse-str.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/parse-str.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: da15b6674
order: 88960
---

parse_str

Analiza una string como una cadena de consulta URL

## Descripción

```php
parse_str(string $string, array $result): void
```php

Analiza la string `string` como si se tratara de los parámetros pasados a través de la URL. Todas las variables que identifica son creadas con sus valores respectivos (o en el array si `result` es proporcionado).

## Parámetros

`string`  
La string de entrada.

`result`  
Una variable pasada por referencia, que será definida como un array conteniendo los pares clave-valor extraídos de `string`. Si el parámetro `result` no es pasado, una variable separada es definida en el ámbito local para cada clave.

> [!WARNING]
> El uso de esta función sin el parámetro `result` está muy fuertemente *desaconsejado* y *no recomendado* a partir de PHP 7.2. A partir de PHP 8.0.0, el parámetro `result` es *obligatorio*.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `result` ya no es opcional. |
| 7.2.0 | El uso de `parse_str` sin el segundo argumento emite una nota `E_DEPRECATED`. |

## Ejemplos

Ejemplo con `parse_str`

```
<?php
$str = "first=value&arr[]=foo+bar&arr[]=baz";

// Recomendado
parse_str($str, $output);
echo $output['first'], PHP_EOL;  // value
echo $output['arr'][0], PHP_EOL; // foo bar
echo $output['arr'][1], PHP_EOL; // baz
?>

    
```php

Cualquier espacio o punto en los nombres de parámetros es convertido a guión bajo al crear claves de array o variables locales. Esto se debe a que los nombres de variables en PHP no pueden contener espacios o puntos, pero esto se aplica incluso cuando se utiliza esta función con el parámetro `result`.

Deformación de nombres por `parse_str`

```
<?php
parse_str("My Value=Something", $output);
echo $output['My_Value']; // Something
?>

    
```php

## Notas

> [!NOTE]
> La función `parse_str` se ve afectada por la directiva [max_input_vars](#ini.max-input-vars). Exceder este límite genera una advertencia `E_WARNING`, y cualquier variable más allá de este límite no es añadida al array de resultado. El valor por omisión es 1000; ajuste [max_input_vars](#ini.max-input-vars) según sus necesidades.

> [!NOTE]
> Todos los valores añadidos en el array `result` (o las variables creadas si el segundo parámetro no está definido) ya están decodificados con las mismas reglas que `urldecode`.

> [!NOTE]
> Para obtener la cadena de consulta de la petición actual, se puede utilizar la variable `$_SERVER['QUERY_STRING']`. Asimismo, puede ser de interés leer la sección sobre las [variables de fuentes externas](#language.variables.external).

## Véase también

`parse_url`, `pathinfo`, `http_build_query`, `urldecode`
