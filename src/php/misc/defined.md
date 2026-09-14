---
title: defined
description: Verifica si una constante con el nombre dado existe
source_url: https://www.php.net/manual/es/function.defined.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/defined.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 36e1d917e
order: 47040
---

defined

Verifica si una constante con el nombre dado existe

## Descripción

```php
defined(string $constant_name): bool
```php

Verifica si una constante con el nombre `constant_name` existe.

Esta función también funciona con las [constantes de clase](#language.oop5.constants) y los [tipos enum](#language.types.enumerations).

> [!NOTE]
> Si se desea verificar si una variable existe, utilice `isset` ya que `defined` solo se aplica a las [constantes](#language.constants). Si se desea ver si una función existe, utilice `function_exists`.

## Parámetros

`constant_name`  
El nombre de la constante.

## Valores devueltos

Retorna `true` si el nombre de la constante proporcionado por el argumento `constant_name` ha sido definido, `false` en caso contrario.

## Ejemplos

Verificar la presencia de constantes con `defined`

```
<?php
/* Observe que el nombre de la constante está entre comillas. Este ejemplo verifica
 * si la cadena 'TEST' es el nombre de la constante llamada TEST */
if (defined('TEST')) {
    echo TEST;
}

interface bar {
    const test = 'foobar!';
}

class foo {
    const test = 'foobar!';
}

var_dump(defined('bar::test')); // bool(true)
var_dump(defined('foo::test')); // bool(true)

?>

    
```php

Verificación de tipos enum (a partir de PHP 8.1.0)

```
<?php

enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

var_dump(defined('Suit::Hearts')); // bool(true)
?>

    
```php

## Véase también

`define`, `constant`, `get_defined_constants`, `function_exists`, La sección sobre las [constantes](#language.constants)
