---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration85.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration85/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 570cdc0ce
order: 1210
---

## Cambios incompatibles con versiones anteriores

## Núcleo de PHP

### Nombres de alias `"array"` y `"callable"`

Ya no es posible utilizar `"array"` y `"callable"` como nombres de alias de clase en `class_alias`

### Comparación imprecisa de objetos incomparables

Anteriormente, la comparación imprecisa de objetos no comparables (p. ej., enumeraciones, `CurlHandle` y otras clases internas) con valores booleanos era inconsistente. Si se comparaba con un literal booleano `$object == true`, se comportaba igual que `(bool)$object`. Si se comparaba con un valor estáticamente desconocido `$object == $true`, siempre devolvía `false`. Este comportamiento se unificó para que siempre se ajustara al de `(bool)$object`.

### Valor de retorno de gc_collect_cycles

El valor de retorno de `gc_collect_cycles` ya no incluye strings y recursos que se recopilaron indirectamente a través de ciclos.

### Sustituir la palabra clave static en la subclase final

Ahora está permitido sustituir `static` por `self` o el nombre de clase concreto en las subclases finales.

### Controladores de ticks

Los controladores de ticks ahora se desactivan después de todas las funciones de apagado, los destructores se hayan ejecutado, y se hayan limpiado los controladores de salida.

### Enlace de rasgos

Ahora, los rasgos se vinculan antes que la clase padre. Este es un cambio de comportamiento sutil, pero debería ajustarse mejor a las expectativas de los usuarios.

### Errores durante la compilación y el enlace de clases

Los errores que se producen durante la compilación y el enlazado de clases ahora se procesan siempre después de la compilación o el enlazado. Los errores fatales que se producen durante la compilación o el enlazado de clases provocan que cualquier error retrasado se procese inmediatamente, sin llamar a los controladores de errores definidos por el usuario.

### Excepciones generadas por el controlador de errores definido por el usuario

Las excepciones generadas por los controladores de errores definidos por el usuario al manejar errores de enlace de clases ya no se convierten en errores fatales y no impiden el enlace.

### Error al aplicar el atributo durante la compilación

Aplicar `#[\Attribute]` a una clase abstracta, enumeración, interfaz o rasgo provoca un error durante la compilación. Anteriormente, se podía agregar el atributo, pero al llamar a ReflectionAttribute::newInstance se producía un error. El error se puede retrasar desde la compilación hasta el tiempo de ejecución mediante el nuevo atributo `#[\DelayedTargetValidation]`.

### Configuración INI disable_classes

