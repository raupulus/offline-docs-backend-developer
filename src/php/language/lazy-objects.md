---
title: Objetos perezosos
source_url: https://www.php.net/manual/es/language.oop5.lazy-objects.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/lazy-objects.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: ee1ce6a0e
order: 2510
---

## Objetos perezosos

Un objeto perezoso es un objeto cuya inicialización se retrasa hasta que su estado sea observado o modificado. Algunos ejemplos de uso incluyen componentes de inyección de dependencias que proporcionan servicios perezosos completamente inicializados solo si es necesario, ORMs que proporcionan entidades perezosas que se hidratan desde la base de datos solo cuando se accede a ellas, o un analizador JSON que retrasa el análisis hasta que se accede a los elementos.

Se admiten dos estrategias de objetos perezosos: los objetos fantasma (Ghost) y los proxys virtuales (Virtual Proxies), a continuación denominados "fantasmas perezosos" y "proxys perezosos". En ambas estrategias, el objeto perezoso se adjunta a un inicializador o a una fábrica que se llama automáticamente cuando su estado es observado o modificado por primera vez. Desde el punto de vista de la abstracción, los objetos perezosos son indiscernibles de los no perezosos: pueden ser utilizados sin saber que son perezosos, lo que permite pasarlos y utilizarlos en código que no es consciente de la pereza. Los proxys perezosos también son transparentes, pero hay que tener cuidado cuando se utiliza su identidad, ya que el proxy y su instancia real tienen identidades diferentes.

> [!NOTE]
> Los objetos perezosos fueron introducidos en PHP 8.4.

## Creación de objetos perezosos

Es posible crear una instancia perezosa de cualquier clase definida por el usuario o de la clase `stdClass` (otras clases internas no son admitidas), o reinicializar una instancia de estas clases para que sea perezosa. Los puntos de entrada para crear un objeto perezoso son los métodos ReflectionClass::newLazyGhost y ReflectionClass::newLazyProxy.

Ambos métodos aceptan una función que se llama cuando el objeto necesita inicialización. El comportamiento esperado de la función varía en función de la estrategia utilizada, como se describe en la documentación de referencia de cada método.

Creación de un fantasma perezoso

```php
<?php
class Example
{
    public function __construct(public int $prop)
    {
        echo __METHOD__, "\n";
    }
}

$reflector = new ReflectionClass(Example::class);
$lazyObject = $reflector->newLazyGhost(function (Example $object) {
    // Inicializa el objeto en el lugar
    $object->__construct(1);
});

var_dump($lazyObject);
var_dump(get_class($lazyObject));

// Desencadena la inicialización
var_dump($lazyObject->prop);
?>

   
```

El ejemplo anterior mostrará:

    lazy ghost object(Example)#3 (0) {
    ["prop"]=>
    uninitialized(int)
    }
    string(7) "Example"
    Example::__construct
    int(1)

Creación de un proxy perezoso

```php
<?php
class Example
{
    public function __construct(public int $prop)
    {
        echo __METHOD__, "\n";
    }
}

$reflector = new ReflectionClass(Example::class);
$lazyObject = $reflector->newLazyProxy(function (Example $object) {
    // Crea y devuelve la instancia real
    return new Example(1);
});

var_dump($lazyObject);
var_dump(get_class($lazyObject));

// Desencadena la inicialización
var_dump($lazyObject->prop);
?>

   
```

El ejemplo anterior mostrará:

    lazy proxy object(Example)#3 (0) {
      ["prop"]=>
      uninitialized(int)
    }
    string(7) "Example"
    Example::__construct
    int(1)

Cualquier acceso a las propiedades de un objeto perezoso desencadena su inicialización (incluyendo a través de `ReflectionProperty`). Sin embargo, algunas propiedades pueden ser conocidas de antemano y no deberían desencadenar la inicialización cuando se accede a ellas:

Inicialización de las propiedades de manera impaciente

```php
<?php
class BlogPost
{
    public function __construct(
       public int $id,
       public string $title,
       public string $content,
    ) { }
}

$reflector = new ReflectionClass(BlogPost::class);

$post = $reflector->newLazyGhost(function ($post) {
    $data = fetch_from_store($post->id);
    $post->__construct($data['id'], $data['title'], $data['content']);
});

// Sin esta línea, la siguiente llamada a ReflectionProperty::setValue() desencadenaría la inicialización.
$reflector->getProperty('id')->skipLazyInitialization($post);
$reflector->getProperty('id')->setValue($post, 123);

// Asimismo, se puede utilizar esto directamente:
$reflector->getProperty('id')->setRawValueWithoutLazyInitialization($post, 123);

// El identificador puede ser accedido sin desencadenar la inicialización
var_dump($post->id);
?>

   
```

