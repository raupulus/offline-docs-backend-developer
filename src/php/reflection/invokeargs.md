---
title: ReflectionFunction::invokeArgs
description: Invoca los argumentos de una función
source_url: https://www.php.net/manual/es/reflectionfunction.invokeargs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunction/invokeargs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 70420
---

ReflectionFunction::invokeArgs

Invoca los argumentos de una función

## Descripción

```php
public ReflectionFunction::invokeArgs(array $args): mixed
```php

Invoca la función y le transmite los argumentos en forma de array.

## Parámetros

`args`  
Los argumentos a utilizar durante la invocación, de manera similar al funcionamiento de `call_user_func_array`.

## Valores devueltos

Retorna el resultado de la función invocada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Las claves de `args` serán interpretadas como los nombres de los parámetros, en lugar de ser ignoradas silenciosamente. |

## Ejemplos

Ejemplo con ReflectionFunction::invokeArgs

```
<?php
function title($title, $name)
{
    return sprintf("%s. %s\r\n", $title, $name);
}

$function = new ReflectionFunction('title');

echo $function->invokeArgs(array('Dr', 'Phil'));
?>

    
```php

El ejemplo anterior mostrará:

    Dr. Phil

Ejemplo para ReflectionFunction::invokeArgs con referencias

```
<?php
function get_false_conditions(array $conditions, array &$false_conditions)
{
    foreach($conditions as $condition) {
       if(!$condition) {
          $false_conditions[] = $condition;
       }
    }
}

$function_ref = new ReflectionFunction('get_false_conditions');

$conditions       = array(true, false, -1, 0, 1);
$false_conditions = array();

$function_ref->invokeArgs(array($conditions, &$false_conditions));

var_dump($false_conditions);
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      [0]=>
      bool(false)
      [1]=>
      int(0)
    }

## Notas

> [!NOTE]
> Si la función tiene argumentos que necesitan ser referencias, entonces deben ser pasados por referencia en la lista de argumentos.

## Véase también

ReflectionFunction::invoke, ReflectionFunctionAbstract::getNumberOfParameters, [\_\_invoke()](#object.invoke), `call_user_func_array`
