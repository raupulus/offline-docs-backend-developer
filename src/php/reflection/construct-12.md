---
title: ReflectionMethod::__construct
description: Construye un nuevo objeto ReflectionMethod
source_url: https://www.php.net/manual/es/reflectionmethod.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 70920
---

ReflectionMethod::\_\_construct

Construye un nuevo objeto ReflectionMethod

## Descripción

```php
public ReflectionMethod::__construct(object $objectOrMethod, string $method)
```php

Firma alternativa (no soportada con argumentos nombrados):

```php
public ReflectionMethod::__construct(string $classMethod)
```

> [!WARNING]
> La firma alternativa está obsoleta a partir de PHP 8.4.0, utilice ReflectionMethod::createFromMethodName en su lugar.

Construye un nuevo objeto `ReflectionMethod`.

## Parámetros

`objectOrMethod`  
Nombre de clase -o instancia de esta- que contiene el método.

`method`  
Nombre del método.

`classMethod`  
Nombre de clase y de método delimitados por `::`.

## Errores/Excepciones

Se emite una `ReflectionException` si el método considerado no existe.

## Ejemplos

Ejemplo con ReflectionMethod::\_\_construct

```php
<?php
class Counter
{
    private static $c = 0;

    /**
     * Contador que se incrementa
     *
     * @final
     * @static
     * @access  public
     * @return  int
     */
    final public static function increment()
    {
        return ++self::$c;
    }
}

// Crea una nueva instancia de la clase ReflectionMethod
$method = new ReflectionMethod('Counter', 'increment');

// Muestra información
printf(
    "===> The %s%s%s%s%s%s%s method '%s' (which is %s)\n" .
    "     declared in %s\n" .
    "     lines %d to %d\n" .
    "     having the modifiers %d[%s]\n",
        $method->isInternal() ? 'internal' : 'user-defined',
        $method->isAbstract() ? ' abstract' : '',
        $method->isFinal() ? ' final' : '',
        $method->isPublic() ? ' public' : '',
        $method->isPrivate() ? ' private' : '',
        $method->isProtected() ? ' protected' : '',
        $method->isStatic() ? ' static' : '',
        $method->getName(),
        $method->isConstructor() ? 'the constructor' : 'a regular method',
        $method->getFileName(),
        $method->getStartLine(),
        $method->getEndline(),
        $method->getModifiers(),
        implode(' ', Reflection::getModifierNames($method->getModifiers()))
);

// Muestra el comentario de documentación
printf("---> Documentation:\n %s\n", var_export($method->getDocComment(), true));

// Muestra las variables estáticas, si existen
if ($statics= $method->getStaticVariables()) {
    printf("---> Static variables: %s\n", var_export($statics, true));
}

// Invoca el método
printf("---> Invocation results in: ");
var_dump($method->invoke(NULL));
?>

    
```

Resultado del ejemplo anterior es similar a:

    ===> The user-defined final public static method 'increment' (which is a regular method)
         declared in /Users/philip/cvs/phpdoc/test.php
         lines 14 to 17
         having the modifiers 261[final public static]
    ---> Documentation:
     '/**
         * Contador que se incrementa
         *
         * @final
         * @static
         * @access  public
         * @return  int
         */'
    ---> Invocation results in: int(1)

## Véase también

ReflectionMethod::export, [Los constructores](#language.oop5.decon.constructor)
