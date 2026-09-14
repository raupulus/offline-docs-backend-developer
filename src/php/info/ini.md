---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/info.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: b1116af46
order: 39270
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [assert.active](#ini.assert.active) | "1" | `INI_ALL` | Obsoleto a partir de PHP 8.3.0 |
| [assert.bail](#ini.assert.bail) | "0" | `INI_ALL` | Obsoleto a partir de PHP 8.3.0 |
| [assert.warning](#ini.assert.warning) | "1" | `INI_ALL` | Obsoleto a partir de PHP 8.3.0 |
| [assert.callback](#ini.assert.callback) | NULL | `INI_ALL` | Obsoleto a partir de PHP 8.3.0 |
| [assert.quiet_eval](#ini.assert.quiet-eval) | "0" | `INI_ALL` | Eliminado a partir de PHP 8.0.0 |
| [assert.exception](#ini.assert.exception) | "1" | `INI_ALL` | Anterior a PHP 8.0.0, el valor por defecto es `"0"` Obsoleto a partir de PHP 8.3.0 |
| [enable_dl](#ini.enable-dl) | "1" | `INI_SYSTEM` | Esta funcionalidad obsoleta *será* ciertamente *eliminada* en el futuro. |
| [max_execution_time](#ini.max-execution-time) | "30" | `INI_ALL` |  |
| [max_input_time](#ini.max-input-time) | "-1" | `INI_PERDIR` |  |
| [max_input_nesting_level](#ini.max-input-nesting-level) | "64" | `INI_PERDIR` |  |
| [max_input_vars](#ini.max-input-vars) | 1000 | `INI_PERDIR` |  |
| [zend.enable_gc](#ini.zend.enable-gc) | "1" | `INI_ALL` |  |
| [zend.max_allowed_stack_size](#ini.zend.max-allowed-stack-size) | "0" | `INI_SYSTEM` | Disponible a partir de PHP 8.3.0. |
| [zend.reserved_stack_size](#ini.zend.reserved-stack-size) | "0" | `INI_SYSTEM` | Disponible a partir de PHP 8.3.0. |
| [fiber.stack_size](#ini.fiber.stack-size) |  | `INI_ALL` | Disponible a partir de PHP 8.1.0. |

Opciones de configuración

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`assert.active` `bool`  
Activa las evaluaciones de tipo `assert`. [zend.assertions](#ini.zend.assertions) debería ser utilizado en su lugar para controlar el comportamiento de `assert`.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`assert.bail` `bool`  
Termina el script si una aserción falla.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`assert.warning` `bool`  
Emite una alerta PHP para cada aserción que falle.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`assert.callback` `string`  
Función definida por el programador, a llamar para cada aserción fallida.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`assert.quiet_eval` `bool`  
> [!WARNING]
> Esta característica ha sido *ELIMINADA* a partir de PHP 8.0.0.

Utiliza la configuración actual de `error_reporting` durante las evaluaciones de aserciones. Si está activada, ningún error es mostrado (error_reporting(0) implícito) durante la evaluación. Si está desactivada, los errores son mostrados según la configuración de `error_reporting`

`assert.exception` `bool`  
Lanza una excepción `AssertionError` cuando una aserción falla.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`enable_dl` `bool`  
Esta directiva permite activar o desactivar la carga dinámica de extensiones PHP con la función PHP `dl`.

La razón principal para desactivar este sistema es la seguridad. Con la carga dinámica, es posible eludir las restricciones impuestas por [open_basedir](#ini.open-basedir).

`max_execution_time` `int`  
Establece el tiempo máximo de ejecución de un script, en segundos. Esto evita que los scripts en bucles infinitos saturen el servidor. La configuración por defecto es de `30` segundos. Cuando PHP funciona desde la [línea de comando](#features.commandline), el valor por defecto es `0`.

En sistemas no-Windows, el tiempo máximo de ejecución no se ve afectado por llamadas al sistema como `sleep`. Consulte la función `set_time_limit` para más detalles.

El servidor web puede tener otras configuraciones de tiempo límite de ejecución que también pueden interrumpir PHP. Apache tiene una directiva `Timeout` e IIS tiene una función CGI para ello. Por defecto, ambas valen 300 segundos. Consulte la documentación del servidor web para más detalles.

`max_input_time` `int`  
Esta opción especifica la duración máxima para analizar los datos de entrada, como POST y GET. Esta duración se mide desde el momento en que PHP es invocado en el servidor hasta el inicio de la ejecución del script. El valor por defecto es `-1`, lo que significa que [max_execution_time](#ini.max-execution-time) es utilizado en su lugar. Establecer el valor a `0` para permitir una ejecución ilimitada.

`max_input_nesting_level` `int`  
Define la profundidad máxima de las [variables de entrada](#language.variables.external) (es decir, `$_GET`, `$_POST`..)

`max_input_vars` `int`  
El número de [variables de entrada](#language.variables.external) que pueden ser aceptadas (este límite se aplica a las variables superglobales \$\_GET, \$\_POST y \$\_COOKIE, por separado). El uso de esta directiva permite limitar las posibilidades de ataque por denegación de servicio utilizando colisiones de hash. Si hay más variables de entrada que el número especificado por esta directiva, una alerta de tipo `E_WARNING` será emitida, y las variables adicionales serán eliminadas de la solicitud.

`zend.enable_gc` `bool`  
Activa o desactiva la recolección de referencias circulares.

`zend.max_allowed_stack_size` `int`  
La cantidad máxima de memoria de pila nativa (stack) permitida por el sistema operativo para el programa. Intentar consumir más de lo que el sistema permite generalmente resulta en un fallo brusco, sin información de depuración fácilmente disponible. Para facilitar la depuración, el motor lanza una `Error` antes de que esto ocurra (cuando el programa utiliza más de [zend.max_allowed_stack_size](#ini.zend.max-allowed-stack-size)-[zend.reserved_stack_size](#ini.zend.reserved-stack-size) bytes de pila).

La recursión en el código definido por el usuario no consume pila nativa. Sin embargo, las funciones internas y los métodos mágicos, sí consumen pila nativa. Una recursión muy profunda que involucre estas funciones puede hacer que el programa agote toda la memoria de pila disponible.

Los valores posibles para este parámetro son: `0` : Detectar automáticamente la memoria de pila nativa máxima que el sistema operativo permite para el programa. Este es el valor por defecto. Cuando la detección es imposible, se utiliza un valor por defecto del sistema., `-1` : Desactiva la verificación del tamaño de la pila en el motor., Entero positivo : Un tamaño fijo, en bytes. Establecer este valor demasiado alto equivale a desactivar la verificación de la tamaño de la pila.

Como el tamaño de pila [de las fibers](#language.fibers) está determinado por [fiber.stack_size](#ini.fiber.stack-size), el valor de este parámetro es utilizado en lugar de [zend.max_allowed_stack_size](#ini.zend.max-allowed-stack-size) durante la verificación del uso de la pila durante la ejecución de una Fiber.

> [!NOTE]
> Esto no tiene ninguna relación con los desbordamientos de búfer de pila *(stack buffer overflows)*, y no es una funcionalidad de seguridad.

`zend.reserved_stack_size` `int`  
El tamaño reservado de la pila, en bytes. Este se resta de la [tamaño máximo de pila permitido](#ini.zend.max-allowed-stack-size), como un margen de seguridad, durante la verificación del tamaño de la pila.

Los valores posibles para este parámetro son: `0` : Detectar automáticamente un tamaño razonable., Entero positivo : Un tamaño fijo, en bytes.

`fiber.stack_size` `int`  
El tamaño de la pila nativa, en bytes, asignada a cada [Fiber](#language.fibers).

El valor por defecto es de 1 Mio en sistemas donde el tamaño de los punteros es inferior a 8 bytes, o de 2 Mio en caso contrario.
