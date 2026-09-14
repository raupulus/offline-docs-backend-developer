---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/wincache.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 101820
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

La siguiente tabla enumera y explica los ajustes de configuración proporcionados por la extensión WinCache:

| Nombre | Por defecto | Mínimo | Máximo | Cambiable | Historial de cambios |
|----|----|----|----|----|----|
| [wincache.fcenabled](#ini.wincache.fcenabled) | "1" | "0" | "1" | `INI_ALL` | Disponible a partir de WinCache 1.0.0 |
| [wincache.fcenabledfilter](#ini.wincache.fcenabledfilter) | "NULL" | "NULL" | "NULL" | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0 |
| [wincache.fcachesize](#ini.wincache.fcachesize) | "24" | "5" | "255" | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0 |
| [wincache.fcndetect](#ini.wincache.fcndetect) | "1" | "0" | "1" | `INI_SYSTEM` | Disponible a partir de WinCache 1.1.0 |
| [wincache.maxfilesize](#ini.wincache.maxfilesize) | "256" | "10" | "2048" | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0 |
| [wincache.ocenabled](#ini.wincache.ocenabled) | "1" | "0" | "1" | `INI_ALL` | Disponible a partir de WinCache 1.0.0. Eliminada a partir de 2.0.0.0 |
| [wincache.ocenabledfilter](#ini.wincache.ocenabledfilter) | "NULL" | "NULL" | "NULL" | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0. Eliminada a partir de 2.0.0.0 |
| [wincache.ocachesize](#ini.wincache.ocachesize) | "96" | "15" | "255" | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0. Eliminada a partir de 2.0.0.0 |
| [wincache.filecount](#ini.wincache.filecount) | "4096" | "1024" | "16384" | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0 |
| [wincache.chkinterval](#ini.wincache.chkinterval) | "30" | "0" | "300" | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0 |
| [wincache.ttlmax](#ini.wincache.ttlmax) | "1200" | "0" | "7200" | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0 |
| [wincache.enablecli](#ini.wincache.enablecli) | 0 | 0 | 1 | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0 |
| [wincache.ignorelist](#ini.wincache.ignorelist) | NULL | NULL | NULL | `INI_ALL` | Disponible a partir de WinCache 1.0.0 |
| [wincache.namesalt](#ini.wincache.namesalt) | NULL | NULL | NULL | `INI_SYSTEM` | Disponible a partir de WinCache 1.0.0 |
| [wincache.ucenabled](#ini.wincache.ucenabled) | 1 | 0 | 1 | `INI_SYSTEM` | Disponible a partir de WinCache 1.1.0 |
| [wincache.ucachesize](#ini.wincache.ucachesize) | 8 | 5 | 85 | `INI_SYSTEM` | Disponible a partir de WinCache 1.1.0 |
| [wincache.scachesize](#ini.wincache.scachesize) | 8 | 5 | 85 | `INI_SYSTEM` | Disponible a partir de WinCache 1.1.0 |
| [wincache.rerouteini](#ini.wincache.rerouteini) | NULL | NULL | NULL | `INI_SYSTEM` | Disponible a partir de WinCache 1.2.0. Eliminada a partir de 1.3.7 |
| [wincache.reroute_enabled](#ini.wincache.reroute_enabled) | 1 | 0 | 1 | `INI_SYSTEM`\|`INI_PERDIR` | Disponible a partir de WinCache 1.3.7 |
| [wincache.srwlocks](#ini.wincache.srwlocks) | 1 | 0 | 1 | `INI_SYSTEM` | Disponible a partir de WinCache 1.3.6.3. Eliminada a partir de 2.0.0.0 |
| [wincache.filemapdir](#ini.wincache.filemapdir) | NULL | NULL | NULL | `INI_SYSTEM` | Disponible a partir de WinCache 1.3.7.4 |

Opciones de configuración de WinCache

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`wincache.fcenabled` `bool`  
Habilita o deshabilita la caché de ficheros.

`wincache.fcenabledfilter` `string`  
Define una lista separada por comas de identificadores de sitios web de IIS donde debería habilitarse o deshabilitarse la caché de ficheros. Esta opción funciona junto con `wincache.fcenabled`: si `wincache.fcenabled` se establece a 1, los sitios enumerados en `wincache.fcenabledfilter` tendrán la caché de ficheros desactivada; si `wincache.fcenabled` se establece a 0, los sitios enumerados en `wincache.fcenabledfilter` tendrán la caché activada.

`wincache.fcachesize` `int`  
Define el tamaño máximo de memoria (en megabytes) que se asigna a la caché de ficheros. Si el tamaño total de ficheros en caché excede el valor especificado en este ajuste, se eliminarán los ficheros más antiguos de la caché de ficheros.

`wincache.fcndetect` `bool`  
Habilita o deshabilita la detección de notificaciones de cambios en ficheros. Si está soportada la notificación de cambios en ficheros, se usará para refrescar las entradas de la caché de códigos de operación y de ficheros en cuanto los ficheros correspondientes sean modificados en un sistema de ficheros. Si la notificación de cambios en ficheros no está soportada, por ejemplo, al usar la compartición de ficheros en red, wincache hará un sondeo para los cambios en ficheros en intervalos de tiempo regulares especificados por `wincache.chkinterval`.

`wincache.maxfilesize` `int`  
Define el tamaño máximo permitido (en kilobytes) para que un fichero sea almacenado en caché. Si un fichero excede el valor especificado, no será almacenado en caché. Este ajuste se aplica solamente a la caché de ficheros.

`wincache.ocenabled` `bool`  
> [!WARNING]
> Esta opción ha sido *eliminada* a partir de 2.0.0.0

Habilita o deshabilita la caché de códigos de operaciones ("opcodes")

`wincache.ocenabledfilter` `string`  
> [!WARNING]
> Esta opción ha sido *eliminada* a partir de 2.0.0.0

Define una lista separada por comas de identificadores de sitios web de IIS donde se debería habilitar o deshabilitar la caché de códigos de operaciones. Este ajuste funciona junto con `wincache.ocenabled`: si `wincache.ocenabled` se establece a 1, los sitios enumerados en `wincache.ocenabledfilter` tendrán la caché de códigos de operaciones desactivada; si `wincache.ocenabled` se establece a 0, los sitios enumerados en `wincache.ocenabledfilter` tendrán la caché de códigos de operaciones activada.

`wincache.ocachesize` `int`  
> [!WARNING]
> Esta opción ha sido *eliminada* a partir de 2.0.0.0

Define el tamaño máximo de memoria (en megabytes) que se asigna a la caché de códigos de operaciones. Si el tamaño de dicha caché excede el valor especificado se eliminarán de la caché los códigos de operación más antiguos. Observe que el tamaño de la caché de códigos de operaciones debe ser al menos tres veces mayor que el tamaño de la caché de ficheros. Si no fuera así, el tamaño de la caché de códigos de operaciones será aumentada automáticamente.

`wincache.filecount` `int`  
Define cuántos ficheros se preveen que almacene en caché la extensión, para así asignar el tamaño de memoria apropiada en el momento del arranque. Si el número de ficheros excede el valor especificado, WinCache reasignará tanta memoria como sea necesaria.

`wincache.chkinterval` `int`  
Define la frecuencia (en segundos) con que la extensión comprobará los cambios en ficheros para refrescar la caché. Si se establece a 0 se deshabilitará el refresco de la caché. Los cambios en ficheros no se verán reflejados en la caché al menos que la entrada de la caché para tales ficheros sea eliminada mediante limpieza ("scavenger"), o la provisión ("pool") de aplicaciones de IIS sea reclicada, o se llame a la función wincache_refresh_if_changed.

`wincache.ttlmax` `int`  
Define el tiempo máximo de vida (en segundos) para una entrada de caché que no se esté usando. Si se establece a 0, se desactivará la limpieza de la caché, por lo que las entradas en caché nunca serán eliminadas durante el tiempo de vida del proceso obrero ("worker") de IIS.

`wincache.enablecli` `bool`  
Define si la caché se habilita cuando PHP se está ejecutando en modo de línea de comandos (CLI).

`wincache.ignorelist` `string`  
Define una lista de ficheros que no deberían ser almacenados en caché por la extensión. La lista de ficheros se especifica empleando solamente nombres de ficheros, separados por el símbolo tubería - "\|".

Ejemplo de `wincache.ignorelist`

```php
wincache.ignorelist = "index.php|misc.php|admin.php"

       
```

`wincache.namesalt` `string`  
Define un string que será usado al nombrar los objetos específicos de la extensión que están almacenados en la memoria compartida. Se emplea para evitar conflictos que podrían causarse si otras aplicaciones dentro de un proceso obrero de IIS intenta acceder a la memoria compartida. La longitud del sting namesalt no puede exceder de 8 caracteres.

`wincache.ucenabled` `bool`  
Habilita o deshabilita la caché de usuarios.

`wincache.ucachesize` `int`  
Define el tamaño máximo de memoria en megabytes que se asigna para la caché de usuario. Si el tamaño total de las variables almacenadas en la caché de usuario excede el valor especificado, se eliminarán las variables más antiguas de la caché.

`wincache.scachesize` `int`  
Define el tamaño máximo de memoria en megabytes que se asigna para la caché de sesión. Si el tamaño total de los datos almacenados en la caché de sesión excede el valor especificado, se eliminarán los datos más antiguos de la caché.

`wincache.rerouteini` `string`  
> [!WARNING]
> Esta opción ha sido *eliminada* a partir de 1.3.7. Véase `wincache.reroute_enabled` para una funcionalidad similar a partir de 1.3.7.

Especifica una ruta absoluta o relativa al fichero reroute.ini que contiene la lista de funciones de PHP cuya implementación debería ser remplazada con las funciones equivalentes de WinCache. Si se especifica una ruta relativa, se asume que sea relativa a la ubicación del fichero php-cgi.exe.

`wincache.reroute_enabled` `bool`  
Habilita o deshabilita el redireccionamiento de varias funciones de E/S de ficheros a través de la caché de ficheros.

`wincache.srwlocks` `bool`  
> [!WARNING]
> Esta opción ha sido *eliminada* a partir de 2.0.0.0

Habilita o deshabilita el uso de bloqueos ("locks) de lectura/escritura compartidos. La deshabilitación es útil cuando se dan condiciones de problemas de punto muerto ("deadlock") en WinCache.

`wincache.filemapdir` `string`  
Especifica una ruta absoluta al directorio donde WinCache almacenará los ficheros temporales empleados para segmentos de memoria compartida.

Este directorio debe estar en la máquina local y no en un sistema de ficheros en la red.

Si no se especifica este directorio, WinCache utilizará el fichero de paginación de Windows para todos los segmentos de memoria compartida.