Los métodos ReflectionProperty::skipLazyInitialization y ReflectionProperty::setRawValueWithoutLazyInitialization ofrecen formas de evitar la inicialización perezosa al acceder a una propiedad.

## Acerca de las estrategias de objetos perezosos

Los *fantasmas perezosos* son objetos que se inicializan en el lugar y, una vez inicializados, son indiscernibles de un objeto que nunca fue perezoso. Esta estrategia es adecuada cuando se controla tanto la instanciación como la inicialización del objeto y es inadecuada si alguna de estas operaciones es gestionada por otra parte.

Los *proxys perezosos*, una vez inicializados, actúan como proxys hacia una instancia real: cualquier operación en un proxy perezoso inicializado es transmitida a la instancia real. La creación de la instancia real puede ser delegada a otra parte, lo que hace que esta estrategia sea útil en los casos en que los fantasmas perezosos son inadecuados. Aunque los proxys perezosos son casi tan transparentes como los fantasmas perezosos, hay que tener cuidado cuando se utiliza su identidad, ya que el proxy y su instancia real tienen identidades distintas.

## Ciclo de vida de los objetos perezosos

Los objetos pueden ser hechos perezosos durante la instanciación utilizando ReflectionClass::newLazyGhost o ReflectionClass::newLazyProxy, o después de la instanciación utilizando ReflectionClass::resetAsLazyGhost o ReflectionClass::resetAsLazyProxy. Luego, un objeto perezoso puede ser inicializado por una de las siguientes operaciones:

Interactuar con el objeto de una manera que desencadene la inicialización automática. Ver

desencadenantes de inicialización

.

Marcar todas sus propiedades como no perezosas utilizando

ReflectionProperty::skipLazyInitialization

o

ReflectionProperty::setRawValueWithoutLazyInitialization

.

Llamar explícitamente a

ReflectionClass::initializeLazyObject

o

ReflectionClass::markLazyObjectAsInitialized

.

Como los objetos perezosos se inicializan cuando todas sus propiedades son marcadas como no perezosas, los métodos anteriores no marcarán un objeto como perezoso si ninguna propiedad puede ser marcada como perezosa.

## Desencadenantes de inicialización

Los objetos perezosos están diseñados para ser completamente transparentes para sus consumidores, de modo que las operaciones normales que observan o modifican el estado del objeto desencadenarán automáticamente la inicialización antes de que se realice la operación. Esto incluye, pero no se limita a, las siguientes operaciones:

Leer o escribir una propiedad

Probar si una propiedad está definida o definirla.

Acceder o modificar una propiedad a través de

ReflectionProperty::getValue

,

ReflectionProperty::getRawValue

,

ReflectionProperty::setValue

, o

ReflectionProperty::setRawValue

.

Listar las propiedades con

ReflectionObject::getProperties

,

ReflectionObject::getProperty

,

get_object_vars

.

Iterar sobre las propiedades de un objeto que no implementa

Iterator

o

IteratorAggregate

utilizando

foreach

.

Serializar el objeto con

serialize

,

json_encode

, etc.

Clonar

el objeto.

Las llamadas a métodos que no acceden al estado del objeto no desencadenarán la inicialización. Asimismo, las interacciones con el objeto que invocan métodos mágicos o funciones de gancho no desencadenarán la inicialización si estos métodos o funciones no acceden al estado del objeto.

### Operaciones no desencadenantes

Las siguientes operaciones o métodos específicos permiten acceder o modificar objetos perezosos sin desencadenar la inicialización:

Marcar las propiedades como no perezosas con

ReflectionProperty::skipLazyInitialization

o

ReflectionProperty::setRawValueWithoutLazyInitialization

.

Recuperar la representación interna de las propiedades utilizando

get_mangled_object_vars

o

convirtiendo el objeto en un array

.

Utilizando

serialize

cuando

ReflectionClass::SKIP_INITIALIZATION_ON_SERIALIZE

está definido, a menos que

\_\_serialize()

o

\_\_sleep()

desencadenen la inicialización.

Llamar a

ReflectionObject::\_\_toString

