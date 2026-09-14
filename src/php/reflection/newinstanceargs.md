---
title: ReflectionClass::newInstanceArgs
description: Crear una nueva instancia utilizando los argumentos proporcionados
source_url: https://www.php.net/manual/es/reflectionclass.newinstanceargs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/newinstanceargs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69610
---

ReflectionClass::newInstanceArgs

Crear una nueva instancia utilizando los argumentos proporcionados

## Descripción

```php
public ReflectionClass::newInstanceArgs([array $args]): object
```php

Crear una nueva instancia de la clase utilizando los argumentos proporcionados para pasarlos al constructor.

## Parámetros

`args`  
Acepta un número variable de argumentos pasados al constructor, como en la función `call_user_func`.

## Valores devueltos

Devuelve una nueva instancia de la clase, o `null` en caso de error.

## Errores/Excepciones

Una `ReflectionException` si el constructor no es público.

Una `ReflectionException` si la clase no tiene constructor y el parámetro `args` contiene al menos un dato.

## Ejemplos

Uso básico de ReflectionClass::newInstanceArgs

```
<?php
$class = new ReflectionClass('ReflectionFunction');
$instance = $class->newInstanceArgs(array('substr'));
var_dump($instance);
?>

    
```php

El ejemplo anterior mostrará:

    object(ReflectionFunction)#2 (1) {
      ["name"]=>
      string(6) "substr"
    }

## Véase también

ReflectionClass::newInstance, ReflectionClass::newInstanceWithoutConstructor
