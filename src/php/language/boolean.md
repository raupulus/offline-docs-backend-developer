---
title: Booleano
source_url: https://www.php.net/manual/es/language.types.boolean.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/boolean.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: ee66d210f
order: 4390
---

## Booleano

El tipo `bool` solo posee dos valores y se utiliza para expresar un valor de verdad. Puede ser `true` o `false`.

## Sintaxis

Para especificar un `bool` literal, utilice la constante `true` o `false`. Ambas son insensibles a mayúsculas y minúsculas.

```php
<?php

$foo = true; // asigna el valor TRUE a $foo

var_dump($foo); // bool(true)
?>

   
```

Típicamente, el resultado de un [operador](#language.operators) que devuelve un `bool`, pasado luego a una [estructura de control](#language.control-structures).

```php
<?php

$action = "show_version";
$show_separators = true;

// == es un operador que prueba
// la igualdad y devuelve un booleano
if ($action == "show_version") {
    echo "La versión es 1.23";
}

// esto no es necesario...
if ($show_separators == TRUE) {
    echo "<hr>\n";
}

// ...en su lugar, se puede utilizar, con el mismo significado:
if ($show_separators) {
    echo "<hr>\n";
}
?>

   
```

## Conversión en booleano

Para convertir explícitamente un valor en `bool`, utilice el cast `(bool)`. Generalmente, esto no es necesario porque cuando un valor se utiliza en un contexto lógico, se interpretará automáticamente como un valor de tipo `bool`. Para más información, ver la página [Type Juggling](#language.types.type-juggling).

Al convertir en `bool`, los siguientes valores son considerados como `false`:

- el [booleano](#language.types.boolean) `false`, en sí mismo

- el [entero](#language.types.integer) `0` (cero)

- los [números de punto flotante](#language.types.float) `0.0` y `-0.0` (cero)

- la [cadena](#language.types.string) vacía `""`, y la [cadena](#language.types.string) `"0"`

- un [array](#language.types.array) sin elementos

- el tipo unidad [NULL](#language.types.null) (incluyendo variables no definidas)

- los objetos internos que sobrecargan su comportamiento de casting en booleano. Por ejemplo, los objetos `GMP` que representan el valor `0`.

Todos los demás valores son considerados como `true` (incluyendo los [recursos](#language.types.resource) y `NAN`).

> [!WARNING]
> `-1` es considerado como `true`, como todos los números diferentes de cero (negativos o positivos) !

Conversión en booleano

```php
<?php
var_dump((bool) "");        // bool(false)
var_dump((bool) "0");       // bool(false)
var_dump((bool) 1);         // bool(true)
var_dump((bool) -2);        // bool(true)
var_dump((bool) "foo");     // bool(true)
var_dump((bool) 2.3e5);     // bool(true)
var_dump((bool) array(12)); // bool(true)
var_dump((bool) array());   // bool(false)
var_dump((bool) "false");   // bool(true)
?>

   
```
