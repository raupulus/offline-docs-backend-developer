---
title: include
source_url: https://www.php.net/manual/es/function.include.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/include.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: b8147b7f0
order: 2200
---

## include

La expresión de lenguaje `include` incluye y ejecuta el fichero especificado en argumento.

Esta documentación también se aplica a la instrucción de lenguaje `require`.

Los ficheros se incluyen siguiendo la ruta del fichero proporcionada; si no se proporciona ninguna, se verificará el [include_path](#ini.include-path). Si el fichero no se encuentra en el [include_path](#ini.include-path), `include` verificará en el directorio del script llamador y en el directorio de trabajo actual antes de fallar. La instrucción `include` emitirá `E_WARNING` si no puede encontrar el fichero; este comportamiento es diferente de `require`, que emitirá `E_ERROR`.

Tenga en cuenta que `include` y `require` lanzarán errores de tipo `E_WARNING`, si el fichero no es accesible, antes de lanzar un error de tipo `E_WARNING` o `E_ERROR`, respectivamente.

Si se define una ruta, absoluta (comenzando con una letra de unidad seguida de `\` para Windows, o `/` para Unix/Linux) o relativa (comenzando con `.` o `..`), el [include_path](#ini.include-path) será ignorado. Por ejemplo, si un nombre de fichero comienza con `../`, PHP buscará en el directorio padre para encontrar el fichero especificado.

Para más información sobre cómo PHP maneja los ficheros incluidos así como la ruta de inclusión, consulte la documentación relativa al [include_path](#ini.include-path).

Cuando un fichero es incluido, el código que lo compone hereda el [ámbito de las variables](#language.variables.scope) de la línea donde aparece la inclusión. Todas las variables disponibles en esa línea en el fichero llamador estarán disponibles en el fichero llamado, a partir de ese punto. Sin embargo, todas las funciones y clases definidas en el fichero incluido tienen un ámbito global.

Ejemplo con `include`

```php
vars.php
<?php

$color = 'verde';
$fruit = 'manzana';

?>

test.php
<?php

echo "Una $fruit $color"; // Una

include 'vars.php';

echo "Una $fruit $color"; // Una manzana verde

?>

   
```

Si la inclusión ocurre dentro de una función, el código incluido será considerado como parte de la función. Esto modifica el contexto de las variables accesibles. Una excepción a esta regla: las [constantes mágicas](#language.constants.magic) son analizadas por el analizador antes de que la inclusión ocurra.

Inclusión de ficheros dentro de una función

```php
<?php

function foo()
{
    global $couleur;

    include 'vars.php';

    echo "Una $fruit $couleur";
}

/* vars.php está en el contexto de foo()
 * por lo tanto $fruit no está disponible fuera de
 * esta función. $couleur sí lo está, ya que es
 * una variable global */

foo();                      // Una pomme verte
echo "Una $fruit $couleur"; // Una  verte

?>

   
```

Es importante señalar que cuando un fichero es incluido, los errores de análisis aparecerán en HTML al principio del fichero, y el análisis del fichero padre no será interrumpido. Por esta razón, el código que está en el fichero debe ser colocado entre [las etiquetas habituales de PHP](#language.basic-syntax.phpmode).

Si los [gestores de inclusión de URL](#ini.allow-url-include) están activados en PHP, puede localizar el fichero con una URL (vía HTTP o bien con un gestor adecuado: ver [???](#wrappers) para una lista de protocolos), en lugar de una simple ruta local. Si el servidor remoto interpreta el fichero como código PHP, variables pueden ser transmitidas al servidor remoto vía la URL y el método GET. Esto no es, estrictamente hablando, lo mismo que heredar el contexto de variable. El fichero incluido es en realidad un script ejecutado a distancia, y su resultado es incluido en el código actual.

Utilizar la instrucción `include` vía HTTP

```php
<?php

/* Este ejemplo supone que www.example.com está configurado para tratar
 * los ficheros .php y no los ficheros .txt. Además,
 * 'Work' significa aquí que las variables
 * $foo y $bar están disponibles en el fichero incluido
 */

// No funciona: file.txt no ha sido tratado por www.example.com como PHP
include 'http://www.example.com/file.txt?foo=1&bar=2';

// No funciona: el script busca un fichero llamado
// 'file.php?foo=1&bar=2' en el sistema local
include 'file.php?foo=1&bar=2';

// Funciona
include 'http://www.example.com/file.php?foo=1&bar=2';
?>

   
```

> [!WARNING]
> Un fichero remoto puede ser tratado en el servidor remoto (dependiendo de la extensión del fichero y si el servidor remoto ejecuta PHP o no) pero debe producir siempre un script PHP válido porque será tratado en el servidor local. Si el fichero del servidor remoto debe ser tratado en el lugar y mostrado solamente, `readfile` es una función mucho más apropiada. De otra manera, debería tener cuidado de asegurar el script remoto para que produzca un código válido y deseado.

Ver también [trabajar con ficheros remotos](#features.remote-files), `fopen` y `file` para información relacionada.

Manejo del retorno: `include` devuelve `false` en caso de error y emite un aviso. Las inclusiones exitosas, incluyendo si son sobrescritas por el fichero incluido, devuelven `1`. Es posible ejecutar la estructura de lenguaje `return` dentro de un fichero incluido para determinar el proceso en ese fichero, y volver al script que lo llamó. Además, es posible devolver valores desde ficheros incluidos. Puede tomar el valor desde la llamada al fichero incluido como desee desde una función normal. Esto no es posible, sin embargo, al incluir ficheros remotos, y esto, mientras la salida del fichero remoto no tenga [etiquetas PHP de inicio y fin válidas](#language.basic-syntax.phpmode) (al igual que para los ficheros locales). Puede declarar las variables necesarias dentro de estas etiquetas y serán introducidas en el lugar donde el fichero fue incluido.

Como `include` es una estructura de lenguaje particular, los paréntesis no son necesarios alrededor del argumento. Tenga cuidado al comparar el valor devuelto.

Comparación del valor devuelto de una inclusión

```php
<?php
// No funciona, evaluado como include(('vars.php') == TRUE), es decir include('1')
if (include('vars.php') == TRUE) {
    echo 'OK';
}

// Funciona
if ((include 'vars.php') == TRUE) {
    echo 'OK';
}
?>

   
```

`include` y `return`

```php
return.php
<?php

$var = 'PHP';

return $var;

?>

noreturn.php
<?php

$var = 'PHP';

?>

testreturns.php
<?php

$foo = include 'return.php';

echo $foo; // muestra 'PHP'

$bar = include 'noreturn.php';

echo $bar; // muestra 1

?>

   
```

`$bar` tiene el valor de `1` ya que la inclusión fue exitosa. Tenga en cuenta la diferencia entre los dos ejemplos anteriores. El primero utiliza el comando `return` en el fichero incluido, mientras que el segundo no lo hace. Si el fichero no puede ser incluido, `false` es devuelto y un error de nivel `E_WARNING` es enviado.

Si hay funciones definidas en el fichero incluido, pueden ser utilizadas en el fichero principal si están antes del `return` o después. Si el fichero es incluido dos veces, PHP emitirá un error fatal ya que las funciones ya han sido declaradas. Se recomienda utilizar `include_once` en lugar de verificar si el fichero ya ha sido incluido y por lo tanto devolver condicionalmente la inclusión del fichero.

Otra forma de incluir un fichero PHP en una variable es capturar la salida utilizando las funciones de [control de salida](#ref.outcontrol) con `include`. Por ejemplo:

Uso del buffer de salida para incluir un fichero PHP en una cadena

```php
<?php
$string = get_include_contents('somefile.php');

function get_include_contents($filename) {
    if (is_file($filename)) {
        ob_start();
        include $filename;
        return ob_get_clean();
    }
    return false;
}

?>

   
```

Para incluir automáticamente ficheros en sus scripts, vea también las opciones de configuración [auto_prepend_file](#ini.auto-prepend-file) y [auto_append_file](#ini.auto-append-file) del `php.ini`.

> [!NOTE]
> Como esto es una estructura del lenguaje, y no una función, no es posible llamarla con las [funciones variables](#functions.variable-functions) o [argumentos nombrados](#functions.named-arguments).

Ver también `require`, `require_once`, `include_once`, `get_included_files`, `readfile`, `virtual`, y [include_path](#ini.include-path).
