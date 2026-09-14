---
title: Generators
source_url: https://www.php.net/manual/es/language.generators.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/generators.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 50e6f42c8
order: 2360
---

## Generators

## Resumen sobre los generadores

Los generadores proporcionan una manera sencilla de implementar [iteradores](#language.oop5.iterations) sin el costo ni la complejidad de desarrollar una clase que implemente la interfaz `Iterator`.

Un generador ofrece un medio conveniente para proporcionar datos a las bucles [`foreach`](#control-structures.foreach) sin tener que construir un array en memoria de antemano, lo cual podría llevar al programa a exceder un límite de memoria o requerir un tiempo de procesamiento considerable para generarlos. En su lugar, se puede utilizar una función generadora, que es idéntica a una [función](#functions.user-defined) normal, excepto que en lugar de [devolver](#functions.returning-values) una sola vez, un generador puede utilizar [`yield`](#control-structures.yield) tantas veces como sea necesario, para proporcionar los valores a recorrer. Al igual que con los iteradores, el acceso aleatorio a los datos no es posible.

Un ejemplo sencillo de este mecanismo es la reimplementación de la función `range` en forma de generador. La función estándar `range` debe generar un array que contenga cada valor y devolverlo, lo cual puede llevar a arrays de gran tamaño: por ejemplo, la llamada al código `range(0, 1000000)` puede consumir significativamente más de 100 MB de memoria.

Como alternativa, se puede implementar un generador `xrange()`, que solo necesitará memoria para la creación de un objeto `Iterator`, y deberá mantener internamente el estado actual del generador, lo cual resulta en un consumo de memoria inferior a 1 KB.

Implementación de la función `range` en forma de generador

```php
<?php
function xrange($start, $limit, $step = 1) {
    if ($start <= $limit) {
        if ($step <= 0) {
            throw new LogicException('El paso debe ser positivo');
        }

        for ($i = $start; $i <= $limit; $i += $step) {
            yield $i;
        }
    } else {
        if ($step >= 0) {
            throw new LogicException('El paso debe ser negativo');
        }

        for ($i = $start; $i >= $limit; $i += $step) {
            yield $i;
        }
    }
}

/*
 * Es de notar que las funciones range() y xrange() producen el
 * mismo resultado, a continuación.
 */

echo 'Números impares de un solo dígito desde range():  ';
foreach (range(1, 9, 2) as $number) {
    echo "$number ";
}
echo "\n";

echo 'Números impares de un solo dígito desde xrange(): ';
foreach (xrange(1, 9, 2) as $number) {
    echo "$number ";
}

   
```

El ejemplo anterior mostrará:

    Números impares de un solo dígito desde range():  1 3 5 7 9
    Números impares de un solo dígito desde xrange(): 1 3 5 7 9

### Los objetos `Generator`

Cuando se llama a una función generadora, se devuelve un objeto de la clase interna `Generator`. Este objeto implementa la interfaz `Iterator` de la misma manera que lo haría un objeto iterador que solo avanza, y proporciona los métodos que pueden ser llamados para manipular el estado del generador, incluyendo el envío de valores y sus retornos.

## Sintaxis de un Generador

Una función generadora se asemeja a una función normal, excepto que en lugar de devolver un valor, un generador [`yield`](#control-structures.yield) devuelve tantos valores como sea necesario. Todas las funciones que contienen [`yield`](#control-structures.yield) son funciones generadoras.

Cuando se llama a una función generadora, devuelve un objeto que se puede recorrer. Cuando se recorre este objeto (por ejemplo, a través de una bucle [`foreach`](#control-structures.foreach)), PHP llamará a los métodos de iteración del objeto cada vez que necesite un valor, luego guardará el estado del generador cuando genere un valor, para que pueda ser reanudado cuando se requiera el siguiente valor.

Cuando no haya más valores para proporcionar, la función generadora puede simplemente devolver, y el código de llamada continuará como si un array no tuviera más valores.

> [!NOTE]
> Un generador puede devolver valores, que pueden ser recuperados utilizando Generator::getReturn.

### La palabra clave `yield`

La palabra clave `yield` es el núcleo de una función generadora. En su forma más simple, una instrucción yield se asemeja a una instrucción return, excepto que en lugar de detener la ejecución de la función y devolver, yield proporciona un valor al código que recorre el generador, y pausa la ejecución de la función generadora.

Un ejemplo sencillo de producción de valores

```php
<?php
function gen_one_to_three() {
    for ($i = 1; $i <= 3; $i++) {
        // Note que $i se preserva entre cada producción de valor.
        yield $i;
    }
}

$generator = gen_one_to_three();
foreach ($generator as $value) {
    echo "$value\n";
}

    
```

El ejemplo anterior mostrará:

    1
    2
    3

> [!NOTE]
> Internamente, se asociarán claves enteras secuenciales con los valores producidos, de la misma manera que para un array no asociativo.

#### Provisión de valores con claves

PHP también soporta arrays asociativos, y los generadores no son diferentes. Además de proporcionar valores simples, como hemos visto anteriormente, también se pueden proporcionar claves simultáneamente.

La sintaxis para producir un par clave/valor es similar a la utilizada para definir un array asociativo; así:

Producción de un par clave/valor

```php
<?php
/*
 * La entrada está compuesta de campos separados por un punto y coma,
 * y el primer campo es un ID para usar como clave.
 */

$input = <<<'EOF'
1;PHP;Le gustan los signos de dólar
2;Python;Le gustan los espacios en blanco
3;Ruby;Le gustan los bloques
EOF;

function input_parser($input) {
    foreach (explode("\n", $input) as $line) {
        $fields = explode(';', $line);
        $id = array_shift($fields);

        yield $id => $fields;
    }
}

foreach (input_parser($input) as $id => $fields) {
    echo "$id:\n";
    echo "    $fields[0]\n";
    echo "    $fields[1]\n";
}

     
```

El ejemplo anterior mostrará:

    1:
        PHP
        Le gustan los signos de dólar
    2:
        Python
        Le gustan los espacios en blanco
    3:
        Ruby
        Le gustan los bloques

#### Producción de valores nulos

Yield puede ser llamado sin argumento para proporcionar un valor `null` con una clave automática.

Producción de valores `null`

```php
<?php
function gen_three_nulls() {
    foreach (range(1, 3) as $i) {
        yield;
    }
}

var_dump(iterator_to_array(gen_three_nulls()));

     
```

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      NULL
      [1]=>
      NULL
      [2]=>
      NULL
    }

#### Producción de valores por referencia

Las funciones generadoras pueden producir valores por referencia. Esto se hace de la misma manera que el [retorno por referencia desde funciones](#functions.returning-values) : añadiendo un ET comercial (&) al nombre de la función.

Producción de valores por referencia

```php
<?php
function &gen_reference() {
    $value = 3;

    while ($value > 0) {
        yield $value;
    }
}

/*
 * Note que es posible cambiar $number en el bucle,
 * y, dado que el generador proporciona referencias, $value
 * en gen_reference() también cambia.
 */
foreach (gen_reference() as &$number) {
    echo (--$number).'... ';
}

     
```

El ejemplo anterior mostrará:

    2... 1... 0...

#### Delegación del generador vía `yield from`

La delegación del generador permite obtener los valores de otro generador, de un objeto `Traversable`, o de un `array` utilizando la palabra clave `yield from`. El generador externo obtendrá así todos los valores del generador interno, del objeto, o del array mientras no sea inválido, después de lo cual, la ejecución continuará en el generador externo.

Si un generador se utiliza con la expresión `yield from`, la expresión `yield from` también devolverá cualquier valor devuelto por el generador interno.

> [!CAUTION]
> `yield from` no reinicia las claves. Preserva las claves devueltas por el objeto `Traversable`, o `array`. Por lo tanto, algunos valores pueden compartir una clave común con otros `yield` o `yield from`, que, al insertarse en un array, sobrescribirá los valores anteriores con esa clave.
>
> Un caso frecuente en el que esto es importante es `iterator_to_array` devolviendo un array con clave por defecto, lo que puede llevar a resultados potencialmente inesperados. `iterator_to_array` tiene un segundo parámetro `preserve_keys` que puede ser definido en `false` para recolectar todos los valores ignorando las claves devueltas por el `Generator`.
>
> <div class="example">
>
> <div class="title">
>
> `yield from` con `iterator_to_array`
>
> </div>
>
> ```
> <?php
> function inner() {
>     yield 1; // clave 0
>     yield 2; // clave 1
>     yield 3; // clave 2
> }
> function gen() {
>     yield 0; // clave 0
>     yield from inner(); // claves 0-2
>     yield 4; // clave 1
> }
> // establece en false el segundo parámetro para obtener un array [0, 1, 2, 3, 4]
> var_dump(iterator_to_array(gen()));
>
>        
> ```
>
> El ejemplo anterior mostrará:
>
>     array(3) {
>       [0]=>
>       int(1)
>       [1]=>
>       int(4)
>       [2]=>
>       int(3)
>     }
>
>            
>
> </div>

Uso básico de `yield from`

```php
<?php
function count_to_ten() {
    yield 1;
    yield 2;
    yield from [3, 4];
    yield from new ArrayIterator([5, 6]);
    yield from seven_eight();
    yield 9;
    yield 10;
}

function seven_eight() {
    yield 7;
    yield from eight();
}

function eight() {
    yield 8;
}

foreach (count_to_ten() as $num) {
    echo "$num ";
}

     
```

El ejemplo anterior mostrará:

    1 2 3 4 5 6 7 8 9 10

`yield from` y los valores devueltos

```php
<?php
function count_to_ten() {
    yield 1;
    yield 2;
    yield from [3, 4];
    yield from new ArrayIterator([5, 6]);
    yield from seven_eight();
    return yield from nine_ten();
}

function seven_eight() {
    yield 7;
    yield from eight();
}

function eight() {
    yield 8;
}

function nine_ten() {
    yield 9;
    return 10;
}

$gen = count_to_ten();
foreach ($gen as $num) {
    echo "$num ";
}
echo $gen->getReturn();

     
```

El ejemplo anterior mostrará:

    1 2 3 4 5 6 7 8 9 10

## Comparación de los generadores con los objetos `Iterator`

La principal ventaja de los generadores es su simplicidad. Menos código debe ser escrito que cuando se trata de implementar una clase `Iterator`, y generalmente es más legible. Por ejemplo, la función y la clase siguientes son equivalentes:

```php
<?php
function getLinesFromFile($fileName) {
    if (!$fileHandle = fopen($fileName, 'r')) {
        return;
    }

    while (false !== $line = fgets($fileHandle)) {
        yield $line;
    }

    fclose($fileHandle);
}

// versus...

class LineIterator implements Iterator {
    protected $fileHandle;

    protected $line;
    protected $i;

    public function __construct($fileName) {
        if (!$this->fileHandle = fopen($fileName, 'r')) {
            throw new RuntimeException('Imposible abrir el fichero: "' . $fileName . '"');
        }
    }

    public function rewind() {
        fseek($this->fileHandle, 0);
        $this->line = fgets($this->fileHandle);
        $this->i = 0;
    }

    public function valid() {
        return false !== $this->line;
    }

    public function current() {
        return $this->line;
    }

    public function key() {
        return $this->i;
    }

    public function next() {
        if (false !== $this->line) {
            $this->line = fgets($this->fileHandle);
            $this->i++;
        }
    }

    public function __destruct() {
        fclose($this->fileHandle);
    }
}

   
```

Sin embargo, esta flexibilidad tiene un costo: los generadores son iteradores que solo avanzan, y no pueden ser reinicializados una vez que su recorrido haya comenzado. Esto también significa que el mismo generador no puede ser utilizado varias veces: el generador deberá ser reconstruido llamando nuevamente a la función generadora.

### Véase también

[Iteración de Objeto](#language.oop5.iterations)
