---
title: ReflectionClass::getMethods
description: Obtiene un array de métodos
source_url: https://www.php.net/manual/es/reflectionclass.getmethods.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getmethods.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69210
---

ReflectionClass::getMethods

Obtiene un array de métodos

## Descripción

```php
public ReflectionClass::getMethods([int $filter]): array
```php

Obtiene un array de los métodos de una clase.

## Parámetros

`filter`  
Filtra los resultados para incluir únicamente los métodos con ciertos atributos. Por omisión, no se aplica ningún filtro.

Cualquier disyunción a nivel de bits de `ReflectionMethod::IS_STATIC`, `ReflectionMethod::IS_PUBLIC`, `ReflectionMethod::IS_PROTECTED`, `ReflectionMethod::IS_PRIVATE`, `ReflectionMethod::IS_ABSTRACT` y `ReflectionMethod::IS_FINAL`, de modo que se devuelven todos los métodos con *cualquiera* de los atributos proporcionados.

> [!NOTE]
> Tenga en cuenta que otras operaciones a nivel de bits, por ejemplo `~` no funcionarán como se espera. En otras palabras, no es posible obtener todos los métodos no estáticos, por ejemplo.

## Valores devueltos

Un `array` de objetos `ReflectionMethod` que reflejan cada método.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 7.2.0   | `filter` ahora es nullable. |

## Ejemplos

Uso simple de ReflectionClass::getMethods

```
<?php
class Apple {
    public function firstMethod() { }
    final protected function secondMethod() { }
    private static function thirdMethod() { }
}

$class = new ReflectionClass('Apple');
$methods = $class->getMethods();
var_dump($methods);
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      object(ReflectionMethod)#2 (2) {
        ["name"]=>
        string(11) "firstMethod"
        ["class"]=>
        string(5) "Apple"
      }
      [1]=>
      object(ReflectionMethod)#3 (2) {
        ["name"]=>
        string(12) "secondMethod"
        ["class"]=>
        string(5) "Apple"
      }
      [2]=>
      object(ReflectionMethod)#4 (2) {
        ["name"]=>
        string(11) "thirdMethod"
        ["class"]=>
        string(5) "Apple"
      }
    }

Filtro de resultados desde ReflectionClass::getMethods

```
<?php
class Apple {
    public function firstMethod() { }
    final protected function secondMethod() { }
    private static function thirdMethod() { }
}

$class = new ReflectionClass('Apple');
$methods = $class->getMethods(ReflectionMethod::IS_STATIC | ReflectionMethod::IS_FINAL);
var_dump($methods);
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      [0]=>
      object(ReflectionMethod)#2 (2) {
        ["name"]=>
        string(12) "secondMethod"
        ["class"]=>
        string(5) "Apple"
      }
      [1]=>
      object(ReflectionMethod)#3 (2) {
        ["name"]=>
        string(11) "thirdMethod"
        ["class"]=>
        string(5) "Apple"
      }
    }

## Véase también

ReflectionClass::getMethod, `get_class_methods`
