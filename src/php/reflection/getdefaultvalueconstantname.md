---
title: ReflectionParameter::getDefaultValueConstantName
description: Devuelve el nombre de la constante del valor por defecto si el valor
  es una constante o null
source_url: https://www.php.net/manual/es/reflectionparameter.getdefaultvalueconstantname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/getdefaultvalueconstantname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 71280
---

ReflectionParameter::getDefaultValueConstantName

Devuelve el nombre de la constante del valor por defecto si el valor es una constante o null

## Descripción

```php
public ReflectionParameter::getDefaultValueConstantName(): string
```php

Devuelve el nombre de la constante que sirve como valor por defecto a un parámetro de una función o método definido por el usuario o interno, si el valor por defecto es constante o nulo. Si el parámetro no es opcional, se lanzará una excepción de tipo `ReflectionException`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` en caso de éxito, o `null` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Este método permite ahora recuperar el nombre de la constante del valor por defecto de funciones y métodos de clase integrados. Anteriormente, `ReflectionException` era emitido. |

## Ejemplos

Recuperar los nombres de las constantes que sirven como valores por defecto a los parámetros de una función

```
<?php
function foo($test, $bar = PHP_INT_MIN)
{
    echo $test . $bar;
}

$function = new ReflectionFunction('foo');

foreach ($function->getParameters() as $param) {
    echo 'Nombre : ' . $param->getName() . PHP_EOL;
    if ($param->isOptional()) {
        echo 'Valor por defecto : ' . $param->getDefaultValueConstantName() . PHP_EOL;
    }
    echo PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    Nombre : test

    Nombre : bar
    Valor por defecto : PHP_INT_MIN

## Véase también

ReflectionParameter::isOptional, ReflectionParameter::isDefaultValueConstant, ReflectionParameter::getDefaultValue
