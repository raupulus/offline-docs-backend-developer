---
title: Recolección de basura (Garbage Collection)
source_url: https://www.php.net/manual/es/features.gc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: features/gc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: features
translation_status: ready
translation_revision: 23e84882d
order: 1570
---

## Recolección de basura (Garbage Collection)

Esta sección explica los méritos del nuevo mecanismo de recolección de basura (también llamado GC, del término inglés Garbage Collection) disponible a partir de PHP 5.3.

## Bases sobre el conteo de referencias

Una variable PHP se almacena internamente en un contenedor llamado "zval". Un contenedor zval contiene, además del tipo de la variable y su valor, dos informaciones adicionales. La primera se llama "is_ref" y es un valor booléano que indica si una variable forma parte de una referencia o no. Gracias a esta información, el motor de PHP sabe diferenciar las variables normales de las referencias. Como PHP permite al programador utilizar referencias, mediante el operador &, un contenedor zval posee también un mecanismo de conteo de referencias para optimizar el uso de la memoria. Esta segunda información, llamada "refcount", contiene el número de variables (también llamadas símbolos) que apuntan a este contenedor zval. Todos los símbolos se almacenan en una tabla de símbolos, y hay una tabla por ámbito de visibilidad (scope). Hay un ámbito global para el script principal (el que se llama, por ejemplo, a través del navegador) y un ámbito por función o método.

Un contenedor zval se crea cuando se crea una nueva variable con un valor constante, como por ejemplo:

Creación de un nuevo contenedor zval

```php
<?php
$a = "new string";
?>

     
```

