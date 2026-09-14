---
title: Enumeraciones
source_url: https://www.php.net/manual/es/language.enumerations.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/enumerations.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 2280
---

## Enumeraciones

## Visión general de las enumeraciones

Las enumeraciones, o "Enums", permiten a un desarrollador definir un tipo personalizado que se limita a uno de un número discreto de valores posibles. Esto puede ser especialmente útil al definir un modelo de dominio, ya que permite "hacer que los estados no válidos sean irrepresentables".

Las enumeraciones aparecen en muchos lenguajes con una variedad de características diferentes. En PHP, las enumeraciones son un tipo especial de objeto. La enumeración en sí es una clase, y sus posibles casos son todos objetos de instancia única de esa clase. Eso significa que los casos de enumeración son objetos válidos y pueden usarse dondequiera que se pueda usar un objeto, incluyendo comprobaciones de tipo.

El ejemplo más popular de enumeraciones es el tipo booleano integrado, que es un tipo enumerado con valores legales `true` y `false`. Las enumeraciones permiten a los desarrolladores definir sus propias enumeraciones arbitrariamente robustas.

## Enumeraciones básicas

Las enumeraciones son similares a las clases y comparten los mismos espacios de nombres que las clases, interfaces y traits. También son autocargables de la misma manera. Una enumeración define un nuevo tipo, que tiene un número fijo y limitado de valores legales posibles.

```php
<?php

enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

   
```

Esta declaración crea un nuevo tipo enumerado llamado `Suit`, que tiene cuatro y solo cuatro valores legales: `Suit::Hearts`, `Suit::Diamonds`, `Suit::Clubs`, y `Suit::Spades`. Las variables pueden ser asignadas a uno de esos valores legales. Una función puede ser comprobada de tipo contra un tipo enumerado, en cuyo caso solo se pueden pasar valores de ese tipo.

```php
<?php

enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

function pick_a_card(Suit $suit)
{
    var_dump($suit);
}

$val = Suit::Diamonds;

// OK
pick_a_card($val);

// OK
pick_a_card(Suit::Clubs);

// TypeError: pick_a_card(): Argument #1 ($suit) must be of type Suit, string given
pick_a_card('Spades');

    
```

Una enumeración puede tener cero o más definiciones de `case`, sin máximo. Una enumeración sin casos es sintácticamente válida, aunque bastante inútil.

