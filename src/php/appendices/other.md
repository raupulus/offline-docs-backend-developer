---
title: Otras modificaciones compatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration70.incompatible.other.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/incompatible/other.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 6a52dd81e
order: 320
---

## Otras modificaciones compatibles con versiones anteriores

### No se pueden asignar nuevos objetos por referencia

El resultado de la instrucción [`new`](#language.oop5.basic.new) ya no se puede asignar a una variable por referencia:

```php
<?php
class C {}
$c =& new C;
?>

   
```

Resultado del ejemplo anterior en PHP 5:

    Deprecated: Assigning the return value of new by reference is deprecated in /tmp/test.php on line 3

       

Resultado del ejemplo anterior en PHP 7:

    Parse error: syntax error, unexpected 'new' (T_NEW) in /tmp/test.php on line 3

### Nombres de clases, interfaces y traits no válidos

Los siguientes nombres no pueden utilizarse para nombrar clases, interfaces o traits:

- `bool`

- `int`

- `float`

- `string`

- null

- true

- false

Además, no deben utilizarse los siguientes nombres. Aunque no generan un error en PHP 7.0, están reservados para uso futuro y se deben considerar obsoletos.

- `resource`

- `object`

- `mixed`

- `numeric`

### Etiquetas ASP y PHP eliminadas

Se ha eliminado el soporte para el uso de etiquetas ASP y script para delimitar código PHP. Las etiquetas afectadas son:

| Etiqueta de apertura      | Etiqueta de cierre |
|---------------------------|--------------------|
| `<%`                      | `%>`               |
| `<%=`                     | `%>`               |
| `<script language="php">` | `</script>`        |

Eliminación de etiquetas ASP y script

### Llamadas desde un contexto incompatible eliminadas

[Anteriormente no recomendado en PHP 5.6](#migration56.deprecated.incompatible-context), Las llamadas estáticas a un método no estático con un contexto incompatible ahora resultarán en que el método llamado tendrá un indefinido `$this` y se emitirá una advertencia de obsolescencia.

```php
<?php
class A {
    public function test() { var_dump($this); }
}

// Nota: NO extiende A
class B {
    public function callNonStaticMethodOfA() { A::test(); }
}

(new B)->callNonStaticMethodOfA();
?>

   
```

Resultado del ejemplo anterior en PHP 5.6:

    Deprecated: Non-static method A::test() should not be called statically, assuming $this from incompatible context in /tmp/test.php on line 8
    object(B)#1 (0) {
    }

       

Resultado del ejemplo anterior en PHP 7:

    Deprecated: Non-static method A::test() should not be called statically in /tmp/test.php on line 8

    Notice: Undefined variable: this in /tmp/test.php on line 3
    NULL

### [`yield`](#control-structures.yield) es ahora un operador asociativo derecho

La construcción [`yield`](#control-structures.yield) ya no requiere paréntesis y ha sido sustituida por un operador asociativo derecho con prioridad entre `print` y `=>`. Esto puede provocar un cambio en el comportamiento:

```php
<?php
echo yield -1;
// Antes se interpretaba como
echo (yield) - 1;
// Y ahora se interpreta como
echo yield (-1);

yield $foo or die;
// Antes se interpretaba como
yield ($foo or die);
// Y ahora se interpreta como
(yield $foo) or die;
?>

   
```

Los paréntesis pueden utilizarse para eliminar la ambigüedad en estos casos.

### Las funciones no pueden tener varios parámetros con el mismo nombre

Ya no es posible definir dos o más parámetros de función con el mismo nombre. Por ejemplo, la siguiente función desencadenará un `E_COMPILE_ERROR`:

```php
<?php
function foo($a, $b, $unused, $unused) {
    //
}
?>

   
```

### Las funciones de inspección de argumentos informan del valor *actual* del parámetro

`func_get_arg`, `func_get_args`, `debug_backtrace` y las trazas de excepciones ya no devuelven el valor original que se pasó a un parámetro, sino que proporcionarán el valor actual (que podría haber sido modificado).

```php
<?php
function foo($x) {
    $x++;
    var_dump(func_get_arg(0));
}
foo(1);?>

   
```

Resultado del ejemplo anterior en PHP 5:

    1

       

Resultado del ejemplo anterior en PHP 7:

    2

### Las instrucciones de conmutación no pueden tener varios bloques por defecto

Ya no es posible definir dos o más bloques por defecto en una instrucción de conmutación. Por ejemplo, la siguiente instrucción switch desencadenará una `E_COMPILE_ERROR`:

```php
<?php
switch (1) {
    default:
    break;
    default:
    break;
}
?>

   
```

### `$HTTP_RAW_POST_DATA` ha sido eliminado

`$HTTP_RAW_POST_DATA` ya no está disponible. El flujo [`php://input`](#wrappers.php.input) debe ser utilizado en su lugar.

### Se han eliminado los comentarios `#` en los ficheros INI

Se ha eliminado el soporte para los comentarios con el prefijo `#` en los ficheros INI. En su lugar se debe utilizar `;` (punto y coma). Este cambio se aplica a los ficheros `php.ini`, así como a los ficheros gestionados por `parse_ini_file` y `parse_ini_string`.

### Extensión JSON reemplazada por JSOND

La extensión JSON se ha reemplazado por JSOND, lo que conlleva tres incompatibilidades menores de retrocompatibilidad. Primero, un número no debe terminar con una coma decimal (es decir, `34.` se debe cambiar a `34.0` o a `34`). Segundo, al usar la notación científica, el exponente `e` no debe seguir inmediatamente a un punto decimal (es decir, `3.e3` se debe cambiar a `3.0e3` o a `3e3`). Finalmente, una cadena vacía ya no se considera como JSON válido.

### Fallo de la función interna en caso de desbordamiento

Anteriormente, las funciones internas truncaban silenciosamente los números producidos a partir de coerciones de tipo float a integer cuando el número era demasiado grande para representarse como un integer. Ahora, se emitirá un E_WARNING y se devolverá `null`.

### Correcciones a los valores de retorno del manejador de sesión personalizado

Todas las funciones de predicado implementadas por manejadores de sesión personalizados que devuelvan `false` o `-1` serán errores fatales. Si se devuelve un valor de estas funciones distinto de un booleano, `-1` o `0`, fallará y se emitirá un E_WARNING.

### Orden de clasificación de elementos iguales

El algoritmo de clasificación interno ha sido mejorado, lo que puede resultar en un orden de clasificación diferente de los elementos que se comparaban como iguales anteriormente.

> [!NOTE]
> No dependa del orden de los elementos que se comparan como iguales; podría cambiar en cualquier momento.

### Instrucciones de interrupción y continuación mal ubicadas

Las instrucciones `break` y `continue` fuera de un bucle o una estructura de control `switch` ahora se detectan en el momento de la compilación en lugar de la ejecución como antes, y desencadenan un `E_COMPILE_ERROR`.

### Constante prohibida como argumento de break y continue

Las instrucciones `break` y `continue` ya no permiten que su argumento sea una constante, y desencadenan un `E_COMPILE_ERROR`.

### Mhash ya no es una extensión

La extensión mhash ha sido completamente integrada en la extensión [Hash](#book.hash). Por lo tanto, ya no es posible detectar el soporte mhash con `extension_loaded`; utilizar `function_exists` en su lugar. Además, mhash ya no se reporta por `get_loaded_extensions` y las funcionalidades relacionadas.

### declare(ticks)

La directiva [declare(ticks) ](#control-structures.declare.ticks) ya no se filtra en diferentes unidades de compilación.
