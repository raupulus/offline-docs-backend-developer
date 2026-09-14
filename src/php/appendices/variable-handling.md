---
title: Modificaciones en el manejo de variables
source_url: https://www.php.net/manual/es/migration70.incompatible.variable-handling.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/incompatible/variable-handling.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 35511ebc5
order: 360
---

## Modificaciones en el manejo de variables

PHP 7 ahora utiliza un árbol de sintaxis abstracta al analizar los ficheros fuente. Esto ha permitido numerosas mejoras en el lenguaje que anteriormente eran imposibles debido a las limitaciones en el analizador utilizado en versiones anteriores de PHP, pero ha conllevado la eliminación de algunos casos especiales por razones de consistencia, lo que rompe la retrocompatibilidad. Estos casos se detallan en esta sección.

### Modificaciones en el manejo de variables, propiedades y métodos indirectos

El acceso indirecto a variables, propiedades y métodos ahora se evaluará estrictamente en orden de izquierda a derecha, en contraste con la combinación anterior de casos especiales. La siguiente tabla muestra cómo ha cambiado el orden de evaluación.

| Expresión             | Interpretación PHP 5    | Interpretación PHP 7    |
|-----------------------|-------------------------|-------------------------|
| `$$foo['bar']['baz']` | `${$foo['bar']['baz']}` | `($$foo)['bar']['baz']` |
| `$foo->$bar['baz']`   | `$foo->{$bar['baz']}`   | `($foo->$bar)['baz']`   |
| `$foo->$bar['baz']()` | `$foo->{$bar['baz']}()` | `($foo->$bar)['baz']()` |
| `Foo::$bar['baz']()`  | `Foo::{$bar['baz']}()`  | `(Foo::$bar)['baz']()`  |

Evaluación antigua y nueva de expresiones indirectas

El código que utilizaba el antiguo orden de evaluación de derecha a izquierda se debe reescribir para usar explícitamente este orden de evaluación con llaves (ver la columna del medio anterior). Esto hará que el código sea compatible con PHP 7.x y retrocompatible con PHP 5.x.

Esto también afecta a la palabra clave [`global`](#language.variables.scope.global). La sintaxis de llaves se puede utilizar para emular el comportamiento anterior si es necesario:

```php
<?php
function f() {
    // Válido solo en PHP 5.
    global $$foo->bar;

    // Válido en PHP 5 y 7.
    global ${$foo->bar};
}
?>

   
```

### Modificaciones en el manejo de `list`

#### La función `list` ya no asigna variables en orden inverso

`list` ahora asignará valores a las variables en el orden en que se definen, en lugar de en orden inverso. En general, esto solo afecta al caso en que `list` se usa en conjunción con el operador de array `[]`, como se ilustra a continuación:

```php
<?php
list($a[], $a[], $a[]) = [1, 2, 3];
var_dump($a);
?>

    
```

Resultado del ejemplo anterior en PHP 5:

    array(3) {
      [0]=>
      int(3)
      [1]=>
      int(2)
      [2]=>
      int(1)
    }

        

Resultado del ejemplo anterior en PHP 7:

    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }

En general, se recomienda no depender del orden en que ocurren las asignaciones de la función `list`, ya que es un detalle de implementación que puede cambiar nuevamente en el futuro.

#### Las asignaciones vacías de `list` se han eliminado

Las construcciones de `list` ya no pueden estar vacías. Los siguientes elementos ya no están permitidos:

```php
<?php
list() = $a;
list(,,) = $a;
list($x, list(), $y) = $a;
?>

    
```

#### `list` no puede desempaquetar `string`s

`list` ya no puede desempaquetar variables de `string`. Debe usarse `str_split` en su lugar.

### El orden de los elementos de los arrays ha cambiado cuando los elementos se crean automáticamente durante las asignaciones por referencia

El orden de los elementos en un array ha cambiado cuando estos elementos se crearon automáticamente al referenciarlos en una asignación por referencia. Por ejemplo:

```php
<?php
$array = [];
$array["a"] =& $array["b"];
$array["b"] = 1;
var_dump($array);
?>

   
```

Resultado del ejemplo anterior en PHP 5:

    array(2) {
      ["b"]=>
      &int(1)
      ["a"]=>
      &int(1)
    }

       

Resultado del ejemplo anterior en PHP 7:

    array(2) {
      ["a"]=>
      &int(1)
      ["b"]=>
      &int(1)
    }

### Los paréntesis alrededor de los argumentos de una función ya no afectan el comportamiento

En PHP 5, el uso de paréntesis redundantes alrededor de un argumento de una función podía silenciar las advertencias de estándares estrictos (strict standards) cuando el argumento de la función se pasaba por referencia. Ahora se emite siempre la advertencia.

```php
<?php
function getArray() {
    return [1, 2, 3];
}

function squareArray(array &$a) {
    foreach ($a as &$v) {
        $v **= 2;
    }
}

// Genera una advertencia en PHP 7.
squareArray((getArray()));
?>

   
```

El ejemplo anterior mostrará:

    Notice: Only variables should be passed by reference in /tmp/test.php on line 13
