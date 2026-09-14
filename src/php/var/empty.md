---
title: empty
description: Determina si una variable está vacía
source_url: https://www.php.net/manual/es/function.empty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/empty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: e6e9c1160
order: 100470
---

empty

Determina si una variable está vacía

## Descripción

```php
empty(mixed $var): bool
```php

Determina si una variable es considerada vacía. Una variable es considerada vacía si no existe, o si su valor equivale a `false`. La función `empty` no genera ninguna alerta si la variable no existe.

## Parámetros

`var`  
Variable a verificar.

Ninguna alerta es generada si la variable no existe. Esto significa que `empty` es estrictamente equivalente a `!isset($var) || $var == false`. Esto se aplica asimismo a las estructuras anidadas, tales como un array multidimensional o propiedades encadenadas.

## Valores devueltos

Retorna `true` si `var` no existe o tiene un valor vacío o igual a cero, es decir, que es considerada "false", ver [conversión en bool](#language.types.boolean.casting). De lo contrario retorna `false`.

## Ejemplos

Una comparación simple `empty` / `isset`.

```
<?php
$var = 0;

 // Evaluada como verdadera ya que $var está vacía
if (empty($var)) {
  echo '$var vale 0, está vacía, o no está definida en absoluto';
}

// Evaluada como verdadera ya que $var está definida
if (isset($var)) {
  echo '$var está definida incluso si está vacía';
}
?>

    
```php

`empty` sobre posiciones en un string

```
<?php
$expected_array_got_string = 'somestring';
var_dump(empty($expected_array_got_string['some_key']));
var_dump(empty($expected_array_got_string[0]));
var_dump(empty($expected_array_got_string['0']));
var_dump(empty($expected_array_got_string['0.5']));
var_dump(empty($expected_array_got_string['0 Mostel']));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(false)
    bool(true)
    bool(true)

`empty` sobre arrays multidimensionales

```
<?php
$multidimensional = [
    'some' => [
        'deep' => [
            'nested' => 'value'
        ]
    ]
];

if (!empty($multidimensional['some']['some']['nested'])) {
    $someVariable = $multidimensional['some']['deep']['nested'];
}

var_dump(empty($multidimensional['some-undefined-key']));
var_dump(empty($multidimensional['some']['deep']['unknown']));
var_dump(empty($multidimensional['some']['deep']['nested']));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(true)
    bool(false)

## Notas

> [!NOTE]
> Como esto es una estructura del lenguaje, y no una función, no es posible llamarla con las [funciones variables](#functions.variable-functions) o [argumentos nombrados](#functions.named-arguments).

> [!NOTE]
> Al utilizar esta función sobre propiedades de objeto inaccesibles, el método mágico [\_\_isset()](#object.isset) será llamado, si existe.

## Véase también

`isset`, [\_\_isset()](#object.isset), `unset`, `array_key_exists`, `count`, `strlen`, [Las tablas de comparación de tipos](#types.comparisons)
