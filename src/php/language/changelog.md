---
title: Modificaciones en POO (Programación orientada a objetos)
source_url: https://www.php.net/manual/es/language.oop5.changelog.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/changelog.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 2420
---

## Modificaciones en POO (Programación orientada a objetos)

Los cambios del modelo de objetos de PHP se recogen aquí. Más información y otras notas pueden encontrarse en la documentación sobre POO en PHP.

| Versión | Descripción |
|----|----|
| 8.4.0 | Adición: Soporte para los [hooks de propiedad](#language.oop5.property-hooks). |
| 8.4.0 | Adición: Soporte de los [objetos perezosos](#language.oop5.lazy-objects). |
| 8.1.0 | Adición: Soporte para el modificador final para las constantes de clase. Además, las constantes de interfaces pueden ser redefinidas por omisión. |
| 8.0.0 | Adición: Soporte del operador [nullsafe](#language.oop5.basic.nullsafe) *?-\>* para acceder a las propiedades y métodos sobre objetos que pueden ser null. |
| 7.4.0 | Cambio: Es ahora posible lanzar excepciones dentro de `__toString`. |
| 7.4.0 | Adición: Soporte limitado para la covarianza del tipo de retorno y contravarianza para el tipo de argumento. Soporte completo de varianza está únicamente disponible si el autocargado es utilizado. Dentro de un fichero único solo las referencias no-cíclicas de tipo son posibles. |
| 7.4.0 | Adición: Es ahora posible tipar las propiedades de clase. |
| 7.3.0 | Incompatibilidad: El desempaquetado de argumento de `Traversable`s con claves no-`int`es ya no es soportado. Este comportamiento no estaba previsto y por consiguiente fue eliminado. |
| 7.3.0 | Incompatibilidad: En versiones anteriores era posible separar las propiedades estáticas asignando una referencia. Esto ha sido eliminado. |
| 7.3.0 | Cambio: El operador [ instanceof](#language.operators.type) permite ahora literales como primer operando, en este caso el resultado es siempre `false`. |
| 7.2.0 | Obsoleto: El método `__autoload` ha sido declarado obsoleto en favor de `spl_autoload_register`. |
| 7.2.0 | Cambio: El siguiente nombre no puede ser utilizado para nombrar clases, interfaces o traits: `object`. |
| 7.2.0 | Cambio: Una coma colgante puede ahora ser añadida a la sintaxis use agrupada para los espacios de nombres. |
| 7.2.0 | Cambio: Ampliación del tipo de los parámetros. El tipo de los parámetros de los métodos reescritos y de implementación de interfaz puede ahora ser omitido. |
| 7.2.0 | Cambio: Los métodos abstractos pueden ahora ser reescritos cuando una clase abstracta extiende otra clase abstracta. |
| 7.1.0 | Cambio: Los siguientes nombres no pueden ser utilizados para nombrar clases, interfaces o traits: `void` y `iterable`. |
| 7.1.0 | Adición: Es ahora posible definir la [visibilidad de las constantes de clase](#language.oop5.visiblity-constants). |
| 7.0.0 | Obsoleto: Llamada [estática](#language.oop5.static) a métodos que no están declarados como estáticos. |
| 7.0.0 | Obsoleto: [Constructor](#language.oop5.decon) estilo PHP 4. Es decir, los métodos que tienen el mismo nombre que la clase en la que están definidos. |
| 7.0.0 | Adición: Declaración *use* agrupada: las clases, funciones y constantes que son importadas desde un mismo espacio de nombres pueden ahora ser agrupadas juntas en una sola declaración use. |
| 7.0.0 | Adición: Soporte para las [clases anónimas](#language.oop5.anonymous) ha sido añadido gracias a `new class`. |
| 7.0.0 | Incompatibilidad: Iterar sobre un no-`Traversable` `object` tendrá ahora el mismo comportamiento que iterar sobre los `array`s por referencia. |
| 7.0.0 | Cambio: La definición de propiedades (compatibles) en dos [traits](#language.oop5.traits) utilizados ya no provoca un error. |
| 5.6.0 | Adición: El método [\_\_debugInfo()](#object.debuginfo). |
| 5.5.0 | Adición: La constante mágica [::class](#language.oop5.basic.class.class). |
| 5.5.0 | Adición: [finally](#language.exceptions) para manejar las excepciones. |
| 5.4.0 | Adición: [traits](#language.oop5.traits). |
| 5.4.0 | Cambio: Si una clase [abstracta](#language.oop5.abstract) define una firma para el [constructor ](#language.oop5.decon), esta será ahora aplicada. |
| 5.3.3 | Cambio: Los métodos con el mismo nombre que el último elemento en un [espacio de nombres](#language.namespaces) ya no son considerados como un [constructor](#language.oop5.decon). Este cambio no afecta a las clases sin espacio de nombres. |
| 5.3.0 | Cambio: Las clases que implementan una interfaz con métodos que tienen valores por omisión definidos en sus prototipos ya no están obligadas a respetar los valores por omisión definidos en la interfaz. |
| 5.3.0 | Cambio: Es ahora posible referenciar una clase utilizando una variable (e.g. : `echo $classname::constant;`). El valor de la variable no puede ser una palabra clave (e.g. : `self`, `parent` o `static`). |
| 5.3.0 | Cambio: Un error de nivel `E_WARNING` es emitido si los métodos mágicos de [sobrecarga](#language.oop5.overloading) son declarados como [estáticos](#language.oop5.static). La visibilidad pública también es requerida. |
| 5.3.0 | Cambio: Anteriormente a 5.3.0, las excepciones lanzadas en la función `__autoload` no podían ser tratadas en un bloque [catch](#language.exceptions) y resultaban en un error fatal. Ahora, las excepciones lanzadas en la función \_\_autoload pueden ser capturadas en un bloque [catch](#language.exceptions) y tratadas. Si una excepción personalizada es lanzada, entonces su clase debe estar disponible. La función \_\_autoload puede ser utilizada recursivamente para autocargar la clase de excepción personalizada. |
| 5.3.0 | Adición: El método [\_\_callStatic](#language.oop5.overloading). |
| 5.3.0 | Adición: [heredoc](#language.types.string.syntax.heredoc) y [nowdoc](#language.types.string.syntax.nowdoc) son soportadas para definir las *constantes* de clases y las propiedades. Nota: Los valores heredoc deben seguir las mismas reglas que los `string` rodeados de comillas dobles (e.g. sin variables dentro). |
| 5.3.0 | Adición: [Resolución Estática Tardía](#language.oop5.late-static-bindings). |
| 5.3.0 | Adición: El método [\_\_invoke()](#object.invoke). |
| 5.2.0 | Cambio: El método [\_\_toString()](#object.tostring) solo era llamado en llamadas a `echo` o `print`. Ahora, es llamado en cualquier contexto de `string` (e.g. en `printf` con el modificador `%s`) pero no en otros contextos (e.g. con el modificador `%d`). A partir de PHP 5.2.0, convertir un `object` sin método [\_\_toString](#object.tostring) en `string` emite un error `E_RECOVERABLE_ERROR`. |
| 5.1.3 | Cambio: En versiones anteriores de PHP 5, el uso de `var` era considerado obsoleto y emitía un error `E_STRICT`. Ya no es el caso. |
| 5.1.0 | Cambio: El método estático [\_\_set_state()](#object.set-state) es ahora llamado para las clases exportadas vía `var_export`. |
| 5.1.0 | Adición: Métodos [\_\_isset()](#object.isset) y [\_\_unset()](#object.unset). |
