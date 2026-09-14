---
title: declare
source_url: https://www.php.net/manual/es/control-structures.declare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/declare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 5499acf9d
order: 2110
---

## declare

El elemento de lenguaje `declare` se utiliza para añadir directivas de ejecución en un bloque de código. La sintaxis de `declare` es similar a la sintaxis de otras funciones de control:

    declare (directive)
        comandos

La expresión `directive` permite controlar la intervención del bloque `declare`. Actualmente, solo tres directivas son reconocidas: [`ticks`](#control-structures.declare.ticks), [`encoding`](#control-structures.declare.encoding), [`strict_types`](#language.types.declarations.strict)

Como las directivas son gestionadas durante la compilación del fichero, solo los literales pueden ser utilizados como valor de estas directivas. Las variables y constantes no pueden ser utilizadas. Para ilustrar:

```php
<?php
// Esto es correcto:
declare(ticks=1);

// Esto es incorrecto:
const TICK_VALUE = 1;
declare(ticks=TICK_VALUE);
?>

   
```

La expresión `comandos` del bloque de `declare` será ejecutada. Cómo será ejecutada, y qué efectos tendrá, depende de la directiva utilizada en el bloque `directive`.

La estructura `declare` puede también ser utilizada en el contexto global. Afecta entonces a todo el código que la sigue (incluso si el fichero con `declare` ha sido incluido después, no afecta al fichero padre).

```php
<?php
// Estas declaraciones son idénticas.

// Se puede utilizar esto
declare(ticks=1) {
    // script entero aquí
}

// o esto
declare(ticks=1);
// script entero aquí
?>

   
```

## Ticks

Un tick es un evento que interviene cada `N` comandos de bajo nivel tickables, ejecutados por el analizador en el bloque de `declare`. El valor de `N` es especificado por la sintaxis `ticks=N` en la sección `directive` del bloque `declare`.

No todos los comandos son tickables. Típicamente, las expresiones de condición y las expresiones de argumentos no son tickables.

Un evento que interviene en cada tick es especificado con la función `register_tick_function`. Consulte el ejemplo a continuación para más detalles. Tenga en cuenta que más de un evento puede intervenir por tick.

Ejemplo de uso de ticks

```php
<?php

declare(ticks=1);

// Una función llamada en cada evento tick
function tick_handler()
{
    echo "tick_handler() llamado\n";
}

register_tick_function('tick_handler'); // causa un evento tick

$a = 1; // causa un evento tick

if ($a > 0) {
    $a += 2; // causa un evento tick
    print $a; // causa un evento tick
}

?>

   
```

Ver también `register_tick_function` y `unregister_tick_function`.

## La codificación

La codificación de un script puede ser especificada por script utilizando la directiva `encoding`.

Declaración de una codificación para un script

```php
<?php
declare(encoding='ISO-8859-1');
// el código
?>

    
```

> [!CAUTION]
> Combinada con los espacios de nombres, la única sintaxis válida para declare es `declare(encoding='...');` donde `...` es el valor de la codificación. `declare(encoding='...') {}` generará un error de interpretación en el caso de los espacios de nombres.

Ver también [zend.script_encoding](#ini.zend.script-encoding).
