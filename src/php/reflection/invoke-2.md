---
title: ReflectionMethod::invoke
description: Invoca
source_url: https://www.php.net/manual/es/reflectionmethod.invoke.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/invoke.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71000
---

ReflectionMethod::invoke

Invoca

## Descripción

```php
public ReflectionMethod::invoke(object $object, mixed ...$args): mixed
```php

Invoca un método reflejado.

## Parámetros

`object`  
El objeto sobre el cual invocar el método. Para los métodos estáticos, se debe pasar `null` como argumento.

`args`  
Argumentos a pasar al método. Esto acepta un número variable de argumentos que serán pasados al método.

## Valores devueltos

Retorna el resultado del método.

## Errores/Excepciones

Una `ReflectionException` si `object` no es una instancia de la clase de la cual el método fue declarado.

Una `ReflectionException` si la invocación del método falla.

## Ejemplos

Ejemplo con ReflectionMethod::invoke

```
<?php
class HelloWorld {

    public function sayHelloTo($name) {
        return 'Hello ' . $name;
    }

}

$reflectionMethod = new ReflectionMethod('HelloWorld', 'sayHelloTo');
echo $reflectionMethod->invoke(new HelloWorld(), 'Mike');
?>

    
```php

El ejemplo anterior mostrará:

    Hello Mike

## Notas

> [!NOTE]
> ReflectionMethod::invoke no puede ser utilizado cuando se esperan argumentos por referencia. ReflectionMethod::invokeArgs debe ser utilizado en su lugar (pasando las referencias en la lista de argumentos).

## Véase también

ReflectionMethod::invokeArgs, [\_\_invoke()](#object.invoke), `call_user_func`
