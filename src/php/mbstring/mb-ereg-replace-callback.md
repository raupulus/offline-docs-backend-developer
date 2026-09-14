---
title: mb_ereg_replace_callback
description: Buscar y reemplazar mediante expresión regular con soporte multi byte
  utilizando una función de devolución de llamada
source_url: https://www.php.net/manual/es/function.mb-ereg-replace-callback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ereg-replace-callback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 14c33cf17
order: 45100
---

mb_ereg_replace_callback

Buscar y reemplazar mediante expresión regular con soporte multi byte utilizando una función de devolución de llamada

## Descripción

```php
mb_ereg_replace_callback(string $pattern, callable $callback, string $string, [string $options]): string
```php

Busca los `string` que coinciden con el argumento `pattern`, luego reemplaza los textos que coinciden con el retorno de la función `callback`.

El comportamiento de esta función es casi idéntico a `mb_ereg_replace`, a excepción de que el argumento `replacement` debe especificar una función de devolución de llamada `callback`.

## Parámetros

`pattern`  
La expresión regular.

Los caracteres multi byte pueden ser utilizados en el `pattern`.

`callback`  
Un callback que será llamado y se le pasará un array de elementos coincidentes en la cadena de caracteres `string`. El callback debe retornar la cadena reemplazada.

Con frecuencia será necesario utilizar la función `callback` para `mb_ereg_replace_callback` solo una vez. En este caso se pueden utilizar las [funciones anónimas](#functions.anonymous) para declarar una función de devolución de llamada al momento de llamar a la función `mb_ereg_replace_callback`. Al hacerlo de esta manera se tiene toda la información necesaria para la llamada de la función en un solo lugar, lo que permite evitar saturar el espacio de nombres de las funciones con un callback de función que no se utiliza en otro lugar.

`string`  
El `string` que debe ser verificado.

`options`  
La opción de búsqueda. Para más explicaciones, consulte `mb_regex_set_options`.

## Valores devueltos

Retorna un `string` en caso de éxito, o `false` en caso de error. Si `string` no es válido para el codificación actual, `null` es retornado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `options` ahora es nullable. |
| 7.1.0 | Esta función verifica si `string` es válido para la codificación actual. |

## Ejemplos

Ejemplo con `mb_ereg_replace_callback`

```
<?php
// este texto fue utilizado en 2002
// se desea actualizarlo para 2003
$text = "April fools day is 04/01/2002\n";
$text.= "Last christmas was 12/24/2001\n";
// la función de devolución de llamada
function next_year($matches)
{
  // como de costumbre: $matches[0] es la coincidencia completa
  // $matches[1] la coincidencia para el primer subpatrón
  // encerrado en '(...)' y así sucesivamente
  return $matches[1].($matches[2]+1);
}
echo mb_ereg_replace_callback(
            "(\d{2}/\d{2}/)(\d{4})",
            "next_year",
            $text);

?>

    
```php

El ejemplo anterior mostrará:

    April fools day is 04/01/2003
    Last christmas was 12/24/2002

`mb_ereg_replace_callback` utilizando funciones anónimas

```
<?php
// este texto fue utilizado en 2002
// se desea actualizarlo para 2003
$text = "April fools day is 04/01/2002\n";
$text.= "Last christmas was 12/24/2001\n";

echo mb_ereg_replace_callback(
            "(\d{2}/\d{2}/)(\d{4})",
            function ($matches) {
               return $matches[1].($matches[2]+1);
            },
            $text);
?>

    
```php

## Notas

> [!NOTE]
> La codificación interna o la codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función.

## Véase también

`mb_regex_encoding`, `mb_ereg_replace`, [Funciones anónimas](#functions.anonymous)
