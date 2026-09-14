---
title: ReflectionFunction::invoke
description: Invoca una función
source_url: https://www.php.net/manual/es/reflectionfunction.invoke.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunction/invoke.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 70410
---

ReflectionFunction::invoke

Invoca una función

## Descripción

```php
public ReflectionFunction::invoke(mixed ...$args): mixed
```php

Invoca una función reflejada.

## Parámetros

`args`  
La lista de argumentos a pasar a la función. Es posible pasar un número variable de argumentos a la función, como para la función `call_user_func`.

## Valores devueltos

Retorna el resultado de la función invocada.

## Ejemplos

Ejemplo con ReflectionFunction::invoke

```
<?php
function title($title, $name)
{
   return sprintf("%s. %s\r\n", $title, $name);
}

$function = new ReflectionFunction('title');

echo $function->invoke('Dr', 'Phil');
?>

    
```php

El ejemplo anterior mostrará:

    Dr. Phil

## Notas

> [!NOTE]
> ReflectionFunction::invoke no puede ser utilizado cuando se esperan parámetros de referencia. ReflectionFunction::invokeArgs debe ser utilizado en su lugar (pasando las referencias en la lista de argumentos).

## Véase también

ReflectionFunction::export, [\_\_invoke()](#object.invoke), `call_user_func`