Se ha eliminado la configuración INI [disable_classes](#ini.disable-classes) ya que provoca que se rompan varias suposiciones del motor.

### Desestructuración de valores que no son arrays

La desestructuración de valores que no son array (distintos de `null`) utilizando `[]` o `list` ahora emite una advertencia.

### Advertencias relacionadas con conversiones

Ahora se emite una advertencia al convertir números de punto flotante (o cadenas que parecen ser de punto flotante) a enteros si no se pueden representar como tales. Esto afecta tanto a las conversiones explícitas como a las implícitas de enteros.

Ahora se emite una advertencia al convertir NAN a otros tipos.

## Bzip2

`bzcompress` ahora lanza un `ValueError` cuando `block_size` no está entre 1 y 9.

`bzcompress` ahora lanza un `ValueError` cuando `work_factor` no está entre 0 y 250.

## DOM

Clonar un `DOMNamedNodeMap`, `DOMNodeList`, `Dom\NamedNodeMap`, `Dom\NodeList`, `Dom\HTMLCollection`, o `Dom\DtdNamedNodeMap` ahora falla. Dado que nunca se generó un objeto funcional, no se espera ningún impacto.

## FileInfo

`finfo_file` y finfo::file ahora lanzan un ValueError en lugar de un TypeError cuando `filename` contiene bytes nulos. Esto alinea el tipo de error que se produce para que sea coherente con el resto del lenguaje.

## Intl

La extensión ahora requiere al menos ICU 57.1.

IntlDateFormatter::setTimeZone/`datefmt_set_timezone` ahora lanza una IntlException en clases no inicializadas/fallos de clonación.

Todos los métodos `Locale` ahora lanzan un ValueError cuando el argumento locale contiene bytes nulos.

El comportamiento de `Collator::SORT_REGULAR` con respecto al manejo de strings numéricas ahora está alineado con el comportamiento de `SORT_REGULAR` en ext/standard.

## LDAP

`ldap_get_option` y `ldap_set_option` ahora lanzan un ValueError al pasar una opción no válida.

## MBString

Las tablas de datos Unicode se han actualizado a Unicode 17.0.

## MySQLi

Ahora ya no es posible llamar al constructor mysqli en un objeto ya construido y lanza un Error.

## ODBC

ODBC ahora presupone que está disponible al menos la funcionalidad de ODBC 3.5. Se han eliminado la definición de ODBCVER y las opciones del sistema de compilación para controlarla.

ODBC ya no incluye opciones de compilación para controladores específicos (excepto DB2) y elimina las excepciones para dichos controladores. Se recomienda encarecidamente usar un administrador de controladores como iODBC o unixODBC en sistemas que no sean Windows.

## Opcache

La extensión Opcache ahora viene integrada en el binario de PHP y siempre se carga. Las directivas INI [opcache.enable](#ini.opcache.enable) y [opcache.enable_cli](#ini.opcache.enable-cli) siguen siendo válidas.

Se han eliminado las opciones de configuración `--enable-opcache`/`--disable-opcache` y la compilación ya no produce objetos `opcache.so` ni `php_opcache.dll`.

El uso de las directivas INI `zend_extension=opcache.so` o `zend_extension=php_opcache.dll` generará una advertencia.

## PCNTL

`pcntl_exec` ahora lanza ValueError cuando las entradas del parámetro `args` contienen bytes nulos.

`pcntl_exec` ahora lanza ValueError cuando las entradas o claves del parámetro `env_vars` contienen bytes nulos.

## PCRE

La extensión se compila sin la opción de compilación PCRE2_EXTRA_ALLOW_LOOKAROUND_BSK, que está semi-obsoleta.

## PDO

Los argumentos del constructor definidos junto con `PDO::FETCH_CLASS` ahora siguen la semántica habitual de CUFA (`call_user_func_array`). Esto significa que las claves de tipo cadena se comportarán como argumentos con nombre. Además, se ha eliminado el ajuste automático de los argumentos por valor pasados ​​a un parámetro por referencia, y ahora se emite la advertencia habitual `E_WARNING` sobre este problema. Para pasar una variable por referencia a un argumento del constructor, utilice la asignación general de referencia a un valor de array: `$ctor_args = [&$valByRef]`

Intentar llamar a PDOStatement::setFetchMode durante una llamada a PDOStatement::fetch, PDOStatement::fetchObject, PDOStatement::fetchAll, por ejemplo, utilizando trucos como pasar el objeto de declaración como argumento de constructor al buscar en un objeto, ahora lanzará un Error.

Los valores de las constantes `PDO::FETCH_GROUP`, `PDO::FETCH_UNIQUE`, `PDO::FETCH_CLASSTYPE`, `PDO::FETCH_PROPS_LATE`, y `PDO::FETCH_SERIALIZE` ha cambiado.

Ahora se lanza un ValueError si se usa `PDO::FETCH_PROPS_LATE` con un modo de obtención diferente de `PDO::FETCH_CLASS`, de forma coherente con otras flags de obtención.

Ahora se lanza un ValueError si se usa `PDO::FETCH_INTO` como modo de obtención en PDOStatement::fetchAll, de forma similar a `PDO::FETCH_LAZY`.

## PDO_FIREBIRD

Ahora se produce un ValueError al intentar establecer un nombre de cursor demasiado largo en un `PDOStatement` resultante del controlador Firebird.

## PDO_SQLITE

SQLite PDO::quote ahora lanzará una excepción o emitirá una advertencia, dependiendo del modo de error, si la cadena contiene un byte nulo.

PDO::sqliteCreateCollation ahora lanzará una excepción si la devolución de llamada tiene un tipo de retorno incorrecto, lo que lo hace más acorde con el comportamiento de Pdo\Sqlite::createCollation.

## POSIX

`posix_kill` ahora lanza una ValueError cuando el argumento process_id es menor o mayor que lo que admite la plataforma (entero con signo o rango largo), la función `posix_setpgid` ahora lanza una ValueError cuando process_id o process_group_id es menor que cero o mayor que lo que admite la plataforma.

`posix_setrlimit` ahora lanza un ValueError cuando los argumentos hard_limit o soft_limit son menores que -1 o si soft_limit es mayor que hard_limit.

## Reflection

ReflectionAttribute::newInstance ahora puede lanzar errores para atributos internos si el atributo se aplicó en un destino no válido y el error se retrasó del tiempo de compilación al tiempo de ejecución a través del atributo \#\[\DelayedTargetValidation\].

## Sesión

Intentar escribir datos de sesión donde `$_SESSION` tiene una clave que contiene el carácter de barra vertical (`|`) ahora emitirá una advertencia en lugar de fallar silenciosamente.

`session_start` es más estricta con respecto al argumento del array. Ahora lanza una ValueError si el array no es un mapa hash, o una TypeError si el valor de read_and_close no es de un tipo válido compatible con int.

## SimpleXML

Pasar una expresión XPath que devuelva algo distinto de un nodo establecido en SimpleXMLElement::xpath ahora emitirá una advertencia y devolverá `false`, en lugar de fallar silenciosamente y devolver un array vacío.

## SNMP

`snmpget`, `snmpset`, `snmp2_get`, `snmp2_set`, `snmp3_get`, `snmp3_set` y SNMP::\_\_construct ahora lanzará una ValueError cuando el nombre de host es demasiado largo, contiene algún byte nulo, o si el puerto proporcionado es negativo o mayor que 65535, los valores de tiempo de espera y reintentos son inferiores a -1 o demasiado grandes.

## SOAP

SoapClient::\_\_doRequest ahora acepta un nuevo parámetro opcional `uriParserClass` que acepta argumentos de tipo string o `null`. `null` representa el método original basado en (`parse_url`), mientras que los nuevos backends se utilizarán al pasar `Uri\Rfc3986\Uri` o `Uri\WhatWg\Url`.

## Sockets

`socket_create_listen`, `socket_bind` y `socket_sendto` ahora lanzan un ValueError si el puerto es menor que 0 o mayor que 65535, y también si alguna de las entradas del array de sugerencias está indexada numéricamente.

`socket_addrinfo_lookup` ahora lanza un TypeError si alguno de los valores de las sugerencias no se puede convertir a int y puede lanzar un ValueError si alguno de estos valores se desborda.

`socket_set_option` con las opciones `MCAST_LEAVE_GROUP`/`MCAST_LEAVE_SOURCE_GROUP` ahora lanzan una excepción si el valor no es un objeto o array válido.

`socket_set_option` con contexto multicast ahora lanza un ValueError cuando el socket creado no es de la familia `AF_INET`/`AF_INET6`.

## SPL

`ArrayObject` ya no acepta enumeraciones, ya que modificar las propiedades \$name o \$value puede romper las suposiciones del motor.

El parámetro SplFileObject::fwrite `length` ahora admite valores nulos. El valor predeterminado cambió de `0` a `null`.

## Estándar

El uso de una función de la familia printf con un formateador que no especificó previamente la precisión incorrectamente restablece la precisión en lugar de tratarla como una precisión de 0.

Pasar un entero `0` como argumento `locales` a `setlocale` ya no es compatible y ahora lanza un TypeError.

## Tidy

tidy::\_\_construct, tidy::parseFile, tidy::parseString ahora lanza un ValueError si la configuración contiene un valor no válido o intenta establecer una entrada interna de solo lectura, y un TypeError si una clave de configuración no es un string.
