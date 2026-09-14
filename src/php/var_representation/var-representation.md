---
title: var_representation
description: Devuelve una representación legible, corta y analizable de una variable
source_url: https://www.php.net/manual/es/function.var-representation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var_representation/functions/var-representation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var_representation
translation_status: ready
translation_revision: 1f64cacbb
order: 100840
---

var_representation

Devuelve una representación legible, corta y analizable de una variable

## Descripción

```php
var_representation(mixed $value, [int $flags]): string
```php

`var_representation` (de la PECL var_representation) devuelve un string de caracteres con información estructurada sobre la variable dada. Es similar a `var_export` con diferencias en la indentación, escape de strings y las representaciones de array.

## Parámetros

`value`  
La variable para generar una representación.

`flags`  
Una máscara de bits que consiste en `VAR_REPRESENTATION_SINGLE_LINE`, `VAR_REPRESENTATION_UNESCAPED`. El comportamiento de estas constantes se describe en la página de las [constantes de var_representation](#var-representation.constants).

## Valores devueltos

Devuelve la representación de la variable.

## Ejemplos

Ejemplo de `var_representation`

```
<?php
$a = [1, 2, ['key' => 'value']];
echo var_representation($a), "\n";
echo var_representation($a, VAR_REPRESENTATION_SINGLE_LINE), "\n";
?>

    
```php

El ejemplo anterior mostrará:

    [
      1,
      2,
      [
        'key' => 'value',
      ],
    ]
    [1, 2, ['key' => 'value']]

Escapado de caracteres de control

```
<?php
echo var_representation("Content-Length: 123\r\n");
?>

    
```php

El ejemplo anterior mostrará:

    "Content-Length: 123\r\n"

Exportar una `stdClass`

```
<?php
$person = new stdClass;
$person->name = 'ElePHPant ElePHPantsdotter';
$person->website = 'https://php.net/elephpant.php';

echo var_representation($person);
?>

    
```php

El ejemplo anterior mostrará:

    (object) [
      'name' => 'ElePHPant ElePHPantsdotter',
      'website' => 'https://php.net/elephpant.php',
    ]

Exportar clases

```
<?php
class A { public $var; }
$a = new A;
$a->var = 5;
echo var_representation($a);
?>

    
```php

El ejemplo anterior mostrará:

    \A::__set_state([
      'var' => 5,
    ])

Uso con [\_\_set_state()](#object.set-state)

```
<?php
class A
{
    public $var1;
    public $var2;

    public static function __set_state($an_array)
    {
        $obj = new A;
        $obj->var1 = $an_array['var1'];
        $obj->var2 = $an_array['var2'];
        return $obj;
    }
}

$a = new A;
$a->var1 = 5;
$a->var2 = 'foo';

eval('$b = ' . var_representation($a) . ';'); // $b = \A::__set_state([
                                              //   'var1' => 5,
                                              //   'var2' => 'foo',
                                              // ]);
var_dump($b);
?>

    
```php

El ejemplo anterior mostrará:

    object(A)#2 (2) {
      ["var1"]=>
      int(5)
      ["var2"]=>
      string(3) "foo"
    }

## Véase también

`var_export`
