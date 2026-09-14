---
title: Cadenas
source_url: https://www.php.net/manual/es/language.types.string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: ddc2a2d09
order: 4540
---

## Cadenas

Un `string` es una serie de caracteres, donde un caracter es lo mismo que un octeto. Esto significa que PHP solo admite un conjunto de 256 caracteres, y por lo tanto no ofrece soporte nativo para Unicode. Ver [los detalles del tipo string](#language.types.string.details).

> [!NOTE]
> En las versiones de 32 bits, un `string` puede ser tan grande como 2 Go (2147483647 octetos maximo)

## Sintaxis

Un `string` literal puede especificarse de cuatro maneras diferentes:

- [entre comillas simples](#language.types.string.syntax.single)

- [entre comillas dobles](#language.types.string.syntax.double)

- [sintaxis heredoc](#language.types.string.syntax.heredoc)

- [sintaxis nowdoc](#language.types.string.syntax.nowdoc)

### Entre comillas simples

La manera más simple de especificar un `string` es encerrarlo entre comillas simples (el caracter `'`).

Para especificar una comilla simple literal, escápela con un backslash (`\`). Para especificar un backslash literal, duplíquelo (`\\`). Todas las demás ocurrencias del backslash serán tratadas como un backslash literal: esto significa que otras secuencias de escape que usted podría conocer, tales como `\r` o `\n`, serán salidas literalmente como se especifica en lugar de tener un significado especial.

> [!NOTE]
> A diferencia de las [comillas dobles](#language.types.string.syntax.double) y [sintaxis heredoc](#language.types.string.syntax.heredoc), las [variables](#language.variables) y las secuencias de escape para caracteres especiales *no* serán extendidas cuando se encuentren en `strings` entre comillas simples.

Variantes de sintaxis

```php
<?php
echo 'esto es un string simple', PHP_EOL;

echo 'Usted puede también tener nuevas líneas integradas
en los strings de esta manera, ya que
es aceptable hacerlo.', PHP_EOL;

// Muestra: Arnold dijo una vez: "Volveré"
echo 'Arnold dijo una vez: "Volveré"', PHP_EOL;

// Muestra: ¿Usted ha borrado C:\*.*?
echo '¿Usted ha borrado C:\\*.* ?', PHP_EOL;

// Muestra: ¿Usted ha borrado C:\*.*?
echo '¿Usted ha borrado C:\*.* ?', PHP_EOL;

// Muestra: Esto no se extenderá: \n una nueva línea
echo 'Esto no se\'extenderá: \n una nueva línea', PHP_EOL;

// Muestra: Las variables no $se\'extienden $tampoco
echo 'Las variables no $se\'extienden $tampoco', PHP_EOL;
?>

    
```

### Entre comillas dobles

Si el `string` está encerrado entre comillas dobles (`"`), PHP interpretará las siguientes secuencias de escape para caracteres especiales:

| Secuencia | Significado |
|----|----|
| `\n` | retorno de carro (LF o 0x0A (10) en ASCII) |
| `\r` | retorno de carro (CR o 0x0D (13) en ASCII) |
| `\t` | tabulación horizontal (HT o 0x09 (9) en ASCII) |
| `\v` | tabulación vertical (VT o 0x0B (11) en ASCII) |
| `\e` | escape (ESC o 0x1B (27) en ASCII) |
| `\f` | avance de formulario (FF o 0x0C (12) en ASCII) |
| `\\` | backslash |
| `\$` | signo de dólar |
| `\"` | comilla doble |
| `\[0-7]{1,3}` | Octal: la secuencia de caracteres correspondiente a la expresión regular `[0-7]{1,3}` es un caracter en notación octal (por ejemplo, `"\101" === "A"`), que desborda silenciosamente para adaptarse a un octeto (por ejemplo, `"\400" === "\000"`) |
| `\x[0-9A-Fa-f]{1,2}` | Hexadecimal: la secuencia de caracteres correspondiente a la expresión regular `[0-9A-Fa-f]{1,2}` es un caracter en notación hexadecimal (por ejemplo, `"\x41" === "A"`) |
| `\u{[0-9A-Fa-f]+}` | Unicode: la secuencia de caracteres correspondiente a la expresión regular `[0-9A-Fa-f]+` es un punto de código Unicode, que será salido en el string bajo la representación UTF-8 de este punto de código. Las llaves son requeridas en la secuencia. Por ejemplo, `"\u{41}" === "A"` |

Caracteres escapados

Como para los `strings` entre comillas simples, escapar cualquier otro caracter también resultará en la impresión del backslash.

La característica más importante de los `strings` entre comillas dobles es el hecho de que los nombres de variables serán extendidos. Ver [la interpolación de strings](#language.types.string.parsing) para más detalles.

### Heredoc

Una tercera manera de delimitar los `strings` es la sintaxis heredoc: `<<<`. Después de este operador, se proporciona un identificador, luego una nueva línea. El `string` mismo sigue, luego el mismo identificador nuevamente para cerrar la cita.

El identificador de cierre puede estar indentado con espacios o tabulaciones, en cuyo caso la indentación será eliminada de todas las líneas en el string doc. Antes de PHP 7.3.0, el identificador de cierre *debe* comenzar en la primera columna de la línea.

Además, el identificador de cierre debe seguir las mismas reglas de nombramiento que cualquier otro etiqueta en PHP: debe contener solo caracteres alfanuméricos y guiones bajos, y debe comenzar con un carácter no numérico o un guión bajo.

Ejemplo básico de Heredoc a partir de PHP 7.3.0

```php
<?php
// sin indentación
echo <<<END
      a
     b
    c
\n
END;

// 4 espacios de indentación
echo <<<END
      a
     b
    c
    END;

    
```

Resultado del ejemplo anterior en PHP 7.3:

          a
         b
        c

      a
     b
    c

Si el identificador de cierre está indentado más que cualquier línea del cuerpo, entonces se levantará un `ParseError`:

El identificador de cierre no debe estar indentado más que cualquier línea del cuerpo

```php
<?php
echo <<<END
  a
 b
c
   END;

    
```

Resultado del ejemplo anterior en PHP 7.3:

    Parse error: Invalid body indentation level (expecting an indentation level of at least 3) in example.php on line 4

Si el identificador de cierre está indentado, las tabulaciones también pueden ser utilizadas, sin embargo, las tabulaciones y los espacios *no deben* mezclarse en cuanto a la indentación del identificador de cierre y la indentación del cuerpo (hasta el identificador de cierre). En cualquiera de estos casos, se levantará un `ParseError`. Estas restricciones de espacio han sido incluidas porque mezclar espacios y tabulaciones para la indentación perjudica la legibilidad.

Indentación diferente para el cuerpo (espacios) identificador de cierre

```php
<?php
// Todo el código siguiente no funciona.

// indentación diferente para el cuerpo (espacios) marcador de fin (tabulaciones)
{
    echo <<<END
        a
        END;
}

// mezcla de espacios y tabulaciones en el cuerpo
{
    echo <<<END
            a
        END;
}

// mezcla de espacios y tabulaciones en el marcador de fin
{
    echo <<<END
            a
        END;
}

    
```

Resultado del ejemplo anterior en PHP 7.3:

    Parse error: Invalid indentation - tabs and spaces cannot be mixed in example.php line 8

El identificador de cierre para el string del cuerpo no es requerido para ser seguido de un punto y coma o un salto de línea. Por ejemplo, el siguiente código es permitido a partir de PHP 7.3.0:

Continuación de una expresión después de un identificador de cierre

```php
<?php
$values = [<<<END
a
  b
    c
END, 'd e f'];
var_dump($values);

    
```

Resultado del ejemplo anterior en PHP 7.3:

    array(2) {
      [0] =>
      string(11) "a
      b
        c"
      [1] =>
      string(5) "d e f"
    }

> [!WARNING]
> Si el identificador de cierre ha sido encontrado al principio de una línea, entonces no importa si formaba parte de otra palabra, puede ser considerado como el identificador de cierre y provocar un `ParseError`.
>
> <div class="example">
>
> <div class="title">
>
> El identificador de cierre en el cuerpo del string tiende a provocar un ParseError
>
> </div>
>
> ```
> <?php
> $values = [<<<END
> a
> b
> END ING
> END, 'd e f'];
>
>      
> ```
>
> Resultado del ejemplo anterior en PHP 7.3:
>
>     Parse error: syntax error, unexpected identifier "ING", expecting "]" in example.php on line 5
>
>          
>
> </div>
>
> Para evitar este problema, es seguro seguir la regla simple: *no elegir una palabra que aparezca en el cuerpo del texto como identificador de cierre*.

> [!WARNING]
> Antes de PHP 7.3.0, es muy importante señalar que la línea que contiene el identificador de cierre no debe contener ningún otro carácter, excepto un punto y coma (`;`). Esto significa principalmente que el identificador *no puede estar indentado*, y no debe haber espacios o tabulaciones antes o después del punto y coma. También es importante darse cuenta de que el primer carácter antes del identificador de cierre debe ser un salto de línea tal como se define en el sistema operativo local. Es `\n` en los sistemas UNIX, incluyendo macOS. El delimitador de cierre también debe ser seguido de un salto de línea.
>
> Si esta regla se viola y el identificador de cierre no está "limpio", no será considerado como un identificador de cierre, y PHP continuará buscando uno. Si un identificador de cierre adecuado no se encuentra antes del final del archivo actual, se producirá un error de análisis en la última línea.
>
> <div class="example">
>
> <div class="title">
>
> Ejemplo inválido, antes de PHP 7.3.0
>
> </div>
>
> ```
>       
>
> <?php
> class foo {
>     public $bar = <<<EOT
> bar
>     EOT;
> }
> // El identificador no debe estar indentado
> ?>
>
>      
> ```
>
> </div>
>
> <div class="example">
>
> <div class="title">
>
> Ejemplo válido, incluso antes de PHP 7.3.0
>
> </div>
>
> ```
>       
>
> <?php
> class foo {
>     public $bar = <<<EOT
> bar
> EOT;
> }
> ?>
>
>      
> ```
>
> </div>
>
> Los heredocs que contienen variables no pueden ser utilizados para inicializar propiedades de clase.

El texto heredoc se comporta exactamente como un `string` entre comillas dobles, sin las comillas. Esto significa que las comillas en un heredoc no necesitan ser escapadas, pero los códigos de escape mencionados anteriormente pueden seguir siendo utilizados. Las variables son desarrolladas, pero debe tenerse el mismo cuidado al expresar variables complejas dentro de un heredoc que para los `strings`.

Ejemplo de cita de string heredoc

```php
<?php
$str = <<<EOD
Ejemplo de string
que se extiende sobre múltiples líneas
usando la sintaxis heredoc.
EOD;

/* Ejemplo más complejo, con variables. */
class foo
{
    var $foo;
    var $bar;

    function __construct()
    {
        $this->foo = 'Foo';
        $this->bar = array('Bar1', 'Bar2', 'Bar3');
    }
}

$foo = new foo();
$name = 'MyName';

echo <<<EOT
Mi nombre es "$name". Estoy imprimiendo $foo->foo.
Ahora, estoy imprimiendo {$foo->bar[1]}.
Esto debería imprimir una 'A' mayúscula: \x41
EOT;
?>

    
```

El ejemplo anterior mostrará:

    Mi nombre es "MyName". Estoy imprimiendo Foo.
    Ahora, estoy imprimiendo Bar2.
    Esto debería imprimir una 'A' mayúscula: A

También es posible utilizar la sintaxis heredoc para pasar datos a los argumentos de función:

Heredoc en ejemplos de argumentos

```php
<?php
var_dump(array(<<<EOD
foobar!
EOD
));
?>

    
```

Es posible inicializar variables estáticas y propiedades/constantes de clase utilizando la sintaxis heredoc:

Uso de Heredoc para inicializar valores estáticos

```php
<?php
// Variables estáticas
function foo()
{
    static $bar = <<<LABEL
Nada aquí...
LABEL;
}

// Propiedades/constantes de clase
class foo
{
    const BAR = <<<FOOBAR
Ejemplo de constante
FOOBAR;

    public $baz = <<<FOOBAR
Ejemplo de propiedad
FOOBAR;
}
?>

    
```

El identificador de apertura del Heredoc puede eventualmente ser encerrado entre comillas dobles:

Uso de comillas dobles en el Heredoc

```php
<?php
echo <<<"FOOBAR"
¡Hola mundo!
FOOBAR;
?>

    
```

### Nowdoc

Los nowdocs son para los strings entre comillas simples lo que los heredocs son para los strings entre comillas dobles. Un nowdoc se especifica de manera similar a un heredoc, pero *ninguna interpolación de string es realizada* dentro de un nowdoc. La construcción es ideal para integrar código PHP o otros bloques de texto voluminosos sin necesidad de escapar. Comparte algunas características con la construcción SGML `<![CDATA[ ]]>`, en el sentido de que declara un bloque de texto que no está destinado a ser analizado.

Un nowdoc es identificado por la misma secuencia `<<<` utilizada para los heredocs, pero el identificador que sigue está encerrado entre comillas simples, por ejemplo `<<<'EOT'`. Todas las reglas para los identificadores heredoc se aplican también a los identificadores nowdoc, en particular aquellas concernientes a la apariencia del identificador de cierre.

Ejemplo de cita de string nowdoc

```php
<?php
echo <<<'EOD'
Ejemplo de string que se extiende sobre múltiples líneas
usando la sintaxis nowdoc. Las barras invertidas son siempre tratadas literalmente,
es decir \\ y \'.
EOD;

    
```

El ejemplo anterior mostrará:

    Ejemplo de string que se extiende sobre múltiples líneas
    usando la sintaxis nowdoc. Las barras invertidas son siempre tratadas literalmente,
    es decir \\ y \'.

Ejemplo de cita de string nowdoc con variables

```php
<?php
class foo
{
    public $foo;
    public $bar;

    function __construct()
    {
        $this->foo = 'Foo';
        $this->bar = array('Bar1', 'Bar2', 'Bar3');
    }
}

$foo = new foo();
$name = 'MyName';

echo <<<'EOT'
Mi nombre es "$name". Estoy imprimiendo $foo->foo.
Ahora, estoy imprimiendo {$foo->bar[1]}.
Esto no debería imprimir una 'A' mayúscula: \x41
EOT;
?>

    
```

El ejemplo anterior mostrará:

    Mi nombre es "$name". Estoy imprimiendo $foo->foo.
    Ahora, estoy imprimiendo {$foo->bar[1]}.
    Esto no debería imprimir una 'A' mayúscula: \x41

Ejemplo de datos estáticos

```php
<?php
class foo {
    public $bar = <<<'EOT'
bar
EOT;
}
?>

    
```

### Interpolación de strings

Cuando un `string` es especificado entre comillas dobles o con heredoc, las [variables](#language.variables) pueden ser sustituidas dentro.

Existen dos tipos de sintaxis: una [básica](#language.types.string.parsing.basic) y una [avanzada](#language.types.string.parsing.advanced). La sintaxis básica es la más común y práctica. Ofrece un medio para incorporar una variable, un valor `array` o una propiedad `objeto` en un `string` con un mínimo de esfuerzo.

#### Sintaxis básica

Si un signo de dólar (`$`) es encontrado, los caracteres que lo siguen y que pueden ser utilizados en un nombre de variable serán interpretados como tales y sustituidos.

Interpolación de strings

```php
<?php
$juice = "manzana";

echo "Él bebió un poco de $juice jugo." . PHP_EOL;

?>

     
```

El ejemplo anterior mostrará:

    Él bebió un poco de manzana jugo.

Formalmente, la estructura para la sintaxis de sustitución de variable básica es la siguiente:

    string-variable::
         variable-name   (offset-or-property)?
       | ${   expression   }

    offset-or-property::
         offset-in-string
       | property-in-string

    offset-in-string::
         [   name   ]
       | [   variable-name   ]
       | [   integer-literal   ]

    property-in-string::
         ->  name

    variable-name::
         $   name

    name::
         [a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*

> [!WARNING]
> La sintaxis `${ expression }` está deprecada desde PHP 8.2.0, ya que puede ser interpretada como [variables de variables](#language.variables.variable):
>
> <div class="informalexample">
>
> ```
> <?php
> const foo = 'bar';
> $foo = 'foo';
> $bar = 'bar';
> var_dump("${foo}");
> var_dump("${(foo)}");
> ?>
>
>        
> ```
>
> Resultado del ejemplo anterior en PHP 8.2:
>
>     Deprecated: Usar ${var} en strings está deprecado, use {$var} en su lugar en el archivo en la línea 6
>
>     Deprecated: Usar ${expr} (variables de variables) en strings está deprecado, use {${expr}} en su lugar en el archivo en la línea 9
>     string(3) "foo"
>     string(3) "bar"
>
>            
>
> El ejemplo anterior mostrará:
>
>     string(3) "foo"
>     string(3) "bar"
>
>            
>
> </div>
>
> La sintaxis de interpolación de string [avanzada](#language.types.string.parsing.advanced) debería ser utilizada en su lugar.

> [!NOTE]
> Si no es posible formar un nombre válido, el signo de dólar tal cual en el string:
>
> <div class="informalexample">
>
> ```
> <?php
> echo "Ninguna interpolación $  ha ocurrido\n";
> echo "Ninguna interpolación $\n ha ocurrido\n";
> echo "Ninguna interpolación $2 ha ocurrido\n";
> ?>
>
>       
> ```
>
> El ejemplo anterior mostrará:
>
>     Ninguna interpolación $  ha ocurrido
>     Ninguna interpolación $
>      ha ocurrido
>     Ninguna interpolación $2 ha ocurrido
>
>           
>
> </div>

Interpolación del valor de la primera dimensión de un array o propiedad

```php
<?php
$juices = array("manzana", "naranja", "string_key" => "violet");

echo "Él bebió un poco de $juices[0] jugo.";
echo PHP_EOL;
echo "Él bebió un poco de $juices[1] jugo.";
echo PHP_EOL;
echo "Él bebió un poco de $juices[string_key] jugo.";
echo PHP_EOL;

class A {
    public $s = "string";
}

$o = new A();

echo "Valor del objeto: $o->s.";
?>

     
```

El ejemplo anterior mostrará:

    Él bebió un poco de manzana jugo.
    Él bebió un poco de naranja jugo.
    Él bebió un poco de violet jugo.
    Valor del objeto: string.

> [!NOTE]
> La clave del array debe ser no citada, y por lo tanto no es posible referenciar una constante como clave con la sintaxis básica. Utilice la sintaxis [avanzada](#language.types.string.parsing.advanced) en su lugar.

Desde PHP 7.1.0, los índices numéricos *negativos* también son soportados.

Índices numéricos negativos

```php
<?php
$string = 'string';
echo "El carácter en el índice -2 es $string[-2].", PHP_EOL;
$string[-3] = 'o';
echo "Cambiar el carácter en el índice -3 a o da $string.", PHP_EOL;
?>

     
```

El ejemplo anterior mostrará:

    El carácter en el índice -2 es n.
    Cambiar el carácter en el índice -3 a o da strong.

Para todo lo que es más complejo, la [sintaxis avanzada](#language.types.string.parsing.advanced) debe ser utilizada.

#### Sintaxis avanzada (sintaxis de llaves)

La sintaxis avanzada permite la interpolación de *variables* con accesorios arbitrarios.

Cualquier variable escalar, elemento de array o propiedad de objeto (estática o no) con una representación `string` puede ser incluida mediante esta sintaxis. La expresión es escrita de la misma manera que aparecería fuera de la `string`, luego encerrada entre `{` y `}`. Dado que `{` no puede ser escapado, esta sintaxis solo será reconocida cuando el `$` siga inmediatamente al `{`. Utilice `{\$` para obtener un `{$`. Aquí hay algunos ejemplos para aclarar:

Sintaxis con llaves

```php
<?php
const DATA_KEY = 'const-key';
$great = 'fantástico';
$arr = [
    '1',
    '2',
    '3',
    [41, 42, 43],
    'key' => 'Valor indexado',
    'const-key' => 'Clave con un signo menos',
    'foo' => ['foo1', 'foo2', 'foo3']
];

// No funcionará, mostrará: Esto es { fantástico}
echo "Esto es { $great}" . PHP_EOL;

// Funciona, mostrará: Esto es fantástico
echo "Esto es {$great}" . PHP_EOL;

// Para mostrar llaves en la salida:
echo "Esto es {{$great}}" . PHP_EOL;

class Square {
    public $width;

    public function __construct(int $width) { $this->width = $width; }
}

$square = new Square(5);

// Funciona
echo "Este cuadrado mide {$square->width}00 centímetros de ancho." . PHP_EOL;

// Funciona, las claves entre comillas solo funcionan con la sintaxis de llaves
echo "Esto funciona: {$arr['key']}" . PHP_EOL;

// Funciona
echo "Esto funciona: {$arr[3][2]}" . PHP_EOL;

echo "Esto funciona: {$arr[DATA_KEY]}" . PHP_EOL;

// Al utilizar arrays multidimensionales, siempre use llaves alrededor de los arrays
// cuando estén dentro de strings
echo "Esto funciona: {$arr['foo'][2]}" . PHP_EOL;

echo "Esto funciona: {$obj->values[3]->name}" . PHP_EOL;

echo "Esto funciona: {$obj->$staticProp}" . PHP_EOL;

// No funcionará, mostrará: C:\directory\{fantástico}.txt
echo "C:\directory\{$great}.txt" . PHP_EOL;

// Funciona, mostrará: C:\directory\fantástico.txt
echo "C:\\directory\\{$great}.txt" . PHP_EOL;
?>

     
```

> [!NOTE]
> Como esta sintaxis permite expresiones arbitrarias, es posible utilizar [variables de variables](#language.variables.variable) en la sintaxis avanzada.

### Acceso y modificación de string por carácter

Los caracteres en los `strings` pueden ser accedidos y modificados especificando el offset basado en cero del carácter deseado después del `string` utilizando corchetes `array`, como en `$str[42]`. Piense en un `string` como un `array` de caracteres para este propósito. Las funciones `substr` y `substr_replace` pueden ser utilizadas cuando se desea extraer o reemplazar más de un carácter.

> [!NOTE]
> Desde PHP 7.1.0, los offsets de string negativos también son soportados. Estos especifican el offset desde el final del string. Anteriormente, los offsets negativos emitían `E_NOTICE` para la lectura (produciendo un string vacío) y `E_WARNING` para la escritura (dejando el string intacto).

> [!NOTE]
> Antes de PHP 8.0.0, los `strings` también podían ser accedidos utilizando llaves, como en `$str{42}`, para el mismo propósito. Esta sintaxis de llaves fue deprecada desde PHP 7.4.0 y ya no es soportada desde PHP 8.0.0.

> [!WARNING]
> Escribir en un offset fuera de alcance llena el string con espacios. Los tipos no enteros son convertidos a entero. Un tipo de offset ilegal emite `E_WARNING`. Solo el primer carácter de un string asignado es utilizado. Desde PHP 7.1.0, asignar un string vacío genera un error fatal. Anteriormente, esto asignaba un octeto NULL.

> [!WARNING]
> Internamente, los strings PHP son arrays de octetos. En consecuencia, acceder o modificar un string utilizando corchetes de array no es seguro para multi-octetos, y solo debe hacerse con strings en codificación de un solo octeto como ISO-8859-1.

> [!NOTE]
> Desde PHP 7.1.0, aplicar el operador de índice vacío a un string vacío genera un error fatal. Anteriormente, el string vacío era silenciosamente convertido a array.

Algunos ejemplos de strings

```php
<?php
// Obtener el primer carácter de un string
$str = 'Esto es una prueba.';
$first = $str[0];
var_dump($first);

// Obtener el tercer carácter de un string
$third = $str[2];
var_dump($third);

// Obtener el último carácter de un string.
$str = 'Esto sigue siendo una prueba.';
$last = $str[strlen($str)-1];
var_dump($last);

// Modificar el último carácter de un string
$str = 'Mire el mar';
$str[strlen($str)-1] = 'e';
var_dump($str);
?>

    
```

Los offsets de string deben ser enteros o strings que parezcan enteros, de lo contrario se emitirá una advertencia.

Ejemplo de offsets de string ilegales

```php
<?php
$str = 'abc';

foreach ($keys as $keyToTry) {
    var_dump(isset($str[$keyToTry]));

    try {
        var_dump($str[$keyToTry]);
    } catch (TypeError $e) {
        echo $e->getMessage(), PHP_EOL;
    }

    echo PHP_EOL;
}
?>

    
```

El ejemplo anterior mostrará:

    bool(true)
    string(1) "b"

    bool(false)
    Cannot access offset of type string on string

    bool(false)
    Cannot access offset of type string on string

    bool(false)

    Warning: Illegal string offset "1x" in Standard input code on line 10
    string(1) "b"

> [!NOTE]
> Acceder a variables de otros tipos (excepto arrays u objetos que implementen las interfaces apropiadas) utilizando `[]` o `{}` devuelve silenciosamente `null`.

> [!NOTE]
> Los caracteres en literales de string pueden ser accedidos utilizando `[]` o `{}`.

> [!NOTE]
> Acceder a caracteres en literales de string utilizando la sintaxis `{}` fue deprecada en PHP 7.4. Esto fue eliminado en PHP 8.0.

## Funciones y operadores útiles

Los `strings` pueden ser concatenados utilizando el operador '.' (punto). Tenga en cuenta que el operador '+' (suma) *no* funcionará para esto. Consulte [los operadores de string](#language.operators.string) para más información.

Existen varias funciones útiles para la manipulación de `strings`.

Consulte la [sección de funciones de string](#ref.strings) para funciones generales, y la [sección de funciones de expresiones regulares compatibles con Perl](#ref.pcre) para funcionalidades avanzadas de búsqueda y reemplazo.

También existen [funciones para strings de URL](#ref.url), y funciones para cifrar/descifrar strings ([Sodium](#ref.sodium) y [Hash](#ref.hash)).

Finalmente, consulte también las [funciones de tipo de carácter](#ref.ctype).

## Conversión a string

Un valor puede ser convertido a `string` utilizando el cast `(string)` o la función `strval`. La conversión a `string` es realizada automáticamente en el contexto de una expresión donde un `string` es necesario. Esto ocurre al utilizar las funciones `echo` o `print`, o cuando una variable es comparada con un `string`. Las secciones sobre [Tipos](#language.types) y [Type Juggling](#language.types.type-juggling) aclararán lo siguiente. Ver también la función `settype`.

Un valor `bool` `true` es convertido al `string` `"1"`. El `bool` `false` es convertido a `""` (el string vacío). Esto permite una conversión de ida y vuelta entre los valores `bool` y `string`.

Un `int` o `float` es convertido a un `string` representando el número textualmente (incluyendo la parte exponencial para los `float`). Los números de punto flotante pueden ser convertidos utilizando la notación exponencial (`4.1E+6`).

> [!NOTE]
> A partir de PHP 8.0.0, el carácter de la coma decimal es siempre un punto ("`.`"). Antes de PHP 8.0.0, el carácter de la coma decimal está definido en la localización del script (categoría LC_NUMERIC). Consulte la función `setlocale`.

Los `arrays` siempre son convertidos al `string` `"Array"`; por lo tanto, `echo` y `print` no pueden por sí solos mostrar el contenido de un `array`. Para mostrar un solo elemento, utilice una construcción como `echo $arr['foo']`. Consulte a continuación consejos para visualizar todo el contenido.

Para convertir `objetos` a `strings`, el método mágico [\_\_toString](#language.oop5.magic) debe ser utilizado.

Los `recursos` siempre son convertidos a `strings` con la estructura `"Resource id #1"`, donde `1` es el número de recurso asignado al `recurso` por PHP en tiempo de ejecución. Aunque la estructura exacta de este string no debe ser considerada como confiable y está sujeta a cambios, siempre será única para un recurso dado durante la duración de ejecución de un script (es decir, una solicitud web o un proceso CLI) y no será reutilizada. Para obtener el tipo de un `recurso`, utilice la función `get_resource_type`.

`null` siempre es convertido a un string vacío.

Como se indicó anteriormente, convertir directamente un `array`, un `objeto` o un `recurso` a `string` no proporciona información útil sobre el valor más allá de su tipo. Consulte las funciones `print_r` y `var_dump` para medios más eficaces de inspeccionar el contenido de estos tipos.

La mayoría de los valores PHP también pueden ser convertidos a `strings` para un almacenamiento permanente. Este método se denomina serialización y es realizado por la función `serialize`.

## Detalles del tipo string

El `string` en PHP está implementado como un array de octetos y un entero indicando la longitud del búfer. No tiene ninguna información sobre cómo estos octetos se traducen en caracteres, dejando esta tarea al programador. No hay limitaciones sobre los valores de los que el string puede estar compuesto; en particular, los octetos de valor `0` («octetos NUL») son permitidos en cualquier parte del string (aunque algunas funciones, dichas en este manual de no ser «seguras para binarios», pueden pasar los strings a bibliotecas que ignoran los datos después de un octeto NUL.)

Esta naturaleza del tipo string explica por qué no hay un tipo «octeto» distinto en PHP - los strings toman este rol. Las funciones que no devuelven datos textuales - por ejemplo, datos arbitrarios leídos desde un socket de red - devolverán strings de todos modos.

Dado que PHP no dicta una codificación específica para los strings, uno podría preguntarse cómo los literales de string están codificados. Por ejemplo, el string `"á"` ¿es equivalente a `"\xE1"` (ISO-8859-1), `"\xC3\xA1"` (UTF-8, forma C), `"\x61\xCC\x81"` (UTF-8, forma D) o cualquier otra representación posible? La respuesta es que el string será codificado de la manera en que está codificado en el archivo de script. Por lo tanto, si el script está escrito en ISO-8859-1, el string será codificado en ISO-8859-1 y viceversa. Sin embargo, esto no se aplica si Zend Multibyte está activado; en este caso, el script puede estar escrito en una codificación arbitraria (que es explícitamente declarada o detectada) y luego convertido a una cierta codificación interna, que luego será la codificación utilizada para los literales de string. Tenga en cuenta que hay ciertas restricciones sobre la codificación del script (o sobre la codificación interna, si Zend Multibyte está activado) - esto significa casi siempre que esta codificación debe ser un superconjunto compatible con ASCII, como UTF-8 o ISO-8859-1. Tenga en cuenta, sin embargo, que las codificaciones dependientes del estado donde las mismas valores de octeto pueden ser utilizados en estados de desplazamiento iniciales y no iniciales pueden causar problemas.

Por supuesto, para ser útiles, las funciones que operan sobre texto pueden necesitar hacer ciertas suposiciones sobre cómo el string está codificado. Desafortunadamente, hay muchas variaciones en este sentido en las funciones de PHP:

- Algunas funciones asumen que el string está codificado en un (todo) conjunto de codificación de un octeto, pero no necesitan interpretar estos octetos como caracteres específicos. Este es el caso, por ejemplo, de `substr`, `strpos`, `strlen` o `strcmp`. Otra forma de pensar en estas funciones es que operan sobre búferes de memoria, es decir, que trabajan con octetos y desplazamientos de octetos.

- Otras funciones reciben la codificación del string, asumiendo posiblemente un valor predeterminado si no se proporciona información de este tipo. Este es el caso de `htmlentities` y la mayoría de las funciones en la [extensión mbstring](#book.mbstring).

- Otras utilizan la localización actual (ver `setlocale`), pero funcionan octeto por octeto.

- Finalmente, pueden simplemente asumir que el string utiliza una codificación específica, generalmente UTF-8. Este es el caso de la mayoría de las funciones en la [extensión intl](#book.intl) y en la [extensión PCRE](#book.pcre) (en este último caso, solo cuando se utiliza el modificador `u`).

En última instancia, esto significa que escribir programas correctos que utilicen Unicode depende de evitar cuidadosamente las funciones que no funcionarán y que probablemente corromperán los datos, y de utilizar en su lugar las funciones que se comportan correctamente, generalmente provenientes de las extensiones [intl](#book.intl) y [mbstring](#book.mbstring). Sin embargo, utilizar funciones capaces de manejar codificaciones Unicode es solo el comienzo. Independientemente de las funciones que el lenguaje proporciona, es esencial conocer la especificación Unicode. Por ejemplo, un programa que asume que solo hay mayúsculas y minúsculas hace una suposición errónea.
