---
title: Variables
source_url: https://www.php.net/manual/es/language.variables.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/variables.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 64007e9f6
order: 4590
---

## Variables

## Conceptos básicos

En PHP las variables se representan con un signo de dólar seguido por el nombre de la variable. El nombre de la variable es sensible a minúsculas y mayúsculas.

Un nombre de variable válido tiene que empezar con una letra (`A-Z`, `a-z`, o los bytes del 128 al 255) o un carácter de subrayado (underscore), seguido de cualquier número de letras, números y caracteres de subrayado. Como expresión regular se podría expresar como: `^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$`

> [!NOTE]
> PHP no soporta Unicode en el nombre de las variables, sin embargo, algunas codificaciones de caracteres (como UTF-8) codifican caracteres de tal manera que todos los bytes de un carácter multibyte están dentro del rango permitido, convirtiéndolo así en un nombre de variable válido.

> [!NOTE]
> `$this` es una variable especial que no puede ser asignada. Antes de PHP 7.1.0, era posible la asignación indirecta (por ejemplo, mediante el uso de [variables variables](#language.variables.variable)).

> [!TIP]
> Véase también [???](#userlandnaming).

Valid variable names

```php
<?php
$var = 'Roberto';
$Var = 'Juan';
echo "$var, $Var";      // Imprime "Roberto, Juan"

$_4site = 'aún no';     // Válido; comienza con un carácter de subrayado
$täyte = 'mansikka';    // Válido; 'ä' es ASCII (Extendido) 228

    
```

Invalid variable names

```php
<?php
$4site = 'aún no';     // Inválido; comienza con un número

    
```

PHP acepta una secuencia de bytes como nombre de variable. Los nombres de variables que no siguen las reglas de nombres mencionadas anteriormente solo pueden accederse de forma dinámica en tiempo de ejecución. Consulte [variables variables](#language.variables.variable) para obtener información sobre cómo acceder a ellas.

Cómo acceder a nombres de variables con caracteres no válidos

```php
<?php
${'invalid-name'} = 'bar';
$name = 'invalid-name';
echo ${'invalid-name'}, " ", $$name;

    
```

El ejemplo anterior mostrará:

    bar bar

Por omisión, las variables siempre se asignan por valor. Esto significa que cuando se asigna una expresión a una variable, el valor completo de la expresión original se copia en la variable de destino. Esto quiere decir que, por ejemplo, después de asignar el valor de una variable a otra, los cambios que se efectúen a una de esas variables no afectará a la otra. Para más información sobre este tipo de asignación, vea el capítulo sobre [Expresiones](#language.expressions).

PHP también ofrece otra forma de asignar valores a las variables: [asignar por referencia](#language.references). Esto significa que la nueva variable simplemente referencia (en otras palabras, "se convierte en un alias de" ó "apunta a") la variable original. Los cambios a la nueva variable afectan a la original, y viceversa.

Para asignar por referencia, simplemente se antepone un signo ampersand (&) al comienzo de la variable cuyo valor se está asignando (la variable fuente). Por ejemplo, el siguiente segmento de código produce la salida '`Mi nombre es Bob`' dos veces:

```php
<?php
$foo = 'Bob';                // Asigna el valor 'Bob' a $foo
$bar = &$foo;                // Referenciar $foo vía $bar.
$bar = "Mi nombre es $bar";  // Modifica $bar...
echo $bar . PHP_EOL;
echo $foo . PHP_EOL;         // $foo también se modifica.

     
```

Algo importante a tener en cuenta es que sólo las variables con nombre pueden ser asignadas por referencia.

```php
<?php
$original = 25;
$ref1 = &$original;        // Esta es una asignación válida.
$ref2 = &(24 * 7);         // Inválida; referencia una expresión sin nombre.

     
```

```php
<?php
// Tenga en cuenta la falta de & que indica un retorno por referencia en la declaración de la función.
// Es decir, la función no retorna una referencia, por lo que el resultado no puede asignarse por referencia.
function test()
{
   $original = 25;
   return $original;
}

// Nota: Se emite un aviso, pero el valor sin referencia es asignado
$result1 = &test();        // Inválido porque test() no devuelve una variable por referencia.
var_dump($result1);

// Esta función está definida como retornando una referencia, pero no retorna una variable
function &test2()
{
    return 26;             // Inválido porque el valor retornado no es una referencia a una variable.
}

// Nota: El valor sin referencia es asignado
$result2 = &test2();
var_dump($result2);

     
```

No es necesario inicializar variables en PHP, sin embargo, es una muy buena práctica. El acceso a una variable no definida generará un `E_WARNING` (en versiones anteriores a PHP 8.0.0, `E_NOTICE`). Una variable no definida tiene un valor predeterminado de `null`. Se puede utilizar la construcción del lenguaje `isset` para detectar si una variable ya se ha inicializado.

Valores predeterminados en variables sin inicializar

```php
<?php
// Una variable no definida Y no referenciada (sin contexto de uso).
var_dump($variable_indefinida);

     
```

El ejemplo anterior mostrará:

    Warning: Undefined variable $unset_var in ...
    NULL

PHP permite la autovivificación de array (creación automática de un nuevo array) a partir de una variable no definida. Añadidiendo un elemento a una variable no definida creará un nuevo array y no producirá ninguna advertencia.

Autovivification de un array a partir de una variable no definida

```php
<?php
$unset_array[] = 'valor'; // No producirá ninguna advertencia.
var_dump($unset_array);

    
```

> [!WARNING]
> Depender del valor predeterminado de una variable sin inicializar es problemático al incluir un archivo en otro que use el mismo nombre de variable.

Una variable puede ser destruida, utilizando la construcción del lenguaje `unset`.

Para información con funciones relativas a variables, mira la [Referencia de funciones de variables](#ref.var).

## Variables Predefinidas

PHP proporciona una gran cantidad de [variables predefinidas](#reserved.variables). PHP ofrece un conjunto adicional de arrays predefinidas que contienen variables del servidor web (cuando es aplicable), el entorno y entradas del usuario. Estos arrays están automáticamente disponibles en cualquier entorno. Por esa razón, a veces son conocidas como "superglobales". (No existe mecanismo en PHP para crear superglobales definidas por el usuario). Referencia de la [lista de superglobales](#language.variables.superglobals) para más detalles.

> [!NOTE]
> Las superglobales no pueden ser usadas como [variables variables](#language.variables.variable) en el interior de funciones o métodos de clase.

Si ciertas variables no son definidas en [variables_order](#ini.variables-order), los arrays de PHP predefinidos asociados a estas, estarán vacíos.

## Ámbito de las variables

El ámbito de una variable es el contexto en el cual la variable está definida. PHP tiene un ámbito de función y un ámbito global. Cualquier variable difinida fuera de una función está limitada al ámbito global. Cuando se incluye un archivo, el código contenido hereda el ámbito de la variable de la línea en la cual se incluye el archivo.

Ejemplo de una variable de ámbito global

```php
<?php
$a = 1;
include 'b.inc'; // La variable $a estará disponible en el interior de b.inc

    
```

Cualquier variable declarada dentro de una función o una [funcíón anónima](#functions.anonymous) está limitada al ámbito del cuerpo de dicha función. Sin embargo, las [funciones de flecha](#functions.arrow) vinculan las variables desde el ámbito padre haciendo que estén disponibles dentro de la función. Si se incluye un archivo dentro de una función, las variables contenidas en el archivo llamado estarán disponibles como si se hubieran definido dentro de la función que realiza la llamada.

Ejemplo de una variable de ámbito local

```php
<?php
$a = 1; // ámbito global

function test()
{
    var_dump($a); // La variable $a no está definida ya que se refiere a una versión local de $a
}

test();

    
```

El ejemplo anterior producirá un `E_WARNING` por una variable no definida (o un `E_NOTICE` antes de PHP 8.0.0). Esto se debe a la expresión echo hace referencia a una versión local de la variable `$a`, a la cual no se le ha asignado un valor dentro de su ámbito. Puede que usted note que hay una pequeña diferencia con el lenguaje C, en el que las variables globales están disponibles automáticamente dentro de la función a menos que sean expresamente sobreescritas por una definición local. Esto puede causar algunos problemas, ya que la gente podría cambiar variables globales sin darse cuenta. En PHP, las variables globales deben ser declaradas globales dentro de la función si van a ser utilizadas dentro de dicha función.

### La palabra clave `global`

La palabra clave `global` se usa para vincular una variable desde el ámbito global a un ámbito local. La palabra clave puede ser usada con una lista de variables o con una sola variable. Una variable local será creada haciendo referendia a una variable global con el mismo nombre. Si no existe la variable global, la variable será creada en el ámbito global y asignado el valor `null`.

Uso de `global`

```php
<?php
$a = 1;
$b = 2;

function Suma()
{
    global $a, $b;

    $b = $a + $b;
}

Suma();
echo $b;

     
```

El ejemplo anterior mostrará:

    3

Al declarar las variables `$a` y `$b` globales dentro de la función, todas las referencias a tales variables se referirán a la versión global. No hay límite al número de variables globales que se pueden manipular dentro de una función.

Un segundo método para acceder a las variables desde un ámbito global es usando el array especial definido por PHP `$GLOBALS`. El ejemplo anterior se puede reescribir así:

Uso de `$GLOBALS` en lugar de global

```php
<?php
$a = 1;
$b = 2;

function Suma()
{
    $GLOBALS['b'] = $GLOBALS['a'] + $GLOBALS['b'];
}

Suma();
echo $b;

     
```

El array `$GLOBALS` es un array asociativo con el nombre de la variable global como clave y los contenidos de dicha variable como el valor del elemento del array. `$GLOBALS` existe en cualquier ámbito, esto ocurre ya que `$GLOBALS` es una [superglobal](#language.variables.superglobals). Aquí hay un ejemplo que demuestra el poder de las superglobales:

Ejemplo que demuestra las superglobales y el ámbito

```php
<?php
function test_superglobal()
{
    echo $_POST['name'];
}

     
```

> [!NOTE]
> Utilizar una clave `global` fuera de una función no es un error. Esta puede ser utilizada aún si el fichero está incluido desde el interior de una función.

### Uso de variables `static`

Otra característica importante del ámbito de las variables es la variable *estática*. Una variable estática existe sólo en el ámbito local de la función, pero no pierde su valor cuando la ejecución del programa abandona este ámbito. Consideremos el siguiente ejemplo:

Ejemplo que demuestra la necesidad de variables estáticas

```php
<?php
function test()
{
    $a = 0;
    echo $a . PHP_EOL;
    $a++;
}

test();
test();
test();

     
```

Esta función tiene poca utilidad ya que cada vez que es llamada asigna a `$a` el valor `0` e imprime un `0`. La sentencia `$a`++, que incrementa la variable, no sirve para nada, ya que en cuanto la función finaliza, la variable `$a` desaparece. Para hacer una función útil para contar, que no pierda la pista del valor actual del conteo, la variable `$a` debe declararse como estática:

Ejemplo del uso de variables estáticas

```php
<?php
function test()
{
    static $a = 0;
    echo $a . PHP_EOL;
    $a++;
}

test();
test();
test();

     
```

Ahora, `$a` se inicializa únicamente en la primera llamada a la función, y cada vez que la función `test()` es llamada, imprimirá el valor de `$a` y lo incrementa.

Las variables estáticas también proporcionan una forma de manejar funciones recursivas. La siguiente función cuenta recursivamente hasta 10, usando la variable estática `$count` para saber cuándo parar:

Variables estáticas con funciones recursivas

```php
<?php
function test()
{
    static $count = 0;

    $count++;
    echo $count . PHP_EOL;
    if ($count < 10) {
        test();
    }
    $count--;
}

test();

     
```

Antes de PHP 8.3.0, las variables estáticas solo podían ser inicializadas usando expresiones constantes. A partir de PHP 8.3.0, expresiones dinámicas (por ejemplo, llamadas a funciones) también están permitidas:

Declarando variables estáticas

```php
<?php
function foo(){
    static $int = 0;          // correcto
    static $int = 1+2;        // correcto
    static $int = sqrt(121);  // correcto a partir de PHP 8.3.0

    $int++;
    echo $int;
}

     
```

Las variables estáticas dentro de funiones anónimas también persisten solo dentro de esa instancia específica de la función. Si la función anónima es recreada en cada llamada, la variable estática será reinicializada.

Variables estáticas en funciones anónimas

```php
<?php
function exampleFunction($input) {
    $result = (static function () use ($input) {
        static $counter = 0;
        $counter++;
        return "Entrada: $input, Contador: $counter\n";
    });

    return $result();
}

// Las llamadas a exampleFunction recrearán la función anónima, por tanto
// la variable estática no retendrá su valor.
echo exampleFunction('A'); // Devolverá: Entrada: A, Contador: 1
echo exampleFunction('B'); // Devolverá: Entrada: B, Contador: 1

    
```

A partir de PHP 8.1.0, cuando un método que usa variables estáticas es heredado (pero no sobrescrito), el método heredado compartirá ahora las variables estáticas con el método padre. Esto significa que las variables estáticas en los métodos ahora se comportan de la misma manera que las propiedades estáticas.

A partir de PHP 8.3.0, las variables estáticas pueden ser inicializadas con expresiones arbitrarias. Esto significa que las llamadas a métodos, por ejemplo, pueden ser usadas para inicializar variables estáticas.

Uso de variables estáticas en métodos heredados

```php
<?php
class Foo {
    public static function counter() {
        static $counter = 0;
        $counter++;
        return $counter;
    }
}
class Bar extends Foo {}
var_dump(Foo::counter()); // int(1)
var_dump(Foo::counter()); // int(2)
var_dump(Bar::counter()); // int(3), antes de PHP 8.1.0 int(1)
var_dump(Bar::counter()); // int(4), antes de PHP 8.1.0 int(2)

    
```

### Referencias con variables `global` y `static`

PHP implementa los modificadores [static](#language.variables.scope.static) y [global](#language.variables.scope.global) para variables en términos de [referencias](#language.references). Por ejemplo, una variable global verdadera importada dentro del ámbito de una función con `global` crea una referencia a la variable global. Esto puede ser causa de un comportamiento inesperado, tal y como podemos comprobar en el siguiente ejemplo:

```php
<?php
function test_global_ref() {
    global $obj;
    $new = new stdClass;
    $obj = &$new;
}

function test_global_noref() {
    global $obj;
    $new = new stdClass;
    $obj = $new;
}

test_global_ref();
var_dump($obj);
test_global_noref();
var_dump($obj);

    
```

El ejemplo anterior mostrará:

    NULL
    object(stdClass)#1 (0) {
    }

Un comportamiento similar se aplica a `static`. Las referencias no son almacenadas estáticamente.

```php
<?php
function &get_instance_ref() {
    static $obj;

    echo 'Objeto estático: ';
    var_dump($obj);
    if (!isset($obj)) {
        $new = new stdClass;
        // Asignar una referencia a la variable estática
        $obj = &$new;
    }
    if (!isset($obj->property)) {
        $obj->property = 1;
    } else {
        $obj->property++;
    }
    return $obj;
}

function &get_instance_noref() {
    static $obj;

    echo 'Objeto estático: ';
    var_dump($obj);
    if (!isset($obj)) {
        $new = new stdClass;
        // Asignar el objeto a la variable estática
        $obj = $new;
    }
    if (!isset($obj->property)) {
        $obj->property = 1;
    } else {
        $obj->property++;
    }
    return $obj;
}

$obj1 = get_instance_ref();
$aun_obj1 = get_instance_ref();
echo "\n";
$obj2 = get_instance_noref();
$aun_obj2 = get_instance_noref();

    
```

El ejemplo anterior mostrará:

    Objeto estático: NULL
    Objeto estático: NULL

    Objeto estático: NULL
    Objeto estático: object(stdClass)#3 (1) {
      ["property"]=>
      int(1)
    }

Este ejemplo demuestra que al asignar una referencia a una variable estática, esta no es *recordada* cuando se invoca la funcion `&obtener_instancia_ref()` por segunda vez.

## Variables variables

A veces es conveniente tener nombres de variables variables. Dicho de otro modo, son nombres de variables que se pueden definir y usar dinámicamente. Una variable normal se establece con una sentencia como:

```php
<?php
$a = 'hola';
var_dump($a);

   
```

Una variable variable toma el valor de una variable y lo trata como el nombre de una variable. En el ejemplo anterior, *hola*, se puede usar como el nombre de una variable utilizando dos signos de dólar. Es decir:

```php
<?php
$a = 'hola';
$$a = 'mundo';
var_dump($hola);

   
```

En este momento se han definido y almacenado dos variables en el árbol de símbolos de PHP: `$a`, que contiene "hola", y `$hola`, que contiene "mundo". Es más, esta sentencia:

```php
<?php
$a = 'hola';
$$a = 'mundo';
echo "$a ${$a}";

   
```

produce el mismo resultado que:

```php
<?php
$a = 'hola';
$$a = 'mundo';
echo "$a $hola";

   
```

esto quiere decir que ambas producen el resultado: `hola mundo`.

Para usar variables variables con arrays hay que resolver un problema de ambigüedad. Si se escribe `$$a[1]`, el intérprete necesita saber si nos referimos a utilizar `$a[1]` como una variable, o si se pretendía utilizar `$$a` como variable y el índice `[1]` como índice de dicha variable. La sintaxis para resolver esta ambigüedad es: `${$a[1]}` para el primer caso y `${$a}[1]` para el segundo.

También se puede acceder a las propiedades de una clase usando el nombre de propiedad variable. Este será resuelto dentro del ámbito del cual se hizo la llamada. Por ejemplo, en la expresión `$foo->$bar`, se buscará `$bar` en el ámibto local y se empleará su valor será como el nombre de la propiedad de `$foo`. Esto también es cierto si `$bar` es un acceso a un array.

También se pueden usar llaves para delimitar de forma clara el nombre de la propiedad. Son muy útila al acceder a valores dentro una propiedad que contiene un array, cuando el nombre de la propiedad está compuesto de múltiples partes, o cuando el nombre de la propiedad contiene caracteres que de otro modo no son válidos (p.ej. desde `json_decode` o [SimpleXML](#book.simplexml)).

Ejemplo de propiedad variable

```php
<?php
class foo {
    var $bar = 'Soy bar.';
    var $arr = array('Soy A.', 'Soy B.', 'Soy C.');
    var $r   = 'Soy r.';
}

$foo = new foo();
$bar = 'bar';
$baz = array('foo', 'bar', 'baz', 'quux');
echo $foo->$bar . "\n";
echo $foo->{$baz[1]} . "\n";

$start = 'b';
$end   = 'ar';
echo $foo->{$start . $end} . "\n";

$arr = 'arr';
echo $foo->{$arr[1]} . "\n";
echo $foo->{$arr}[1] . "\n";

    
```

El ejemplo anterior mostrará:

    Soy bar.
    Soy bar.
    Soy bar.
    Soy r.
    Soy B.

> [!WARNING]
> Por favor tenga en cuenta que las variables variables no pueden usarse con los [Arrays superglobales](#language.variables.superglobals) de PHP al interior de funciones o métodos de clase. La variable `$this` es también una variable especial que no puede ser referenciada dinámicamente.

## Variables desde fuentes externas

### Formularios HTML (GET y POST)

Cuando se envía un formulario a un script de PHP, la información de dicho formulario pasa a estar automáticamente disponible en el script. Existen algunas formas de acceder a esta información, por ejemplo:

Un formulario HTML sencillo

```php
<form action="foo.php" method="post">
    Nombre usuario: <input type="text" name="username" /><br />
    Email:  <input type="text" name="email" /><br />
    <input type="submit" name="submit" value="¡Enviarme!" />
</form>

     
```

Solamente existen dos maneras de acceder a datos desde formularios HTML. Los métodos disponibles actualmente se enumeran a continuación:

Acceso a datos de un formulario HTML sencillo con POST

```php
<?php
echo $_POST['username'];
echo $_REQUEST['username'];

     
```

Usar un formulario con GET es similar excepto en el uso de variables predefinidas, que en este caso serán del tipo GET. GET también se usa con `QUERY_STRING` (la información despues del símbolo '?' en una URL). Por ejemplo `http://www.example.com/test.php?id=3` contiene datos GET que son accesibles con `$_GET['id']`. Véase también `$_REQUEST`.

> [!NOTE]
> Puntos y espacios en nombres de variables son convertidos a guiones bajos. Por ejemplo `<input name="a.b" />` se convierte en `$_REQUEST["a_b"]`.

PHP también entiende arrays en el contexto de variables de formularios (vea la [faq relacionada](#faq.html)). Se puede, por ejemplo, agrupar juntas variables relacionadas o usar esta característica para obtener valores de una entrada "select" múltiple. Por ejemplo, vamos a mandar un formulario a sí mismo y a presentar los datos cuando se reciban:

Variables de formulario más complejas

```php
<?php
if ($_POST) {
    echo '<pre>';
    echo htmlspecialchars(print_r($_POST, true));
    echo '</pre>';
}
?>
<form action="" method="post">
    Nombre:  <input type="text" name="personal[nombre]" /><br />
    Email:   <input type="text" name="personal[email]" /><br />
    Cerveza: <br />
    <select multiple name="cerveza[]">
        <option value="warthog">Warthog</option>
        <option value="guinness">Guinness</option>
        <option value="stuttgarter">Stuttgarter Schwabenbräu</option>
    </select><br />
    <input type="submit" value="¡enviarme!" />
</form>

     
```

> [!NOTE]
> Si una variable externa comienza con una sintaxis de array válida, Los caracteres finales se ignoran en silencio. Por ejemplo, `<input name="foo[bar]baz">` se convierte en `$_REQUEST['foo']['bar']`.

#### Nombres de variables tipo IMAGE SUBMIT

Cuando se envía un formulario, es posible usar una imagen en vez del botón estándar "submit":

```php
<input type="image" src="image.gif" name="sub" />

      
```

Cuando el usuario hace click en cualquier parte de la imagen, el formulario que la acompaña se transmitirá al servidor con dos variables adicionales, `sub_x` y `sub_y`. Éstas contienen las coordenadas del clic del usuario dentro de la imagen. Los más experimentados puede notar que los nombres de variable enviados por el navegador contienen un guión en vez de un subrayado (guión bajo), pero PHP convierte el guión en subrayado automáticamente.

### Cookies HTTP

PHP soporta cookies de HTTP de forma transparente tal y como están definidas en [RFC 6265](https://datatracker.ietf.org/doc/html/rfc6265). Las cookies son un mecanismo para almacenar datos en el navegador y así rastrear o identificar a usuarios que vuelven. Se pueden crear cookies usando la función `setcookie`. Las cookies son parte de la cabecera HTTP, así que se debe llamar a la función SetCookie antes de que se envíe cualquier salida al navegador. Es la misma restricción que para la función `header`. Los datos de una cookie están disponibles en el array de datos de la cookies apropiada, tal como `$_COOKIE` y `$_REQUEST`. Véase la página de `setcookie` del manual para más detalles y ejemplos.

> [!NOTE]
> A partir de PHP 7.2.34, 7.3.23 y 7.4.11, respectivamente, los *nombres* de las cookies entrantes ya no son con url-decoded por razones de seguridad.

Si se quieren asignar múltiples valores a una sola cookie, basta con asignarlo como un array. Por ejemplo:

```php
<?php
setcookie("MiCookie[foo]", 'Prueba 1', time()+3600);
setcookie("MiCookie[bar]", 'Prueba 2', time()+3600);

     
```

Esto creará dos cookies separadas aunque `MiCookie` será un array simple en el script. Si se quiere definir una sola cookie con valores múltiples, considere el uso de la función `serialize` o `explode` primero en el valor.

Nótese que una cookie reemplazará a una cookie anterior que tuviese el mismo nombre en el navegador a menos que la ruta o el dominio fuesen diferentes. Así, para una aplicación de carrito de compras se podría querer mantener un contador e ir pasándolo. Es decir:

Un ejemplo de `setcookie`

```php
<?php
if (isset($_COOKIE['count'])) {
    $count = $_COOKIE['count'] + 1;
} else {
    $count = 1;
}
setcookie('conteo', $count, time()+3600);
setcookie("Carrito[$count]", $item, time()+3600);

     
```

### Puntos en los nombres de variables de entrada

Típicamente, PHP no altera los nombres de las variables cuando se pasan a un script. Sin embargo, hay que notar que el punto no es un carácter válido en el nombre de una variable PHP. Para conocer la razón, considere el siguiente ejemplo:

```php
<?php
$varname.ext;  /* nombre de variable inválido */

     
```

Lo que el intérprete vé es el nombre de una variable `$varname`, seguido por el operador de concatenación, y seguido por la cadena pura (es decir, una cadena sin entrecomillar que no coincide con ninguna palabra clave o reservada conocida) 'ext'. Obviamente, no se pretendía que fuese éste el resultado.

Por esta razón, es importante hacer notar que PHP reemplazará automáticamente cualquier punto en los nombres de variables de entrada por guiones bajos (subrayados).

### Determinación de los tipos de variables

Dado que PHP determina los tipos de las variables y los convierte (generalmente) según lo que necesita, no siempre resulta obvio de qué tipo es una variable dada en un momento concreto. PHP incluye varias funciones que descubren de qué tipo es una variable: `gettype`, `is_array`, `is_float`, `is_int`, `is_object`, y `is_string`. Vea también el capítulo sobre [Tipos](#language.types).

Dado que HTTP es un protocolo de texto, la mayoría, si no todo, el contenido que llega en [arrays superglobales](#language.variables.superglobals), como `$_POST` y `$_GET`, permanecerá como cadenas de texto. PHP no intentará convertir los valores a un tipo específico. En el ejemplo siguiente, `$_GET["var1"]` contendrá la cadena "null" y `$_GET["var2"]`, la cadena "123".

    /index.php?var1=null&var2=123

          

### Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.34, 7.3.23, 7.4.11 | Los *nombres* de las cookies entrantes ya no son con url-decoded por razones de seguridad. |
