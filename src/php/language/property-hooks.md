---
title: Hooks de propiedad
source_url: https://www.php.net/manual/es/language.oop5.property-hooks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/property-hooks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 2570
---

## Hooks de propiedad

Los hooks de propiedad, también conocidos como "métodos de acceso de propiedad" en otros lenguajes, son una forma de interceptar y reemplazar el comportamiento de lectura y escritura de una propiedad. Esta funcionalidad sirve a dos fines:

1.  Permite utilizar propiedades directamente, sin necesidad de métodos get y set, dejando la posibilidad de añadir un comportamiento adicional en el futuro. Esto hace que la mayoría de los métodos get/set sean innecesarios, incluso sin usar hooks.

2.  Permite definir propiedades que describen un objeto sin almacenar directamente un valor.

Existen dos hooks disponibles en las propiedades no estáticas: `get` y `set`. Permiten reemplazar el comportamiento de lectura y escritura de una propiedad, respectivamente. Los hooks están disponibles para propiedades tipadas y no tipadas.

Un objeto puede ser "backed" o "virtual". Una propiedad "backed" es una propiedad que almacena efectivamente un valor. Cualquier propiedad que no tenga hooks es "backed". Una propiedad virtual es una propiedad que tiene hooks y estos hooks no interactúan con la propiedad misma. En este caso, los hooks son efectivamente los mismos que los métodos, y el objeto no utiliza espacio para almacenar un valor para esta propiedad.