En este caso, el nuevo símbolo `a` se crea en el ámbito global, y se crea un nuevo contenedor con el tipo `string` y el valor `new string`. El bit "is_ref" se establece por omisión en `false` ya que ninguna referencia ha sido creada por el programador. El contador de referencias "refcount" se establece en `1` ya que solo hay un símbolo que utiliza este contenedor. Es de destacar que las referencias (es decir, "is_ref" es `true`) con "refcount" `1`, se tratan como si no fueran referencias (es decir, como si "is_ref" fuera `false`). Si ha instalado [Xdebug](http://xdebug.org/), puede mostrar esta información llamando a `xdebug_debug_zval`.

Mostrar información zval

```php
<?php
$a = "new string";
xdebug_debug_zval('a');
?>

     
```

El ejemplo anterior mostrará:

    a: (refcount=1, is_ref=0)='new string'

Asignar esta variable a otro símbolo incrementará el refcount.

Incrementar el refcount de una zval

```php
<?php
$a = "new string";
$b = $a;
xdebug_debug_zval( 'a' );
?>

     
```

El ejemplo anterior mostrará:

    a: (refcount=2, is_ref=0)='new string'

El refcount vale `2` aquí, ya que el mismo contenedor está ligado tanto a `a` como a `b`. PHP es lo suficientemente inteligente como para no duplicar el contenedor cuando no es necesario. Los contenedores se destruyen cuando su "refcount" llega a cero. El "refcount" se decrementa en uno cuando cualquier símbolo ligado a un contenedor sale del ámbito (por ejemplo: cuando la función termina) o cuando un símbolo se desasigna (por ejemplo: por la llamada a `unset`). El siguiente ejemplo lo demuestra:

Decrementar el refcount de una zval

```php
<?php
$a = "new string";
$c = $b = $a;
xdebug_debug_zval( 'a' );
$b = 42;
xdebug_debug_zval( 'a' );
unset( $c );
xdebug_debug_zval( 'a' );
?>

     
```

El ejemplo anterior mostrará:

    a: (refcount=3, is_ref=0)='new string'
    a: (refcount=2, is_ref=0)='new string'
    a: (refcount=1, is_ref=0)='new string'

Si ahora se llama a `unset($a);`, el contenedor zval, incluyendo el tipo y el valor, será eliminado de la memoria.

### Tipos compuestos

Las cosas se complican en el caso de tipos compuestos como `array` y `object`. A diferencia de los valores escalares, los `array` y `object` almacenan sus propiedades en una tabla de símbolos que les es propia. Esto significa que el siguiente ejemplo crea tres contenedores zval:

Creación de una zval `array`

```php
<?php
$a = array( 'meaning' => 'life', 'number' => 42 );
xdebug_debug_zval( 'a' );
?>

      
```

Resultado del ejemplo anterior es similar a:

    a: (refcount=1, is_ref=0)=array (
       'meaning' => (refcount=1, is_ref=0)='life',
       'number' => (refcount=1, is_ref=0)=42
    )

          

O gráficamente

![Zvals de un array simple](en/features/figures/simple-array.png)

Los tres contenedores zval son: `a`, `meaning`, y `number`. Las mismas reglas se aplican para el incremento y la decrementación de los "refcounts". A continuación, se añade otro elemento al array, y se asigna su valor con el contenido de un elemento ya existente del array:

Añadir un elemento ya existente al array

```php
<?php
$a = array( 'meaning' => 'life', 'number' => 42 );
$a['life'] = $a['meaning'];
xdebug_debug_zval( 'a' );
?>

      
```

Resultado del ejemplo anterior es similar a:

    a: (refcount=1, is_ref=0)=array (
       'meaning' => (refcount=2, is_ref=0)='life',
       'number' => (refcount=1, is_ref=0)=42,
       'life' => (refcount=2, is_ref=0)='life'
    )

          

O gráficamente

![Zvals para un array simple con una referencia](en/features/figures/simple-array2.png)

La salida Xdebug que vemos indica que el antiguo y el nuevo elemento del array apuntan ahora ambos a un contenedor zval cuyo "refcount" vale `2`. Aunque la salida XDebug muestra dos contenedores zval con el valor 'life', son los mismos. La función `xdebug_debug_zval` no muestra esto, pero se podría ver mostrando también el puntero de memoria.

Eliminar un elemento del array es asimilable a la eliminación de un símbolo desde un espacio. Al hacerlo, el "refcount" del contenedor al que apunta el elemento del array se decrementa. Una vez más, si llega a cero, el contenedor zval se elimina de la memoria. El siguiente ejemplo lo demuestra:

Eliminación de un elemento de array

```php
<?php
$a = array( 'meaning' => 'life', 'number' => 42 );
$a['life'] = $a['meaning'];
unset( $a['meaning'], $a['number'] );
xdebug_debug_zval( 'a' );
?>

      
```

Resultado del ejemplo anterior es similar a:

    a: (refcount=1, is_ref=0)=array (
       'life' => (refcount=1, is_ref=0)='life'
    )

Ahora, las cosas se vuelven interesantes si añadimos el array como elemento de sí mismo. Hacemos esto en el siguiente ejemplo, utilizando un operador de referencia para evitar que PHP cree una copia:

Añadir el array como referencia a sí mismo como elemento

```php
<?php
$a = array( 'one' );
$a[] =& $a;
xdebug_debug_zval( 'a' );
?>

      
```

Resultado del ejemplo anterior es similar a:

    a: (refcount=2, is_ref=1)=array (
       0 => (refcount=1, is_ref=0)='one',
       1 => (refcount=2, is_ref=1)=...
    )

          

O gráficamente

![Zvals en un array con referencia circular](en/features/figures/loop-array.png)

Se puede ver que la variable array (`a`) así como el segundo elemento (`1`) apuntan ahora a un contenedor cuyo "refcount" vale `2`. Los "..." en la visualización indican una recursión, que, en este caso, significa que el "..." apunta al array mismo.

Como antes, eliminar una variable elimina su símbolo, y el refcount del contenedor al que apuntaba se decrementa. Por lo tanto, si eliminamos la variable `$a` después de ejecutar el código anterior, el contador de referencias del contenedor al que apuntan `$a` y el elemento "1" se decrementará en uno, pasando de "2" a "1". Esto se puede representar como:

Eliminación de `$a`

    (refcount=1, is_ref=1)=array (
       0 => (refcount=1, is_ref=0)='one',
       1 => (refcount=1, is_ref=1)=...
    )

          

O gráficamente

![Zvals después de la eliminación del array que contiene una referencia circular, fuga de memoria](en/features/figures/leak-array.png)

### Problemas de limpieza

Aunque ya no haya ningún símbolo en el espacio de variables actual que apunte a esta estructura, no puede ser limpiada, ya que el elemento "1" del array sigue apuntando a este mismo array. Como ya no hay ningún símbolo externo que apunte a esta estructura, el usuario no puede limpiarla manualmente; por lo tanto, hay una fuga de memoria. Afortunadamente, PHP destruirá esta estructura al final de la solicitud, pero antes de esta etapa, la memoria no se libera. Esta situación ocurre a menudo si se implementa un algoritmo de análisis u otras ideas donde se tiene un hijo que apunta a su padre. Lo mismo puede ocurrir, por supuesto, con los objetos, y es incluso más probable, ya que siempre se utilizan implícitamente por "[referencia](#language.oop5.references)".

Esto puede no ser molesto si ocurre solo una o dos veces, pero si hay miles, o incluso millones, de estas fugas de memoria, entonces obviamente esto puede convertirse en un problema importante. Esto es particularmente problemático para los scripts que duran mucho tiempo, como los demonios para los cuales la solicitud nunca termina, o incluso en grandes suites de pruebas unitarias. Este último caso se encontró al lanzar las pruebas unitarias del componente Template de la biblioteca eZ Components. En algunos casos, la suite de pruebas requería más de 2Go de memoria, que el servidor de prueba no tenía realmente disponible.

## Limpieza de Ciclos

Tradicionalmente, los mecanismos de conteo de referencias, como los utilizados anteriormente en PHP, no saben manejar las fugas de memoria debidas a referencias circulares; sin embargo, desde PHP 5.3.0, un algoritmo síncrono derivado del análisis [Concurrent Cycle Collection in Reference Counted Systems](https://pages.cs.wisc.edu/~cymen/misc/interests/Bacon01Concurrent.pdf) se utiliza para abordar este problema en particular.

Una explicación completa del funcionamiento del algoritmo iría un poco más allá del alcance de esta sección, pero aquí presentaremos los principios básicos. En primer lugar, estableceremos algunas reglas básicas. Si un refcount se incrementa, el contenedor siempre se utiliza, por lo tanto, no se limpia. Si el refcount se decrementa y llega a cero, el contenedor zval puede ser eliminado y la memoria liberada. En primer lugar, esto significa que los ciclos perturbadores solo pueden crearse cuando el refcount se decrementa a un valor diferente de cero. Luego, en un ciclo problemático, es posible detectar la basura verificando si es posible o no decrementar su refcount en uno, verificando luego qué zvals tienen un refcount a cero.

![Algoritmo de recolección de basura](en/features/figures/gc-algorithm.png)

Para evitar tener que llamar a la rutina de limpieza en cada decrementación de refcount posible, el algoritmo coloca todas las raíces zval en un "búfer de raíces" (marcándolas en "violeta"). También se asegura de que cada raíz aparezca solo una vez en el búfer. El mecanismo de limpieza solo interviene cuando el búfer está lleno. Vea el paso A en la figura anterior.

En el paso B, el algoritmo lanza una búsqueda en todas las raíces posibles, para decrementar en una unidad los refcounts de todas las zvals que encuentra, teniendo mucho cuidado de no decrementar dos veces el refcount de la misma zval (marcándolas como "grises"). En el paso C, el algoritmo relanza una búsqueda en todas las raíces posibles y escanea el valor de refcount de cada zval. Si encuentra un refcount a cero, la zval se marca como "blanca" (azul en la figura). Si encuentra un valor superior a cero, cancela la decrementación del refcount realizando una búsqueda desde este nodo, y las marca como "negras" nuevamente. En el último paso, D, el algoritmo recorre todo el búfer de raíces y las elimina, escaneando cada zval; cualquier zval marcada como "blanca" en el paso anterior será entonces eliminada de la memoria.

Ahora que se sabe globalmente cómo funciona el algoritmo, se verá cómo se ha integrado en PHP. Por omisión, el recolector de basura de PHP está activado. Sin embargo, hay una opción de `php.ini` para cambiar esto: [zend.enable_gc](#ini.zend.enable-gc).

Cuando el recolector de basura está activado, el algoritmo de búsqueda de ciclos descrito anteriormente se ejecuta cada vez que el búfer está lleno. El búfer de raíces tiene un tamaño fijado a 10.000 raíces (este parámetro es modificable gracias a `GC_THRESHOLD_DEFAULT` en `Zend/zend_gc.c` en el código fuente de PHP, por lo tanto, se necesita una recompilación). Si el recolector de basura está desactivado, la búsqueda de ciclos también lo está. Sin embargo, las raíces posibles siempre se registrarán en el búfer, esto no depende de la activación del recolector de basura.

Si el búfer está lleno mientras el mecanismo de limpieza está desactivado, las raíces ya no se registrarán. Estas raíces nunca serán analizadas por el algoritmo, y si formaban parte de referencias circulares, nunca se limpiarán, y causarán fugas de memoria.

La razón por la que las raíces posibles se registran en el búfer incluso si el mecanismo está desactivado es que habría sido demasiado costoso verificar la posible activación del mecanismo en cada intento de agregar una raíz al búfer. El mecanismo de recolección de basura y análisis puede, por su parte, ser muy costoso en tiempo.

Además de poder cambiar el valor del parámetro de configuración [zend.enable_gc](#ini.zend.enable-gc), también se puede activar o desactivar el mecanismo de recolección de basura llamando a las funciones `gc_enable` o `gc_disable` respectivamente. Utilizar estas funciones tendrá el mismo efecto que modificar el parámetro de configuración. También se tiene la posibilidad de forzar la ejecución del recolector de basura en un momento dado en el script, incluso si el búfer aún no está completamente lleno. Para ello, utilice la función `gc_collect_cycles`, que devolverá el número de ciclos recolectados.

Se puede tomar el control desactivando el recolector de basura o forzándolo a pasar en un momento dado porque algunas partes de la aplicación podrían depender fuertemente del tiempo de procesamiento, en cuyo caso se podría desear que el recolector de basura no se inicie. Por supuesto, al desactivar el recolector de basura para algunas partes de la aplicación, se corre el riesgo de crear fugas de memoria, ya que algunas raíces probables podrían no registrarse en el búfer de memoria de tamaño limitado. En consecuencia, generalmente se recomienda desencadenar manualmente el proceso gracias a `gc_collect_cycles` justo antes de la llamada a `gc_disable`, para liberar memoria. Esto dejará un búfer vacío, y habrá más espacio para raíces probables cuando el mecanismo esté desactivado.

## Consideraciones sobre el rendimiento

Ya se ha visto en las secciones anteriores que la recolección de raíces probables tenía un impacto muy ligero en el rendimiento, pero esto es en comparación con PHP 5.2 a PHP 5.3. Aunque el registro de raíces probables es más lento que no registrarlas en absoluto, como en PHP 5.2, otras mejoras aportadas por PHP 5.3 hacen que esta operación no se sienta a nivel de rendimiento.

Hay principalmente dos niveles para los cuales se afecta el rendimiento. El primero es la huella de memoria reducida, y el segundo es el retraso en la ejecución, cuando el mecanismo de limpieza realiza su operación de liberación de memoria. Se estudiarán estos dos ejes.

### Huella de memoria reducida

En primer lugar, la razón principal de la implementación del mecanismo de recolección de basura es la reducción de la memoria consumida, limpiando las referencias circulares cuando se cumplen las condiciones requeridas. Con PHP, esto ocurre tan pronto como el búfer de raíces está lleno, o cuando se llama a la función `gc_collect_cycles`. En el gráfico a continuación, se muestra el uso de memoria del siguiente script, con PHP 5.2 y con PHP 5.3, excluyendo la memoria obligatoria que PHP consume por sí mismo al inicio.

Ejemplo de uso de memoria

```php
<?php
class Foo
{
    public $var = '3.14159265359';
    public $self;
}

$baseMemory = memory_get_usage();

for ( $i = 0; $i <= 100000; $i++ )
{
    $a = new Foo;
    $a->self = $a;
    if ( $i % 500 === 0 )
    {
        echo sprintf( '%8d: ', $i ), memory_get_usage() - $baseMemory, "\n";
    }
}
?>

      
```

![Comparación del consumo de memoria entre PHP 5.2 y PHP 5.3](en/features/figures/gc-benchmark.png)

En este ejemplo algo académico, se crea un objeto que tiene un atributo que se referencia a sí mismo. Cuando la variable `$a` en el script se reasigna a la siguiente iteración, aparecerá una fuga de memoria. En este caso, los dos contenedores zval se fugan (el zval del objeto y el del atributo), pero solo se encuentra una raíz probable: la variable que ha sido eliminada. Cuando el búfer de raíces está lleno después de 10.000 iteraciones (con un total de 10.000 raíces probables), el mecanismo de recolección de basura entra en juego y libera la memoria asociada a estas raíces probables. Esto se ve muy claramente en los gráficos de uso de memoria de PHP 5.3. Después de cada 10.000 iteraciones, el mecanismo se desencadena y libera la memoria asociada a las variables circularmente referenciadas. El mecanismo en cuestión no tiene mucho trabajo en este ejemplo, porque la estructura que se fugó es extremadamente simple. El diagrma muestra que el uso máximo de memoria de PHP 5.3 es de aproximadamente 9Mo, mientras que sigue aumentando con PHP 5.2.

### Ralentizaciones durante la ejecución

El segundo punto donde el mecanismo de recolección de basura (GC) afecta el rendimiento es cuando se ejecuta para liberar la memoria "desperdiciada". Para cuantificar este impacto, se modifica ligeramente el script anterior para tener un número de iteraciones más alto y eliminar la recolección del uso de memoria intermedia. El segundo script se reproduce a continuación:

Impacto de GC en el rendimiento

```php
<?php
class Foo
{
    public $var = '3.14159265359';
    public $self;
}

for ( $i = 0; $i <= 1000000; $i++ )
{
    $a = new Foo;
    $a->self = $a;
}

echo memory_get_peak_usage(), "\n";
?>

      
```

Se lanzará este script 2 veces, una vez con [zend.enable_gc](#ini.zend.enable-gc) en on, y una vez en off:

Ejecución del script anterior

```php
time php -dzend.enable_gc=0 -dmemory_limit=-1 -n example2.php
## y
time php -dzend.enable_gc=1 -dmemory_limit=-1 -n example2.php

      
```

En mi máquina, el primer comando parece durar siempre 10,7 segundos, mientras que el segundo comando tarda aproximadamente 11,4 segundos. Esto corresponde a un retraso de aproximadamente el 7%. Sin embargo, la cantidad total de memoria utilizada por el script se reduce en un 98%, pasando de 931Mo a 10Mo. Este benchmark no es muy científico ni representativo de aplicaciones reales, pero demuestra concretamente en qué medida el mecanismo de recolección de basura puede ser útil en términos de consumo de memoria. El punto positivo es que el retraso es siempre del 7%, en el caso particular de este script, mientras que la memoria preservada será cada vez más importante a medida que aparezcan referencias circulares durante la ejecución.

### Estadísticas internas del GC de PHP

Es posible obtener algunas informaciones adicionales concernientes al mecanismo de recolección de basura interno de PHP. Pero para ello, se debe recompilar PHP con el soporte de benchmarking y recolección de datos. Se debe establecer la variable de entorno `CFLAGS` con `-DGC_BENCH=1` antes de lanzar `./configure` con las opciones que interesan. El siguiente ejemplo lo demuestra:

Recompilar PHP para activar el soporte de benchmark del GC

```php
export CFLAGS=-DGC_BENCH=1
./config.nice
make clean
make

      
```

Cuando se re-ejecuta el código del script anterior con el binario PHP recién reconstruido, se debería ver el siguiente resultado después de la ejecución:

Estadísticas GC

```php
GC Statistics
-------------
Runs:               110
Collected:          2072204
Root buffer length: 0
Root buffer peak:   10000

      Possible            Remove from  Marked
        Root    Buffered     buffer     grey
      --------  --------  -----------  ------
ZVAL   7175487   1491291    1241690   3611871
ZOBJ  28506264   1527980     677581   1025731

      
```

Las estadísticas más interesantes se muestran en el primer bloque. Se ve aquí que el mecanismo de recolección de basura se ha desencadenado 110 veces, y que en total son más de 2 millones de asignaciones de memoria las que se han liberado durante estos 110 pasos. Tan pronto como el mecanismo haya intervenido al menos una vez, el pico del búfer de raíces es siempre de 10000.

### Conclusión

En general, la recolección de basura de PHP solo causará un retraso cuando el algoritmo de recolección de ciclos se ejecute, lo que significa que en los scripts normales (más cortos), no debería haber ningún impacto en el rendimiento.

Sin embargo, cuando el mecanismo de recolección de ciclos se desencadene en scripts normales, la reducción de la huella de memoria permitirá la ejecución paralela de un número mayor de estos scripts, ya que se utilizará menos memoria en total.

Las ventajas se sienten más claramente en el caso de scripts demonio o que deben ejecutarse durante mucho tiempo. Así, para las aplicaciones [PHP-GTK](http://gtk.php.net/) que a menudo duran más que los scripts web, el nuevo mecanismo debería reducir significativamente las fugas de memoria a largo plazo.
