---
title: dotnet La clase dotnet
source_url: https://www.php.net/manual/es/class.dotnet.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/dotnet.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 7650
---

## Introducción

La clase dotnet permite instanciar una clase desde un ensamblado .NET y llamar y acceder a sus propiedades, si la clase y los métodos y las propiedades son [visible para COM](https://docs.microsoft.com/dotnet/api/system.runtime.interopservices.comvisibleattribute).

Ni la instanciación de clases estáticas ni la llamada de métodos estáticos es soportada. La instanciación de clases genéricas como `System.Collections.Generic.List` tampoco está soportada.

Algunas clases .Net no implementan IDispatch, por lo que aunque pueden ser instanciadas, llamar a métodos o acceder a propiedades en estas clases no es soportado.

> [!NOTE]
> Se debe instalar el motor de ejecución .Net en el servidor web para aprovechar esta funcionalidad.

> [!NOTE]
> Anterior a PHP 8.0.0, el framework .Net 4.0 y versiones posteriores no son soportados por la clase `dotnet`. Si los ensamblados han sido registrados con `regasm.exe`, las clases pueden ser instanciadas como objetos `com`, sin embargo. A partir de PHP 8.0.0, el framework .Net 4.0 y las versiones posteriores son soportados a través de la directiva `php.ini` [com.dotnet_version](#ini.com.dotnet-version).

## Sinopsis de la clase

dotnet

extends

variant

Métodos

## Métodos sobrecargados

El objeto devuelto es un objeto sobrecargado, lo que significa que PHP no ve los métodos fijados como lo hace con las clases normales; en su lugar, todo acceso a propiedades o métodos se pasa a través de COM y desde allí a DOTNET. En otras palabras, el objeto .Net se mapea a través de la capa de interoperabilidad COM proporcionada por el motor de ejecución .Net.

Una vez que se ha creado un objeto dotnet, PHP lo trata de la misma manera que cualquier otro objeto COM; se aplican las mismas reglas.

## Ejemplos dotnet

Ejemplo dotnet

```php
<?php
$stack = new dotnet("mscorlib", "System.Collections.Stack");
$stack->Push(".Net");
$stack->Push("Hello ");
echo $stack->Pop() . $stack->Pop();
?>

     
```
