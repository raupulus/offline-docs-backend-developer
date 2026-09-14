---
title: ReflectionClass::getReflectionConstants
description: Recupera las constantes de clase
source_url: https://www.php.net/manual/es/reflectionclass.getreflectionconstants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getreflectionconstants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69290
---

ReflectionClass::getReflectionConstants

Recupera las constantes de clase

## Descripción

```php
public ReflectionClass::getReflectionConstants([int $filter]): array
```php

Recupera las constantes reflejadas.

## Parámetros

`filter`  
El filtro opcional, para filtrar las constantes con la visibilidad deseada. Esto se configura utilizando las [constantes ReflectionClassConstant](#reflectionclassconstant.constants.modifiers), y por omisión recupera todas las constantes independientemente de la visibilidad.

## Valores devueltos

Un array de objetos `ReflectionClassConstant`.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.0.0   | `filter` ha sido añadido. |

## Ejemplos

Ejemplo básico de `ReflectionClass::getReflectionConstants`

```
<?php
class Foo {
    public    const FOO  = 1;
    protected const BAR  = 2;
    private   const BAZ  = 3;
}

$foo = new Foo();

$reflect = new ReflectionClass($foo);
$consts  = $reflect->getReflectionConstants();

foreach ($consts as $const) {
    print $const->getName() . "\n";
}

var_dump($consts);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    FOO
    BAR
    BAZ
    array(3) {
      [0]=>
      object(ReflectionClassConstant)#3 (2) {
        ["name"]=>
        string(3) "FOO"
        ["class"]=>
        string(3) "Foo"
      }
      [1]=>
      object(ReflectionClassConstant)#4 (2) {
        ["name"]=>
        string(3) "BAR"
        ["class"]=>
        string(3) "Foo"
      }
      [2]=>
      object(ReflectionClassConstant)#5 (2) {
        ["name"]=>
        string(3) "BAZ"
        ["class"]=>
        string(3) "Foo"
      }
    }

## Véase también

ReflectionClass::getReflectionConstant, `ReflectionClassConstant`
