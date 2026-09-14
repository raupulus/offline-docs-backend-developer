---
title: print
description: Muestra un string
source_url: https://www.php.net/manual/es/function.print.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/print.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 45042fef6
order: 88970
---

print

Muestra un string

## Descripción

```php
print(string $expression): int
```php

Muestra `expression`.

`print` no es una función sino una construcción del lenguaje. Su argumento es la expresión que sigue a la palabra clave `print`, y no está delimitado por paréntesis.

La diferencia principal con `echo` es que `print` solo acepta un argumento y siempre devuelve 1.

## Parámetros

`expression`  
La expresión a mostrar. Los valores que no son strings serán convertidos a string, incluso si la [directiva `strict_types`](#language.types.declarations.strict) está activada.

## Valores devueltos

Devuelve `1`, siempre.

## Ejemplos

Ejemplo con `print`

```
<?php
print "print no requiere paréntesis.";
print PHP_EOL;

// No se añade salto de línea ni espacio; lo siguiente se muestra como "helloworld" en una sola línea
print "hello";
print "world";
print PHP_EOL;

print "Este string abarca
múltiples líneas. Los saltos de línea también
se mostrarán";
print PHP_EOL;

print "Este string abarca\nmúltiples líneas. Los saltos de línea\nse mostrarán también.";
print PHP_EOL;

// El argumento puede ser cualquier expresión que produzca un string
$foo = "example";
print "foo es $foo"; // foo es example
print PHP_EOL;

$fruits = ["lemon", "orange", "banana"];
print implode(" y ", $fruits); // lemon y orange y banana
print PHP_EOL;

// Las expresiones no-string son convertidas a string, incluso si se usa declare(strict_types=1)
print 6 * 7; // 42
print PHP_EOL;

// Como print tiene un valor de retorno, puede ser usado en expresiones
// Lo siguiente muestra "hello world"
if ( print "hello" ) {
    echo " world";
}
print PHP_EOL;

// Lo siguiente muestra "true"
( 1 === 1 ) ? print 'true' : print 'false';
print PHP_EOL;
?>

    
```php

## Notas

> [!NOTE]
> Rodear el argumento de `print` con paréntesis no generará un error de sintaxis, y produce una sintaxis similar a una llamada normal de función. No obstante, esto puede ser engañoso, ya que los paréntesis forman en realidad parte de la expresión que se está mostrando, y no parte de la sintaxis de `print` en sí mismo.
>
> <div class="informalexample">
>
> ```
> <?php
> print "hello";
> // muestra "hello"
>
> print("hello");
> // también muestra "hello", porque ("hello") es una expresión válida
>
> print(1 + 2) * 3;
> // muestra "9"; los paréntesis hacen que 1+2 se evalúe primero, luego 3*3
> // la sentencia print ve toda la expresión como un argumento
>
> if ( print("hello") && false ) {
>     print " - dentro de if";
> }
> else {
>     print " - dentro de else";
> }
> // muestra " - dentro de if"
> // la expresión ("hello") && false se evalúa primero, dando false
> // esto se convierte al string vacío "" y se muestra
> // la construcción print luego devuelve 1, por lo que se ejecuta el código en el bloque if
> ?>
>
>      
> ```
>
> </div>
>
> Cuando `print` se usa en una expresión más grande, colocar tanto la palabra clave como su argumento entre paréntesis puede ser necesario para obtener el resultado esperado:
>
> <div class="informalexample">
>
> ```
> <?php
> if ( (print "hello") && false ) {
>     print " - dentro de if";
> }
> else {
>     print " - dentro de else";
> }
> // muestra "hello - dentro de else"
> // a diferencia del ejemplo anterior, la expresión (print "hello") se evalúa primero
> // después de mostrar "hello", print devuelve 1
> // como 1 && false es false, se ejecuta el código en el bloque else
>
> print "hello " && print "world";
> // muestra "world1"; print "world" se evalúa primero,
> // luego la expresión "hello " && 1 se pasa al print de la izquierda
>
> (print "hello ") && (print "world");
> // muestra "hello world"; los paréntesis fuerzan a que las expresiones print
> // se evalúen antes del &&
> ?>
>
>      
> ```
>
> </div>

> [!NOTE]
> Como esto es una estructura del lenguaje, y no una función, no es posible llamarla con las [funciones variables](#functions.variable-functions) o [argumentos nombrados](#functions.named-arguments).

## Véase también

`echo`, `printf`, `flush`, [Forma de especificar strings literales](#language.types.string)
