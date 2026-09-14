---
title: Los espacios de nombres
source_url: https://www.php.net/manual/es/language.namespaces.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/namespaces.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 2370
---

## Los espacios de nombres

## Introducción a los espacios de nombres

¿Qué son los espacios de nombres? En su definición más amplia, representan un medio para encapsular elementos. Esto puede concebirse como un concepto abstracto, por varias razones. Por ejemplo, en un sistema de archivos, los directorios representan un grupo de archivos asociados y sirven como espacio de nombres para los archivos que contienen. Un ejemplo concreto es que el archivo `foo.txt` puede existir en ambos directorios `/home/greg` y `/home/other`, pero que las dos copias de `foo.txt` no pueden coexistir en el mismo directorio. Además, para acceder al archivo `foo.txt` desde fuera del directorio `/home/greg`, es necesario especificar el nombre del directorio utilizando un separador de directorios, como `/home/greg/foo.txt`. El mismo principio se aplica a los espacios de nombres en el mundo de la programación.

En el mundo de PHP, los espacios de nombres están diseñados para resolver dos problemas que enfrentan los autores de bibliotecas y aplicaciones al reutilizar elementos como clases o bibliotecas de funciones:

1.  Colisiones de nombres entre el código que se crea, las clases, funciones o constantes internas de PHP, o las de bibliotecas de terceros.

2.  La capacidad de crear alias o acortar nombres como Nombres_Extremadamente_Largos para ayudar a resolver el primer problema y mejorar la legibilidad del código.

Los espacios de nombres de PHP proporcionan un medio para agrupar clases, interfaces, funciones o constantes. Aquí hay un ejemplo de sintaxis de los espacios de nombres de PHP:

Ejemplo de sintaxis de espacios de nombres

```php
   
<?php
namespace mi\nombre; // Ver la sección "Definición de espacios de nombres"

class MiClase {}
function mifuncion() {}
const MICONSTANTE = 1;

$a = new MiClase;
print $a::class . "\n";
$c = new \mi\nombre\MiClase; // Ver la sección "Espacio global"
print $c::class . "\n";

$a = strlen('hola'); // Ver "Uso de espacios de nombres: retorno al espacio global
print $a . "\n";

$d = namespace\MICONSTANTE; // Ver "El operador namespace y la constante __NAMESPACE__
print $d . "\n";

$d = __NAMESPACE__ . '\MICONSTANTE';
echo constant($d); // Ver "Espacios de nombres y características dinámicas"
    
   
```

> [!NOTE]
> Los nombres de espacios de nombres no son sensibles a mayúsculas/minúsculas.

> [!NOTE]
> Los espacios de nombres `PHP`, así como los nombres compuestos que comienzan con estos nombres (como `PHP\Classes`) están reservados para el uso interno del lenguaje y no deben usarse en el código del espacio de usuario.

## Definición de espacios de nombres

Aunque el código PHP válido puede contenerse en un espacio de nombres, solo los siguientes tipos de código pueden verse afectados por los espacios de nombres: las clases (incluyendo las abstractas, los traits y los enums), las interfaces, las funciones y las constantes.

