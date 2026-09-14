---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/yaf.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: e2f2172bf
order: 104490
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [yaf.library](#ini.yaf.library) |  | `INI_ALL` |  |
| [yaf.action_prefer](#ini.yaf.action-prefer) | 0 | `INI_ALL` |  |
| [yaf.lowcase_path](#ini.yaf.lowcase-path) | 0 | `INI_ALL` |  |
| [yaf.use_spl_autoload](#ini.yaf.use-spl-autoload) | 0 | `INI_ALL` |  |
| [yaf.forward_limit](#ini.yaf.forward-limit) | 5 | `INI_ALL` |  |
| [yaf.name_suffix](#ini.yaf.name-suffix) | 1 | `INI_ALL` |  |
| [yaf.name_separator](#ini.yaf.name-separator) |  | `INI_ALL` |  |
| [yaf.cache_config](#ini.yaf.cache-config) | 0 | `INI_SYSTEM` |  |
| [yaf.environ](#ini.yaf.environ) | product | `INI_SYSTEM` |  |
| [yaf.use_namespace](#ini.yaf.use-namespace) | 0 | `INI_ALL` |  |

Opciones de configuración de Yaf

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`yaf.library` `string`  
La ruta de la biblioteca global, Yaf_loader buscará la biblioteca global dentro de este directorio.

`yaf.action_prefer` `int`  
Si solamente hay una parte en PATH_INFO, debería considerarse como un controlador o una acción.

Si se configura a "On", se considerará como un nombre de una Acción.

`yaf.lowcase_path` `int`  
Si transformar a minúsculas todas las rutas durante la autocarga de clases.

`yaf.use_spl_autoload` `int`  
Cuando este valor es "On", si `Yaf_Loader` no puede encontrar una clase, devolverá `false`, después da la oportunidad de llamar a otra función de autocarga.

Cuando este valor es "Off", si `Yaf_Loader` no puede encontrar una clase, devolverá `true`, y hará que la autocarga de la clase falle permanentemente.

> [!NOTE]
> Yaf registrará su cargador durante la instanciación de `Yaf_Application`, por lo que cualquier otro autocargador que se registre antes de la instanciación será llamado antes de Yaf_Loader::autoload.

Cuando este valor es "Off" (predeterminado), Yaf_Loader::autoload devolverá siempre `true`.

`yaf.forward_limit` `int`  
La cuenta hacia adelante máxima, por defecto es 5, lo que significa que se puede tener un valor máximo de 5 en la pila hacia adelante.

Esto es una protección para prevenir Yaf_Controller_Abstract::forward recursivas.

`yaf.name_suffix` `int`  
Cuando es "On", Yaf_Loader identificará una clase por su sufijo para decidir si es una clase MVC.

Cuando es "Off", Yaf_Loader buscará el prefijo del nombre de la clase.

`yaf.name_separator` `string`  
Cuando no está vacío, Yaf_Loader identificará el sufijo de la clase y el valor de la cadena para ésta.

Por ejemplo, cuando este valor es "\_", Yaf_Loader tomará Index_Controller como una clase Controladora, e IndexController como una clase normal.

`yaf.cache_config` `int`  
Si es "On", y mientras que se use el archifo de configuración ini como parámetro de Yaf_Application, el resultado de la compilación del fichero de configuración ini será almacenado en caché en el proceso de PHP.

> [!NOTE]
> Yaf examina el mtime del fichero ini, y si cambió desde la última compilación, Yaf lo recargará.

> [!WARNING]
> Yaf utiliza la ruta del fichero ini como la clave de entrada de caché, por lo que usa la ruta absoluta en la ruta del fichero ini, de otro modo podrían existir conflictos si dos aplicaciones usasen la misma ruta relativa de la configuración ini.

`yaf.environ` `string`  
Este valor es "product" por omisión, usado por Yaf para obtener la sección de configuración de un fichero de configuración ini.

Es decir, si este valor es "product", Yaf usará la sección llamada "product" en el fichero de configuración ini (el primier parámetro de la clase `Yaf_Application`) como configuración final de la clase `Yaf_Application`.

`yaf.use_namespace` `int`  
Si este valor es "On", todas las clases de Yaf se nombrarán al estilo del espacio de nombres.

Por ejemplo:

    Yaf_Route_Rewrite => \Yaf\Route\Rewrite
    Yaf_Request_Http  => \Yaf\Request\Http
            
          

Existe una excepción, que es algunas clases como `Yaf_Controller_Abstract`. El último coponente es una palabra clave de PHP, no podría usarse como nombre de una clase, por lo que para tales clases:

    Yaf_Controller_Abstract => \Yaf\Controller_Abstract
    Yaf_Route_Static => \Yaf\Route_Static