.

Utilizar

var_dump

o

debug_zval_dump

, a menos que

\_\_debugInfo()

desencadene la inicialización

## Secuencia de inicialización

Esta sección describe la secuencia de operaciones realizadas cuando se desencadena una inicialización, en función de la estrategia utilizada.

### Objetos fantasma

El objeto es marcado como no perezoso.

Las propiedades no inicializadas con

ReflectionProperty::skipLazyInitialization

o

ReflectionProperty::setRawValueWithoutLazyInitialization

se establecen en sus valores por defecto, si corresponde. En este punto, el objeto se asemeja a un objeto creado con

ReflectionClass::newInstanceWithoutConstructor

, excepto por las propiedades ya inicializadas.

La función de inicialización es llamada luego con el objeto como primer parámetro. La función debe, pero no está obligada, inicializar el estado del objeto, y debe devolver

null

o ningún valor. El objeto ya no es perezoso en este punto, por lo que la función puede acceder directamente a sus propiedades.

Después de la inicialización, el objeto es indiscernible de un objeto que nunca fue perezoso.

### Objetos proxy

El objeto es marcado como no perezoso.

A diferencia de los objetos fantasma, las propiedades del objeto no se modifican en esta etapa.

La función fabrica es llamada con el objeto como primer parámetro y debe devolver una instancia no perezosa de una clase compatible (ver

ReflectionClass::newLazyProxy

).

La instancia devuelta es llamada

instancia real

y se adjunta al proxy.

Los valores de las propiedades del proxy son descartados como si

unset

es llamado.

Después de la inicialización, el acceso a cualquier propiedad en el proxy dará el mismo resultado que el acceso a la propiedad correspondiente en la instancia real; todos los accesos a las propiedades en el proxy son transmitidos a la instancia real, incluyendo las propiedades declaradas, dinámicas, inexistentes, o las propiedades marcadas con ReflectionProperty::skipLazyInitialization o ReflectionProperty::setRawValueWithoutLazyInitialization.

El objeto proxy en sí mismo *no* es reemplazado o sustituido por la instancia real.

Aunque la fabrica recibe el proxy como primer parámetro, no se espera que lo modifique (las modificaciones están permitidas pero serán perdidas en la etapa final de inicialización). Sin embargo, el proxy puede ser utilizado para decisiones basadas en los valores de las propiedades inicializadas, la clase, el objeto mismo, o su identidad. Por ejemplo, el inicializador podría utilizar el valor de una propiedad inicializada durante la creación de la instancia real.

### Comportamiento común

El alcance y el contexto `$this` de la función de inicialización o de la fabrica permanecen sin cambios, y se aplican las restricciones de visibilidad habituales.

Después de una inicialización exitosa, la función de inicialización o la fabrica ya no es referenciada por el objeto y puede ser liberada si no tiene otras referencias.

Si la inicialización lanza una excepción, el estado del objeto se restaura a su estado pre-inicialización y el objeto es marcado nuevamente como perezoso. En otras palabras, todos los efectos en el objeto mismo son anulados. Otros efectos secundarios, como los efectos en otros objetos, no son anulados. Esto evita la exposición de una instancia parcialmente inicializada en caso de fallo.

## Clonación

[Clonar](#language.oop5.cloning) un objeto perezoso desencadena su inicialización antes de que el clon sea creado, resultando en un objeto inicializado.

Para los objetos proxy, el proxy y su instancia real son clonados, y el clon del proxy es devuelto. La método [`__clone`](#object.clone) es llamada en la instancia real, no en el proxy. El proxy clonado y la instancia real clonada están enlazados como lo están durante la inicialización, por lo que los accesos al clon del proxy son transmitidos al clon de la instancia real.

Este comportamiento garantiza que el clon y el objeto original mantengan estados separados. Las modificaciones realizadas en el objeto original o en el estado de su inicializador después de la clonación no afectan al clon. Clonar tanto el proxy como su instancia real, en lugar de devolver un clon de la instancia real solamente, garantiza que la operación de clonación devuelva sistemáticamente un objeto de la misma clase.

## Destructores

Para los objetos perezosos, el destructor solo es llamado si el objeto ha sido inicializado. Para los proxys, el destructor solo es llamado en la instancia real, si existe.

Los métodos ReflectionClass::resetAsLazyGhost y ReflectionClass::resetAsLazyProxy pueden invocar el destructor del objeto reinicializado.