Los espacios de nombres se declaran con la palabra clave `namespace`. Un archivo que contiene un espacio de nombres debe declarar el espacio al principio del archivo, antes de cualquier otro código, con una sola excepción: la palabra clave [???](#control-structures.declare).

Declaración de un espacio de nombres

```php
     
<?php
namespace MonProjet;

const CONNEXION_OK = 1;
class Connexion { /* ... */ }
function connecte() { /* ... */ }

    
```

> [!NOTE]
> Los nombres completamente calificados (es decir, los nombres que comienzan con un backslash) no están autorizados en las declaraciones de espacios de nombres, ya que tales construcciones se interpretan como expresiones de espacio de nombres relativo.

El único elemento autorizado antes de la declaración de espacio de nombres es la instrucción `declare`, para definir la codificación del archivo fuente. Además, ningún código no-PHP puede preceder a la declaración de espacio de nombres, incluyendo espacios:

Error de declaración de un espacio de nombres

```php
     
<html>
<?php
namespace MonProjet; // error fatal: el espacio de nombres debe ser el primer elemento del script

    
```

Además, a diferencia de otras estructuras de PHP, el mismo espacio de nombres puede definirse en varios archivos, lo que permite dividir el contenido de un espacio de nombres en varios archivos.

## Declaración de un subespacio de nombres

Al igual que con los archivos y los directorios, los espacios de nombres también son capaces de especificar una jerarquía de espacios de nombres. Por lo tanto, un nombre de espacio de nombres puede definirse con sus subniveles:

Declaración de un espacio de nombres con jerarquía

```php
     
<?php
namespace MonProjet\Sous\Niveau;

const CONNEXION_OK = 1;
class Connexion { /* ... */ }
function connecte() { /* ... */  }

    
```

En el ejemplo anterior, se crean la constante `MonProjet\Sous\Niveau\CONNEXION_OK`, la clase `MonProjet\Sous\Niveau\Connexion` y la función `MonProjet\Sous\Niveau\connecte`.

## Definición de varios espacios de nombres en el mismo archivo

También pueden declararse varios espacios de nombres en el mismo archivo. Hay dos sintaxis autorizadas.

Declaración de varios espacios de nombres, sintaxis de combinación simple

```php
     
<?php
namespace MonProjet;

const CONNEXION_OK = 1;
class Connexion { /* ... */ }
function connecte() { /* ... */  }

namespace AutreProjet;

const CONNEXION_OK = 1;
class Connexion { /* ... */ }
function connecte() { /* ... */  }

    
```

Esta sintaxis no se recomienda para combinar espacios de nombres en un solo archivo. En su lugar, se recomienda utilizar la sintaxis de llaves.

Declaración de varios espacios de nombres, sintaxis de llaves

```php
     
<?php
namespace MonProjet {

const CONNEXION_OK = 1;
class Connexion { /* ... */ }
function connecte() { /* ... */  }
}

namespace AutreProjet {

const CONNEXION_OK = 1;
class Connexion { /* ... */ }
function connecte() { /* ... */  }
}

    
```

Se recomienda encarecidamente, como práctica de codificación, no mezclar varios espacios de nombres en el mismo archivo. El uso recomendado es combinar varios scripts PHP en el mismo archivo.

Para combinar varios códigos sin espacios de nombres en código con espacio de nombres, solo se admite la sintaxis de llaves. El código global debe estar encerrado por un espacio de nombres sin nombre, como este:

Declaración de varios espacios de nombres con un espacio sin nombre

```php
     
<?php
namespace MonProjet {

const CONNEXION_OK = 1;
class Connexion {
    public static function start() {
        print __METHOD__ . "\n";
    }
}

function connecte() {
    print __FUNCTION__ . "\n";
}
}

namespace { // código global
print strlen("hi") . "\n";
MonProjet\connecte();
MonProjet\Connexion::start();
}

    
```

No puede existir ningún código PHP fuera de las llaves del espacio de nombres, excepto para abrir una nueva instrucción declare.

Declaración de varios espacios de nombres con un espacio sin nombre (2)

```php
     
<?php
declare(strict_types=1);
namespace MonProjet {

const CONNEXION_OK = 1;
class Connexion {
    public static function start() {
        print __METHOD__ . "\n";
    }
}

function connecte() {
    print __FUNCTION__ . "\n";
}
}

namespace { // código global
print strlen("hi") . "\n";
MonProjet\connecte();
MonProjet\Connexion::start();
}

    
```

## Uso de espacios de nombres: introducción

Antes de discutir el uso de espacios de nombres, es importante comprender cómo PHP deduce qué espacio de nombres está utilizando su código. Puede hacerse una analogía simple entre los espacios de nombres de PHP y un sistema de archivos. Hay tres formas de acceder a un archivo en un sistema de archivos:

1.  Un nombre de archivo relativo, como `foo.txt`. Esto se resuelve en `dossiercourant/foo.txt` donde `dossiercourant` es el directorio de trabajo. Si el directorio actual es `/home/foo`, este nombre se resuelve en `/home/foo/foo.txt`.

2.  Una ruta relativa, como `sub-dossier/foo.txt`. Esto se resuelve en `dossiercourant/sub-dossier/foo.txt`.

3.  Una ruta absoluta, como `/main/foo.txt`. Esto se resuelve en `/main/foo.txt`.

El mismo principio puede aplicarse a los espacios de nombres de PHP. Por ejemplo, puede hacer referencia a una clase de tres maneras:

1.  Un nombre sin calificador, o una clase sin prefijo, como `$a = new foo();` o `foo::methodestatique();`. Si el espacio de nombres actual es `espacedenomscourant`, esto se resuelve en `espacedenomscourant\foo`. Si el espacio de nombres es global, es decir, el espacio de nombres sin nombre, esto se convierte en `foo`.

    Una advertencia: los nombres sin calificador para funciones y constantes se tomarán del espacio de nombres global, si la función no está definida en el espacio de nombres actual. Ver [Uso de espacios de nombres: retorno al espacio de nombres global para funciones y constantes](#language.namespaces.fallback) para más detalles.

2.  Un nombre calificado, o una clase con prefijo como `$a = new sousespacedenoms\foo();` o `sousespacedenoms\foo::methodestatique();`. Si el espacio de nombres actual es `espacedenomscourant`, esto se convierte en `espacedenomscourant\sousespacedenoms\foo`. Si el código es global, es decir, el espacio de nombres sin nombre, esto se convierte en `sousespacedenoms\foo`.

3.  Un nombre absoluto, o un nombre con prefijo con un operador global como `$a = new \espacedenomscourant\foo();` o `\espacedenomscourant\foo::methodestatique();`. Esto siempre hace referencia al nombre literal especificado en el código: `espacedenomscourant\foo`.

Aquí hay un ejemplo de las tres sintaxis, en código real:

file1.php

```php
     
<?php
namespace Foo\Bar\sousespacedenoms;

const FOO = 1;
function foo() {}
class foo
{
    static function methodestatique() {}
}
     
    
```

file2.php

```php
     
<?php
namespace Foo\Bar;
include 'file1.php';

const FOO = 2;
function foo() {}
class foo
{
    static function methodestatique() {}
}

/* nombre no calificado */
foo(); // Se convierte en Foo\Bar\foo
foo::methodestatique(); // Se convierte en Foo\Bar\foo, método methodestatique
echo FOO; // Se convierte en la constante Foo\Bar\FOO

/* nombre calificado */
sousespacedenoms\foo(); // Se convierte en la función Foo\Bar\sousespacedenoms\foo
sousespacedenoms\foo::methodestatique(); // se convierte en la clase Foo\Bar\sousespacedenoms\foo,
                                  // método methodestatique
echo sousespacedenoms\FOO; // Se convierte en la constante Foo\Bar\sousespacedenoms\FOO

/* nombre absoluto */
\Foo\Bar\foo(); // Se convierte en la función Foo\Bar\foo
\Foo\Bar\foo::methodestatique(); // Se convierte en la clase Foo\Bar\foo, método methodestatique
echo \Foo\Bar\FOO; // Se convierte en la constante Foo\Bar\FOO
     
    
```

Tenga en cuenta que para acceder a cualquier clase, función o constante global, puede utilizarse un nombre absoluto, como `\strlen` o `\Exception` o \\`INI_ALL`.

Acceso a clases, funciones y constantes globales desde un espacio de nombres

```php
     
<?php
namespace Foo;

function strlen() {}
const INI_ALL = 3;
class Exception {}

print \strlen('hi') . "\n"; // llama a la función global strlen
print \INI_ALL . "\n"; // acceso a una constante INI_ALL
$c = new \Exception('error'); // instancia la clase global Exception
print $c::class . "\n";
     
    
```

## Espacios de nombres y lenguaje dinámico

La implementación de espacios de nombres de PHP está influenciada por su naturaleza dinámica como lenguaje de programación. Por lo tanto, para convertir código como el del siguiente ejemplo en un espacio de nombres:

Acceso dinámico a elementos

example1.php:

```php
     
<?php
class classname
{
    function __construct()
    {
        echo __METHOD__,"\n";
    }
}
function funcname()
{
    echo __FUNCTION__,"\n";
}
const constname = "global";

$a = 'classname';
$obj = new $a; // muestra classname::__construct
$b = 'funcname';
$b(); // muestra funcname
echo constant('constname'), "\n"; // muestra global
    
    
```

Es necesario utilizar un nombre absoluto (el nombre de la clase, con su prefijo de espacio de nombres). Tenga en cuenta que no hay diferencia entre un nombre absoluto y un nombre calificado en un nombre de clase, función o constante dinámica, lo que hace que el backslash inicial no sea necesario.

Acceso dinámico a espacios de nombres

```php
     
<?php
namespace nomdelespacedenoms;
class classname
{
    function __construct()
    {
        echo __METHOD__,"\n";
    }
}
function funcname()
{
    echo __FUNCTION__,"\n";
}
const constname = "namespaced";

/* Tenga en cuenta que si utiliza comillas dobles, "\\nomdelespacedenoms\\classname" debe usarse */
$a = '\nomdelespacedenoms\classname';
$obj = new $a; // muestra nomdelespacedenoms\classname::__construct
$a = 'nomdelespacedenoms\classname';
$obj = new $a; // también muestra nomdelespacedenoms\classname::__construct
$b = 'nomdelespacedenoms\funcname';
$b(); // muestra nomdelespacedenoms\funcname
$b = '\nomdelespacedenoms\funcname';
$b(); // también muestra nomdelespacedenoms\funcname
echo constant('\nomdelespacedenoms\constname'), "\n"; // muestra namespaced
echo constant('nomdelespacedenoms\constname'), "\n"; // también muestra namespaced
    
    
```

Se recomienda leer la [nota sobre la protección de espacios de nombres en cadenas](#language.namespaces.faq.quote).

## El comando namespace y la constante \_\_NAMESPACE\_\_

PHP admite dos medios para acceder de manera abstracta a los elementos en el espacio de nombres actual, a saber, la constante mágica `__NAMESPACE__` y el comando `namespace`.

El valor de `__NAMESPACE__` es una cadena que contiene el nombre del espacio de nombres actual. En el espacio global, sin nombre, contiene una cadena vacía.

Ejemplo con \_\_NAMESPACE\_\_, en un código con espacio de nombres

```php
     
<?php
namespace MonProjet;

echo '"', __NAMESPACE__, '"'; // muestra "MonProjet"

    
```

Ejemplo con \_\_NAMESPACE\_\_, en un código con espacio de nombres global

```php
     
<?php
echo '"', __NAMESPACE__, '"'; // muestra ""

    
```

La constante `__NAMESPACE__` es útil para construir dinámicamente nombres, como:

Uso de \_\_NAMESPACE\_\_ para una construcción dinámica de nombres

```php
     
<?php
namespace MonProjet;

function get($classname)
{
    $a = __NAMESPACE__ . '\\' . $classname;
    return new $a;
}

    
```

El comando `namespace` también puede usarse para solicitar explícitamente un elemento del espacio de nombres actual, o de un subespacio. Es el equivalente para los espacios de nombres del operador `self` de las clases.

El operador namespace, en un espacio de nombres

```php
     
<?php
namespace MonProjet;

use blah\blah as mine; // Ver "Uso de espacios de nombres: alias e importación"

blah\mine(); // llama a la función MonProjet\blah\mine()
namespace\blah\mine(); // llama a la función MonProjet\blah\mine()

namespace\func(); // llama a la función MonProjet\func()
namespace\sub\func(); // llama a la función MonProjet\sub\func()
namespace\cname::method(); // llama al método estático "method" de la clase MonProjet\cname
$a = new namespace\sub\cname(); // instancia un objeto de la clase MonProjet\sub\cname
$b = namespace\CONSTANT; // asigna el valor de la constante MonProjet\CONSTANT a $b

    
```

El operador namespace, en el espacio de nombres global

```php
     
<?php

namespace\func(); // llama a la función func()
namespace\sub\func(); // llama a la función sub\func()
namespace\cname::method(); // llama al método estático "method" de la clase cname
$a = new namespace\sub\cname(); // instancia un objeto de la clase sub\cname
$b = namespace\CONSTANT; // asigna el valor de la constante CONSTANT a $b

    
```

## Uso de espacios de nombres: importación y alias

La capacidad de hacer referencia a un nombre absoluto con un alias o importando un espacio de nombres es estratégica. Es un beneficio similar a los enlaces simbólicos en un sistema de archivos.

PHP puede crear alias(/importar) constantes, funciones, clases, interfaces, traits, enumeraciones y espacios de nombres.

Un alias se crea con el operador `use`. Aquí hay un ejemplo que presenta los cinco tipos de importación:

Importación y alias con el operador use

```php
     
<?php
namespace foo;
use My\Full\Classname as Another;

// Esto es lo mismo que use My\Full\NSname as NSname
use My\Full\NSname;

// importación de una clase global
use ArrayObject;

// importación de una función
use function My\Full\functionName;

// alias de una función
use function My\Full\functionName as func;

// importación de una constante
use const My\Full\CONSTANT;

$obj = new namespace\Another; // instancia un objeto de la clase foo\Another
$obj = new Another; // instancia un objeto de la clase My\Full\Classname
NSname\subns\func(); // llama a la función My\Full\NSname\subns\func
$a = new ArrayObject(array(1)); // instancia un objeto de la clase ArrayObject
// Sin la instrucción "use ArrayObject" habríamos instanciado un objeto de la clase foo\ArrayObject
func(); // Llama a la función My\Full\functionName
echo CONSTANT; // muestra el valor de My\Full\CONSTANT

    
```

Tenga en cuenta que para los nombres con ruta (los nombres absolutos que contienen separadores de espacios, como `Foo\Bar`, en comparación con los nombres globales, como `FooBar`, que no los contienen), el backslash inicial no es necesario y no se recomienda, ya que los nombres importados deben ser absolutos y no se resuelven relativamente al espacio de nombres actual.

Además, PHP admite atajos prácticos, como las instrucciones use múltiples.

Importación y alias múltiples con el operador use

```php
     
<?php
use My\Full\Classname as Another, My\Full\NSname;

$obj = new Another; // instancia un objeto de la clase My\Full\Classname
NSname\subns\func(); // llama a la función My\Full\NSname\subns\func

    
```

La importación se realiza durante la compilación, por lo que no afecta a las clases, funciones y constantes dinámicas.

Importación y nombres de espacios dinámicos

```php
     
<?php
use My\Full\Classname as Another, My\Full\NSname;

$obj = new Another; // instancia un objeto de la clase My\Full\Classname
$a = 'Another';
$obj = new $a;      // instancia un objeto de la clase Another

    
```

Además, la importación solo afecta a los nombres sin calificación. Los nombres absolutos siguen siendo absolutos y no se modifican por una importación.

Importación y nombres de espacios absolutos

```php
     
<?php
use My\Full\Classname as Another, My\Full\NSname;

$obj = new Another; // instancia un objeto de la clase My\Full\Classname
$obj = new \Another; // instancia un objeto de la clase Another
$obj = new Another\untruc; // instancia un objeto de la clase My\Full\Classname\untruc
$obj = new \Another\untruc; // instancia un objeto de la clase Another\untruc

    
```

### Reglas de contexto para la importación

La palabra clave `use` debe declararse en el contexto más externo de un archivo (el contexto global) o en las declaraciones de espacio de nombres. Esto se debe a que la importación se realiza durante la compilación y no durante la ejecución, por lo que no se pueden apilar los contextos. El ejemplo siguiente muestra usos incorrectos de la palabra clave `use`:

Reglas de importación incorrectas

```php
<?php
namespace Languages;

function toGreenlandic
{
    use Languages\Danish;
    // ...
}

     
```

> [!NOTE]
> Las reglas de importación se basan en archivos, lo que significa que los archivos incluidos no heredarán *PAS* las reglas de importación del archivo padre.

### Declaración del grupo `use`

Las clases, funciones y constantes importadas desde el mismo [`namespace`](#language.namespaces.definition) pueden agruparse en una sola instrucción [`use`](#language.namespaces.importing).

```php
<?php

use some\namespace\ClassA;
use some\namespace\ClassB;
use some\namespace\ClassC as C;

use function some\namespace\fn_a;
use function some\namespace\fn_b;
use function some\namespace\fn_c;

use const some\namespace\ConstA;
use const some\namespace\ConstB;
use const some\namespace\ConstC;

// es equivalente a la siguiente declaración de grupo use
use some\namespace\{ClassA, ClassB, ClassC as C};
use function some\namespace\{fn_a, fn_b, fn_c};
use const some\namespace\{ConstA, ConstB, ConstC};

    
```

## Espacio de nombres global

Sin ninguna definición de espacio de nombres, todas las clases y las funciones se colocan en el espacio de nombres global: como en PHP antes de que los espacios de nombres fueran introducidos. Al prefijar un nombre con un backslash `\`, se puede solicitar el uso del espacio de nombres global, incluso en un contexto de espacio de nombres específico.

Especificación de espacio de nombres global

```php
     
<?php
namespace A\B\C;

/* Esta función es A\B\C\fopen */
function fopen() {
     /* ... */
     $f = \fopen(...); // llamada a fopen global
     return $f;
}
    
    
```

## Uso de espacios de nombres: retorno al espacio global para funciones y constantes

En un espacio de nombres, cuando PHP encuentra un nombre sin calificación, ya sea una clase, una función o una constante, lo resuelve con diferentes prioridades. Los nombres de clases siempre se resuelven con el espacio de nombres actual. Para acceder a clases internas o a clases que no están en un espacio de nombres, es necesario representarlas con su nombre absoluto, como:

Acceso a clases globales desde un espacio de nombres

```php
     
<?php
namespace A\B\C;
class Exception extends \Exception {}

$a = new Exception('hi'); // $a es un objeto de la clase A\B\C\Exception
var_dump($a::class);
$b = new \Exception('hi'); // $b es un objeto de la clase Exception
var_dump($b::class);

$c = new ArrayObject; // error fatal, clase A\B\C\ArrayObject no encontrada
    
    
```

Para las funciones y constantes, PHP las buscará en el espacio global si no puede encontrarlas en el espacio de nombres actual.

Acceso a funciones y constantes globales en un espacio de nombres

```php
     
<?php
namespace A\B\C;

const E_ERROR = 45;
function strlen($str)
{
    return \strlen($str) - 1;
}

echo E_ERROR, "\n"; // muestra "45"
echo INI_ALL, "\n"; // muestra "7": acceso al espacio de nombres global INI_ALL

echo strlen('hi'), "\n"; // muestra "1"
if (is_array('hi')) { // muestra "no es un array"
    echo "es un array\n";
} else {
    echo "no es un array\n";
}
    
    
```

## Reglas de resolución de nombres

En el contexto de las reglas de resolución, hay varias definiciones importantes:

nombre no calificado  
Esto es un identificador que no contiene un separador de espacio de nombres. Por ejemplo: `Foo`

nombre calificado  
Esto es un identificador que contiene un separador de espacio de nombres. Por ejemplo: `Foo\Bar`

Nombre absoluto  
Esto es un identificador que comienza con un separador de espacio de nombres. Por ejemplo: `\Foo\Bar`. El espacio de nombres `Foo` también es un nombre absoluto.

Nombre Relativo  
Es un identificador que comienza con `namespace`, como `namespace\Foo\Bar`.

Los nombres se resuelven siguiendo las siguientes reglas:

1.  Los nombres absolutos siempre se traducen a nombres sin el separador de namespace. Por ejemplo, `\A\B` se traduce a `A\B`.

2.  Todos los nombres que no son absolutos se traducen con `namespace` reemplazado por el namespace actual. Si el nombre aparece en el namespace global, el prefijo `namespace\` se elimina. Por ejemplo `namespace\A` en el namespace `X\Y` se traduce a `X\Y\A`. El mismo nombre en el namespace global se traduce a `A`.

3.  Para los nombres absolutos, el primer segmento se traduce de acuerdo con la clase/namespace de la tabla de importación. Por ejemplo, si el namespace `A\B\C` se importa como `C`, el nombre `C\D\E` se traduce a `A\B\C\D\E`.

4.  Para los nombres absolutos, si ninguna regla de importación se aplica, el namespace actual se prefiere al nombre. Por ejemplo, el nombre `C\D\E` en el namespace `A\B`, se traduce a `A\B\C\D\E`.

5.  Para los nombres absolutos, el nombre se traduce en relación con la tabla actual de importación para el tipo de símbolo respectivo. Esto significa que un nombre que se asemeja a una clase se traduce de acuerdo con la tabla de importación de class/namespace, los nombres de funciones utilizando la tabla de importación de funciones, y las constantes utilizando la tabla de importación de constantes. Por ejemplo, después `use A\B\C;` un uso como `new C()` corresponde al nombre `A\B\C()`. De manera similar, después de `use function A\B\foo;` un uso como `foo()` corresponde al nombre `A\B\foo`.

6.  Para los nombres relativos, si ninguna regla se aplica, y el nombre hace referencia a una clase, el namespace actual sirve como prefijo. Por ejemplo `new C()` en el namespace `A\B` corresponde al nombre `A\B\C`.

7.  Para los nombres relativos, si ninguna regla se aplica, y el nombre hace referencia a una función o constante, y el código está fuera del namespace global, el nombre se resuelve durante la ejecución. Supongamos que el código está en el namespace `A\B`, aquí es cómo se resuelve una llamada a la función `foo()`:

    1.  Busca una función en el espacio de nombres actual: `A\B\foo()`.

    2.  Intenta encontrar y llamar a la función *global* `foo()`.

Ejemplos de resolución de espacios de nombres

```php
<?php
namespace A;
use B\D, C\E as F;

// llamadas de funciones

foo();      // intenta llamar a la función "foo" en el espacio de nombres "A"
            // luego llama a la función global "foo"

\foo();     // llama a la función "foo" definida en el espacio de nombres global

my\foo();   // llama a la función "foo" definida en el espacio de nombres "A\my"

F();        // intenta llamar a la función "F" definida en el espacio "A"
            // luego intenta llamar a la función global "F"

// referencias de clases

new B();    // crea un objeto de la clase "B" definida en el espacio de nombres  "A"
            // si no se encuentra, intenta el autocargado en la clase "A\B"

new D();    // crea un objeto de la clase "D" definida en el espacio de nombres  "B"
            // si no se encuentra, intenta el autocargado en la clase "B\D"

new F();    // crea un objeto de la clase "E" definida en el espacio de nombres  "C"
            // si no se encuentra, intenta el autocargado en la clase "C\E"

new \B();   // crea un objeto de la clase "B" definida en el espacio de nombres global
            // si no se encuentra, intenta el autocargado en la clase "B"

new \D();   // crea un objeto de la clase "D" definida en el espacio de nombres global
            // si no se encuentra, intenta el autocargado en la clase "D"

new \F();   // crea un objeto de la clase "F" definida en el espacio de nombres global
            // si no se encuentra, intenta el autocargado en la clase "F"

// métodos estáticos y funciones de espacio de nombres de otro espacio

B\foo();    // llama a la función "foo" del espacio de nombres "A\B"

B::foo();   // llama al método "foo" de la clase "B" definida en el espacio de nombres  "A"
            // si la clase "A\B" no se encuentra, intenta el autocargado en la clase "A\B"

D::foo();   // llama al método "foo" de la clase "D" definida en el espacio de nombres  "B"
            // si la clase "B\D" no se encuentra, intenta el autocargado en la clase "B\D"

\B\foo();   // llama a la función "foo" del espacio de nombres "B"

\B::foo();  // llama al método "foo" de la clase "B" ubicada en el espacio de nombres global
            // si la clase "B" no se encuentra, intenta el autocargado en la clase "B"

// métodos estáticos y funciones de espacio de nombres del espacio actual

A\B::foo();   // llama al método "foo" de la clase "B" del espacio de nombres "A\A"
              // si la clase "A\A\B" no se encuentra, intenta el autocargado en la clase "A\A\B"

\A\B::foo();  // llama al método "foo" de la clase "B" del espacio de nombres "A"
              // si la clase "A\B" no se encuentra, intenta el autocargado en la clase "A\B"

   
```

## Preguntas frecuentes: lo que debe saber sobre espacios de nombres

Esta FAQ se divide en dos secciones: las preguntas comunes, y los puntos particulares de la implementación, que pueden ser útiles para la comprensión global.

Primero, las preguntas comunes.

1.  [Si no utilizo espacios de nombres, ¿debo preocuparme por ellos?](#language.namespaces.faq.shouldicare)

2.  [¿Cómo utilizar una clase global o interna desde un espacio de nombres?](#language.namespaces.faq.globalclass)

3.  [¿Cómo utilizar las clases de espacios de nombres, las funciones o las constantes en su propio espacio?](#language.namespaces.faq.innamespace)

4.  [ ¿Cómo se resuelve un nombre como `\mon\nom` o `\nom`? ](#language.namespaces.faq.full)

5.  [¿Cómo se resuelve un nombre como `mon\nom`?](#language.namespaces.faq.qualified)

6.  [¿Cómo se resuelve un nombre de clase sin calificación, como `nom`?](#language.namespaces.faq.shortname1)

7.  [¿Cómo se resuelve una función sin calificación o una constante de nombre `nom`?](#language.namespaces.faq.shortname2)

Aquí están los puntos particulares de la implementación, que pueden ser útiles para la comprensión global.

1.  [Los nombres importados no deben entrar en conflicto con las clases definidas en el mismo archivo](#language.namespaces.faq.conflict)

2.  [Los espacios de nombres anidados están prohibidos](#language.namespaces.faq.nested)

3.  [Los nombres de espacios de nombres dinámicos deben proteger el backslash](#language.namespaces.faq.quote)

4.  [Las constantes no definidas referenciadas con un backslash producen un error fatal](#language.namespaces.faq.constants)

5.  [Imposible reemplazar constantes especiales como `null`, `true` o `false`](#language.namespaces.faq.builtinconst)

### Si no utilizo espacios de nombres, ¿debo preocuparme por ellos?

No, los espacios de nombres no afectan el código existente, de una manera u otra, ni el código que se producirá y que no utiliza espacios de nombres. Puede escribir esto si lo desea:

Acceso a una clase global desde fuera de un espacio de nombres

```php
<?php
$a = new \stdClass;
print $a::class;

     
```

Es una funcionalidad equivalente a:

Acceder a clases globales fuera de un espacio de nombres

```php
<?php
$a = new stdClass;
print $a::class;

     
```

### ¿Cómo utilizar una clase global o interna desde un espacio de nombres?

Acceso a clases internas desde un espacio de nombres

```php
<?php
namespace foo;
$a = new \stdClass;
print $a::class . "\n";

function test(?\ArrayObject $parameter_type_example = null) {}

$a = \FilesystemIterator::CURRENT_AS_FILEINFO;
print $a . "\n";

// extensión de una clase interna o global
class MyException extends \Exception {}
print MyException::class . "\n";

     
```

### ¿Cómo utilizar las clases de espacios de nombres, las funciones o las constantes en su propio espacio?

Acceso a clases, funciones y constantes internas en un espacio de nombres

```php
<?php
namespace foo;

class MaClasse {}

// uso de una clase en el espacio de nombres actual, como tipo de parámetro
function test(?MaClasse $parameter_type_example = null) {}

// otra manera de usar una clase en el espacio de nombres actual como tipo de parámetro
function test2(?\foo\MaClasse $parameter_type_example = null) {}

// extensión de una clase en el espacio de nombres actual
class Extended extends MaClasse {}
print Extended::class . "\n";

// acceso a una función global
$a = \strlen("test");
print $a . "\n";

// acceso a una constante global
$b = \INI_ALL;
print $b . "\n";

     
```

### ¿Cómo se resuelve un nombre como `\mon\nom` o `\nom`?

Los nombres que comienzan con `\` siempre se resuelven como son, por lo que `\mon\nom` es en realidad `mon\nom`, y `\Exception` es `Exception`.

Nombres de espacios absolutos

```php
<?php
namespace foo;
$a = new \mon\nom(); // instancia la clase "mon\nom"
echo \strlen('hi'); // llama a la función "strlen"
$a = \INI_ALL; // $a recibe el valor de la constante "INI_ALL"

     
```

### ¿Cómo se resuelve un nombre como `mon\nom`?

Los nombres que contienen un backslash pero no comienzan con un backslash, como `mon\nom` pueden resolverse de dos maneras diferentes.

Si ha habido una instrucción de importación que hace un alias de `mon`, entonces el alias importado se aplica en lugar de `mon`, y el espacio de nombres se convierte en `mon\nom`.

De lo contrario, el espacio de nombres actual se agrega antes del camino de la clase `mon\nom`.

Nombres calificados

```php
<?php
namespace foo;
use blah\blah as foo;

$a = new mon\nom(); // instancia la clase "foo\mon\nom"
foo\bar::name(); // llama al método estático "name" en la clase "blah\blah\bar"
mon\bar(); // llama a la función "foo\mon\bar"
$a = mon\BAR; // asigna a $a el valor de la constante "foo\mon\BAR"

     
```

### ¿Cómo se resuelve un nombre de clase sin calificación, como `nom`?

Los nombres de clases que no contienen backslash como `nom` pueden resolverse de dos maneras diferentes.

Si hay una instrucción de importación que define un alias para `nom`, entonces se aplica el alias.

De lo contrario, se utiliza el espacio de nombres actual y se prefiere a `nom`.

Clases sin calificación

```php
<?php
namespace foo;
use blah\blah as foo;

$a = new nom(); // instancia la clase "foo\nom"
foo::nom(); // llama al método estático "nom" en la clase "blah\blah"

     
```

### ¿Cómo se resuelve una función sin calificación o una constante de nombre `nom`?

Las funciones y constantes que no tienen backslash en su nombre como `nom` se resuelven de dos maneras diferentes:

Primero, se prefiere el espacio de nombres actual a `nom`.

Luego, si la constante o función `nom` no existe en el espacio de nombres actual, se utiliza la versión global de la constante o la función `nom`.

Funciones y constantes sin espacio de nombres

```php
<?php
namespace foo;
use blah\blah as foo;

const FOO = 1;

function mon() {
    print __FUNCTION__ . "\n";
}
function foo() {
    print __FUNCTION__ . "\n";
}
function sort(&$a)
{
    \sort($a); // Llamada a la función global "sort"
    $a = array_flip($a);
    return $a;
}

mon(); // llama "foo\mon"
print strlen('hi') . "\n"; // llama a la función global "strlen" ya que "foo\strlen" no existe
$arr = array(1,3,2);
$b = sort($arr); // llama a la función "foo\sort"
var_dump($b);
foo(); // llama a la función "foo\foo": la importación no se aplica

$a = FOO; // asigna a $a el valor de la constante "foo\FOO": la importación no se aplica
print $a;
$b = INI_ALL; // asigna a $b el valor de la constante "INI_ALL"
print $b;

     
```

### Los nombres importados no deben entrar en conflicto con las clases definidas en el mismo archivo

La siguiente combinación de scripts es válida:

file1.php

```php
     
<?php
namespace mes\trucs;
class MaClasse {}
     
     
```

another.php

```php
     
<?php
namespace another;
class untruc {}
     
     
```

file2.php

```php
     
<?php
namespace mes\trucs;
include 'file1.php';
include 'another.php';

use another\untruc as MaClasse;
$a = new MaClasse; // instancia la clase "untruc" del espacio de nombres another
     
     
```

No hay conflicto de nombres, incluso si la clase `MaClasse` existe en el espacio de nombres `mes\trucs`, ya que la definición de MaClasse está en un archivo separado. Sin embargo, el siguiente ejemplo produce un error fatal debido a un conflicto de nombres, ya que MaClasse se define en el mismo archivo que la instrucción use.

```php
     
<?php
namespace mes\trucs;
use another\untruc as MaClasse;
class MaClasse {} // error fatal: MaClasse está en conflicto con la instrucción de importación
$a = new MaClasse;
     
     
```

### Los espacios de nombres anidados están prohibidos

PHP no permite anidar espacios de nombres.

```php
     
<?php
namespace mes\trucs {
    namespace nested {
        class foo {}
    }
}
     
     
```

Sin embargo, es fácil simular espacios de nombres anidados, como esto:

```php
     
<?php
namespace mes\trucs\nested {
    class foo {}
}
     
     
```

### Los nombres de espacios de nombres dinámicos deben proteger el backslash

Es muy importante darse cuenta de que, como los backslash se utilizan como caracteres de escape en las cadenas, siempre deben duplicarse para poder usarlos en una cadena. De lo contrario, existe el riesgo de uso inesperado:

Peligros de usar espacios de nombres en una cadena

```php
      
<?php
$a = "dangereux\nom"; // \n es una nueva línea en una cadena!
$obj = new $a;

$a = 'pas\vraiment\dangereux'; // ningún problema aquí
$obj = new $a;
      
     
```

En una cadena de comillas dobles, la secuencia de escape es mucho más segura de usar, pero aún se recomienda proteger siempre los backslashs en una cadena que contiene un espacio de nombres.

### Constantes no definidas referenciadas con un backslash producen un error fatal

Cualquier constante no definida que no tenga calificador como `FOO` producirá una advertencia: PHP asumía que `FOO` era el valor de la constante. Cualquier constante, calificada parcialmente o totalmente, que contenga un backslash, producirá un error fatal si no está definida.

Constantes no definidas

```php
      
<?php
namespace bar;
$a = FOO; // produce una advertencia: constante no definida "FOO", que toma el valor de "FOO";
$a = \FOO; // error fatal, constante de espacio de nombres no definida FOO
$a = Bar\FOO; // error fatal, constante de espacio de nombres no definida bar\Bar\FOO
$a = \Bar\FOO; // error fatal, constante de espacio de nombres no definida Bar\FOO
      
     
```

### Imposible reemplazar constantes especiales como `null`, `true` o `false`

Cualquier intento en un espacio de nombres de reemplazar las constantes nativas o especiales, produce un error fatal.

Constantes que no pueden ser redefinidas

```php
      
<?php
namespace bar;
const NULL = 0; // error fatal;
const true = 'stupid'; // aún otro error fatal;
// etc.
      
     
```
