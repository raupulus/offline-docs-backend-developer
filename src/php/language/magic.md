---
title: Métodos mágicos
source_url: https://www.php.net/manual/es/language.oop5.magic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/magic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8f51247cb
order: 2520
---

## Métodos mágicos

Los métodos mágicos son métodos especiales que sobrescriben la acción por omisión de PHP cuando se realizan ciertas acciones sobre un objeto.

> [!CAUTION]
> Todos los métodos que comienzan por `__` están reservados por PHP. Por lo tanto, no se recomienda utilizar un nombre de método de este tipo, excepto cuando se sobrescribe el comportamiento de PHP.

Los siguientes métodos se consideran mágicos: [\_\_construct()](#object.construct), [\_\_destruct()](#object.destruct), [\_\_call()](#object.call), [\_\_callStatic()](#object.callstatic), [\_\_get()](#object.get), [\_\_set()](#object.set), [\_\_isset()](#object.isset), [\_\_unset()](#object.unset), [\_\_serialize()](#object.serialize), [\_\_unserialize()](#object.unserialize), [\_\_sleep()](#object.sleep), [\_\_wakeup()](#object.wakeup), [\_\_toString()](#object.tostring), [\_\_invoke()](#object.invoke), [\_\_set_state()](#object.set-state) [\_\_clone()](#object.clone), y [\_\_debugInfo()](#object.debuginfo).

> [!WARNING]
> Todos los métodos mágicos, excepto [\_\_construct()](#object.construct), [\_\_destruct()](#object.destruct), y [\_\_clone()](#object.clone), *deben* ser declarados como `public`, de lo contrario se emitirá una `E_WARNING`. Anterior a PHP 8.0.0, no se emitía ningún diagnóstico para los métodos mágicos [\_\_sleep()](#object.sleep), [\_\_wakeup()](#object.wakeup), [\_\_serialize()](#object.serialize), [\_\_unserialize()](#object.unserialize), y [\_\_set_state()](#object.set-state).

> [!WARNING]
> Si se utilizan declaraciones de tipos en la definición de un método mágico, deben ser idénticas a la firma descrita en este documento. De lo contrario, se emitirá un error fatal. Anterior a PHP 8.0.0, no se emitía ningún diagnóstico. Sin embargo, [\_\_construct()](#object.construct) y [\_\_destruct()](#object.destruct) no deben declarar un tipo de retorno; de lo contrario, se emitirá un error fatal.

## [\_\_serialize()](#object.serialize) y [\_\_unserialize()](#object.unserialize)

```php
public __serialize(): array
```php

```php
public __unserialize(array $data): void
```

`serialize` verifica si la clase tiene un método con el nombre mágico [\_\_serialize()](#object.serialize). Si es así, este método será ejecutado antes de cualquier serialización. Debe construir y devolver un array asociativo de pares clave/valor que represente la forma serializada del objeto. Si no se devuelve ningún array, se lanzará una `TypeError`.

> [!NOTE]
> Si [\_\_serialize()](#object.serialize) y [\_\_sleep()](#object.sleep) están ambas definidas en el mismo objeto, entonces solo [\_\_serialize()](#object.serialize) será llamada. [\_\_sleep()](#object.sleep) será ignorada. Si el objeto implementa la interfaz [Serializable](#class.serializable), el método `serialize()` de la interfaz será ignorado y [\_\_serialize()](#object.serialize) será utilizada en su lugar.

El uso previsto de [\_\_serialize()](#object.serialize) es definir una representación arbitraria del objeto para serializarlo fácilmente. Los elementos del array pueden corresponder a las propiedades del objeto, pero esto no es requerido.

Inversamente, `unserialize` verifica la presencia de una función con el nombre mágico [\_\_unserialize()](#object.unserialize). Si está presente, esta función recibirá el array restaurado devuelto por [\_\_serialize()](#object.serialize). Puede entonces restaurar las propiedades del objeto desde este array como sea apropiado.

> [!NOTE]
> Si [\_\_unserialize()](#object.unserialize) y [\_\_wakeup()](#object.wakeup) están ambas definidas en el mismo objeto, entonces solo [\_\_unserialize()](#object.unserialize) será llamada. [\_\_wakeup()](#object.wakeup) será ignorada.

> [!NOTE]
> Esta funcionalidad está disponible a partir de PHP 7.4.0.

Serialize y unserialize

```php
<?php
class Connection
{
    protected $link;
    private $dsn, $username, $password;

    public function __construct($dsn, $username, $password)
    {
        $this->dsn = $dsn;
        $this->username = $username;
        $this->password = $password;
        $this->connect();
    }

    private function connect()
    {
        $this->link = new PDO($this->dsn, $this->username, $this->password);
    }

    public function __serialize(): array
    {
        return [
          'dsn' => $this->dsn,
          'user' => $this->username,
          'pass' => $this->password,
        ];
    }

    public function __unserialize(array $data): void
    {
        $this->dsn = $data['dsn'];
        $this->username = $data['user'];
        $this->password = $data['pass'];

        $this->connect();
    }
}?>

    
```

## [\_\_sleep()](#object.sleep) y [\_\_wakeup()](#object.wakeup)

> [!WARNING]
> Este mecanismo de serialización está soft-deprecated a partir de PHP 8.5.0. Se mantiene por compatibilidad con versiones anteriores. Sin embargo, el código nuevo y existente debe migrarse para usar los métodos mágicos [\_\_serialize()](#object.serialize) y [\_\_unserialize()](#object.unserialize) en su lugar.

```php
public __sleep(): array
```php

```php
public __wakeup(): void
```

`serialize` verifica si la clase tiene un método con el nombre mágico [\_\_sleep()](#object.sleep). Si es así, este método será ejecutado antes de cualquier serialización. Puede limpiar el objeto, y se supone que devuelve un array con los nombres de todas las variables del objeto que deben ser serializadas. Si el método no devuelve nada, entonces `null` será serializado, y se emitirá una alerta de tipo `E_NOTICE`.

> [!NOTE]
> No es posible para [\_\_sleep()](#object.sleep) devolver nombres de propiedades privadas de las clases padres. Hacerlo resultará en un error de nivel `E_NOTICE`. Utilice [\_\_serialize()](#object.serialize) en su lugar.

> [!NOTE]
> A partir de PHP 8.0.0, devolver un valor que no sea un array desde [\_\_sleep()](#object.sleep) emite una advertencia. Anteriormente se emitía una notificación.

El propósito declarado de [\_\_sleep()](#object.sleep) es validar datos pendientes o realizar operaciones de limpieza. Además, esta función es útil si un objeto muy grande no necesita ser guardado en su totalidad.

Reciprocamente, la función `unserialize` verifica la presencia de un método cuyo nombre es el nombre mágico [\_\_wakeup()](#object.wakeup). Si está presente, esta función puede reconstruir cualquier recurso que el objeto pudiera poseer.

El propósito declarado de [\_\_wakeup()](#object.wakeup) es restablecer cualquier conexión de base de datos que se haya perdido durante la serialización y realizar tareas de reinicialización.

Uso de sleep() y wakeup()

```php
<?php
class Connection
{
    protected $link;
    private $dsn, $username, $password;

    public function __construct($dsn, $username, $password)
    {
        $this->dsn = $dsn;
        $this->username = $username;
        $this->password = $password;
        $this->connect();
    }

    private function connect()
    {
        $this->link = new PDO($this->dsn, $this->username, $this->password);
    }

    public function __sleep()
    {
        return array('dsn', 'username', 'password');
    }

    public function __wakeup()
    {
        $this->connect();
    }
}?>

   
```

## [\_\_toString()](#object.tostring)

```php
public __toString(): string
```php

El método [\_\_toString()](#object.tostring) determina cómo el objeto debe reaccionar cuando se trata como una cadena de caracteres. Por ejemplo, lo que `echo $obj;` mostrará.

> [!WARNING]
> A partir de PHP 8.0.0, el valor de retorno sigue las semánticas estándar de PHP, lo que significa que el valor será convertido en una `string` si es posible y si el [typing stricte](#language.types.declarations.strict) está desactivado.
>
> Un objeto Stringable *no* será aceptado por una declaración de tipo `string` si la [declaración de tipo estricta](#language.types.declarations.strict) está activada. Si se desea tal comportamiento, la declaración de tipo debe aceptar tanto Stringable como `string` a través de un tipo de unión.
>
> A partir de PHP 8.0.0, cualquier clase que contenga un método [\_\_toString()](#object.tostring) implementa también implícitamente la interfaz Stringable, y por lo tanto pasará las verificaciones de tipos para esta interfaz. Se recomienda implementar explícitamente la interfaz de todos modos.
>
> En PHP 7.4, el valor de retorno *debe* ser una `string`, de lo contrario se lanzará un `Error`.
>
> Anterior a PHP 7.4.0, el valor de retorno *debe* ser una `string`, de lo contrario se emitirá una `E_RECOVERABLE_ERROR` fatal.

> [!WARNING]
> Era imposible lanzar una excepción desde el método [\_\_toString()](#object.tostring) anterior a PHP 7.4.0. Esto resultaría en un error fatal.

Ejemplo simple

```
<?php
// Declaración de una clase simple
class ClasseTest
{
    public $foo;

    public function __construct($foo)
    {
        $this->foo = $foo;
    }

    public function __toString()
    {
        return $this->foo;
    }
}

$class = new ClasseTest('Bonjour');
echo $class;
?>

    
```php

El ejemplo anterior mostrará:

    Bonjour

## [\_\_invoke()](#object.invoke)

```php
__invoke(...$values): mixed
```

El método [\_\_invoke()](#object.invoke) es llamado cuando un script intenta llamar a un objeto como una función.

Ejemplo con [\_\_invoke()](#object.invoke)

```php
<?php
class CallableClass
{
    public function __invoke($x)
    {
        var_dump($x);
    }
}
$obj = new CallableClass;
$obj(5);
var_dump(is_callable($obj));
?>

    
```

El ejemplo anterior mostrará:

    int(5)
    bool(true)

Ejemplo con [\_\_invoke()](#object.invoke)

```php
<?php
class Sort
{
    private $key;

    public function __construct(string $key)
    {
        $this->key = $key;
    }

    public function __invoke(array $a, array $b): int
    {
        return $a[$this->key] <=> $b[$this->key];
    }
}

$customers = [
    ['id' => 1, 'first_name' => 'John', 'last_name' => 'Do'],
    ['id' => 3, 'first_name' => 'Alice', 'last_name' => 'Gustav'],
    ['id' => 2, 'first_name' => 'Bob', 'last_name' => 'Filipe']
];

// ordenar los clientes por nombre
usort($customers, new Sort('first_name'));
print_r($customers);

// ordenar los clientes por apellido
usort($customers, new Sort('last_name'));
print_r($customers);
?>

    
```

El ejemplo anterior mostrará:

         
    Array
    (
        [0] => Array
            (
                [id] => 3
                [first_name] => Alice
                [last_name] => Gustav
            )

        [1] => Array
            (
                [id] => 2
                [first_name] => Bob
                [last_name] => Filipe
            )

        [2] => Array
            (
                [id] => 1
                [first_name] => John
                [last_name] => Do
            )

    )
    Array
    (
        [0] => Array
            (
                [id] => 1
                [first_name] => John
                [last_name] => Do
            )

        [1] => Array
            (
                [id] => 2
                [first_name] => Bob
                [last_name] => Filipe
            )

        [2] => Array
            (
                [id] => 3
                [first_name] => Alice
                [last_name] => Gustav
            )

    )

## [\_\_set_state()](#object.set-state)

```php
static __set_state(array $properties): object
```php

Este método [estático](#language.oop5.static) es llamado para las clases exportadas por la función `var_export`.

El único parámetro de este método es un array que contiene las propiedades exportadas en la forma `['property' => value, ...]`.

Uso de [\_\_set_state()](#object.set-state)

```
class A
{
    public $var1;
    public $var2;

    public static function __set_state($an_array)
    {
        $obj = new A;
        $obj->var1 = $an_array['var1'];
        $obj->var2 = $an_array['var2'];
        return $obj;
    }
}

$a = new A;
$a->var1 = 5;
$a->var2 = 'foo';

$b = var_export($a, true);
var_dump($b);
eval('$c = ' . $b . ';');
var_dump($c);
?>

    
```php

El ejemplo anterior mostrará:

    string(60) "A::__set_state(array(
       'var1' => 5,
       'var2' => 'foo',
    ))"
    object(A)#2 (2) {
      ["var1"]=>
      int(5)
      ["var2"]=>
      string(3) "foo"
    }

> [!NOTE]
> Al exportar un objeto, `var_export` no verifica si [\_\_set_state()](#object.set-state) está implementada por la clase del objeto, por lo que la reimportación de objetos resultará en una excepción `Error`, si \_\_set_state() no está implementada. En particular, esto afecta a ciertas clases internas.
>
> Es responsabilidad del programador verificar que solo los objetos cuya clase implementa \_\_set_state() serán re-importados.

## [\_\_debugInfo()](#object.debuginfo)

```php
__debugInfo(): array
```

Este método es llamado por `var_dump` al procesar un objeto para recuperar las propiedades que deben ser mostradas. Si el método no está definido en un objeto, entonces todas las propiedades públicas, protegidas y privadas serán mostradas.

Uso de [\_\_debugInfo()](#object.debuginfo)

```php
<?php
class C {
    private $prop;

    public function __construct($val) {
        $this->prop = $val;
    }

    public function __debugInfo() {
        return [
            'propSquared' => $this->prop ** 2,
        ];
    }
}

var_dump(new C(42));
?>

    
```

El ejemplo anterior mostrará:

    object(C)#1 (1) {
      ["propSquared"]=>
      int(1764)
    }
