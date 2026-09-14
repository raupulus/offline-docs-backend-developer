---
title: ReflectionClass::getConstant
description: Obtiene una constante
source_url: https://www.php.net/manual/es/reflectionclass.getconstant.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getconstant.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: e5c8e7add
order: 69080
---

ReflectionClass::getConstant

Obtiene una constante

## Descripción

```php
public ReflectionClass::getConstant(string $name): mixed
```php

Obtiene una constante definida.

## Parámetros

`name`  
El nombre de la constante de clase a obtener.

## Valores devueltos

Valor de la constante con el nombre `name`. Devuelve `false` si la constante no ha sido encontrada en la clase.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | La llamada a ReflectionClass::getConstant para constantes que no existen ha quedado obsoleta. |

## Ejemplos

Uso de ReflectionClass::getConstant

```
<?php

class Example {
    const C1 = false;
    const C2 = 'I am a constant';
}

$reflection = new ReflectionClass('Example');

var_dump($reflection->getConstant('C1'));
var_dump($reflection->getConstant('C2'));
var_dump($reflection->getConstant('C3'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    string(15) "I am a constant"
    bool(false)

## Véase también

ReflectionClass::getConstants
