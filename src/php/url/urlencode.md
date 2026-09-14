---
title: urlencode
description: Codifica como URL una cadena
source_url: https://www.php.net/manual/es/function.urlencode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/urlencode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_revision: '767338231'
order: 100280
---

urlencode

Codifica como URL una cadena

## Descripción

```php
urlencode(string $string): string
```php

Esta función es conveniente cuando se codifica una cadena a ser usada como la parte de consulta de una URL, como método práctico para pasar variables a la siguiente página.

## Parámetros

`string`  
La cadena a ser codificada.

## Valores devueltos

Devuelve una cadena en la que todos los caracteres no-alfanuméricos excepto `-_.` han sido reemplazados con un signo de porcentaje (`%`) seguido por dos dígitos hexadecimales y los espacios son codificados como signos de suma (`+`). Esta es la misma codificación usada en los datos publicados desde un formulario WWW, es decir, el mismo mecanismo usado para el tipo de medios `application/x-www-form-urlencoded`. Este mecanismo difiere de la codificación en el [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986) (vea `rawurlencode`) en que, por razones históricas, los espacios son codificados como signos de suma (+).

## Ejemplos

Ejemplo de `urlencode`

```
<?php
$userinput = 'Data123!@-_ +';
echo "UserInput: $userinput\n";
echo '<a href="mycgi?foo=', urlencode($userinput), '">';
?>

    
```php

El ejemplo anterior mostrará:

```
UserInput: Data123!@-_ +
<a href="mycgi?foo=Data123%21%40-_+%2B">

    
```php

Ejemplo de `urlencode` y ejemplo de `htmlentities`

```
<?php
$foo = 'Data123!@-_ +';
$bar = "Not the same content as $foo";
echo "foo: $foo\n";
echo "bar: $bar\n";
$query_string = 'foo=' . urlencode($foo) . '&bar=' . urlencode($bar);
echo '<a href="mycgi?' . htmlentities($query_string) . '">';
?>

    
```php

El ejemplo anterior mostrará:

```
foo: Data123!@-_ +
bar: Not the same content as Data123!@-_ +
<a href="mycgi?foo=Data123%21%40-_+%2B&amp;bar=Not+the+same+content+as+Data123%21%40-_+%2B">

    
```php

## Notas

> [!NOTE]
> Tenga cuidado con las variables que puedan coincidir con entidades HTML. Secuencias como &amp, &copy y &pound son procesadas por el navegador y la entidad real es usada en lugar del nombre de variable deseado. Este es un problema obvio sobre el cual el consorcio W3 ha estado alertando a las personas por años. La referencia esta aquí: <http://www.w3.org/TR/html4/appendix/notes.html#h-B.2.2>.
>
> PHP soporta la modificación del separador de argumentos al punto-y-coma sugerido por el W3C a través de la directiva .ini arg_separator. Desafortunadamente, la mayoría de agentes de usuario no envían datos de formularios en este formato separado por punto-y-coma. Una forma más portable es usar \&amp; en lugar de & como separador. No es necesario modificar el valor arg_separator de PHP para esto. Déjelo como &, y simplemente codifique sus URLs usando `htmlentities` o `htmlspecialchars`.

## Véase también

`urldecode`, `htmlentities`, `rawurlencode`, `rawurldecode`, [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)
