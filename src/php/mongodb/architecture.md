---
title: Arquitectura y funcionalidades especiales Explicaciones de la arquitectura
  del controlador y de las funcionalidades especiales
source_url: https://www.php.net/manual/es/mongodb.architecture.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/architecture.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 10e6a2b04
order: 47330
---

## Explicaciones de la arquitectura del controlador y de las funcionalidades especiales

## Visión general de la arquitectura

Este artículo explica cómo se integran todos los diferentes componentes del controlador PHP, desde las bibliotecas del sistema base, hasta la extensión, y las bibliotecas PHP en la parte superior.

<img src="en/reference/mongodb/images/driver_arch.svg" width="625" height="450" alt="El diagrama de la arquitectura del controlador MongoDB PHP. El nivel más bajo del controlador son nuestras bibliotecas del sistema: libmongoc, libbson, y libmongocrypt. El nivel intermedio es la extensión PHP MongoDB. El nivel superior es el código del usuario PHP e incluye la biblioteca MongoDB PHP y paquetes de nivel superior como las integraciones de marcos de trabajo y las aplicaciones." />

En la parte superior de esta pila se encuentra una [biblioteca PHP](https://github.com/mongodb/mongo-php-library), que distribuye un [paquete Composer](https://packagist.org/packages/mongodb/mongodb). Esta biblioteca proporciona una API coherente con otros [controladores](https://www.mongodb.com/docs/drivers/) MongoDB e implementa diversas [especificaciones](https://github.com/mongodb/specifications) cruzadas. Aunque la extensión puede ser utilizada directamente, la biblioteca tiene un sobrecoste mínimo y debería ser una dependencia común para la mayoría de las aplicaciones construidas con MongoDB.

Debajo de esta biblioteca se encuentra una extensión PHP, que se distribuye a través de [PECL](https://pecl.php.net/package/mongodb). La extensión forma la cola entre PHP y nuestras bibliotecas del sistema ([libmongoc](https://github.com/mongodb/mongo-c-driver), [libbson](https://github.com/mongodb/mongo-c-driver/tree/master/src/libbson), y [libmongocrypt](https://github.com/mongodb/libmongocrypt)). Su API pública proporciona únicamente las funcionalidades más esenciales: Gestión de conexiones, Codificación y decodificación BSON, Serialización y deserialización de documentos (soporte de bibliotecas ODM), Ejecución de comandos, consultas y operaciones de escritura, Gestión de cursores para los resultados de comandos y consultas

| Proyecto | GitHub | JIRA |
|----|----|----|
| Bibliotecas PHP | [mongodb/mongo-php-library](https://github.com/mongodb/mongo-php-library) | [PHPLIB](https://jira.mongodb.org/browse/PHPLIB) |
| Extensiones PHP | [mongodb/mongo-php-driver](https://github.com/mongodb/mongo-php-driver) | [PHPC](https://jira.mongodb.org/browse/PHPC) |

Código fuente del controlador y proyectos JIRA

## Gestión de la conexión y de la persistencia

> [!NOTE]
> En las plataformas Unix, la extensión MongoDB es sensible a los scripts que utilizan la llamada al sistema fork() sin llamar a exec(). No se deben reutilizar instancias `MongoDB\Driver\Manager` en un proceso hijo derivado de un fork.

### Conexiones y topología persistente (versión PHP desde 1.2.0)

Todas las versiones de la extensión desde 1.2.0 conservan el objeto cliente [libmongoc](https://github.com/mongodb/mongo-c-driver) en el proceso PHP, lo que le permite reutilizar las conexiones de base de datos, los estados de autenticación, *y* la información de topología a través de múltiples consultas.

Cuando MongoDB\Driver\Manager::\_\_construct es invocado, se crea un hash a partir de sus argumentos (es decir, la cadena URI y el array de opciones). La extensión intentará encontrar un objeto cliente [libmongoc](https://github.com/mongodb/mongo-c-driver) persistido previamente para este hash. Si no se puede encontrar un cliente existente para el hash, se creará un nuevo cliente y se persistirá para su uso futuro. Este comportamiento puede ser desactivado a través de la opción del controlador `"disableClientPersistence"`.

Cada cliente contiene sus propias conexiones de base de datos y una vista de la topología del servidor (por ejemplo, autónomo, conjunto de réplicas, grupo de fragmentos). Al persistir el cliente entre las consultas PHP, la extensión es capaz de reutilizar las conexiones de base de datos establecidas y eliminar la necesidad de [descubrir la topología del servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md) en cada consulta.

Considere el siguiente ejemplo:

```php
<?php

$managers = [
    new MongoDB\Driver\Manager('mongodb://127.0.0.1'),
    new MongoDB\Driver\Manager('mongodb://127.0.0.1'),
    new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017'),
    new MongoDB\Driver\Manager('mongodb://rs1.example.com,rs2.example.com/', ['replicaSet' => 'myReplicaSet']),
];

foreach ($managers as $manager) {
    $manager->executeCommand('test', new MongoDB\Driver\Command(['ping' => 1]));
}

?>

   
```

Los dos primeros objetos `Manager` compartirán el mismo cliente [libmongoc](https://github.com/mongodb/mongo-c-driver) ya que sus argumentos de constructor son idénticos. Los tercer y cuarto objetos utilizarán cada uno su propio cliente. En total, se crearán tres clientes y el proceso PHP ejecutando este script abrirá dos conexiones a `127.0.0.1` y una conexión a cada uno de `rs1.example.com` y `rs2.example.com`. Si la extensión descubre miembros adicionales del conjunto de réplicas después de emitir comandos `hello`, abrirá conexiones adicionales a estos servidores también.

Si las mismas conexiones son reutilizadas por el mismo proceso PHP, los tres clientes serán reutilizados y no se establecerá ninguna nueva conexión. En función del tiempo transcurrido desde la última consulta servida, la extensión puede necesitar emitir comandos `hello` adicionales para actualizar su vista de las topologías.

### Persistencia de sockets (versiones PHP antes de 1.2.0)

Las versiones de la extensión antes de 1.2.0 utilizan la API de flujos PHP para las conexiones de base de datos, utilizando una API en [libmongoc](https://github.com/mongodb/mongo-c-driver) para designar gestores personalizados para la comunicación por socket; sin embargo, se crea un nuevo cliente libmongoc para cada `MongoDB\Driver\Manager`. En consecuencia, la extensión persiste las conexiones de base de datos individuales pero no el estado de autentificación o la información de topología. Esto significa que la extensión debe emitir comandos al inicio de cada consulta para autenticarse y [descubrir la topología del servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md).

Las conexiones de base de datos son persistidas por un hash derivado del host del servidor, del puerto y de la cadena URI utilizada para construir el `MongoDB\Driver\Manager`. Las opciones del array del constructor no están incluidas en este hash.

> [!NOTE]
> Las versiones de la extensión \>= 1.1.8 y \< 1.2.0 no persisten los sockets para las conexiones SSL. Ver [PHPC-720](https://jira.mongodb.org/browse/PHPC-720) para más información.

A pesar de sus carencias con las conexiones SSL persistentes y la información de topología, esta versión de la extensión soporta todas las [opciones de contexto SSL](#context.ssl) ya que utiliza la API de flujos PHP.

## Serialización y deserialización de variables PHP en MongoDB

Este documento explica cómo se convierten las estructuras compuestas (es decir, los documentos, los arrays y los objetos) entre los valores BSON y PHP.

### Serialización en BSON

#### Arrays

Si un array es un *array compacto* — es decir, un array vacío o las claves comienzan en 0 y son secuenciales sin huecos : *array BSON*.

Si el array no es compacto — es decir, que tiene claves asociativas (cadenas), que las claves no comienzan en 0, o que hay huecos : *objeto BSON*.

Un documento de nivel superior (raíz), *siempre* serializado como documento BSON.

##### Ejemplos

Estos ejemplos se serializan como array BSON :

```php
[ 8, 5, 2, 3 ] => [ 8, 5, 2, 3 ]
[ 0 => 4, 1 => 9 ] => [ 4, 9 ]

     
```

Estos ejemplos se serializan como objeto BSON :

```php
[ 0 => 1, 2 => 8, 3 => 12 ] => { "0" : 1, "2" : 8, "3" : 12 }
[ "foo" => 42 ] => { "foo" : 42 }
[ 1 => 9, 0 => 10 ] => { "1" : 9, "0" : 10 }

     
```

Es de notar que los cinco ejemplos son *extractos* de un documento completo, y solo representan un *valor* dentro de un documento.

#### Objetos

Si un objeto es de la clase `stdClass`, serializar como *documento BSON*.

Si un objeto es una clase soportada que implementa MongoDB\BSON\Type, entonces utilizar la lógica de serialización BSON para este tipo específico. Las instancias de MongoDB\BSON\Type (a excepción de MongoDB\BSON\Serializable) solo pueden ser serializadas como valor de campo de documento. Intentar serializar tal objeto como documento raíz lanzará una `MongoDB\Driver\Exception\UnexpectedValueException`.

Si un objeto es de una clase desconocida que implementa la interfaz MongoDB\BSON\Type, entonces se lanza una `MongoDB\Driver\Exception\UnexpectedValueException`.

Si un objeto es de otra clase, sin implementar una interfaz especial, serializar como *documento BSON*. Mantener solo las propiedades *públicas*, e ignorar las propiedades *protegidas* y *privadas*.

Si un objeto es de una clase que implementa MongoDB\BSON\Serializable, llamar MongoDB\BSON\Serializable::bsonSerialize y utilizar el array o `stdClass` devuelto para serializar como documento BSON o array. El tipo BSON será determinado por las siguientes reglas :

1.  Los documentos raíz deben ser serializados como documento BSON.

2.  Los objetos MongoDB\BSON\Persistable deben ser serializados como documento BSON.

3.  Si MongoDB\BSON\Serializable::bsonSerialize devuelve un array compacto, serializar como array BSON.

4.  Si MongoDB\BSON\Serializable::bsonSerialize devuelve un array no compacto o `stdClass`, serializar como objeto BSON.

5.  Si MongoDB\BSON\Serializable::bsonSerialize no devuelve un array o `stdClass`, lanzar una excepción `MongoDB\Driver\Exception\UnexpectedValueException`.

Si un objeto es de una clase que implementa la interfaz MongoDB\BSON\Persistable (lo que implica MongoDB\BSON\Serializable), obtener las propiedades de manera similar a los párrafos anteriores, pero *también* añadir una propiedad \_\_pclass como valor binario, con un subtipo `0x80` y datos que llevan el nombre de la clase completamente calificado del objeto que se serializa.

La propiedad \_\_pclass se añade al array o al objeto devuelto por MongoDB\BSON\Serializable::bsonSerialize, lo que significa que sobrescribirá cualquier clave/propiedad \_\_pclass en el valor de retorno de MongoDB\BSON\Serializable::bsonSerialize. Si se desea evitar este comportamiento y definir su propio valor \_\_pclass, no se debe *implementar* MongoDB\BSON\Persistable y se debería implementar MongoDB\BSON\Serializable directamente.

##### Ejemplos

```php
<?php

class stdClass
{
    public $foo = 42;
} // => {"foo": 42}

class MyClass
{
    public $foo = 42;
    protected $prot = 'wine';
    private $fpr = 'cheese';
} // => {"foo": 42}

class AnotherClass1 implements MongoDB\BSON\Serializable
{
    public $foo = 42;
    protected $prot = 'wine';
    private $fpr = 'cheese';

    public function bsonSerialize(): array
    {
        return ['foo' => $this->foo, 'prot' => $this->prot];
    }
} // => {"foo": 42, "prot": "wine"}

class AnotherClass2 implements MongoDB\BSON\Serializable
{
    public $foo = 42;

    public function bsonSerialize(): self
    {
        return $this;
    }
} // => MongoDB\Driver\Exception\UnexpectedValueException("bsonSerialize() did not return an array or stdClass")

class AnotherClass3 implements MongoDB\BSON\Serializable
{
    private $elements = ['foo', 'bar'];

    public function bsonSerialize(): array
    {
        return $this->elements;
    }
} // => {"0": "foo", "1": "bar"}

/**
 * Nesting Serializable classes
 */

class AnotherClass4 implements MongoDB\BSON\Serializable
{
    private $elements = [0 => 'foo', 2 => 'bar'];

    public function bsonSerialize(): array
    {
        return $this->elements;
    }
} // => {"0": "foo", "2": "bar"}

class ContainerClass1 implements MongoDB\BSON\Serializable
{
    public $things;

    public function __construct()
    {
        $this->things = new AnotherClass4();
    }

    function bsonSerialize(): array
    {
        return ['things' => $this->things];
    }
} // => {"things": {"0": "foo", "2": "bar"}}

class AnotherClass5 implements MongoDB\BSON\Serializable
{
    private $elements = [0 => 'foo', 2 => 'bar'];

    public function bsonSerialize(): array
    {
        return array_values($this->elements);
    }
} // => {"0": "foo", "1": "bar"} como clase raíz
  //        ["foo", "bar"] como valor anidado

class ContainerClass2 implements MongoDB\BSON\Serializable
{
    public $things;

    public function __construct()
    {
        $this->things = new AnotherClass5();
    }

    public function bsonSerialize(): array
    {
        return ['things' => $this->things];
    }
} // => {"things": ["foo", "bar"]}

class AnotherClass6 implements MongoDB\BSON\Serializable
{
    private $elements = ['foo', 'bar'];

    function bsonSerialize(): object
    {
        return (object) $this->elements;
    }
} // => {"0": "foo", "1": "bar"}

class ContainerClass3 implements MongoDB\BSON\Serializable
{
    public $things;

    public function __construct()
    {
        $this->things = new AnotherClass6();
    }

    public function bsonSerialize(): array
    {
        return ['things' => $this->things];
    }
} // => {"things": {"0": "foo", "1": "bar"}}

class UpperClass implements MongoDB\BSON\Persistable
{
    public $foo = 42;
    protected $prot = 'wine';
    private $fpr = 'cheese';

    private $data;

    public function bsonUnserialize(array $data): void
    {
        $this->data = $data;
    }

    public function bsonSerialize(): array
    {
        return ['foo' => $this->foo, 'prot' => $this->prot];
    }
} // => {"foo": 42, "prot": "wine", "__pclass": {"$type": "80", "$binary": "VXBwZXJDbGFzcw=="}}

?>

     
```

### Deserialización desde BSON

> [!WARNING]
> Los documentos BSON pueden contener técnicamente claves duplicadas ya que los documentos se almacenan como una lista de pares clave-valor; sin embargo, las aplicaciones deben abstenerse de generar documentos con claves duplicadas ya que el comportamiento del servidor y del controlador puede ser indefinido. Dado que los objetos y arrays de PHP no pueden tener claves duplicadas, los datos también podrían perderse al decodificar un documento BSON con claves duplicadas.

La extensión `mongodb` deserializa los documentos BSON y los arrays BSON como arrays PHP. Aunque los arrays PHP son prácticos de usar, este comportamiento era problemático ya que diferentes tipos BSON podían ser deserializados en el mismo valor PHP (por ejemplo `{"0": "foo"}` y `["foo"]`) y hacía imposible inferir el tipo BSON original. Por defecto, la extensión `mongodb` aborda esta preocupación asegurándose de que los arrays BSON y los documentos BSON se conviertan en arrays y objetos PHP, respectivamente.

Para los tipos compuestos, existen tres tipos de datos :

raíz  
se refiere a un documento BSON de nivel superior *solo*

documento  
se refiere a documentos BSON anidados *solo*

array  
se refiere a un array BSON

Además de los tres tipos colectivos, también es posible configurar campos específicos en su documento para mapear los tipos de datos mencionados a continuación. Por ejemplo, el siguiente tipo de mapa le permite mapear cada documento incrustado en un array `"addresses"` a una clase `Address` *y* cada campo `"city"` en estos documentos de dirección incrustados a una clase `City`:

```php
[
    'fieldPaths' => [
        'addresses.$' => 'MyProject\Address',
        'addresses.$.city' => 'MyProject\City',
    ],
]

    
```

Cada uno de estos tres tipos de datos, así como los mapeos específicos de los campos, pueden ser mapeados contra diferentes tipos PHP. Los valores de mapeo posibles son:

*no definido* o `NULL` (por defecto)  
- Un array BSON será deserializado en un `array` PHP.

- Un documento BSON (raíz o anidado) sin propiedad \_\_pclass [^1] se convierte en un objeto `stdClass`, con cada clave de documento BSON definida como una propiedad de `stdClass` pública.

- Un documento BSON (raíz o anidado) con una propiedad \_\_pclass se convierte en un objeto PHP de la clase nombrada por la propiedad \_\_pclass.

  Si la clase nombrada implementa la interfaz MongoDB\BSON\Persistable, entonces las propiedades del documento BSON, incluyendo la propiedad \_\_pclass, se envían como array asociativo a la función MongoDB\BSON\Unserializable::bsonUnserialize para inicializar las propiedades del objeto.

  Si la clase nombrada no existe o no implementa la interfaz MongoDB\BSON\Persistable, `stdClass` será utilizado y cada clave de documento BSON (incluyendo \_\_pclass) será definida como una propiedad pública de `stdClass`.

  La funcionalidad \_\_pclass se basa en el hecho de que la propiedad sea parte de un documento MongoDB recuperado. Si utiliza una [proyección](#mongodb-driver-query.construct-queryOptions) al buscar documentos, debe incluir el campo \_\_pclass en la proyección para que esta funcionalidad funcione.

`"array"`  
Transforma un array BSON en un `array` PHP. No habrá tratamiento especial de una propiedad \_\_pclass pero puede ser definida como un elemento en el array devuelto si estaba presente en el documento BSON.

`"object"` o `"stdClass"`  
Transforma un array BSON o un documento BSON en un objeto `stdClass`. No habrá tratamiento especial de una propiedad \_\_pclass pero puede ser definida como una propiedad pública en el objeto devuelto si estaba presente en el documento BSON.

`"bson"`  
Transforma un array BSON en un `MongoDB\BSON\PackedArray` y un documento BSON en un `MongoDB\BSON\Document`, independientemente de si el documento BSON tiene una propiedad \_\_pclass .

> [!NOTE]
> El valor `bson` solo está disponible para los tres tipos raíz, y no en los mapeos específicos de los campos.

todas las otras cadenas de caracteres  
Define el nombre de la clase a la que el documento BSON debe ser deserializado. Para los documentos BSON que incluyen propiedades \_\_pclass, esta clase tendrá prioridad.

Si la clase nombrada no existe o no implementa la interfaz MongoDB\BSON\Unserializable, se lanza una excepción `MongoDB\Driver\Exception\InvalidArgumentException`.

Si el objeto BSON tiene una propiedad \_\_pclass y esta clase existe e implementa MongoDB\BSON\Persistable, tendrá prioridad sobre la clase proporcionada en el mapa de tipos.

Las propiedades del documento BSON, *incluyendo* la propiedad \_\_pclass, serán enviadas como array asociativo a la función MongoDB\BSON\Unserializable::bsonUnserialize para inicializar las propiedades del objeto.

#### TypeMaps

Los TypeMaps pueden ser definidos a través del método MongoDB\Driver\Cursor::setTypeMap en un objeto `MongoDB\Driver\Cursor`, o el argumento `$typeMap` de `MongoDB\BSON\toPHP`, MongoDB\BSON\Document::toPHP, y MongoDB\BSON\PackedArray::toPHP. Cada una de las tres clases (*raíz*, *documento*, y *array*) puede ser definida individualmente, además de los tipos específicos de los campos.

Si el valor en el TypeMap es `NULL`, esto significa lo mismo que el valor *por defecto* para este elemento.

#### Ejemplos

Estos ejemplos utilizan las siguientes clases:

MyClass  
que no implementa *ninguna* interfaz

YourClass  
que implementa MongoDB\BSON\Unserializable

OurClass  
que implementa MongoDB\BSON\Persistable

TheirClass  
que extiende OurClass

El método MongoDB\BSON\Unserializable::bsonUnserialize de YourClass, OurClass, TheirClass itera sobre el array y define las propiedades sin modificaciones. También *añade* la propiedad `$unserialized` a `true`:

```php
<?php

function bsonUnserialize( array $map )
{
    foreach ( $map as $k => $value )
    {
        $this->$k = $value;
    }
    $this->unserialized = true;
}

      
```

```php
/* typemap: [] (todos los valores por defecto) */
{ "foo": "yes", "bar" : false }
  -> stdClass { $foo => 'yes', $bar => false }

{ "foo": "no", "array" : [ 5, 6 ] }
  -> stdClass { $foo => 'no', $array => [ 5, 6 ] }

{ "foo": "no", "obj" : { "embedded" : 3.14 } }
  -> stdClass { $foo => 'no', $obj => stdClass { $embedded => 3.14 } }

{ "foo": "yes", "__pclass": "MyClass" }
  -> stdClass { $foo => 'yes', $__pclass => 'MyClass' }

{ "foo": "yes", "__pclass": { "$type" : "80", "$binary" : "MyClass" } }
  -> stdClass { $foo => 'yes', $__pclass => Binary(0x80, 'MyClass') }

{ "foo": "yes", "__pclass": { "$type" : "80", "$binary" : "YourClass") }
  -> stdClass { $foo => 'yes', $__pclass => Binary(0x80, 'YourClass') }

{ "foo": "yes", "__pclass": { "$type" : "80", "$binary" : "OurClass") }
  -> OurClass { $foo => 'yes', $__pclass => Binary(0x80, 'OurClass'), $unserialized => true }

{ "foo": "yes", "__pclass": { "$type" : "44", "$binary" : "YourClass") }
  -> stdClass { $foo => 'yes', $__pclass => Binary(0x44, 'YourClass') }

      
```

```php
/* typemap: [ "root" => "MissingClass" ] */
{ "foo": "yes" }
  -> MongoDB\Driver\Exception\InvalidArgumentException("MissingClass does not exist")

/* typemap: [ "root" => "MyClass" ] */
{ "foo": "yes", "__pclass" : { "$type": "80", "$binary": "MyClass" } }
  -> MongoDB\Driver\Exception\InvalidArgumentException("MyClass does not implement Unserializable interface")

/* typemap: [ "root" => "MongoDB\BSON\Unserializable" ] */
{ "foo": "yes" }
  -> MongoDB\Driver\Exception\InvalidArgumentException("Unserializable is not a concrete class")

/* typemap: [ "root" => "YourClass" ] */
{ "foo": "yes", "__pclass" : { "$type": "80", "$binary": "MongoDB\BSON\Unserializable" } }
  -> YourClass { $foo => "yes", $__pclass => Binary(0x80, "MongoDB\BSON\Unserializable"), $unserialized => true }

/* typemap: [ "root" => "YourClass" ] */
{ "foo": "yes", "__pclass" : { "$type": "80", "$binary": "MyClass" } }
  -> YourClass { $foo => "yes", $__pclass => Binary(0x80, "MyClass"), $unserialized => true }

/* typemap: [ "root" => "YourClass" ] */
{ "foo": "yes", "__pclass" : { "$type": "80", "$binary": "OurClass" } }
  -> OurClass { $foo => "yes", $__pclass => Binary(0x80, "OurClass"), $unserialized => true }

/* typemap: [ "root" => "YourClass" ] */
{ "foo": "yes", "__pclass" : { "$type": "80", "$binary": "TheirClass" } }
  -> TheirClass { $foo => "yes", $__pclass => Binary(0x80, "TheirClass"), $unserialized => true }

/* typemap: [ "root" => "OurClass" ] */
{ foo: "yes", "__pclass" : { "$type": "80", "$binary": "TheirClass" } }
  -> TheirClass { $foo => "yes", $__pclass => Binary(0x80, "TheirClass"), $unserialized => true }

      
```

```php
/* typemap: [ 'root' => 'YourClass' ] */
{ foo: "yes", "__pclass" : { "$type": "80", "$binary": "YourClass" } }
  -> YourClass { $foo => 'yes', $__pclass => Binary(0x80, 'YourClass'), $unserialized => true }

      
```

```php
/* typemap: [ 'root' => 'array', 'document' => 'array' ] */
{ "foo": "yes", "bar" : false }
  -> [ "foo" => "yes", "bar" => false ]

{ "foo": "no", "array" : [ 5, 6 ] }
  -> [ "foo" => "no", "array" => [ 5, 6 ] ]

{ "foo": "no", "obj" : { "embedded" : 3.14 } }
  -> [ "foo" => "no", "obj" => [ "embedded => 3.14 ] ]

{ "foo": "yes", "__pclass": "MyClass" }
  -> [ "foo" => "yes", "__pclass" => "MyClass" ]

{ "foo": "yes", "__pclass" : { "$type": "80", "$binary": "MyClass" } }
  -> [ "foo" => "yes", "__pclass" => Binary(0x80, "MyClass") ]

{ "foo": "yes", "__pclass" : { "$type": "80", "$binary": "OurClass" } }
  -> [ "foo" => "yes", "__pclass" => Binary(0x80, "OurClass") ]

      
```

```php
/* typemap: [ 'root' => 'object', 'document' => 'object' ] */
{ "foo": "yes", "__pclass": { "$type": "80", "$binary": "MyClass" } }
  -> stdClass { $foo => "yes", "__pclass" => Binary(0x80, "MyClass") }

      
```

[^1]: Una propiedad \_\_pclass solo se considera existente si una propiedad con ese nombre existe, y es un valor binario, y el subtipo del valor binario es 0x80. Si alguna de estas tres condiciones no se cumple, la propiedad \_\_pclass no existe y debe ser tratada como cualquier otra propiedad normal.
