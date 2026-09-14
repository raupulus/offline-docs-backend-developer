---
title: var_export
description: Devuelve el código PHP utilizado para generar una variable
source_url: https://www.php.net/manual/es/function.var-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/var-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 100800
---

var_export

Devuelve el código PHP utilizado para generar una variable

## Descripción

```php
var_export(mixed $value, [bool $return]): string
```php

`var_export` devuelve datos estructurados sobre la variable dada. Es el mismo principio que `var_dump` pero con una excepción: el resultado devuelto es código PHP válido.

## Parámetros

`value`  
La variable que se desea exportar.

`return`  
Si se utiliza y se establece a `true`, `var_export` devolverá la representación de la variable en lugar de mostrarla.

## Valores devueltos

Devuelve la representación de la variable cuando el parámetro `return` se utiliza y se evalúa a `true`. De lo contrario, esta función devolverá `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Los nombres de clase exportados son ahora completamente calificados. Anteriormente, la barra invertida inicial era omitida. |
| 7.3.0 | Exporta ahora los objetos `stdClass` como un `array` convertido a un objeto (`(object) array( ... )`), en lugar de utilizar el método no existente stdClass::\_\_set_state. El efecto práctico es que ahora `stdClass` es exportable, y que el código resultante funcionará incluso en versiones anteriores de PHP. |

## Ejemplos

Ejemplo con `var_export`

```
<?php

$a = array (1, 2, array ("a", "b", "c"));
var_export($a);

?>

    
```php

El ejemplo anterior mostrará:

    array (
      0 => 1,
      1 => 2,
      2 =>
      array (
        0 => 'a',
        1 => 'b',
        2 => 'c',
      ),
    )

        

```
<?php

$b = 3.1;
$v = var_export($b, true);
echo $v; // 3.1

?>

    
```php

El ejemplo anterior mostrará:

    3.1

Exportar stdClass (a partir de PHP 7.3.0)

```
<?php
$person = new stdClass;
$person->name = 'ElePHPant ElePHPantsdotter';
$person->website = 'https://php.net/elephpant.php';

var_export($person);

    
```php

El ejemplo anterior mostrará:

    (object) array(
       'name' => 'ElePHPant ElePHPantsdotter',
       'website' => 'https://php.net/elephpant.php',
    )

Exportar clases

```
<?php
class A { public $var; }
$a = new A;
$a->var = 5;
var_export($a);
?>

    
```php

El ejemplo anterior mostrará:

    \A::__set_state(array(
       'var' => 5,
    ))

Uso de [\_\_set_state](#object.set-state)

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

eval('$b = ' . var_export($a, true) . ';'); // $b = A::__set_state(array(
                                     //    'var1' => 5,
                                     //    'var2' => 'foo',
                                     // ));
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

## Notas

> [!NOTE]
> Las variables de tipo `resource` no pueden ser exportadas por esta función.

> [!NOTE]
> `var_export` no maneja referencias circulares ya que sería imposible generar código PHP analizable para este tipo de datos. Si se desea hacer algo con la representación completa de un array o un objeto, se debe utilizar la función `serialize`.

> [!WARNING]
> Anterior a PHP 8.2.0, cuando `var_export` exportaba objetos, la barra invertida inicial no era incluida en el espacio de nombres de la clase y esto, para un máximo de compatibilidad.

> [!NOTE]
> Para poder evaluar el PHP generado por `var_export`, todos los objetos analizados deben implementar el método mágico [\_\_set_state](#object.set-state). La única excepción es `stdClass`; que es exportada utilizando un cast de un `array` a un objeto.

## Véase también

`print_r`, `serialize`, `var_dump`
