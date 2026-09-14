---
title: Sobrecarga mágica
source_url: https://www.php.net/manual/es/language.oop5.overloading.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/overloading.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 2540
---

## Sobrecarga mágica

La sobrecarga mágica en PHP permite “crear” dinámicamente propiedades y métodos. Estas entidades dinámicas son tratadas a través de métodos mágicos establecidos que se pueden posicionar en una clase para diversos tipos de acciones.

Los métodos mágicos de sobrecarga son llamados durante la interacción con propiedades o métodos que no han sido declarados o no son [visibles](#language.oop5.visibility) en el contexto actual. El resto de esta sección utiliza los términos de “propiedades inaccesibles” y de “métodos inaccesibles” para referirse a esta combinación de declaración y visibilidad.

Todos los métodos mágicos de sobrecarga deben ser definidos como `public`.

> [!NOTE]
> Ninguno de los argumentos de estos métodos mágicos puede ser [pasado por referencia](#functions.arguments.by-reference).

> [!NOTE]
> La interpretación PHP de la “sobrecarga” es diferente de la de la mayoría de los lenguajes orientados a objetos. La sobrecarga, habitualmente, proporciona la posibilidad de tener varios métodos con el mismo nombre pero con una cantidad y tipos diferentes de argumentos.

## Sobrecarga de propiedades

```php
public __set(string $name, mixed $value): void
```php

```php
public __get(string $name): mixed
```

```php
public __isset(string $name): bool
```php

```php
public __unset(string $name): void
```

[\_\_set()](#object.set) es solicitada al escribir datos hacia propiedades inaccesibles (protegidas o privadas) o no existentes.

[\_\_get()](#object.get) es llamada para leer datos desde propiedades inaccesibles (protegidas o privadas) o no existentes.

[\_\_isset()](#object.isset) es solicitada cuando `isset` o `empty` son llamadas sobre propiedades inaccesibles (protegidas o privadas) o no existentes.

[\_\_unset()](#object.unset) es invocada cuando `unset` es llamada sobre propiedades inaccesibles (protegidas o privadas) o no existentes.

El argumento `$name` es el nombre de la propiedad con la que se interactúa. El argumento del método [\_\_set()](#object.set) `$value` especifica el valor al que la propiedad `$name` debería ser definida.

La sobrecarga de propiedades solo funciona en contextos de objeto. Estos métodos mágicos no serán lanzados en contexto estático. Por consiguiente, estos métodos no deberían ser declarados como [estáticos](#language.oop5.static). Se lanza un aviso si alguno de los métodos mágicos es declarado como `static`.

> [!NOTE]
> El valor devuelto por [\_\_set()](#object.set) es ignorado debido a la forma en que PHP trata el operador de asignación. De la misma manera, [\_\_get()](#object.get) nunca es llamada durante una asignación encadenada, como esta: `$a = $obj->b = 8;`

> [!NOTE]
> PHP no llamará a un método sobrecargado desde el mismo método sobrecargado. Esto significa, por ejemplo, que escribir `return $this->foo` dentro de [\_\_get()](#object.get) devolverá `null` y lanzará un `E_WARNING` si no hay una propiedad `foo` definida, en lugar de llamar a [\_\_get()](#object.get) una segunda vez. Sin embargo, los métodos de sobrecarga pueden invocar otros métodos de sobrecarga de manera implícita (por ejemplo, [\_\_set()](#object.set) desencadenando [\_\_get()](#object.get)).

Ejemplo de sobrecarga de propiedades con los métodos [\_\_get()](#object.get), [\_\_set()](#object.set), [\_\_isset()](#object.isset) y [\_\_unset()](#object.unset)

```php
<?php
class PropertyTest
{
    /**  Variable para los datos sobrecargados.  */
    private $data = array();

    /**  La sobrecarga no es utilizada en las propiedades declaradas.  */
    public $declared = 1;

    /**  La sobrecarga solo es lanzada cuando se accede a esta propiedad desde fuera de la clase.  */
    private $hidden = 2;

    public function __set($name, $value)
    {
        echo "Definición de '$name' al valor '$value'\n";
        $this->data[$name] = $value;
    }

    public function __get($name)
    {
        echo "Recuperación de '$name'\n";
        if (array_key_exists($name, $this->data)) {
            return $this->data[$name];
        }

        $trace = debug_backtrace();
        trigger_error(
            'Propiedad no definida vía __get() : ' . $name .
            ' en ' . $trace[0]['file'] .
            ' en la línea ' . $trace[0]['line'],
            E_USER_NOTICE);
        return null;
    }

    public function __isset($name)
    {
        echo "¿Está '$name' definido?\n";
        return isset($this->data[$name]);
    }

    public function __unset($name)
    {
        echo "Borrado de '$name'\n";
        unset($this->data[$name]);
    }

    /**  Este no es un método mágico, necesario aquí solo para el ejemplo.  */
    public function getHidden()
    {
        return $this->hidden;
    }
}

$obj = new PropertyTest;

$obj->a = 1;
echo $obj->a . "\n\n";

var_dump(isset($obj->a));
unset($obj->a);
var_dump(isset($obj->a));
echo "\n";

echo $obj->declared . "\n\n";

echo "Manipulemos ahora la propiedad privada llamada 'hidden' :\n";
echo "'hidden' es visible desde la clase, por lo que __get() no es utilizado...\n";
echo $obj->getHidden() . "\n";
echo "'hidden' no es visible fuera de la clase, por lo que __get() es utilizado...\n";
echo $obj->hidden . "\n";
?>

    
```

El ejemplo anterior mostrará:

```php
Definición de 'a' a '1'
Recuperación de 'a'
1

¿Está 'a' definido?
bool(true)
Borrado de 'a'
¿Está 'a' definido?
bool(false)

1

Manipulemos ahora la propiedad privada llamada 'hidden' :
'hidden' es visible desde la clase, por lo que __get() no es utilizado...
2
'hidden' no es visible fuera de la clase, por lo que __get() es utilizado...
Recuperación de 'hidden'

Notice: Propiedad no definida vía __get() : hidden en <file> en la línea 64 en <file> en la línea 28

    
```

## Sobrecarga de métodos

```php
public __call(string $name, array $arguments): mixed
```php

```php
public static __callStatic(string $name, array $arguments): mixed
```

[\_\_call()](#object.call) es llamada cuando se invoca métodos inaccesibles en un contexto de objeto.

[\_\_callStatic()](#object.callstatic) es lanzada cuando se invoca métodos inaccesibles en un contexto estático.

El argumento `$name` es el nombre del método llamado. El argumento `$arguments` es un array que contiene los parámetros pasados al método `$name`.

Sobrecarga de métodos con [\_\_call()](#object.call) y [\_\_callStatic()](#object.callstatic)

```php
  
<?php
class MethodTest
{
    public function __call($name, $arguments)
    {
        // Nota: el valor de $name es sensible a mayúsculas y minúsculas.
        echo "Llamada al método '$name' "
             . implode(', ', $arguments). "\n";
    }

    public static function __callStatic($name, $arguments)
    {
        // Nota: el valor de $name es sensible a mayúsculas y minúsculas.
        echo "Llamada al método estático '$name' "
             . implode(', ', $arguments). "\n";
    }
}

$obj = new MethodTest;
$obj->runTest('en un contexto de objeto');

MethodTest::runTest('en un contexto static');
?>

    
```

El ejemplo anterior mostrará:

```php
Llamada al método 'runTest' en un contexto de objeto
Llamada al método estático 'runTest' en un contexto static

    
```
