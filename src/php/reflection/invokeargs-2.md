---
title: ReflectionMethod::invokeArgs
description: Invoca los argumentos
source_url: https://www.php.net/manual/es/reflectionmethod.invokeargs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/invokeargs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71010
---

ReflectionMethod::invokeArgs

Invoca los argumentos

## Descripción

```php
public ReflectionMethod::invokeArgs(object $object, array $args): mixed
```php

Invoca el método reflejado y le pasa los argumentos en forma de array.

## Parámetros

`object`  
El objeto sobre el cual invocar el método. Si el método es estático, puede pasarse `null` para este argumento.

`args`  
Los argumentos a pasar al método, en forma de array.

## Valores devueltos

Devuelve el resultado del método.

## Errores/Excepciones

Una `ReflectionException` si `object` no es una instancia de la clase prevista para este método.

Una `ReflectionException` si la invocación del método falla.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Las claves de `args` serán interpretadas como los nombres de los argumentos, en lugar de ser ignoradas silenciosamente. |

## Ejemplos

Ejemplo para ReflectionMethod::invokeArgs

```
<?php
class HelloWorld {

    public function sayHelloTo($name) {
        return 'Hello ' . $name;
    }

}

$reflectionMethod = new ReflectionMethod('HelloWorld', 'sayHelloTo');
echo $reflectionMethod->invokeArgs(new HelloWorld(), array('Mike'));
?>

    
```php

El ejemplo anterior mostrará:

    Hello Mike

## Notas

> [!NOTE]
> Si la función tiene argumentos que necesitan ser referencias, entonces deben ser pasados por referencia en la lista de argumentos.

## Véase también

ReflectionMethod::invoke, [\_\_invoke()](#object.invoke), `call_user_func_array`
