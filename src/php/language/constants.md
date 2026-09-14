---
title: Constantes
source_url: https://www.php.net/manual/es/language.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 6e885e524
order: 1980
---

## Constantes

Una constante es un identificador (nombre) para un valor simple. Como su nombre sugiere, ese valor no puede cambiar durante la ejecución del script (excepto las [ constantes mágicas](#language.constants.magic), que en realidad no son constantes). Las constantes distinguen entre mayúsculas y minúsculas. Por convención, los identificadores de constantes se escriben siempre en mayúsculas.

> [!NOTE]
> Antes de PHP 8.0.0, las constantes definidas con la función `define` podían no distinguir entre mayúsculas y minúsculas.

El nombre de una constante sigue las mismas reglas que cualquier etiqueta en PHP. Un nombre de constante válido comienza con una letra o guion bajo, seguido de cualquier cantidad de letras, números o guiones bajos. Como expresión regular, se expresaría así: `^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$`

Es posible definir constantes con `define` usando nombres reservados o incluso inválidos, cuyo valor solo puede obtenerse con la función `constant`. Sin embargo, no se recomienda hacerlo.

> [!TIP]
> Véase también [???](#userlandnaming).

Nombres de constantes válidos e inválidos

```php
<?php

// Nombres de constantes válidos
define("FOO",     "something");
define("FOO2",    "something else");
define("FOO_BAR", "something more");

// Nombres de constantes inválidos
define("2FOO",    "something");

// Esto es válido, pero debe evitarse:
// PHP podría algún día proporcionar una constante mágica
// que rompa el script
define("__FOO__", "something");

    
```

> [!NOTE]
> Para estos propósitos, una letra es a-z, A-Z y los caracteres ASCII del 128 al 255 (0x80-0xff).

Al igual que las [superglobals](#language.variables.predefined), el ámbito de una constante es global. Las constantes pueden ser accedidas desde cualquier lugar del script sin importar el ámbito. Para más información sobre el ámbito, consulte la sección del manual sobre [ámbito de las variables](#language.variables.scope).

> [!NOTE]
> A partir de PHP 7.1.0, las constantes de clase pueden declarar una visibilidad protected o private, haciéndolas disponibles únicamente en el ámbito jerárquico de la clase en la que se definen.

## Sintaxis

Las constantes pueden definirse usando la palabra clave `const` o usando la función `define`. Mientras que `define` permite definir una constante con una expresión arbitraria, la palabra clave `const` tiene restricciones como se describe en el siguiente párrafo. Una vez definida, una constante no puede ser modificada ni eliminada.

Al usar la palabra clave `const`, solo se aceptan expresiones escalares (`bool`, `int`, `float` y `string`) y `array`s constantes que contengan únicamente expresiones escalares. Es posible definir constantes como `resource`, pero debe evitarse, ya que puede causar resultados inesperados.

El valor de una constante se obtiene simplemente especificando su nombre. A diferencia de las variables, una constante *no* va precedida de un signo `$`. También es posible usar la función `constant` para leer el valor de una constante si su nombre se obtiene dinámicamente. Use `get_defined_constants` para obtener una lista de todas las constantes definidas.

> [!NOTE]
> Las constantes y las variables (globales) se encuentran en espacios de nombres diferentes. Esto implica que, por ejemplo, `true` y `$TRUE` son generalmente diferentes.

Si se usa una constante no definida, se lanza un `Error`. Antes de PHP 8.0.0, las constantes no definidas se interpretaban como una cadena (`string`) sin comillas, es decir (CONSTANT vs "CONSTANT"). Este comportamiento está obsoleto desde PHP 7.2.0, y se emite un error de nivel `E_WARNING` cuando ocurre. Antes de PHP 7.2.0, se emitía un error de nivel [E_NOTICE](#ref.errorfunc). Consulte también la entrada del manual sobre por qué [\$foo\[bar\]](#language.types.array.foo-bar) es incorrecto (a menos que `bar` sea una constante). Esto no se aplica a las [constantes (totalmente) cualificadas](#language.namespaces.rules), que siempre lanzarán un `Error` si no están definidas.

> [!NOTE]
> Para comprobar si una constante está definida, use la función `defined`.

Estas son las diferencias entre constantes y variables:

- Las constantes no llevan el signo de dólar (`$`) delante;

- Las constantes pueden definirse y accederse desde cualquier lugar sin importar las reglas de ámbito de las variables;

- Las constantes no pueden redefinirse ni eliminarse una vez establecidas; y

- Las constantes solo pueden evaluarse a valores escalares o arrays.

Definición de constantes

```php
<?php
define("CONSTANT", "Hello world.");
echo CONSTANT; // muestra "Hello world."
echo Constant; // Lanza un Error: Undefined constant "Constant"
               // Antes de PHP 8.0.0, muestra "Constant" y emite una advertencia.

     
```

Definición de constantes usando la palabra clave `const`

```php
<?php
// Valor escalar simple
const CONSTANT = 'Hello World';

echo CONSTANT . "\n";

// Expresión escalar
const ANOTHER_CONST = CONSTANT . '; Goodbye World';
echo ANOTHER_CONST . "\n";

const ANIMALS = array('dog', 'cat', 'bird');
echo ANIMALS[1] . "\n"; // muestra "cat"

// Arrays constantes
define('ANIMALS_DEF', array(
    'dog',
    'cat',
    'bird'
));
echo ANIMALS_DEF[1] . "\n"; // muestra "cat"

     
```

> [!NOTE]
> A diferencia de la definición de constantes con `define`, las constantes definidas con la palabra clave `const` deben declararse en el ámbito de nivel superior porque se definen en tiempo de compilación. Esto significa que no pueden declararse dentro de funciones, bucles, instrucciones `if` o bloques `try`/`catch`.

### Véase también

[Constantes de clase](#language.oop5.constants)

## Constantes predefinidas

PHP proporciona un gran número de [constantes predefinidas](#reserved.constants) a cualquier script que ejecuta. Muchas de estas constantes, sin embargo, son creadas por diversas extensiones, y solo estarán presentes cuando esas extensiones estén disponibles, ya sea mediante carga dinámica o porque se han compilado con PHP.

## Constantes mágicas

Existen varias constantes mágicas que cambian dependiendo de dónde se utilicen. Por ejemplo, el valor de `__LINE__` depende de la línea en la que se use en el script. Todas estas constantes "mágicas" se resuelven en tiempo de compilación, a diferencia de las constantes regulares, que se resuelven en tiempo de ejecución. Estas constantes especiales no distinguen entre mayúsculas y minúsculas y son las siguientes:

| Nombre | Descripción |
|----|----|
| `__LINE__` | El número de línea actual del archivo. |
| `__FILE__` | La ruta completa y el nombre del archivo con los enlaces simbólicos resueltos. Si se usa dentro de un include, se devuelve el nombre del archivo incluido. |
| `__DIR__` | El directorio del archivo. Si se usa dentro de un include, se devuelve el directorio del archivo incluido. Es equivalente a `dirname(__FILE__)`. El nombre del directorio no incluye la barra final a menos que sea el directorio raíz. |
| `__FUNCTION__` | El nombre de la función, o `{closure}` para las funciones anónimas. |
| `__CLASS__` | El nombre de la clase. El nombre de la clase incluye el espacio de nombres en el que fue declarada (p. ej. `Foo\Bar`). Cuando se usa en un método de trait, `__CLASS__` es el nombre de la clase en la que se utiliza el trait. |
| `__TRAIT__` | El nombre del trait. El nombre del trait incluye el espacio de nombres en el que fue declarado (p. ej. `Foo\Bar`). |
| `__METHOD__` | El nombre del método de la clase. |
| `__PROPERTY__` | Solo es válido dentro de un [hook de propiedad](#language.oop5.property-hooks). Es igual al nombre de la propiedad. |
| `__NAMESPACE__` | El nombre del espacio de nombres actual. |
| `ClassName::class` | El nombre completo cualificado de la clase. |

Constantes mágicas de PHP

### Véase también

[::class](#language.oop5.basic.class.class), `get_class`, `get_object_vars`, `file_exists`, `function_exists`
