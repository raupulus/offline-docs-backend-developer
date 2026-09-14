---
title: Introducción
source_url: https://www.php.net/manual/es/mysqli.overview.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/overview.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 56050
---

## Introducción

Esta sección proporciona información sobre las soluciones disponibles al desarrollar una aplicación PHP que necesita interactuar con una base de datos MySQL.

**¿Qué es una API?**

Una Interfaz de Programación de Aplicaciones, o `Application Programming Interface` (API), define las clases, métodos, funciones y variables que su aplicación utilizará para ejecutar diferentes tareas. En el caso de las aplicaciones PHP, las comunicaciones con una base de datos se realizan generalmente a través de una API que está expuesta en una extensión PHP.

Las API pueden ser procedimentales u orientadas a objetos. Con una API procedimental, se pueden llamar funciones para ejecutar comandos; con una API orientada a objetos, es necesario crear objetos y llamar a los métodos de estos objetos. De las dos, esta última es generalmente preferida, ya que es más moderna y conduce a un código más organizado.

Al escribir aplicaciones PHP que deben conectarse a MySQL, hay varias API disponibles. Este documento presenta estas API y proporciona la información necesaria para elegir la mejor solución para su aplicación.

**¿Qué es un conector?**

En la documentación de MySQL, el término *conector* se refiere a un software que permite a una aplicación conectarse a una base de datos MySQL. MySQL proporciona conectores para una amplia colección de lenguajes, incluyendo PHP.

Si su aplicación PHP necesita comunicarse con un servidor de base de datos, es necesario escribir código para poder conectarse, enviar consultas al servidor, etc. Se requiere un software para proporcionar la interfaz que PHP utilizará y gestionar las comunicaciones entre su aplicación y el servidor de base de datos: eventualmente, se necesitan bibliotecas intermedias. Estos programas se denominan genéricamente conectores, ya que permiten *conectarse* a un servidor de base de datos.

**¿Qué es un controlador?**

Un controlador es un software diseñado para comunicarse con un tipo particular de base de datos. Un controlador también puede llamarse biblioteca, como la `MySQL Client Library` o el MySQL Native Driver. Estas bibliotecas implementan el protocolo de bajo nivel para comunicarse con un servidor MySQL.