Para los casos de enumeración, se aplican las mismas reglas sintácticas que a cualquier etiqueta en PHP, ver [Constantes](#language.constants).

Por omisión, los casos no están respaldados intrínsecamente por un valor escalar. Es decir, `Suit::Hearts` no es igual a `"0"`. En su lugar, cada caso está respaldado por un objeto singleton de ese nombre. Eso significa que:

```php
<?php

enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

$a = Suit::Spades;
$b = Suit::Spades;

if ($a === $b) {
    print "Los palos coinciden usando ===\n";
}

if ($a instanceof Suit) {
    print "Los palos coinciden usando instanceof\n";
}

if ($a !== 'Spades') {
    print "El palo no coincide con la cadena\n";
}

    
```

También significa que los valores de enumeración nunca son `<` o `>` entre sí, ya que esas comparaciones no tienen significado en los objetos. Esas comparaciones siempre devolverán `false` al trabajar con valores de enumeración.

Este tipo de caso, sin datos relacionados, se denomina "Caso Puro". Una enumeración que contiene solo Casos Puros se denomina Enumeración Pura.

Todos los Casos Puros se implementan como instancias de su tipo de enumeración. El tipo de enumeración está representado internamente como una clase.

Todos los Casos tienen una propiedad de solo lectura, `name`, que es el nombre sensible a mayúsculas y minúsculas del caso en sí.

```php
<?php

enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

print Suit::Spades->name;
// imprime "Spades"

    
```

También es posible usar las funciones `defined` y `constant` para verificar la existencia o leer un caso de enumeración si el nombre se obtiene dinámicamente. Sin embargo, esto se desaconseja ya que el uso de [Enumeraciones respaldadas](#language.enumerations.backed) debería funcionar para la mayoría de los casos de uso.

## Enumeraciones respaldadas

Por omisión, los Casos Enumerados no tienen equivalente escalar. Son simplemente objetos singleton. Sin embargo, hay amplios casos en los que un Caso Enumerado necesita poder hacer un viaje de ida y vuelta a una base de datos o un almacén de datos similar, por lo que tener un equivalente escalar integrado (y por lo tanto trivialmente serializable) definido intrínsecamente es útil.

Para definir un equivalente escalar para una Enumeración, la sintaxis es la siguiente:

```php
<?php

enum Suit: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

  
```

Un caso que tiene un equivalente escalar se denomina Caso Respaldado, ya que está "respaldado" por un valor más simple. Una enumeración que contiene todos los Casos Respaldados se denomina "Enumeración Respaldada". Una Enumeración Respaldada solo puede contener Casos Respaldados. Una Enumeración Pura solo puede contener Casos Puros.

Una Enumeración Respaldada puede estar respaldada por tipos de `int` o `string`, y una enumeración dada admite solo un tipo a la vez (es decir, no hay unión de `int|string`). Si una enumeración está marcada como que tiene un equivalente escalar, entonces todos los casos deben tener un equivalente escalar único definido explícitamente. No hay equivalentes escalares generados automáticamente (por ejemplo, enteros secuenciales). Los casos respaldados deben ser únicos; dos casos de enumeración respaldados no pueden tener el mismo equivalente escalar. Sin embargo, una constante puede referirse a un caso, creando efectivamente un alias. Ver [Constantes de enumeración](#language.enumerations.constants).

Los valores equivalentes pueden ser una expresión escalar constante. Antes de PHP 8.2.0, los valores equivalentes debían ser literales o expresiones literales. Esto significa que las constantes y expresiones constantes no estaban admitidas. Es decir, `1 + 1` estaba permitido, pero `1 + SOME_CONST` no.

Los Casos Respaldados tienen una propiedad adicional de solo lectura, `value`, que es el valor especificado en la definición.

```php
<?php

enum Suit: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

print Suit::Clubs->value;
// Imprime "C"

   
```

Para hacer cumplir la propiedad `value` como de solo lectura, una variable no puede ser asignada como referencia a ella. Es decir, lo siguiente genera un error:

```php
<?php

enum Suit: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

$suit = Suit::Clubs;
$ref = &$suit->value;
// Error fatal: No se puede modificar indirectamente la propiedad de solo lectura Suit::$value

   
```

Las enumeraciones respaldadas implementan una interfaz interna BackedEnum, que expone dos métodos adicionales:

from(int\|string): self

tomará un escalar y devolverá el Caso de Enumeración correspondiente. Si no se encuentra ninguno, lanzará un

ValueError

. Esto es principalmente útil en casos donde el escalar de entrada es confiable y un valor de enumeración faltante debería ser considerado un error que detiene la aplicación.

tryFrom(int\|string): ?self

tomará un escalar y devolverá el Caso de Enumeración correspondiente. Si no se encuentra ninguno, devolverá

null

. Esto es principalmente útil en casos donde el escalar de entrada no es confiable y el llamador quiere implementar su propia lógica de manejo de errores o valores por omisión.

Los métodos `from()` y `tryFrom()` siguen las reglas estándar de tipado débil/fuerte. En modo de tipado débil, pasar un entero o string es admisible y el sistema coercionará el valor en consecuencia. Pasar un float también funcionará y será coercionado. En modo de tipado estricto, pasar un entero a `from()` en una enumeración respaldada por string (o viceversa) resultará en un `TypeError`, al igual que un float en todas las circunstancias. Todos los demás tipos de parámetros lanzarán un TypeError en ambos modos.

```php
<?php

enum Suit: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

function get_stuff_from_database($id) {
    return [
        'suit' => 'S',
    ];
}

$record = get_stuff_from_database(42);
print $record['suit'] . "\n";

$suit = Suit::tryFrom('A') ?? Suit::Spades;
// Datos no válidos devuelven null, por lo que se usa Suit::Spades en su lugar.
print $suit->value . "\n";

$suit =  Suit::from('X');
// Datos no válidos lanzan un ValueError: "X" is not a valid backing scalar value for enum Suit
print $suit->value . "\n";

   
```

Definir manualmente un método `from()` o `tryFrom()` en una Enumeración Respaldada resultará en un error fatal.

## Métodos de enumeración

Las enumeraciones (tanto Enumeraciones Puras como Enumeraciones Respaldadas) pueden contener métodos y pueden implementar interfaces. Si una enumeración implementa una interfaz, entonces cualquier comprobación de tipo para esa interfaz también aceptará todos los casos de esa enumeración.

```php
<?php

interface Colorful
{
    public function color(): string;
}

enum Suit implements Colorful
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;

    // Cumple con el contrato de la interfaz.
    public function color(): string
    {
        return match ($this) {
            Suit::Hearts, Suit::Diamonds => 'Red',
            Suit::Clubs, Suit::Spades => 'Black',
        };
    }

    // No forma parte de una interfaz; eso está bien.
    public function shape(): string
    {
        return "Rectangle";
    }
}

function paint(Colorful $c)
{
   print $c->color() . "\n";
}

paint(Suit::Clubs);  // Funciona

print Suit::Diamonds->shape(); // imprime "Rectangle"

   
```

En este ejemplo, las cuatro instancias de `Suit` tienen dos métodos, `color()` y `shape()`. En cuanto al código de llamada y las comprobaciones de tipo, se comportan exactamente igual que cualquier otra instancia de objeto.

En una Enumeración Respaldada, la declaración de interfaz va después de la declaración del tipo de respaldo.

```php
   
<?php

interface Colorful
{
    public function color(): string;
}

enum Suit: string implements Colorful
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';

    // Cumple con el contrato de la interfaz.
    public function color(): string
    {
        return match ($this) {
            Suit::Hearts, Suit::Diamonds => 'Red',
            Suit::Clubs, Suit::Spades => 'Black',
        };
    }
}

  
```

Dentro de un método, la variable `$this` está definida y se refiere a la instancia del Caso.

Los métodos pueden ser arbitrariamente complejos, pero en la práctica suelen devolver un valor estático o [match](#control-structures.match) en `$this` para proporcionar diferentes resultados para diferentes casos.

Tenga en cuenta que en este caso sería una mejor práctica de modelado de datos también definir un tipo de enumeración `SuitColor` con valores Red y Black y devolver eso en su lugar. Sin embargo, eso complicaría este ejemplo.

La jerarquía anterior es lógicamente similar a la siguiente estructura de clase (aunque este no es el código real que se ejecuta):

```php
<?php

interface Colorful
{
    public function color(): string;
}

final class Suit implements UnitEnum, Colorful
{
    public const Hearts = new self('Hearts');
    public const Diamonds = new self('Diamonds');
    public const Clubs = new self('Clubs');
    public const Spades = new self('Spades');

    private function __construct(public readonly string $name) {}

    public function color(): string
    {
        return match ($this) {
            Suit::Hearts, Suit::Diamonds => 'Red',
            Suit::Clubs, Suit::Spades => 'Black',
        };
    }

    public function shape(): string
    {
        return "Rectangle";
    }

    public static function cases(): array
    {
        // Método ilegal, porque definir manualmente un método cases() en una Enumeración no está permitido.
        // Ver también la sección "Listado de valores".
    }
}

  
```

Los métodos pueden ser públicos, privados o protegidos, aunque en la práctica privado y protegido son equivalentes ya que la herencia no está permitida.

## Métodos estáticos de enumeración

Las enumeraciones también pueden tener métodos estáticos. El uso de métodos estáticos en la enumeración en sí es principalmente para constructores alternativos. Por ejemplo:

```php
<?php

enum Size
{
    case Small;
    case Medium;
    case Large;

    public static function fromLength(int $cm): self
    {
        return match (true) {
            $cm < 50 => self::Small,
            $cm < 100 => self::Medium,
            default => self::Large,
        };
    }
}

var_dump(Size::fromLength(50));

   
```

Los métodos estáticos pueden ser públicos, privados o protegidos, aunque en la práctica privado y protegido son equivalentes ya que la herencia no está permitida.

## Constantes de enumeración

Las enumeraciones pueden incluir constantes, que pueden ser públicas, privadas o protegidas, aunque en la práctica privada y protegida son equivalentes ya que la herencia no está permitida.

Una constante de enumeración puede referirse a un caso de enumeración:

```php
<?php

enum Size
{
    case Small;
    case Medium;
    case Large;

    public const Huge = self::Large;
}

var_dump(Size::Huge);

   
```

## Traits

Las enumeraciones pueden aprovechar los traits, que se comportarán igual que en las clases. La salvedad es que los traits `use`ados en una enumeración no deben contener propiedades. Solo pueden incluir métodos, métodos estáticos y constantes. Un trait con propiedades resultará en un error fatal.

```php
<?php

interface Colorful
{
    public function color(): string;
}

trait Rectangle
{
    public function shape(): string
    {
        return "Rectangle";
    }
}

enum Suit implements Colorful
{
    use Rectangle;

    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;

    public function color(): string
    {
        return match ($this) {
            Suit::Hearts, Suit::Diamonds => 'Red',
            Suit::Clubs, Suit::Spades => 'Black',
        };
    }
}

$suit = Suit::Spades;
var_dump($suit->color());
var_dump($suit->shape());

   
```

## Valores de enumeración en expresiones constantes

Debido a que los casos están representados como constantes en la enumeración en sí, pueden usarse como valores estáticos en la mayoría de las expresiones constantes: valores por omisión de propiedades, valores por omisión de variables estáticas, valores por omisión de parámetros, valores de constantes globales y de clase. No pueden usarse en otros valores de casos de enumeración, pero las constantes normales pueden referirse a un caso de enumeración.

Sin embargo, las llamadas implícitas a métodos mágicos como `ArrayAccess` en enumeraciones no están permitidas en definiciones estáticas o constantes, ya que no podemos garantizar absolutamente que el valor resultante sea determinista o que la invocación del método esté libre de efectos secundarios. Las llamadas a funciones, llamadas a métodos y el acceso a propiedades continúan siendo operaciones no válidas en expresiones constantes.

```php
<?php

// Esta es una definición de Enumeración completamente legal.
enum Direction implements ArrayAccess
{
    case Up;
    case Down;

    public function offsetExists($offset): bool
    {
        return false;
    }

    public function offsetGet($offset): mixed
    {
        return null;
    }

    public function offsetSet($offset, $value): void
    {
        throw new Exception();
    }

    public function offsetUnset($offset): void
    {
        throw new Exception();
    }
}

class Foo
{
    // Esto está permitido.
    const DOWN = Direction::Down;

    // Esto no está permitido, ya que puede no ser determinista.
    const UP = Direction::Up['short'];
    // Error fatal: No se puede usar [] en enumeraciones en expresión constante
}

// Esto es completamente legal, porque no es una expresión constante.
$x = Direction::Up['short'];
var_dump("\$x is " . var_export($x, true));

$foo = new Foo();

  
```

## Diferencias con los objetos

Aunque las enumeraciones están construidas sobre clases y objetos, no admiten toda la funcionalidad relacionada con objetos. En particular, los casos de enumeración tienen prohibido tener estado.

Los constructores y destructores están prohibidos.

La herencia no está admitida. Las enumeraciones no pueden extender ni ser extendidas.

No se permiten propiedades estáticas u objetuales.

Clonar un caso de enumeración no está admitido, ya que los casos deben ser instancias singleton.

Métodos mágicos

, excepto los listados a continuación, no están permitidos.

Las enumeraciones siempre deben declararse antes de ser usadas.

La siguiente funcionalidad de objetos está disponible y se comporta igual que en cualquier otro objeto:

Métodos públicos, privados y protegidos.

Métodos estáticos públicos, privados y protegidos.

Constantes públicas, privadas y protegidas.

Las enumeraciones pueden implementar cualquier número de interfaces.

Las enumeraciones y los casos pueden tener

atributos

adjuntos a ellos. El filtro de destino

TARGET_CLASS

incluye las enumeraciones en sí. El filtro de destino

TARGET_CLASS_CONST

incluye los Casos de Enumeración.

\_\_call

,

\_\_callStatic

, y

\_\_invoke

métodos mágicos

Las constantes

\_\_CLASS\_\_

y

\_\_FUNCTION\_\_

se comportan normalmente

La constante mágica `::class` en un tipo de enumeración se evalúa al nombre del tipo incluyendo cualquier espacio de nombres, exactamente igual que un objeto. La constante mágica `::class` en una instancia de Caso también se evalúa al tipo de enumeración, ya que es una instancia de ese tipo.

Además, los casos de enumeración no pueden ser instanciados directamente con `new`, ni con ReflectionClass::newInstanceWithoutConstructor en reflexión. Ambos resultarán en un error.

```php
<?php

$clovers = new Suit();
// Error: No se puede instanciar la enumeración Suit

$horseshoes = (new ReflectionClass(Suit::class))->newInstanceWithoutConstructor()
// Error: No se puede instanciar la enumeración Suit

  
```

## Listado de valores

Tanto las Enumeraciones Puras como las Enumeraciones Respaldadas implementan una interfaz interna llamada UnitEnum. `UnitEnum` incluye un método estático `cases()`. `cases()` devuelve un array compacto de todos los Casos definidos en el orden de declaración.

```php
<?php

enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

var_dump(Suit::cases());

enum SuitBacked: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

var_dump(SuitBacked::cases());

   
```

Definir manualmente un método `cases()` en una Enumeración resultará en un error fatal.

## Serialización

Las enumeraciones se serializan de manera diferente a los objetos. Específicamente, tienen un nuevo código de serialización, `"E"`, que especifica el nombre del caso de enumeración. La rutina de deserialización puede entonces usar eso para establecer una variable al valor singleton existente. Eso asegura que:

```php
<?php

enum Suit: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

Suit::Hearts === unserialize(serialize(Suit::Hearts));

print serialize(Suit::Hearts);
// E:11:"Suit:Hearts";

   
```

Al deserializar, si no se puede encontrar una enumeración y un caso para coincidir con un valor serializado, se emitirá una advertencia y se devolverá `false`.

La opción `allowed_classes` de `unserialize` no afecta a las [Enumeraciones](#language.enumerations).

Si una Enumeración Pura se serializa a JSON, se lanzará un error. Si una Enumeración Respaldada se serializa a JSON, estará representada solo por su valor escalar, en el tipo apropiado. El comportamiento de ambas puede ser sobrescrito implementando `JsonSerializable`.

Para `print_r`, la salida de un caso de enumeración es ligeramente diferente de los objetos para minimizar la confusión.

```php
<?php

enum Foo
{
    case Bar;
}

enum Baz: int
{
    case Beep = 5;
}

print_r(Foo::Bar);
print_r(Baz::Beep);

/* Produce

Foo Enum (
    [name] => Bar
)
Baz Enum:int {
    [name] => Beep
    [value] => 5
}
*/

   
```

## Por qué las enumeraciones no son extensibles

Las clases tienen contratos en sus métodos:

```php
<?php

class A {}
class B extends A {}

function foo(A $a) {}

function bar(B $b)
{
    foo($b);
}

 
```

Este código es seguro en cuanto a tipos, ya que B sigue el contrato de A, y a través de la magia de la co/contravariancia, cualquier expectativa que uno pueda tener de los métodos será preservada, exceptuando las excepciones.

Las enumeraciones tienen contratos en sus casos, no en sus métodos:

```php
<?php

enum ErrorCode
{
    case SOMETHING_BROKE;
}

function quux(ErrorCode $errorCode)
{
    // Cuando se escribe, este código parece cubrir todos los casos
    match ($errorCode) {
        ErrorCode::SOMETHING_BROKE => true,
    };
}

  
```

La sentencia [match](#control-structures.match) en la función `quux` puede ser analizada estáticamente para cubrir todos los casos en ErrorCode.

Pero imagina que estuviera permitido extender enumeraciones:

```php
<?php

// Código de experimento mental donde las enumeraciones no son finales.
// Nota: esto no funcionará realmente en PHP.
enum MoreErrorCode extends ErrorCode
{
    case PEBKAC;
}

function fot(MoreErrorCode $errorCode)
{
    quux($errorCode);
}

fot(MoreErrorCode::PEBKAC);

  
```

Bajo las reglas normales de herencia, una clase que extiende a otra pasará la comprobación de tipo.

El problema sería que la sentencia [match](#control-structures.match) en `quux()` ya no cubriría todos los casos. Debido a que no sabe acerca de `MoreErrorCode::PEBKAC`, el match lanzará una excepción.

Debido a esto, las enumeraciones son finales y no pueden ser extendidas.

## Ejemplos

Valores limitados básicos

```php
<?php

enum SortOrder
{
    case Asc;
    case Desc;
}

function query($fields, $filter, SortOrder $order = SortOrder::Asc)
{
     /* ... */
}

    
```

La función `query()` ahora puede proceder con la seguridad de que `$order` está garantizado que sea `SortOrder::Asc` o `SortOrder::Desc`. Cualquier otro valor habría resultado en un `TypeError`, por lo que no se necesita ninguna comprobación o prueba de errores adicional.

Valores exclusivos avanzados

```php
<?php

enum UserStatus: string
{
    case Pending = 'P';
    case Active = 'A';
    case Suspended = 'S';
    case CanceledByUser = 'C';

    public function label(): string
    {
        return match ($this) {
            self::Pending => 'Pending',
            self::Active => 'Active',
            self::Suspended => 'Suspended',
            self::CanceledByUser => 'Canceled by user',
        };
    }
}

$status = UserStatus::Suspended;
var_dump($status->label());

    
```

En este ejemplo, el estado de un usuario puede ser uno de, y exclusivamente, `UserStatus::Pending`, `UserStatus::Active`, `UserStatus::Suspended`, o `UserStatus::CanceledByUser`. Una función puede tipar un parámetro contra `UserStatus` y luego solo aceptar esos cuatro valores, punto.

Los cuatro valores tienen un método `label()`, que devuelve un string legible por humanos. Ese string es independiente del string equivalente escalar de "nombre de máquina", que puede usarse en, por ejemplo, un campo de base de datos o un cuadro de selección HTML.

```php
<?php

enum UserStatus: string
{
    case Pending = 'P';
    case Active = 'A';
    case Suspended = 'S';
    case CanceledByUser = 'C';

    public function label(): string
    {
        return match ($this) {
            self::Pending => 'Pending',
            self::Active => 'Active',
            self::Suspended => 'Suspended',
            self::CanceledByUser => 'Canceled by user',
        };
    }
}

foreach (UserStatus::cases() as $case) {
    printf(
        "<option value=\"%s\">%s</option>\n",
        htmlentities($case->value),
        htmlentities($case->label())
    );
}

    
```
