---
title: ReflectionParameter::getType
description: Obtiene el tipo del parámetro
source_url: https://www.php.net/manual/es/reflectionparameter.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71310
---

ReflectionParameter::getType

Obtiene el tipo del parámetro

## Descripción

```php
public ReflectionParameter::getType(): ReflectionType
```php

Obtiene el tipo asociado de un parámetro.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto `ReflectionType` si se especifica un tipo de parámetro, `null` en caso contrario.

## Ejemplos

Uso de ReflectionParameter::getType a partir de PHP 7.1.0

A partir de PHP 7.1.0, ReflectionType::\_\_toString está obsoleto, y ReflectionParameter::getType *puede* devolver una instancia de `ReflectionNamedType`. Para obtener el nombre del tipo de parámetro, ReflectionNamedType está disponible en este caso.

```
<?php
function someFunction(int $param, $param2) {}

$reflectionFunc = new ReflectionFunction('someFunction');
$reflectionParams = $reflectionFunc->getParameters();
$reflectionType1 = $reflectionParams[0]->getType();
$reflectionType2 = $reflectionParams[1]->getType();

assert($reflectionType1 instanceof ReflectionNamedType);
echo $reflectionType1->getName(), PHP_EOL;
var_dump($reflectionType2);
?>

    
```php

El ejemplo anterior mostrará:

    int
    NULL

Uso de ReflectionParameter::getType anterior a PHP 7.1.0

```
<?php
function someFunction(int $param, $param2) {}

$reflectionFunc = new ReflectionFunction('someFunction');
$reflectionParams = $reflectionFunc->getParameters();
$reflectionType1 = $reflectionParams[0]->getType();
$reflectionType2 = $reflectionParams[1]->getType();

echo $reflectionType1, PHP_EOL;
var_dump($reflectionType2);
?>

    
```php

Resultado del ejemplo anterior en PHP 7.0:

    int
    NULL

Uso de ReflectionParameter::getType en PHP 8.0.0 y posteriores

A partir de PHP 8.0.0, este método puede devolver una instancia de `ReflectionNamedType` o de `ReflectionUnionType`. Lo siguiente es una colección del primero. Para analizar un tipo, es a menudo práctico normalizarlo en un array de objetos `ReflectionNamedType`. La función siguiente devolverá un array de `0` o más instancias de `ReflectionNamedType`

```
<?php
function getAllTypes(ReflectionParameter $reflectionParameter): array
{
    $reflectionType = $reflectionParameter->getType();

    if (!$reflectionType) return [];

    return $reflectionType instanceof ReflectionUnionType
        ? $reflectionType->getTypes()
        : [$reflectionType];
}
?>

    
```php

## Véase también

ReflectionParameter::hasType, ReflectionType::\_\_toString
