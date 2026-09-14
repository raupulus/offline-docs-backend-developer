---
title: ReflectionParameter::getDefaultValue
description: Obtiene el valor por defecto del argumento
source_url: https://www.php.net/manual/es/reflectionparameter.getdefaultvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/getdefaultvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 71270
---

ReflectionParameter::getDefaultValue

Obtiene el valor por defecto del argumento

## Descripción

```php
public ReflectionParameter::getDefaultValue(): mixed
```php

Obtiene el valor por defecto del argumento de una función o método definido en el espacio de nombres del usuario o interno. Si el argumento no es opcional, se emitirá una excepción `ReflectionException`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor por defecto del argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Este método permite ahora obtener el valor por defecto de funciones y métodos de clase integrados. Anteriormente, `ReflectionException` era emitido. |

## Ejemplos

Obtener los valores por defecto de los argumentos de la función

```
<?php
function foo($test, $bar = 'baz')
{
    echo $test . $bar;
}

$function = new ReflectionFunction('foo');

foreach ($function->getParameters() as $param) {
    echo 'Nombre : ' . $param->getName() . PHP_EOL;
    if ($param->isOptional()) {
        echo 'Valor por defecto : ' . $param->getDefaultValue() . PHP_EOL;
    }
    echo PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    Nombre : test

    Nombre : bar
    Valor por defecto : baz

## Véase también

ReflectionParameter::isOptional, ReflectionParameter::isDefaultValueAvailable, ReflectionParameter::getDefaultValueConstantName, ReflectionParameter::isPassedByReference
