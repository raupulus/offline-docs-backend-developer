---
title: strval
description: Obtiene el valor de una variable en formato string
source_url: https://www.php.net/manual/es/function.strval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/strval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 3f1e479bf
order: 100760
---

strval

Obtiene el valor de una variable en formato string

## Descripción

```php
strval(mixed $value): string
```php

Obtiene el valor de la variable `value`, en formato string. Consulte la documentación sobre `string` para obtener más información sobre la conversión a string.

Esta función no realiza ningún formateo en el valor devuelto. Si se busca una forma de formatear un valor numérico como string, consulte la función `sprintf` o la función `number_format`.

## Parámetros

`value`  
La variable a convertir en `string`.

`value` puede ser un escalar, `null`, o un `object` que implemente el método mágico [\_\_toString()](#object.tostring). No se puede utilizar la función `strval` con arrays o objetos que no implementen el método mágico [\_\_toString()](#object.tostring).

## Valores devueltos

El valor `string` del argumento `value`.

## Ejemplos

Ejemplo para `strval` utilizando el método mágico PHP [\_\_toString()](#object.tostring).

```
<?php
class StrValTest
{
    public function __toString()
    {
        return __CLASS__;
    }
}

// Muestra 'StrValTest'
echo strval(new StrValTest);
?>

    
```php

## Véase también

`boolval`, `floatval`, `intval`, `settype`, `sprintf`, `number_format`, [La manipulación de tipos](#language.types.type-juggling), [\_\_toString()](#object.tostring)
