---
title: Atributos
source_url: https://www.php.net/manual/es/language.attributes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/attributes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 50e6f42c8
order: 1960
---

## Atributos

## Descripción general de atributos

Los atributos de PHP ofrecen metadatos estructurados y legibles por máquinas para clases, métodos, funciones, parámetros, propiedades y constantes. Pueden ser inspeccionados en tiempo de ejecución a través de la [API de Reflection](#book.reflection), lo que permite un comportamiento dinámico sin modificar el código. Los atributos proporcionan una forma declarativa de anotar el código con metadatos.

Los atributos permiten desacoplar la implementación de una funcionalidad de su uso. Mientras que las interfaces definen la estructura mediante la imposición de métodos, los atributos proporcionan metadatos en varios elementos, incluidos métodos, funciones, propiedades y constantes. A diferencia de las interfaces, que obligan a implementar métodos, los atributos anotan el código sin alterar su estructura.

Los atributos pueden complementar o reemplazar métodos opcionales de una interfaz al proporcionar metadatos en lugar de una estructura impuesta. Considera una interfaz `ActionHandler` que representa una operación en una aplicación. Algunas implementaciones pueden necesitar un paso de configuración, mientras que otras no. En lugar de obligar a todas las clases que implementan `ActionHandler` a definir un método `setUp()`, un atributo puede indicar los requisitos de configuración. Este enfoque aumenta la flexibilidad, permitiendo que los atributos se apliquen varias veces cuando sea necesario.

Implementación de métodos opcionales de una interfaz mediante atributos

```php
<?php
interface ActionHandler
{
    public function execute();
}

#[Attribute]
class SetUp {}

class CopyFile implements ActionHandler
{
    public string $fileName;
    public string $targetDirectory;

    #[SetUp]
    public function fileExists()
    {
        if (!file_exists($this->fileName)) {
            throw new RuntimeException("El archivo no existe");
        }
    }

    #[SetUp]
    public function targetDirectoryExists()
    {
        if (!file_exists($this->targetDirectory)) {
            mkdir($this->targetDirectory);
        } elseif (!is_dir($this->targetDirectory)) {
            throw new RuntimeException("El directorio de destino $this->targetDirectory no es un directorio");
        }
    }

    public function execute()
    {
        copy($this->fileName, $this->targetDirectory . '/' . basename($this->fileName));
    }
}

function executeAction(ActionHandler $actionHandler)
{
    $reflection = new ReflectionObject($actionHandler);

    foreach ($reflection->getMethods() as $method) {
        $attributes = $method->getAttributes(SetUp::class);

        if (count($attributes) > 0) {
            $methodName = $method->getName();

            $actionHandler->$methodName();
        }
    }

    $actionHandler->execute();
}

$copyAction = new CopyFile();
$copyAction->fileName = "/tmp/foo.jpg";
$copyAction->targetDirectory = "/home/user";

executeAction($copyAction);

     
```

## Sintaxis de atributos

La sintaxis de atributos consta de varios componentes clave. Una declaración de atributo comienza con `#[` y termina con `]`. Dentro de esta, se pueden listar uno o más atributos, separados por comas. El nombre del atributo puede ser no cualificado, cualificado o totalmente cualificado, como se describe en [Uso de los espacios de nombres: lo básico](#language.namespaces.basics). Los argumentos para el atributo son opcionales y se encierran entre paréntesis `()`. Los argumentos solo pueden ser valores literales o expresiones constantes. Se admite la sintaxis de argumentos posicionales y nombrados.

Los nombres de los atributos y sus argumentos se resuelven en una clase, y los argumentos se pasan a su constructor cuando se solicita una instancia del atributo a través de la API de Reflection. Por lo tanto, se recomienda crear una clase para cada atributo.

Sintaxis de atributos

```php
<?php
// a.php
namespace MyExample;

use Attribute;

#[Attribute]
class MyAttribute
{
    const VALUE = 'value';

    private $value;

    public function __construct($value = null)
    {
        $this->value = $value;
    }
}

// b.php

namespace Another;

use MyExample\MyAttribute;

#[MyAttribute]
#[\MyExample\MyAttribute]
#[MyAttribute(1234)]
#[MyAttribute(value: 1234)]
#[MyAttribute(MyAttribute::VALUE)]
#[MyAttribute(array("key" => "value"))]
#[MyAttribute(100 + 200)]
class Thing
{
}

#[MyAttribute(1234), MyAttribute(5678)]
class AnotherThing
{
}

    
```

## Lectura de atributos con la API de Reflection

Para acceder a los atributos de clases, métodos, funciones, parámetros, propiedades y constantes de clase, utiliza el método `getAttributes` proporcionado por la API de Reflection. Este método devuelve un array de instancias de `ReflectionAttribute`. Estas instancias pueden consultarse para obtener el nombre del atributo, los argumentos, y también pueden usarse para instanciar una instancia del atributo representado.

Separar la representación reflejada del atributo de su instancia real proporciona un mayor control sobre la gestión de errores, como clases de atributos faltantes, argumentos mal escritos, o valores ausentes. Los objetos de la clase de atributo se instancian solo después de llamar a `ReflectionAttribute::newInstance`, lo que garantiza que la validación de los argumentos se realice en ese momento.

Lectura de atributos con la API de Reflection

```php
<?php

#[Attribute]
class MyAttribute
{
    public $value;

    public function __construct($value)
    {
        $this->value = $value;
    }
}

#[MyAttribute(value: 1234)]
class Thing
{
}

function dumpAttributeData($reflection) {
    $attributes = $reflection->getAttributes();

    foreach ($attributes as $attribute) {
       var_dump($attribute->getName());
       var_dump($attribute->getArguments());
       var_dump($attribute->newInstance());
    }
}

dumpAttributeData(new ReflectionClass(Thing::class));

    
```

El ejemplo anterior mostrará:

    string(11) "MyAttribute"
    array(1) {
      ["value"]=>
      int(1234)
    }
    object(MyAttribute)#3 (1) {
      ["value"]=>
      int(1234)
    }

En lugar de iterar sobre todos los atributos en la instancia de reflexión, puedes recuperar solo aquellos de una clase de atributo específica pasando el nombre de la clase de atributo como argumento.

Lectura de atributos específicos utilizando la API de Reflection

```php
<?php
#[Attribute]
class MyAttribute
{
    public $value;

    public function __construct($value)
    {
        $this->value = $value;
    }
}

#[MyAttribute(value: 1234)]
class Thing
{
}

function dumpMyAttributeData($reflection) {
    $attributes = $reflection->getAttributes(MyAttribute::class);

    foreach ($attributes as $attribute) {
       var_dump($attribute->getName());
       var_dump($attribute->getArguments());
       var_dump($attribute->newInstance());
    }
}

dumpMyAttributeData(new ReflectionClass(Thing::class));

     
```

## Declaración de clases de atributos

Se recomienda definir una clase separada para cada atributo. En el caso más simple, una clase vacía con la declaración `#[Attribute]` es suficiente. El atributo puede ser importado desde el espacio de nombres global utilizando una declaración `use`.

Clase de atributo simple

```php
<?php

namespace Example;

use Attribute;

#[Attribute]
class MyAttribute
{
}

   
```

Para restringir los tipos de declaraciones a los que se puede aplicar un atributo, pasa una máscara de bits como primer argumento en la declaración `#[Attribute]`

Usar la especificación de destino para restringir dónde se pueden usar los atributos

```php
<?php

namespace Example;

use Attribute;

#[Attribute(Attribute::TARGET_METHOD | Attribute::TARGET_FUNCTION)]
class MyAttribute
{
}

    
```

Declarar `MyAttribute` en otro tipo ahora generará una excepción durante la llamada a `ReflectionAttribute::newInstance`

Los siguientes destinos se pueden especificar:

Attribute::TARGET_CLASS

Attribute::TARGET_FUNCTION

Attribute::TARGET_METHOD

Attribute::TARGET_PROPERTY

Attribute::TARGET_CLASS_CONSTANT

Attribute::TARGET_PARAMETER

Attribute::TARGET_ALL

Por defecto, un atributo solo se puede usar una vez por declaración. Para permitir que un atributo sea repetible, especifícalo en la máscara de bits de la declaración `#[Attribute]` utilizando el flag `Attribute::IS_REPEATABLE`

Usar IS_REPEATABLE para permitir que un atributo se use varias veces en una declaración

```php
<?php

namespace Example;

use Attribute;

#[Attribute(Attribute::TARGET_METHOD | Attribute::TARGET_FUNCTION | Attribute::IS_REPEATABLE)]
class MyAttribute
{
}

    
```
