---
title: echo
description: Muestra una string
source_url: https://www.php.net/manual/es/function.echo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/echo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 45042fef6
order: 88710
---

echo

Muestra una string

## Descripción

```php
echo(string ...$expressions): void
```php

Muestra una o varias expresiones, sin espacios o nueva línea adicionales.

`echo` no es una función sino una construcción del lenguaje. Sus argumentos son una lista de expresiones que siguen la palabra clave `echo`, separados por comas, y no delimitados por paréntesis. A diferencia de otras construcciones del lenguaje, `echo` no tiene valor de retorno, por lo que no puede ser utilizada en el contexto de una expresión.

`echo` también dispone de una sintaxis corta, donde se puede hacer seguir inmediatamente la etiqueta PHP de apertura con un signo igual (`=`). Esta sintaxis está disponible incluso si la directiva de configuración [`short_open_tag`](#ini.short-open-tag) está desactivada.

```
Tengo <?=$foo?> foo.

    
```php

La mayor diferencia con `print` es que `echo` acepta múltiples argumentos y no retorna ningún valor.

## Parámetros

`expressions`  
Una o varias expresiones de string a mostrar, separadas por comas. Los valores que no son strings serán convertidos a strings, incluso si la directiva [`strict_types`](#language.types.declarations.strict) está activada.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `echo`

```
<?php
echo "echo no requiere paréntesis.";

// Las strings pueden ser pasadas individualmente como múltiples argumentos o
// concatenadas y pasadas como un solo argumento
echo 'Esta ', 'string ', 'fue ', 'creada ', 'con múltiples parámetros.', "\n";
echo 'Esta ' . 'string ' . 'fue ' . 'creada ' . 'con concatenación.' . "\n";

// Ninguna nueva línea o espacio es añadido; lo siguiente muestra "helloworld", todo en una línea
echo "hola";
echo "mundo";

// Igual que lo anterior
echo "hola", "mundo";

echo "Esta string abarca
múltiples líneas. Los saltos de línea serán
mostrados también";

echo "Esta string abarca\nmúltiples líneas. Los saltos de línea serán\nmostrados también.";

// El argumento puede ser cualquier expresión que produzca una string
$foo = "ejemplo";
echo "foo es $foo"; // foo es ejemplo

$frutas = ["limón", "naranja", "plátano"];
echo implode(" y ", $frutas); // limón y naranja y plátano

// Las expresiones que no son strings son convertidas a strings, incluso si declare(strict_types=1) es utilizado
echo 6 * 7; // 42

// Sin embargo, los siguientes ejemplos funcionarán:
($some_var) ? print 'true' : print 'false'; // print también es una construcción, pero
                                            // es una expresión válida, retornando 1.
                                            // Por lo tanto puede ser utilizada en este contexto.

echo $some_var ? 'true': 'false'; // evaluando la expresión primero y luego pasándola a echo

    
```php

`echo` no es una expresión

```
<?php
// Debido a que echo no se comporta como una expresión, el siguiente código es inválido.
($some_var) ? echo 'true' : echo 'false';
?>

    
```php

## Notas

> [!NOTE]
> Como esto es una estructura del lenguaje, y no una función, no es posible llamarla con las [funciones variables](#functions.variable-functions) o [argumentos nombrados](#functions.named-arguments).

> [!NOTE]
> Rodear un solo argumento de `echo` con paréntesis no generará un error de sintaxis, y produce una sintaxis similar a una llamada normal de función. Sin embargo, esto puede ser engañoso, ya que los paréntesis son en realidad parte de la expresión que se está mostrando, y no parte de la sintaxis de `echo` en sí mismo.
>
> <div class="example">
>
> <div class="title">
>
> Uso de paréntesis
>
> </div>
>
> ```
>       
> <?php
> echo "hola", PHP_EOL;
> // muestra "hola"
>
> echo("hola"), PHP_EOL;
> // también muestra "hola", ya que ("hola") es una expresión válida
>
> echo(1 + 2) * 3, PHP_EOL;
> // muestra "9"; el paréntesis permite que 1+2 sea evaluado primero, luego 3*3
> // echo ve el resultado de la expresión como un solo argumento
>
> echo "hola", " mundo", PHP_EOL;
> // muestra "hola mundo"
>
> echo("hola"), (" mundo"), PHP_EOL;
> // muestra "hola mundo"; los paréntesis son parte de cada expresión
> ?>
>
>     
> ```
>
> </div>
>
> <div class="example">
>
> <div class="title">
>
> Expresión inválida
>
> </div>
>
> ```
>      
> <?php
> echo("hola", " mundo"), PHP_EOL;
> // Genera un error de análisis ya que ("hola", " mundo") no es una expresión válida
> ?>
>
>      
> ```
>
> </div>

> [!TIP]
> Pasar múltiples argumentos a `echo` permite evitar complicaciones que aparecen debido a la precedencia de la operación de concatenación en PHP. Por ejemplo, el operador de concatenación tiene una precedencia mayor que el operador ternario, y anteriormente a PHP 8.0.0, tenía la misma precedencia que la suma y la resta:
>
> ```
> <?php
> // A continuación, la expresión 'Hola ' . isset($name) es evaluada primero,
> // y siempre es verdadera, por lo que el argumento para echo siempre es $name
> echo 'Hola ' . isset($name) ? $name : 'John Doe' . '!';
>
> // El comportamiento deseado requiere paréntesis adicionales
> echo 'Hola ' . (isset($name) ? $name : 'John Doe') . '!';
>
> // En PHP anterior a 8.0.0, lo siguiente muestra "2", en lugar de "Suma: 3"
> echo 'Suma: ' . 1 + 2;
>
> // Nuevamente, añadir paréntesis asegura el orden de evaluación deseado
> echo 'Suma: ' . (1 + 2);
>
>    
> ```
>
> Si se proporcionan múltiples argumentos, entonces los paréntesis no serán necesarios para aumentar la precedencia, ya que cada expresión está separada:
>
> ```
> <?php
> echo "Hola ", isset($name) ? $name : "John Doe", "!";
>
> echo "Suma: ", 1 + 2;
>
>    
> ```

## Véase también

`print`, `printf`, `flush`, [Forma de especificar strings literales](#language.types.string)
