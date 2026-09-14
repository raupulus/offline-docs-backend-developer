---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration80.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration80/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 820
---

## Otros cambios

## Cambios en los módulos SAPI

### Apache2Handler

El módulo PHP ha sido renombrado de `php7_module` a `php_module`.

## Funciones cambiadas

### Reflection

Los resultados de ReflectionClass::getConstants y ReflectionClass::getReflectionConstants pueden ser filtrados a través de un nuevo parámetro `filter`. Tres nuevas constantes han sido añadidas para ser usadas junto a la clase:

`ReflectionClassConstant::IS_PUBLIC`, `ReflectionClassConstant::IS_PROTECTED`, `ReflectionClassConstant::IS_PRIVATE`

### Estándar

Las funciones matemáticas `abs`, `ceil`, `floor` y `round` ahora respetan correctamente [la directiva `strict_types`](#language.types.declarations.strict). Anteriormente, coercionaban el primer argumento incluso en modo de tipo estricto.

### Zip

- Los métodos ZipArchive::addGlob y ZipArchive::addPattern aceptan más valores en el `options` argumento de array:

  `flags`, `comp_method`, `comp_flags`, `env_method`, `enc_password`

- ZipArchive::addEmptyDir, ZipArchive::addFile and ZipArchive::addFromString methods have a new `flags` argument. This allows managing name encoding (`ZipArchive::FL_ENC_*`) and entry replacement (`ZipArchive::FL_OVERWRITE`).

- ZipArchive::extractTo ahora restaura el tiempo de modificación del archivo.

## Otros cambios a las extensiones

### CURL

- La extensión CURL ahora requiere al menos libcurl 7.29.0.

- El parámetro obsoleto `version` de `curl_version` ha sido eliminado.

### Fecha y Tiempo

`DatePeriod` ahora implementa IteratorAggregate (instead of Traversable).

### DOM

`DOMNamedNodeMap` y `DOMNodeList` ahora implementan IteratorAggregate (instead of Traversable).

### Intl

`IntlBreakIterator` y `ResourceBundle` ahora implementan IteratorAggregate (instead of Traversable).

### Enchant

La extensión enchant ahora usa libenchant-2 por defecto cuando esté disponible. libenchant versión 1 sigue siendo soportado pero está obsoleto y podría ser borrado en el futuro.

### GD

- El `num_points` párametro de `imagepolygon`, `imageopenpolygon` y `imagefilledpolygon` es ahora opcional, p.e. esas funciones pueden ser llamadas con 3 o 4 argumentos. Si el argumento está omitido, está calculado como `count($points)/2`.

- La función `imagegetinterpolation` para obtener la interpolación actual ha sido añadida.

### JSON

La extensión JSON no puede ser deshabilitada y siempre será una parte integral de cualquier build PHP. De manera similar a la extensión de fecha.

### MBString

La tabla unicode ha sido actualizada a la versión 13.0.0.

### PDO

`PDOStatement` ahora implementa IteratorAggregate (instead of Traversable).

### LibXML

La versión mínima requerida es 2.9.0. Esto significa que la carga externa está garantizada de ser deshabilitada por defecto y no habrá pasos extras para protegerse frente a los ataques XXE

### MySQLi / PDO MySQL

- Cuando mysqlnd no sea usado (que es la opción recomendada y por defecto), la versión libmysqlclient mínima soportada es ahora 5.5.

- `mysqli_result` ahora implementa IteratorAggregate (instead of Traversable).

### PGSQL / PDO PGSQL

Las extensiones PGQSQL y PDO PGSQL ahora requieren al menos libpq 9.1.

### Readline

Llamar a `readline_completion_function` antes de que un prompt interactivo comience (e.g. in [auto_prepend_file](#ini.auto-prepend-file)) ahora sobreescribirá default interactive prompt completion function. Previamente `readline_completion_function` solo trabajaba cuando se le llamaba antes de comenzar el prompt interactivo.

### SimpleXML

`SimpleXMLElement` ahora implementa RecursiveIterator y absorve la funcionalidad de `SimpleXMLIterator`. `SimpleXMLIterator` es una extensión vacía de `SimpleXMLElement`.

## Cambios en la gestión del archivo INI

- com.dotnet_version es una nueva directiva INI para elegir la versión del framework .NET a usar en los objetos `dotnet` .

- zend.exception_string_param_max_len es una nueva directiva INI para establecer la longitud máxima de la cadena de una traza de pila convertida a cadena.

## EBCDIC

Los objetivos EBCDIC no estarán más soportadas, aunque es poco probable que todavía estuvieran trabajando en el primer lugar.

## Rendimiento

- Un compilador Just-In-Time (JIT) ha sido añadido a la extensión opcache

- `array_slice` de un array sin gaps no escaneará más el array completo para encontrar el offset del comienzo. Esto puede ser significante al reducir el runtime de la función con offsets más largos y tamaños más pequeños.

- `strtolower` ahora usa una implementación SIMD cuando se usa `"C"` `LC_CTYPE` locale (que es la opción por defecto).
