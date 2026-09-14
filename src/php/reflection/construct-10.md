---
title: ReflectionFunction::__construct
description: Construye un nuevo objeto ReflectionFunction
source_url: https://www.php.net/manual/es/reflectionfunction.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunction/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 629dfc9ec
order: 70380
---

ReflectionFunction::\_\_construct

Construye un nuevo objeto ReflectionFunction

## Descripción

```php
public ReflectionFunction::__construct(Closure $function)
```php

Construye un nuevo objeto `ReflectionFunction`.

## Parámetros

`function`  
El nombre de la función a reflejar o una [fermeture](#functions.anonymous).

## Errores/Excepciones

Se lanza una excepción `ReflectionException` si el argumento `function` contiene una función inválida.

## Ejemplos

Ejemplo con ReflectionFunction::\_\_construct

```
<?php
/**
 * Un simple contador
 *
 * @return    int
 */
function counter1()
{
    static $c = 0;
    return ++$c;
}

/**
 * Otro simple contador
 *
 * @return    int
 */
$counter2 = function()
{
    static $d = 0;
    return ++$d;

};

function dumpReflectionFunction($func)
{
    // Muestra información básica
    printf(
        "\n\n===> La función '%s' '%s'\n".
        "     declarada en %s\n".
        "     líneas %d a %d\n",
        $func->isInternal() ? 'interna' : 'definida por el usuario',
        $func->getName(),
        $func->getFileName(),
        $func->getStartLine(),
        $func->getEndline()
    );

    // Muestra los comentarios de documentación
    printf("---> Documentación:\n %s\n", var_export($func->getDocComment(), true));

    // Muestra las variables estáticas existentes
    if ($statics = $func->getStaticVariables())
    {
        printf("---> Variables estáticas: %s\n", var_export($statics, true));
    }
}

// Crear una instancia de la clase ReflectionFunction
dumpReflectionFunction(new ReflectionFunction('counter1'));
dumpReflectionFunction(new ReflectionFunction($counter2));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    ===> La función definida por el usuario 'counter1'
         declarada en Z:\reflectcounter.php
         líneas 7 a 11
    ---> Documentación:
     '/**
     * A simple counter
     *
     * @return    int
     */'
    ---> Variables estáticas: array (
      'c' => 0,
    )

    ===> La función definida por el usuario '{closure}'
         declarada en Z:\reflectcounter.php
         líneas 18 a 23
    ---> Documentación:
     '/**
     * Another simple counter
     *
     * @return    int
     */'
    ---> Variables estáticas: array (
      'd' => 0,
    )

## Véase también

ReflectionMethod::\_\_construct, [Los constructores](#language.oop5.decon.constructor)
