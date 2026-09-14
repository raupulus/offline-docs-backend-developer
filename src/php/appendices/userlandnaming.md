---
title: Guía de entorno de usuario para nombres
source_url: https://www.php.net/manual/es/userlandnaming.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/userlandnaming.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 0ad6aa08f
order: 1350
---

## Guía de entorno de usuario para nombres

La siguiente es una guía para saber cómo elegir el mejor nombre para los identificadores del código del entorno del usuario PHP. Cuando se eligen nombres para cualquier código que crea símbolos en el espacio de nombres global, es importante tener en cuenta los siguientes lineamientos para evitar que en futuras versiones de PHP estos choquen con los símbolos elegidos.

## Espacio de nombres global

Aquí hay una visión general de las construcciones de código que van al espacio de nombres global:

- funciones

- clases

- interfaces

- constantes (no constanstes de clase)

- variables definidas fuera de funciones/métodos

## Reglas

La siguiente lista muestra un resumen de los derechos que se reserva el proyecto PHP para sí mismo, cuando elige los nombres para los nuevos identificadores internos. La guía definitiva son los [ESTÁNDARES DE CODIFICACION](https://github.com/php/php-src/raw/master/CODING_STANDARDS.md) oficiales:

- PHP es el propietario de el namespace de nivel superior, pero trata de encontrar una descripción decente de nombres y evitar así futuros choques.

- Los nombres de función usan guion bajo entre palabras, mientras que los nombres de las clases usan las reglas `camelCase` o `PascalCase`.

- PHP antepondrá a cualquier símbolo global de una extensión el nombre de de la extensión. (En el pasado, han habido numerosas excepciones a esta regla). Ejemplos:

  - `curl_close`

  - `mysql_query`

  - PREG_SPLIT_DELIM_CAPTURE

  - new DOMDocument()

  - `strpos` (ejemplo de un error del pasado)

  - new SplFileObject()

- Iteradores y Excepciones son como siempre, simplemente postfijados con "`Iterator`" y `Exception`." Ejemplos:

  - `ArrayIterator`

  - `LogicException`

- PHP se reserva todos los simbolos que comienzan con `__` como magicos. Es recomendado que no se creen simbolos que comiencen con `__` en PHP a menos que se quiera usar una funcionalidad magica documentada. Ejemplos:

  - [\_\_get()](#object.get)

  - `__autoload`

## Consejos

Con el fin de escribir código que funcione en el futuro, se recomienda no colocar muchas variables, funciones o clases en el espacio de nombres global. Esto prevendrá de conflictos de nombres con código de terceros así como con posibles adiciones futuras al lenguaje.

Una manera común de evitar conflictos con nombres de funciones y clases es añadirlos a su propio [espacio de nombres](#language.namespaces) dedicado.

```php
<?php

namespace MiProyecto;

function mi_función() {
    return true;
}

\MiProyecto\mi_función();

   
```

Esto todavía necesita que se mantenga la cuenta de los espacios de nombres ya utilizados, pero una vez que se decido el espacio de nombres que se va a usar se pueden añadir todas las funciones y clases e él sin tener que pensar más en conflictos.

Es una buena práctica limitar el número de variables añadidas al ámbito global para evitar conflictos de nombres con código de terceros.

> [!NOTE]
> Debido a las [reglas de ámbito](#language.variables.scope) de PHP, las variables definidas dentro de funciones y métodos no están en el ámbito global y, por tanto, no pueden crear conflictos con otras variables definidas en el ámbito global.
