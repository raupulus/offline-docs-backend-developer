---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/com.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 8000
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [com.allow_dcom](#ini.com.allow-dcom) | "0" | `INI_SYSTEM` |  |
| [com.autoregister_typelib](#ini.com.autoregister-typelib) | "0" | `INI_ALL` |  |
| [com.autoregister_verbose](#ini.com.autoregister-verbose) | "0" | `INI_ALL` |  |
| [com.autoregister_casesensitive](#ini.com.autoregister-casesensitive) | "1" | `INI_ALL` |  |
| [com.code_page](#ini.com.code-page) | "" | `INI_ALL` |  |
| [com.dotnet_version](#ini.com.dotnet-version) | "" | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0 |
| [com.typelib_file](#ini.com.typelib-file) | "" | `INI_SYSTEM` |  |

Opciones de configuración para COM

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`com.allow_dcom`  
Si esta directiva está activada, PHP tendrá permiso para operar como un cliente D-COM (Distributed COM) y permitirá a PHP instanciar objetos COM en un servidor remoto.

`com.autoregister_typelib`  
Si esta directiva está activada, PHP intentará declarar constantes provenientes de la biblioteca typelibrary de los objetos `COM` que instancia, si estos objetos implementan la interfaz requerida para obtener los datos solicitados. La sensibilidad de las constantes a la casse está controlada por la directiva de configuración `php.ini` [com.autoregister_casesensitive](#ini.com.autoregister-casesensitive).

`com.autoregister_verbose`  
Cuando esta directiva está activada, cualquier problema encontrado durante la carga de una typelibrary durante la instanciación del objeto será reportado utilizando el mecanismo de errores de PHP. Por defecto, está desactivada, lo que no da ninguna indicación sobre el fallo de la operación durante una búsqueda o carga de la biblioteca de tipo.

`com.autoregister_casesensitive`  
Esta directiva está activada por defecto y hace que las constantes encontradas en las bibliotecas de tipos autocargadas durante la instanciación de objetos `COM` sean registradas en modo sensible a la casse. Véase `com_load_typelib` para más detalles.

`com.code_page`  
Esta directiva permite especificar el code-page de los juegos de caracteres a utilizar al enviar y recibir cadenas hacia objetos COM. Si está vacía, PHP asumirá que se desea `CP_ACP`, que es el code-page sistema ANSI por defecto.

Si el texto en sus scripts está codificado con un diferente codificación o juego de caracteres por defecto, configurar esta directiva evitará tener que pasar todo su código como parámetro del constructor de la clase [???](#class.com). Tenga en cuenta que al usar esta directiva (como cualquier configuración de PHP), su código PHP pierde portabilidad. Se debe utilizar el parámetro del constructor siempre que sea posible.

`com.dotnet_version`  
La versión del framework .NET a utilizar para los objetos `dotnet`. El valor de esta configuración corresponde a los tres primeros números del número de la versión del framework, separados por puntos, y precedidos por la letra `v`, i.e. `v4.0.30319`.

`com.typelib_file`  
Cuando está configurada, esta directiva debe ser la ruta hacia un fichero que contiene una lista de bibliotecas a cargar al inicio. Cada línea será interpretada como el nombre de la biblioteca de tipos y cargada como si se hubiera utilizado `com_load_typelib`. Las constantes serán registradas de forma persistente, para que la biblioteca solo sea cargada una vez. Si el nombre de una biblioteca de tipos termina con `#cis` o `#case_insensitive`, entonces las constantes de esa biblioteca de tipos serán registradas en modo insensible a la casse.
