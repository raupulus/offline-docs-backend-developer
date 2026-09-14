---
title: preg_match
description: Realiza una búsqueda de coincidencia con una expresión regular estándar
source_url: https://www.php.net/manual/es/function.preg-match.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-match.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: false
translation_revision: 4de6272a1
order: 61620
---

preg_match

Realiza una búsqueda de coincidencia con una expresión regular estándar

## Descripción

```php
preg_match(string $pattern, string $subject, [array $matches], [int $flags], [int $offset]): int
```php

Analiza `subject` para encontrar la expresión que coincide con `pattern`.

## Parámetros

`pattern`  
El patrón a buscar, en forma de cadena.

`subject`  
La cadena de entrada.

`matches`  
Si `matches` es proporcionado, será llenado con los resultados de la búsqueda. `$matches[0]` contendrá el texto que satisface el patrón completo, `$matches[1]` contendrá el texto que satisface la primera subexpresión capturante, etc.

`flags`  
El parámetro `flags` puede ser una combinación de los siguientes flags:

`PREG_OFFSET_CAPTURE`  
Si esta opción está activada, todas las subcadenas que satisfacen el patrón también serán identificadas por su offset (en bytes). Tenga en cuenta que esto modifica el valor de `matches` que se convierte en un array donde cada elemento es un array que contiene la cadena que coincide con el patrón en el offset `0` así como el offset de la cadena en `subject` en el offset `1`.

```
<?php
preg_match('/(foo)(bar)(baz)/', 'foobarbaz', $matches, PREG_OFFSET_CAPTURE);
print_r($matches);
?>

            
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Array
            (
                [0] => foobarbaz
                [1] => 0
            )

        [1] => Array
            (
                [0] => foo
                [1] => 0
            )

        [2] => Array
            (
                [0] => bar
                [1] => 3
            )

        [3] => Array
            (
                [0] => baz
                [1] => 6
            )

    )

`PREG_UNMATCHED_AS_NULL`  
Si este flag es pasado, los subpatrones no coincidentes son reportados como `null`; de lo contrario son reportados como una `string` vacía.

```
<?php
preg_match('/(a)(b)*(c)/', 'ac', $matches);
var_dump($matches);
preg_match('/(a)(b)*(c)/', 'ac', $matches, PREG_UNMATCHED_AS_NULL);
var_dump($matches);
?>

            
```php

El ejemplo anterior mostrará:

    array(4) {
      [0]=>
      string(2) "ac"
      [1]=>
      string(1) "a"
      [2]=>
      string(0) ""
      [3]=>
      string(1) "c"
    }
    array(4) {
      [0]=>
      string(2) "ac"
      [1]=>
      string(1) "a"
      [2]=>
      NULL
      [3]=>
      string(1) "c"
    }

`offset`  
Normalmente, la búsqueda comienza al inicio de la cadena subject. El parámetro opcional `offset` puede ser utilizado para especificar una posición para el inicio de la búsqueda (en bytes).

> [!NOTE]
> Utilizar el parámetro `offset` no es equivalente a pasar `substr($subject, $offset)` a `preg_match_all` en lugar de la cadena subject, ya que `pattern` puede contener aserciones como *^*, *\$* o *(?\<=x)*. Compárese:
>
> <div class="informalexample">
>
> ```
> <?php
> $subject = "abcdef";
> $pattern = '/^def/';
> preg_match($pattern, $subject, $matches, PREG_OFFSET_CAPTURE, 3);
> print_r($matches);
> ?>
>
>          
> ```
>
> El ejemplo anterior mostrará:
>
>     Array
>     (
>     )
>
>              
>
> con este ejemplo:
>
> ```
> <?php
> $subject = "abcdef";
> $pattern = '/^def/';
> preg_match($pattern, substr($subject,3), $matches, PREG_OFFSET_CAPTURE);
> print_r($matches);
> ?>
>
>          
> ```
>
> producirá:
>
>     Array
>     (
>         [0] => Array
>             (
>                 [0] => def
>                 [1] => 0
>             )
>
>     )
>
>              
>
> Por lo tanto, para evitar el uso de `substr`, utilizar la aserción `\G` en lugar del ancla `^`, o el modificador `A`, ambos funcionan con el parámetro `offset`.
>
> </div>

## Valores devueltos

`preg_match` devuelve 1 si el `pattern` coincide con el `subject` dado, 0 si no coincide, o `false` si ocurre un error.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Errores/Excepciones

Si el patrón regex pasado no se compila a una regex válida, se emite una `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | `PREG_UNMATCHED_AS_NULL` ahora es soportado para el parámetro `flags`. |

## Ejemplos

Encontrar la cadena "php"

```
<?php
// El "i" después del delimitador del patrón indica que la búsqueda no será sensible a mayúsculas/minúsculas
if (preg_match("/php/i", "PHP es el mejor lenguaje de script del web.")) {
    echo "Se encontró un resultado.";
} else {
    echo "No se encontró ningún resultado.";
}
?>

    
```php

Encontrar la palabra "web"

```
<?php
/* \b, en el patrón, indica un límite de palabra, de forma que la palabra
 "web" sea detectada, y no solo partes de palabras como
 en "webbing" o "cobweb" */
if (preg_match("/\bweb\b/i", "PHP es el mejor lenguaje de script del web.")) {
    echo "La palabra fue encontrada.";
} else {
    echo "La palabra no fue encontrada.";
}

echo "\n";

if (preg_match("/\bweb\b/i", "PHP es el mejor lenguaje de script del web.")) {
    echo "La palabra fue encontrada.";
} else {
    echo "La palabra no fue encontrada.";
}
?>

    
```php

Leer un nombre de dominio en una URL

```
<?php
// detectar el nombre del host en la URL
preg_match('@^(?:http://)?([^/]+)@i',
    "http://www.php.net/index.html", $matches);
$host = $matches[1];

// detectar los dos últimos segmentos del nombre del host
preg_match('/[^.]+\.[^.]+$/', $host, $matches);
echo "El nombre de dominio es: {$matches[0]}\n";
?>

    
```php

El ejemplo anterior mostrará:

    El nombre de dominio es: php.net

Uso de subpatrones nombrados

```
<?php

$str = 'foobar: 2008';

preg_match('/(?P<name>\w+): (?P<digit>\d+)/', $str, $matches);

/* Alternativa */
// preg_match('/(?<name>\w+): (?<digit>\d+)/', $str, $matches);

print_r($matches);

?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => foobar: 2008
        [name] => foobar
        [1] => foobar
        [digit] => 2008
        [2] => 2008
    )

## Notas

> [!TIP]
> No utilice `preg_match` si solo desea saber si una cadena está contenida en otra. Utilice `strpos` en su lugar, ya que será más rápido.

## Véase también

[Patrones PCRE](#pcre.pattern), `preg_quote`, `preg_match_all`, `preg_replace`, `preg_split`, `preg_last_error`, `preg_last_error_msg`