Por ejemplo, la capa de abstracción de base de datos [PHP Data Objects (PDO)](#mysqli.overview.pdo) utiliza uno o más controladores de base de datos. Uno de estos controladores es el controlador PDO MYSQL, que permite interactuar con MySQL.

A veces, los desarrolladores utilizan los términos conector y controlador de manera intercambiable, lo que puede resultar confuso. En la documentación de MySQL, el término “controlador” está reservado para los programas que son la interfaz específica con la base de datos del paquete.

**¿Qué es una extensión?**

En la documentación de PHP, se encontrará con otro término: *extensión*. El código PHP está compuesto por un núcleo, con extensiones opcionales. Las extensiones relacionadas con MySQL de PHP, como la extensión `mysqli` y la extensión de controlador PDO MySQL, están implementadas utilizando el framework de extensión de PHP.

Una extensión expone típicamente una API a un desarrollador PHP, para facilitar la programación. Sin embargo, algunas extensiones que utilizan el framework de PHP no exponen ninguna API al desarrollador PHP.

La extensión de controlador PDO MySQL, por ejemplo, no expone ninguna API al desarrollador PHP, pero proporciona una interfaz a la capa PDO.

Los términos API y extensión no deberían significar lo mismo, ya que una extensión PHP no proporciona necesariamente una API particular al desarrollador PHP.

**¿Cuáles son las API de PHP para MySQL?**

Hay dos API principales para conectarse a MySQL:

- La extensión mysqli

- PHP Data Objects (PDO)

Cada una tiene sus ventajas e inconvenientes. Las siguientes secciones ofrecen una presentación rápida de cada API.

**¿Qué es la extensión mysqli de PHP?**

La extensión `mysqli`, o como a veces se la denomina, la extensión MySQL *mejorada* (i para `improved` en inglés), fue desarrollada para aprovechar las nuevas características de los sistemas MySQL versión 4.1.3 y posteriores. La extensión `mysqli` está incluida en PHP desde la versión 5.

La extensión `mysqli` tiene una gran cantidad de ventajas y mejoras con respecto a la extensión `mysql`:

- Interfaz orientada a objetos

- Soporte para sentencias preparadas

- Soporte para múltiples sentencias

- Soporte para transacciones

- Capacidades avanzadas de depuración

Además de una interfaz orientada a objetos, la extensión también ofrece una interfaz procedimental.

La extensión `mysqli` está compilada con el framework de PHP, y su código fuente se encuentra en el directorio `ext/mysqli`.

Para más información sobre la extensión `mysqli`, consulte [???](#book.mysqli).

**¿Qué es la extensión PDO de PHP?**

`PHP Data Objects`, o PDO, es una capa de abstracción de base de datos específica para PHP. PDO ofrece una API coherente para sus aplicaciones PHP, independientemente del tipo de base de datos con la que se trabaje. En teoría, si se utiliza PDO, se puede cambiar de base de datos, por ejemplo de Firebird a MySQL, y solo realizar cambios menores en el código PHP.

Otros ejemplos de capas de abstracción de base de datos incluyen JDBC para Java y DBI para Perl.

Si PDO tiene sus ventajas, como una API limpia, simple y portable, sus principales inconvenientes son que no permite utilizar todas las características avanzadas de las últimas versiones de MySQL. Por ejemplo, PDO no permite realizar consultas múltiples.

PDO está implementado utilizando el framework de PHP, y su código fuente se encuentra en el directorio `ext/pdo`.

Para más información sobre PDO, consulte [???](#book.pdo).

**¿Qué es el controlador MySQL para PDO?**

El controlador PDO MYSQL no es una API en sí mismo, al menos desde el punto de vista del desarrollador PHP. De hecho, el controlador PDO MYSQL forma parte de PDO, y proporciona las funcionalidades específicas de MySQL. El desarrollador llama a la API PDO, pero PDO utiliza el controlador PDO MYSQL para gestionar las comunicaciones con MySQL.

El controlador PDO MYSQL forma parte de la gran familia de controladores PDO. Otros controladores disponibles gestionan las comunicaciones con Firebird y PostgreSQL, entre otros.

El controlador PDO MYSQL está implementado con el framework de extensión de PHP. Su código fuente se encuentra en el directorio `ext/pdo_mysql`. No expone ninguna API al desarrollador PHP.

Para más detalles sobre el controlador PDO de MySQL, consulte [???](#ref.pdo-mysql).

**¿Qué es el controlador nativo MySQL de PHP?**

Para comunicarse con el servidor MySQL, la extensión `mysqli` y el controlador PDO MYSQL utilizan una biblioteca de bajo nivel que implementa el protocolo MySQL. En el pasado, la única biblioteca disponible era la `MySQL Client Library`, también llamada `libmysqlclient`.

Sin embargo, la interfaz presentada por `libmysqlclient` no estaba optimizada para las comunicaciones con PHP, y `libmysqlclient` estaba diseñada originalmente en C, para aplicaciones de tipo similar. Por esta razón, el controlador MySQL nativo `mysqlnd` fue desarrollado como una alternativa a `libmysqlclient` para aplicaciones PHP.

La extensión `mysqli` y el controlador MySQL nativo pueden configurarse individualmente para utilizar `libmysqlclient` o `mysqlnd`. Como `mysqlnd` fue diseñado específicamente para el sistema PHP, ofrece numerosas ventajas y mejoras con respecto a `libmysqlclient`. Se recomienda encarecidamente su uso.

El MySQL Native Driver está implementado sobre la base del framework de extensión de PHP. El código fuente se encuentra en `ext/mysqlnd`. No expone ninguna nueva API al desarrollador PHP.

**Comparación de características**

La siguiente tabla compara las características de los métodos principales para conectarse a MySQL desde PHP:

|  | Extensión mysqli | PDO (con el controlador PDO MySQL Driver y MySQL Native Driver) |
|----|----|----|
| Versión de introducción en PHP | 5.0 | 5.0 |
| Estado de desarrollo de MySQL | Desarrollo activo | Desarrollo activo |
| La API soporta juegos de caracteres | Sí | Sí |
| La API soporta sentencias preparadas | Sí | Sí |
| La API soporta sentencias preparadas del lado del cliente | No | Sí |
| La API soporta procedimientos almacenados | Sí | Sí |
| La API soporta múltiples sentencias | Sí | La mayoría |
| Todas las características de MySQL 4.1 y posteriores | Sí | La mayoría |

Comparación de las opciones de API MySQL para PHP {#mysqli.overview.option.comparison}
