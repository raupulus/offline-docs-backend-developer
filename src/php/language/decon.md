---
title: Constructores y destructores
source_url: https://www.php.net/manual/es/language.oop5.decon.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/decon.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 82fc6a1c8
order: 2450
---

## Constructores y destructores

## Constructor

```php
__construct(mixed ...$values): void
```php

PHP permite a los desarrolladores declarar constructores para las clases. Las clases que poseen un método constructor llaman a este método cada vez que se crea una nueva instancia del objeto, lo cual es interesante para todas las inicializaciones de las que el objeto necesita antes de ser utilizado.

> [!NOTE]
> Los constructores padres no son llamados implícitamente si la clase hija define un constructor. Si se desea utilizar un constructor padre, será necesario hacer llamada a `parent::__construct` desde el constructor hijo. Si el hijo no define un constructor entonces, puede ser heredado de la clase padre, exactamente de la misma forma que una método lo sería (si no ha sido declarado como privado).

Constructor durante la herencia

```
<?php
class BaseClass {
    function __construct() {
        print "En el constructor de BaseClass\n";
    }
}

class SubClass extends BaseClass {
    function __construct() {
        parent::__construct();
        print "En el constructor de SubClass\n";
    }
}

class OtherSubClass extends BaseClass {
    // Constructor heredado de BaseClass
}

// En el constructor de BaseClass
$obj = new BaseClass();

// En el constructor de BaseClass
// En el constructor de SubClass
$obj = new SubClass();

// En el constructor de BaseClass
$obj = new OtherSubClass();
?>
    
```php