Los hooks de propiedad son incompatibles con las propiedades `readonly`. Si es necesario restringir el acceso a una operación `get` o `set` además de modificar su comportamiento, utilice [la visibilidad asimétrica de propiedad](#language.oop5.visibility-members-aviz).

> [!NOTE]
> Los hooks de propiedad fueron introducidos en PHP 8.4.

## Sintaxis básica de los hooks

La sintaxis general para declarar un hook es la siguiente.

Hooks de propiedad (versión completa)

```php
<?php
class Example
{
    private bool $modified = false;

    public string $foo = 'valor por omisión' {
        get {
            if ($this->modified) {
                return $this->foo . ' (modificado)';
            }
            return $this->foo;
        }
        set(string $value) {
            $this->foo = strtolower($value);
            $this->modified = true;
        }
    }
}

$example = new Example();
$example->foo = 'cambiado';
print $example->foo;
?>

   
```

La propiedad `$foo` termina con `{}`, en lugar de un punto y coma. Esto indica la presencia de hooks. Se definen un hook `get` y un hook `set`, aunque es posible definir solo uno. Ambos hooks tienen un cuerpo, indicado por `{}`, que puede contener código arbitrario.

El hook `set` también permite especificar el tipo y el nombre de un valor entrante, utilizando la misma sintaxis que una método. El tipo debe ser el mismo que el tipo de la propiedad, o [contravariante](#language.oop5.variance.contravariance) (más amplio) que este. Por ejemplo, una propiedad de tipo `string` podría tener un hook `set` que acepte un `stringStringable`, pero no uno que acepte solo `array`.

Al menos uno de los hooks hace referencia a `$this->foo`, la propiedad misma. Esto significa que la propiedad será "backed". Cuando se llama a `$example->foo = 'cambiado'`, la cadena proporcionada se convertirá primero en minúsculas y luego se guardará en el valor de respaldo. Al leer la propiedad, el valor previamente guardado puede ser condicionalmente complementado con texto adicional.

Hay varias variantes de sintaxis abreviada para manejar los casos comunes.

Si el hook `get` es una simple expresión, entonces los `{}` pueden ser omitidos y reemplazados por una expresión flecha.

Expresión de propiedad get

Este ejemplo es equivalente al ejemplo anterior.

```php
<?php
class Example
{
    private bool $modified = false;

    public string $foo = 'valor por omisión' {
        get => $this->foo . ($this->modified ? ' (modificado)' : '');

        set(string $value) {
            $this->foo = strtolower($value);
            $this->modified = true;
        }
    }
}
?>

   
```

Si el tipo del parámetro del hook `set` es el mismo que el tipo de la propiedad (lo cual es típico), puede ser omitido. En este caso, el valor a definir se nombra automáticamente `$value`.

Parámetros por omisión de propiedad

Este ejemplo es equivalente al ejemplo anterior.

```php
<?php
class Example
{
    private bool $modified = false;

    public string $foo = 'valor por omisión' {
        get => $this->foo . ($this->modified ? ' (modificado)' : '');

        set {
            $this->foo = strtolower($value);
            $this->modified = true;
        }
    }
}
?>

   
```

Si el hook `set` solo define una versión modificada del valor pasado, también puede simplificarse en una expresión flecha. El valor al que se evalúa la expresión se definirá en el valor de respaldo.

Expresión de propiedad set

```php
<?php
class Example
{
    private bool $modified = false;

    public string $foo = 'valor por omisión' {
        get => $this->foo . ($this->modified ? ' (modificado)' : '');
        set => strtolower($value);
    }
}
?>

   
```

Este ejemplo no es completamente equivalente al anterior, ya que tampoco modifica `$this->modified`. Si se necesitan múltiples instrucciones en el cuerpo del hook, utilice la versión con llaves.

Una propiedad puede implementar cero, uno o ambos hooks según la situación. Todas las versiones abreviadas son mutuamente independientes. Es decir, utilizar un atajo para obtener una definición larga, o un atajo para definir un tipo explícito, etc., es válido.

En una propiedad "backed", omitir un hook `get` o `set` significa que se utilizará el comportamiento de lectura o escritura por omisión.

> [!NOTE]
> Los hooks pueden ser definidos al utilizar la [promoción de propiedades en el constructor](#language.oop5.decon.constructor.promotion). Sin embargo, en este caso, los valores proporcionados al constructor deben coincidir con el tipo asociado a la propiedad, independientemente de lo que el hook `set` podría permitir.
>
> Considere el siguiente ejemplo:
>
> ```
> <?php
> class Example
> {
>     public function __construct(
>         public private(set) DateTimeInterface $created {
>             set (string|DateTimeInterface $value) {
>                 if (is_string($value)) {
>                     $value = new DateTimeImmutable($value);
>                 }
>                 $this->created = $value;
>             }
>         },
>     ) {
>     }
> }
>
>    
> ```
>
> Internamente, el motor descompone esto de la siguiente manera:
>
> ```
> <?php
> class Example
> {
>     public private(set) DateTimeInterface $created {
>         set (string|DateTimeInterface $value) {
>             if (is_string($value)) {
>                 $value = new DateTimeImmutable($value);
>             }
>             $this->created = $value;
>         }
>     }
>
>     public function __construct(
>         DateTimeInterface $created,
>     ) {
>         $this->created = $created;
>     }
> }
>
>    
> ```
>
> Cualquier intento de definir la propiedad fuera del constructor permitirá un `string` o un valor de tipo DateTimeInterface, pero el constructor solo permitirá DateTimeInterface. Esto se debe a que el tipo definido para la propiedad (DateTimeInterface) se utiliza como tipo de parámetro en la firma del constructor, independientemente de lo que el hook `set` permita.
>
> Si este tipo de comportamiento es necesario desde el constructor, la promoción de propiedades en el constructor no puede ser utilizada.

## Propiedades virtuales

Las propiedades virtuales son propiedades que no tienen un valor de respaldo. Una propiedad es virtual si ni su hook `get` ni su hook `set` hace referencia a la propiedad misma utilizando una sintaxis exacta. Es decir, una propiedad nombrada `$foo` cuyo hook contiene `$this->foo` será respaldada. Pero la siguiente propiedad no es una propiedad respaldada, y generará un error:

Propiedad virtual inválida

```php
<?php
class Example
{
    public string $foo {
        get {
            $temp = __PROPERTY__;
            return $this->$temp; // No se refiere a $this->foo, por lo que no cuenta.
        }
    }
}
?>

   
```

Para las propiedades virtuales, si se omite un hook, entonces esa operación no existe y tratar de utilizarla producirá un error. Las propiedades virtuales no ocupan espacio de memoria en un objeto. Las propiedades virtuales son adecuadas para las propiedades "derivadas", tales como las que son la combinación de dos otras propiedades.

Propiedad virtual

```php
<?php
class Rectangle
{
    // Una propiedad virtual.
    public int $area {
        get => $this->h * $this->w;
    }

    public function __construct(public int $h, public int $w) {}
}

$s = new Rectangle(4, 5);
print $s->area; // muestra 20
$s->area = 30; // Error, ya que no hay operación de definición.
?>

   
```

Definir tanto un hook `get` como un hook `set` en una propiedad virtual también está permitido.

## Alcance

Todos los hooks funcionan en el alcance del objeto modificado. Esto significa que tienen acceso a todos los métodos públicos, privados o protegidos del objeto, así como a todas las propiedades públicas, privadas o protegidas, incluyendo las propiedades que pueden tener sus propios hooks de propiedad. Acceder a otra propiedad desde un hook no elude los hooks definidos en esa propiedad.

La consecuencia más notable de esto es que los hooks no triviales pueden llamar a un método arbitrariamente complejo si lo desean.

Llamada a un método desde un hook

```php
<?php
class Person {
    public string $phone {
        set => $this->sanitizePhone($value);
    }

    private function sanitizePhone(string $value): string {
        $value = ltrim($value, '+');
        $value = ltrim($value, '1');

        if (!preg_match('/\d\d\d\-\d\d\d\-\d\d\d\d/', $value)) {
            throw new \InvalidArgumentException();
        }
        return $value;
    }
}
?>

   
```

## Referencias

Debido a que la presencia de hooks intercepta el proceso de lectura y escritura de las propiedades, plantean problemas al adquirir una referencia a una propiedad o con una modificación indirecta, tal como `$this->arrayProp['key'] = 'value';`. Esto se debe a que cualquier intento de modificar el valor por referencia eludiría un hook de definición si existiera uno.

En el caso raro en que sea necesario obtener una referencia a una propiedad para la cual se definen hooks, el hook `get` puede ser prefijado por `&` para que devuelva por referencia. Definir tanto `get` como `&get` en la misma propiedad es un error de sintaxis.

Definir tanto los hooks `&get` como `set` en una propiedad "backed" no está permitido. Como se indicó anteriormente, escribir en el valor devuelto por referencia eludiría el hook `set`. En las propiedades virtuales, no hay un valor común necesario compartido entre los dos hooks, por lo que definir ambos está permitido.

Escribir en un índice de una propiedad de array implica también una referencia implícita. Por esta razón, escribir en una propiedad de array "backed" con hooks definidos está permitido si y solo si define solo un hook `&get`. En una propiedad virtual, escribir en el array devuelto por `get` o `&get` es legal, pero si esto tiene un impacto en el objeto depende de la implementación del hook.

Sobrecargar la propiedad de array completa está permitido, y se comporta de la misma manera que cualquier otra propiedad. Trabajar solo con elementos del array requiere atención especial.

## Herencia

### Hooks finales

Los hooks también pueden ser declarados [final](#language.oop5.final), en cuyo caso no pueden ser reemplazados.

Hooks finales

```php
<?php
class User
{
    public string $username {
        final set => strtolower($value);
    }
}

class Manager extends User
{
    public string $username {
        // Esto está permitido
        get => strtoupper($this->username);

        // Esto NO está permitido, ya que set es final en el padre.
        set => strtoupper($value);
    }
}
?>

    
```

Una propiedad también puede ser declarada [final](#language.oop5.final). Una propiedad final no puede ser redeclarada por una clase hija de ninguna manera, lo que excluye la modificación de los hooks o la ampliación de su acceso.

Declarar hooks finales en una propiedad que es declarada final es redundante, y será silenciosamente ignorado. Es el mismo comportamiento que para los métodos finales.

Una clase hija puede declarar o cambiar hooks individuales en una propiedad redefiniendo la propiedad y solo los hooks que desea reemplazar. Una clase hija también puede añadir hooks a una propiedad que no los tenía. Esto es esencialmente lo mismo que si los hooks fueran métodos.

Herencia de hook

```php
<?php
class Point
{
    public int $x;
    public int $y;
}

class PositivePoint extends Point
{
    public int $x {
        set {
            if ($value < 0) {
                throw new \InvalidArgumentException('Demasiado pequeño');
            }
            $this->x = $value;
        }
    }
}
?>

    
```

Cada hook reemplaza las implementaciones parentales de manera independiente. Si una clase hija añade hooks, cualquier valor por omisión definido en la propiedad es eliminado, y debe ser redeclarado. Esto es coherente con el funcionamiento de la herencia en las propiedades sin hooks.

### Acceso a los hooks parentales

Un hook en una clase hija puede acceder a la propiedad de la clase padre utilizando la palabra clave `parent::$prop`, seguida del hook deseado. Por ejemplo, `parent::$propName::get()`. Esto puede ser leído como "acceder a la `prop` definida en la clase padre, luego ejecutar su operación get" (o set, según el caso).

Si no se accede de esta manera, el hook de la clase padre es ignorado. Este comportamiento es coherente con el funcionamiento de todos los métodos. Esto también proporciona una manera de acceder al almacenamiento de la clase padre, si es necesario. Si no hay un hook en la propiedad padre, su comportamiento por omisión get/set será utilizado. Los hooks no pueden acceder a otro hook que no sea su propio padre en su propia propiedad.

El ejemplo anterior podría ser reescrito de la siguiente manera, lo que permitiría a la clase `Point` añadir su propio hook `set` en el futuro sin problemas (en el ejemplo anterior, un hook añadido a la clase padre sería ignorado en la clase hija).

Acceso a los hooks parentales (set)

```php
<?php
class Point
{
    public int $x;
    public int $y;
}

class PositivePoint extends Point
{
    public int $x {
        set {
            if ($value < 0) {
                throw new \InvalidArgumentException('Demasiado pequeño');
            }
            parent::$x::set($value);
        }
    }
}
?>

    
```

Un ejemplo de reemplazo de solo un hook get podría ser:

Acceso a los hooks parentales (get)

```php
<?php
class Strings
{
    public string $val;
}

class CaseFoldingStrings extends Strings
{
    public bool $uppercase = true;

    public string $val {
        get => $this->uppercase
            ? strtoupper(parent::$val::get())
            : strtolower(parent::$val::get());
    }
}
?>

    
```

## Serialización

PHP tiene varias formas diferentes de serializar un objeto, ya sea para consumo público o para fines de depuración. El comportamiento de los hooks varía según el uso. En algunos casos, el valor bruto de respaldo de una propiedad será utilizado, eludiendo cualquier hook. En otros, la propiedad será leída o escrita "a través" del hook, como cualquier otra acción de lectura/escritura normal.

var_dump

: Utiliza el valor bruto

serialize

: Utiliza el valor bruto

unserialize

: Utiliza el valor bruto

\_\_serialize()

/

\_\_unserialize()

: Lógica propia, utiliza los hooks de recuperación/definición

Conversión a array: Utiliza el valor bruto

var_export

: Utiliza el hook de recuperación

json_encode

: Utiliza el hook de recuperación

JsonSerializable

: Lógica propia, utiliza el hook de recuperación

get_object_vars

: Utiliza el hook de recuperación

get_mangled_object_vars

: Utiliza el valor bruto
