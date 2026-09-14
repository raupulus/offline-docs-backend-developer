---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/pdo.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 8d40a1fab
order: 61770
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

## Cursores

Véase también `PDO::ATTR_CURSOR_NAME`.

`PDO::FETCH_ORI_NEXT` (`int`)  
Recupera la próxima línea de un conjunto de resultados. Válido solo para los cursores desplazables.

`PDO::FETCH_ORI_PRIOR` (`int`)  
Recupera la línea anterior de un conjunto de resultados. Válido solo para los cursores desplazables.

`PDO::FETCH_ORI_FIRST` (`int`)  
Recupera la primera línea de un conjunto de resultados. Válido solo para los cursores desplazables.

`PDO::FETCH_ORI_LAST` (`int`)  
Recupera la última línea de un conjunto de resultados. Válido solo para los cursores desplazables.

`PDO::FETCH_ORI_ABS` (`int`)  
Recupera la línea solicitada por un número de línea de un conjunto de resultados. Válido solo para los cursores desplazables.

`PDO::FETCH_ORI_REL` (`int`)  
Recupera la línea solicitada por una posición relativa a la posición actual del cursor de un conjunto de resultados. Válido solo para los cursores desplazables.

`PDO::CURSOR_FWDONLY` (`int`)  
Crea un objeto `PDOStatement` con un cursor solo de avance. Es la opción por defecto para el cursor, ya que es el patrón de acceso a datos más rápido y común en PHP.

`PDO::CURSOR_SCROLL` (`int`)  
Crea un objeto `PDOStatement` con un cursor desplazable. Pasar las constantes `PDO::FETCH_ORI_*` para controlar las líneas recuperadas del conjunto de resultados.

## Otras Constantes

`PDO::PARAM_BOOL` (`int`)  
Representa el tipo de datos booleano.

`PDO::PARAM_NULL` (`int`)  
Representa el tipo de datos NULL SQL.

`PDO::PARAM_INT` (`int`)  
Representa el tipo de datos INTEGER SQL.

`PDO::PARAM_STR` (`int`)  
Representa los tipos de datos CHAR, VARCHAR o los otros tipos de datos en forma de string SQL.

`PDO::PARAM_STR_NATL` (`int`)  
Indicador para designar un string que utiliza el juego de caracteres nacional.

Disponible a partir de PHP 7.2.0

`PDO::PARAM_STR_CHAR` (`int`)  
Indicador para designar un string que utiliza el juego de caracteres normal.

Disponible a partir de PHP 7.2.0

`PDO::PARAM_LOB` (`int`)  
Representa el tipo de datos "objeto grande" SQL.

`PDO::PARAM_STMT` (`int`)  
Representa un tipo de conjunto de resultados. Actualmente no es soportado por ningún controlador.

`PDO::PARAM_INPUT_OUTPUT` (`int`)  
Especifica que el argumento es un argumento INOUT para un procedimiento almacenado. Esta constante debe combinarse con el operador OR a nivel de bits con una de las constantes `PDO::PARAM_*`.

`PDO::ATTR_AUTOCOMMIT` (`bool`)  
Si el valor es `false`, PDO intenta desactivar la validación automática cuando la conexión comienza una transacción.

A partir de PHP 8.4.0 esta constante es de tipo `bool`; anteriormente, era de tipo `int`.

`PDO::ATTR_PREFETCH` (`int`)  
Definir el tamaño de precarga permite equilibrar la velocidad con el uso de memoria de una aplicación. No todas las combinaciones bases de datos / controladores soportan la configuración del tamaño de precarga. Un mayor tamaño de precarga resulta en un mayor rendimiento a costa de un mayor uso de memoria.

