---
title: ReflectionFunctionAbstract::getReturnType
description: Obtiene el tipo de retorno definido para una función
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.getreturntype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/getreturntype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70630
---

ReflectionFunctionAbstract::getReturnType

Obtiene el tipo de retorno definido para una función

## Descripción

```php
public ReflectionFunctionAbstract::getReturnType(): ReflectionType
```php

Obtiene el tipo de retorno definido para una función reflejada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto `ReflectionType` si un tipo de retorno está definido, `null` en caso contrario.

## Ejemplos

Ejemplo con ReflectionFunctionAbstract::getReturnType

```
<?php

function to_int($param) : int {
    return (int) $param;
}

$reflection1 = new ReflectionFunction('to_int');
echo $reflection1->getReturnType();

    
```php

El ejemplo anterior mostrará:

    int

Uso con funciones integradas

```
<?php

$reflection2 = new ReflectionFunction('array_merge');

var_dump($reflection2->getReturnType());

    
```php

El ejemplo anterior mostrará:

    null

Este es el caso, ya que muchas funciones internas no definen un tipo para sus argumentos o su valor de retorno. Por lo tanto, se recomienda evitar el uso de este método con funciones integradas.

## Véase también

ReflectionFunctionAbstract::hasReturnType, ReflectionType::\_\_toString