A diferencia de otros métodos, [\_\_construct()](#object.construct) está excluido de las [reglas de compatibilidad de firmas](#language.oop.lsp) usuales cuando se extiende.

Los constructores son métodos ordinarios que son llamados durante la instanciación de su objeto correspondiente. Por lo tanto, pueden definir un número arbitrario de argumentos, que pueden ser requeridos, tener un tipo, y pueden tener un valor por defecto. Los argumentos de un constructor son llamados colocando los argumentos dentro de paréntesis después del nombre de la clase.

Utilizar los argumentos de un constructor

```
<?php
class Point {
    protected int $x;
    protected int $y;

    public function __construct(int $x, int $y = 0) {
        $this->x = $x;
        $this->y = $y;
    }
}

// Pasar ambos parámetros.
$p1 = new Point(4, 5);
// Pasar solo el parámetro requerido. $y tomará su valor por defecto de 0.
$p2 = new Point(4);
// Con parámetros nombrados (a partir de PHP 8.0):
$p3 = new Point(y: 5, x: 4);
?>
    
```php

Si una clase no tiene un constructor, o si el constructor no tiene argumentos requeridos, los paréntesis pueden ser omitidos.

### Estilo antiguo de los constructores

Anterior a PHP 8.0.0, las clases en el espacio de nombres global interpretarán un método que tenga el mismo nombre que la clase como un constructor de estilo antiguo. Esta sintaxis está obsoleta, y resultará en un error `E_DEPRECATED` pero llamará a esta función como un constructor. Si [\_\_construct()](#object.construct) y un método con el mismo nombre están definidos, [\_\_construct()](#object.construct) será llamado.

Las clases en espacios de nombres, o cualquier clase a partir de PHP 8.0.0, un método con el mismo nombre que la clase nunca tiene un significado particular.

Siempre utilizar [\_\_construct()](#object.construct) en nuevo código.

### Promoción del Constructor

A partir de PHP 8.0.0, los parámetros del constructor pueden ser promovidos para corresponder a una propiedad del objeto. Es muy común que los parámetros de un constructor sean asignados a una propiedad sin realizar operaciones sobre ellos. La promoción del constructor proporciona un atajo para este caso de uso. El ejemplo anterior puede ser reescrito de la siguiente manera.

Utilizando la promoción de propiedad de constructor

```
<?php
class Point {
    public function __construct(protected int $x, protected int $y = 0) {
    }
}

     
```php

Cuando un argumento de constructor incluye un modificador, PHP lo interpretará como una propiedad de objeto y un argumento del constructor, y asignará el valor del argumento a la propiedad. El cuerpo del constructor puede estar entonces vacío o puede contener otras declaraciones. Todas las declaraciones adicionales serán ejecutadas después de que el valor del argumento haya sido asignado a su propiedad correspondiente.

Todos los argumentos no necesitan ser promovidos. Es posible mezclar y combinar los argumentos promovidos y no promovidos, en cualquier orden. Los argumentos promovidos no tienen ningún impacto en el código que llama al constructor.

> [!NOTE]
> Utilizar un [modificador de visibilidad](#language.oop5.visibility) (`public`, `protected` o `private`) es la manera más probable de aplicar la promoción de propiedad, pero cualquier otro modificador único (como `readonly`) tendrá el mismo efecto.

> [!NOTE]
> Las propiedades de objeto no pueden ser tipadas `callable` debido a las ambigüedades del motor que esto introduciría. Por lo tanto, los argumentos promovidos, tampoco pueden ser tipados `callable`. Sin embargo, cualquier otra [declaración de tipo](#language.types.declarations) está permitida.

> [!NOTE]
> Como las propiedades promovidas son a la vez desucradas a una propiedad y también como el parámetro de una función, todas las restricciones de nombramiento para las propiedades y los parámetros se aplican.

> [!NOTE]
> Los [atributos](#language.attributes) colocados sobre un argumento de constructor promovido serán replicados tanto en la propiedad como en el argumento. Los valores por defecto en un argumento de constructor promovido solo serán replicados en el argumento y no en la propiedad.

### Novedades en inicializadores

A partir de PHP 8.1.0, los objetos pueden ser utilizados como valor por defecto para los parámetros, variables estáticas, constantes globales y los argumentos de atributos. Los objetos pueden ser ahora pasados a `define`.

> [!NOTE]
> El uso de un nombre de clase dinámico o no-string o una clase anónima no está permitido. El uso del desempacado de argumentos no está permitido. El uso de expresiones no soportadas como argumento no está permitido.

Uso de new en inicializadores

```
<?php

// Todos permitidos:
static $x = new Foo;

const C = new Foo;

function test($param = new Foo) {}

#[AnAttribute(new Foo)]
class Test {
    public function __construct(
        public $prop = new Foo,
    ) {}
}

// Todos no permitidos (error de compilación):
function test(
    $a = new (CLASS_NAME_CONSTANT)(), // nombre de clase dinámico
    $b = new class {}, // clase anónima
    $c = new A(...[]), // desempacado de argumentos
    $d = new B($abc), // expresión de constante no soportada
) {}
?>
     
```php

### Método de creación estático

PHP soporta únicamente un constructor por clase. Sin embargo, en ciertos casos puede ser deseable permitir que un objeto sea construido de manera diferente con entradas diferentes. La forma recomendada de hacer esto es utilizando métodos estáticos como una envolvente del constructor.

Utilizando la creación mediante un método estático

```
<?php
$some_json_string = '{ "id": 1004, "name": "Elephpant" }';
$some_xml_string = "<animal><id>1005</id><name>Elephpant</name></animal>";

class Product {

    private ?int $id;
    private ?string $name;

    private function __construct(?int $id = null, ?string $name = null) {
        $this->id = $id;
        $this->name = $name;
    }

    public static function fromBasicData(int $id, string $name): static {
        $new = new static($id, $name);
        return $new;
    }

    public static function fromJson(string $json): static {
        $data = json_decode($json, true);
        return new static($data['id'], $data['name']);
    }

    public static function fromXml(string $xml): static {
        $data = simplexml_load_string($xml);
        $new = new static();
        $new->id = (int) $data->id;
        $new->name = $data->name;
        return $new;
    }
}

$p1 = Product::fromBasicData(5, 'Widget');
$p2 = Product::fromJson($some_json_string);
$p3 = Product::fromXml($some_xml_string);

var_dump($p1, $p2, $p3);

     
```php

El constructor puede ser hecho privado o protegido para evitar su llamada desde el exterior. En este caso, solo un método estático será capaz de instanciar la clase. Puesto que están en la misma definición de clase, tienen acceso a los métodos privados, incluso en una instancia diferente del objeto. Un constructor privado es opcional y puede o no tener sentido dependiendo del caso de uso.

Los tres métodos estáticos públicos demuestran entonces diferentes maneras de instanciar el objeto.

fromBasicData()

toma los parámetros exactos que son necesarios, luego crea el objeto llamando al constructor y retornando el resultado.

fromJson()

acepta una cadena de caracteres JSON y realiza un preprocesamiento sobre sí mismo para convertirse en el formato deseado por el constructor. Luego retorna el nuevo objeto.

fromXml()

acepta una cadena de caracteres XML, realiza un preprocesamiento, luego crea un objeto bruto. El constructor es llamado, pero como todos los parámetros son opcionales el método los ignora. Luego asigna los valores a las propiedades del objeto directamente antes de retornar el resultado.

En los tres casos, la palabra clave `static` es traducida al nombre de la clase de la cual el código se encuentra. En este caso, `Product`.

## Destructor

```php
__destruct(): void
```

PHP posee un concepto de destructor similar al de otros lenguajes orientados a objeto, como el C++. El método destructor es llamado tan pronto como ya no hay referencias a un objeto dado, o en cualquier orden durante la secuencia de parada.

Ejemplo con un Destructor

```php
<?php

class MyDestructableClass
{
    function __construct() {
        print "In constructor\n";
    }

    function __destruct() {
        print "Destroying " . __CLASS__ . "\n";
    }
}

$obj = new MyDestructableClass();

    
```

Al igual que el constructor, el destructor padre no será llamado implícitamente por el motor. Para ejecutar el destructor padre, se debe llamar explícitamente a la función `parent::__destruct` en el cuerpo del destructor. Al igual que los constructores, una clase hija puede heredar el destructor del padre si no lo implementa ella misma.

El destructor será llamado incluso si la ejecución del script es detenida utilizando la función `exit`. Llamar a la función `exit` en un destructor evitará la ejecución de las rutinas de parada restantes.

Si un destructor crea nuevas referencias a su objeto, no será llamado una segunda vez cuando el contador de referencias alcance nuevamente cero o durante la secuencia de parada.

A partir de PHP 8.4.0, cuando la [colección de ciclos](#features.gc.collecting-cycles) ocurre durante la ejecución de una [fibra](#language.fibers), los destructores de los objetos programados para la colección son ejecutados en una fibra distinta, llamada `gc_destructor_fiber`. Si esta fibra es suspendida, una nueva fibra será creada para ejecutar los destructores restantes. La anterior `gc_destructor_fiber` ya no será referenciada por el recolector de basura y podrá ser colectada si no es referenciada en otro lugar. Los objetos cuyo destructor está suspendido no serán colectados hasta que el destructor haya terminado o que la fibra misma sea colectada.

> [!NOTE]
> Los destructores llamados durante la parada del script están en una situación donde los encabezados HTTP ya han sido enviados. La carpeta de trabajo en la fase de parada del script puede ser diferente con ciertas APIs (ej. Apache).

> [!NOTE]
> Intentar lanzar una excepción desde un destructor (llamado al final del script) resulta en un error fatal.