El controlador PDO_PGSQL, en cambio, trata este atributo como un conmutador: a partir de PHP 8.5.0, un valor de `0` habilita la obtención perezosa (fila a fila); véase la [documentación del controlador PDO_PGSQL](#pdo-pgsql.constants.attr-prefetch) para más detalles.

`PDO::ATTR_TIMEOUT` (`int`)  
Define el valor de espera en segundos para las comunicaciones con la base de datos.

`PDO::ATTR_ERRMODE` (`int`)  
Ver la sección sobre los [errores y la gestión de errores](#pdo.error-handling) para más información sobre este atributo.

`PDO::ATTR_SERVER_VERSION` (`int`)  
Atributo de solo lectura; devuelve información sobre la versión de la base de datos a la que PDO está conectado.

`PDO::ATTR_CLIENT_VERSION` (`int`)  
Atributo de solo lectura; devuelve información sobre la versión de la biblioteca cliente utilizada por PDO.

`PDO::ATTR_SERVER_INFO` (`int`)  
Atributo de solo lectura; devuelve algunas meta-informaciones sobre el servidor de base de datos al que PDO está conectado.

`PDO::ATTR_CONNECTION_STATUS` (`int`)  

`PDO::ATTR_CASE` (`int`)  
Fuerza los nombres de columna a un formato específico especificado por las constantes `PDO::CASE_*`.

`PDO::ATTR_CURSOR_NAME` (`int`)  
Recupera o define el nombre a utilizar para un cursor. Muy útil al utilizar cursores desplazables y actualizaciones posicionadas.

`PDO::ATTR_CURSOR` (`int`)  
Selecciona el tipo de cursor. PDO actualmente soporta `PDO::CURSOR_FWDONLY` o `PDO::CURSOR_SCROLL`. A menos que se necesiten cursores desplazables, se debe usar el modo de cursor `PDO::CURSOR_FWDONLY`.

`PDO::ATTR_DRIVER_NAME` (`int`)  
Devuelve el nombre del controlador.

Uso de `PDO::ATTR_DRIVER_NAME`

```php
<?php
if ($db->getAttribute(PDO::ATTR_DRIVER_NAME) == 'mysql') {
   echo "Uso de mysql; hacer algo específico de mysql aquí\n";
}
?>

      
```

`PDO::ATTR_ORACLE_NULLS` (`int`)  
Convierte las cadenas vacías en valores NULL SQL en los datos recuperados.

`PDO::ATTR_PERSISTENT` (`int`)  
Solicita una conexión persistente, en lugar de crear una nueva conexión. Ver las [conexiones y el gestor de conexión](#pdo.connections) para más información sobre este atributo.

`PDO::ATTR_STATEMENT_CLASS` (`int`)  
Define el nombre de la clase bajo la cual los datos son devueltos.

`PDO::ATTR_FETCH_CATALOG_NAMES` (`int`)  
Añade el contenido del catálogo de nombres en cada nombre de columna devuelto en el conjunto de resultados. El catálogo de nombres y los nombres de columnas están separados por un punto (.). El soporte de este atributo es a nivel de controlador; puede no estar disponible por el controlador en uso.

`PDO::ATTR_FETCH_TABLE_NAMES` (`int`)  
Añade el contenido de la tabla de nombres en cada nombre de columna devuelto en el conjunto de resultados. La tabla de nombres y los nombres de columnas están separados por un punto (.). El soporte de este atributo es a nivel de controlador; puede no estar disponible por el controlador en uso.

`PDO::ATTR_STRINGIFY_FETCHES` (`int`)  
Fuerza todas las valores recuperados (excepto `null`) a ser tratados como strings. Los valores `null` permanecen sin cambios, a menos que `PDO::ATTR_ORACLE_NULLS` esté definido en `PDO::NULL_TO_STRING`.

`PDO::ATTR_MAX_COLUMN_LEN` (`int`)  
Define la longitud máxima del nombre de columna.

`PDO::ATTR_DEFAULT_FETCH_MODE` (`int`)  

`PDO::ATTR_EMULATE_PREPARES` (`bool`)  
Indica si se debe activar o desactivar la emulación de las sentencias preparadas. Algunos controladores no soportan las sentencias preparadas nativas o solo tienen un soporte limitado de ellas. Cuando se define a `true`, PDO siempre emula las sentencias preparadas; cuando se define a `false`, utiliza las sentencias preparadas nativas del controlador.

A partir de PHP 8.4.0 esta constante es de tipo `bool`; anteriormente, era de tipo `int`.

`PDO::ATTR_DEFAULT_STR_PARAM` (`int`)  
Define el tipo de argumento de string por defecto, esto puede ser `PDO::PARAM_STR_NATL` o `PDO::PARAM_STR_CHAR`.

Disponible a partir de PHP 7.2.0

`PDO::ERRMODE_SILENT` (`int`)  
No envía error ni excepción si ocurre un error. El desarrollador debe verificar explícitamente los errores. Antes de PHP 8.0.0, este era el modo predeterminado. Ver los [errores y la gestión de errores](#pdo.error-handling) para más información sobre este atributo.

`PDO::ERRMODE_WARNING` (`int`)  
Envía un error de nivel `E_WARNING` si ocurre un error. Ver los [errores y la gestión de errores](#pdo.error-handling) para más información sobre este atributo.

`PDO::ERRMODE_EXCEPTION` (`int`)  
Lanza una excepción `PDOException` si ocurre un error. Ver los [errores y la gestión de errores](#pdo.error-handling) para más información sobre este atributo.

`PDO::CASE_NATURAL` (`int`)  
Deja los nombres de columnas como se devuelven por el controlador de base de datos.

`PDO::CASE_LOWER` (`int`)  
Fuerza los nombres de columnas en minúsculas.

`PDO::CASE_UPPER` (`int`)  
Fuerza los nombres de columnas en mayúsculas.

`PDO::NULL_NATURAL` (`int`)  

`PDO::NULL_EMPTY_STRING` (`int`)  

`PDO::NULL_TO_STRING` (`int`)  

`PDO::ERR_NONE` (`string`)  
Corresponde a SQLSTATE `'00000'`, lo que significa que la consulta SQL ha tenido éxito sin error ni advertencia. Esta constante es útil para ayudar al verificar PDO::errorCode o PDOStatement::errorCode para determinar si ha ocurrido un error. Esto suele conocerse examinando el código de retorno del método que generó la condición de error de todos modos.

`PDO::PARAM_EVT_ALLOC` (`int`)  
Asigna un evento

`PDO::PARAM_EVT_FREE` (`int`)  
Elimina un evento

`PDO::PARAM_EVT_EXEC_PRE` (`int`)  
Evento desencadenado antes de la ejecución de una sentencia preparada.

`PDO::PARAM_EVT_EXEC_POST` (`int`)  
Evento desencadenado tras la ejecución de una sentencia preparada.

`PDO::PARAM_EVT_FETCH_PRE` (`int`)  
Evento desencadenado antes de recuperar un resultado de un conjunto de resultados.

`PDO::PARAM_EVT_FETCH_POST` (`int`)  
Evento desencadenado tras recuperar un resultado de un conjunto de resultados.

`PDO::PARAM_EVT_NORMALIZE` (`int`)  
Evento activado durante el registro de parámetros vinculados permitiendo al controlador normalizar el nombre del parámetro.

`PDO::SQLITE_DETERMINISTIC` (`int`)  
> [!WARNING]
> Esta constante está *OBSOLETA* a partir de PHP 8.5.0. Utilice `Pdo\Sqlite::DETERMINISTIC` en su lugar.

Especifica que una función creada con PDO::PDO::sqliteCreateFunction es determinista, es decir, siempre devuelve el mismo resultado por las mismas entradas en una sola instrucción SQL. (Disponible a partir de PHP 7.1.4.)
