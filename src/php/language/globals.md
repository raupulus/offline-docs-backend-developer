---
title: $GLOBALS
description: Hace referencia a todas las variables disponibles en un contexto global
source_url: https://www.php.net/manual/es/reserved.variables.globals.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/globals.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: d58ee8eaa
order: 4170
---

\$GLOBALS

Hace referencia a todas las variables disponibles en un contexto global

## Descripción

Un `array` asociativo que contiene referencias a todas las variables globales actualmente definidas en el contexto de ejecución global del script. Los nombres de las variables son los índices del array.

## Ejemplos

Ejemplo con `$GLOBALS`

```php
<?php

function test()
{
    $foo = "variable local";

    echo '$foo en el contexto global : ' . $GLOBALS["foo"] . "\n";
    echo '$foo en el contexto actual : ' . $foo . "\n";
}

$foo = "Contenido de ejemplo";
test();

?>

    
```

Resultado del ejemplo anterior es similar a:

    $foo en el contexto global : Contenido de ejemplo
    $foo en el contexto actual : variable local

> [!WARNING]
> A partir de PHP 8.1.0, el acceso en escritura al array entero `$GLOBALS` ya no es soportado:
>
> <div id="variable.globals.entire_write_error" class="example">
>
> <div class="title">
>
> Escribir en el array entero `$GLOBALS` resultará en un error.
>
> </div>
>
> ```
> <?php
>
> // Genera un error durante la compilación:
> $GLOBALS = [];
> $GLOBALS += [];
> $GLOBALS =& $x;
> $x =& $GLOBALS;
> unset($GLOBALS);
> array_pop($GLOBALS);
> // ...y cualquier otra operación de escritura/lectura-escritura en $GLOBALS
>
> ?>
>
>      
> ```
>
> </div>

## Notas

> [!NOTE]
> Esto es una 'superglobal', o variable global automática. Esto significa simplemente que esta variable está disponible en todos los contextos del script. No es necesario hacer `global $variable;` para acceder a ella en las funciones o los métodos.

> [!NOTE]
> A diferencia de todas las demás [superglobales](#language.variables.superglobals), `$GLOBALS` siempre ha estado disponible en PHP.

> [!NOTE]
> A partir de PHP 8.1.0, `$GLOBALS` es ahora una copia de solo lectura del [array de símbolos](#features.gc.refcounting-basics) global. Es decir, las variables globales no pueden ser modificadas a través de su copia. Anteriormente, el array `$GLOBALS` estaba excluido del comportamiento habitual por valor de los arrays de PHP y las variables globales podían ser modificadas a través de su copia.
>
> <div class="informalexample">
>
> ```
> <?php
>
> // Antes de PHP 8.1.0
> $a = 1;
>
> $globals = $GLOBALS; // Copia ostensiblemente por valor
> $globals['a'] = 2;
> var_dump($a); // int(2)
>
> // A partir de PHP 8.1.0
> // esto ya no modifica $a. El comportamiento anterior violaba la semántica por valor.
> $globals = $GLOBALS;
> $globals['a'] = 1;
>
> // Para restaurar el comportamiento anterior, iterar su copia y asignar cada propiedad de vuelta a $GLOBALS.
> foreach ($globals as $key => $value) {
>     $GLOBALS[$key] = $value;
> }
>
> ?>
>
>      
> ```
>
> </div>
