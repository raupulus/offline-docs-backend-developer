---
title: '"winreg" --- Windows registry access'
source_url: https://docs.python.org/es/3
source_path: library/winreg.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4530
---

# "winreg" --- Windows registry access

======================================================================

Estas funciones exponen la API de registro de Windows a Python. En
lugar de utilizar un número entero como identificador de registro, se
utiliza un handle object para garantizar que los identificadores se
cierren correctamente, incluso si el programador se niega a cerrarlos
explícitamente.

Availability: Windows.

Distinto en la versión 3.3: Varias funciones de este módulo solían
lanzar un "WindowsError", que ahora es un alias de "OSError".

## Funciones

Este módulo ofrece las siguientes funciones:

winreg.CloseKey(hkey)

   Cierra una clave de registro abierta previamente. El argumento
   *hkey* especifica una clave abierta previamente.

   Nota:

     Si *hkey* no se cierra con este método (o mediante
     "hkey.Close()"), se cierra cuando Python destruye el objeto
     *hkey*.

winreg.ConnectRegistry(computer_name, key)

   Establece una conexión con un identificador de registro predefinido
   en otra computadora y retorna un handle object.

   *computer_name* es el nombre de la computadora remota, de la forma
   "r”\\computername”". Si es "None", se utiliza la computadora local.

   *key* es el identificador predefinido al que conectarse.

   El valor de retorno es el identificador de la llave abierta. Si la
   función falla, se lanza una excepción "OSError".

   Lanza un auditing event "winreg.ConnectRegistry" con argumentos
   "computer_name", "key".

   Distinto en la versión 3.3: Ver above.

winreg.CreateKey(key, sub_key)

   Crea o abre la clave especificada, retornando un handle object.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *sub_key* es una cadena de caracteres que nombra la clave que este
   método abre o crea.

   Si *key* es una de las claves predefinidas, *sub_key* puede ser
   "None". En ese caso, el identificador retornado es el mismo
   identificador de clave que se pasó a la función.

   Si la clave ya existe, esta función abre la clave existente.

   El valor de retorno es el identificador de la llave abierta. Si la
   función falla, se lanza una excepción "OSError".

   Lanza un auditing event "winreg.CreateKey" con los argumentos
   "key", "sub_key", "access".

   Lanza un auditing event "winreg.OpenKey/result" con el argumento
   "key".

   Distinto en la versión 3.3: Ver above.

winreg.CreateKeyEx(key, sub_key, reserved=0, access=KEY_WRITE)

   Crea o abre la clave especificada, retornando un handle object.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *sub_key* es una cadena de caracteres que nombra la clave que este
   método abre o crea.

   *reserved* es un número entero reservado y debe ser cero. El valor
   predeterminado es cero.

   *access* es un número entero que especifica una máscara de acceso
   que describe el acceso de seguridad deseado para la clave. El valor
   predeterminado es "KEY_WRITE". Ver Access Rights para otros valores
   permitidos.

   Si *key* es una de las claves predefinidas, *sub_key* puede ser
   "None". En ese caso, el identificador retornado es el mismo
   identificador de clave que se pasó a la función.

   Si la clave ya existe, esta función abre la clave existente.

   El valor de retorno es el identificador de la llave abierta. Si la
   función falla, se lanza una excepción "OSError".

   Lanza un auditing event "winreg.CreateKey" con los argumentos
   "key", "sub_key", "access".

   Lanza un auditing event "winreg.OpenKey/result" con el argumento
   "key".

   Added in version 3.2.

   Distinto en la versión 3.3: Ver above.

winreg.DeleteKey(key, sub_key)

   Elimina la clave especificada.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *sub_key* es una cadena de caracteres que debe ser una subclave de
   la clave identificada por el parámetro *key*. Este valor no debe
   ser "None", y es posible que la clave no tenga subclaves.

   *Este método no puede eliminar claves con subclaves.*

   Si el método tiene éxito, se elimina toda la clave, incluidos todos
   sus valores. Si el método falla, se lanza una excepción "OSError".

   Lanza un auditing event "winreg.DeleteKey" con los argumentos
   "key", "sub_key", "access".

   Distinto en la versión 3.3: Ver above.

winreg.DeleteKeyEx(key, sub_key, access=KEY_WOW64_64KEY, reserved=0)

   Elimina la clave especificada.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *sub_key* es una cadena de caracteres que debe ser una subclave de
   la clave identificada por el parámetro *key*. Este valor no debe
   ser "None", y es posible que la clave no tenga subclaves.

   *reserved* es un número entero reservado y debe ser cero. El valor
   predeterminado es cero.

   *access* es un número entero que especifica una máscara de acceso
   que describe el acceso de seguridad deseado para la clave. El valor
   predeterminado es "KEY_WOW64_64KEY". En Windows de 32-bit, las
   constantes WOW64 son ignoradas. Ver Access Rights para otros
   valores permitidos.

   *Este método no puede eliminar claves con subclaves.*

   Si el método tiene éxito, se elimina toda la clave, incluidos todos
   sus valores. Si el método falla, se lanza una excepción "OSError".

   En versiones de Windows no compatibles, se lanza
   "NotImplementedError".

   Lanza un auditing event "winreg.DeleteKey" con los argumentos
   "key", "sub_key", "access".

   Added in version 3.2.

   Distinto en la versión 3.3: Ver above.

winreg.DeleteValue(key, value)

   Elimina un valor con nombre de una clave de registro.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *value* es una cadena que identifica el valor a eliminar.

   Lanza un auditing event "winreg.DeleteValue" con argumentos "key",
   "value".

winreg.EnumKey(key, index)

   Enumera las subclaves de una clave de registro abierta y retorna
   una cadena de caracteres.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *index* es un número entero que identifica el índice de la clave a
   recuperar.

   La función recupera el nombre de una subclave cada vez que se
   llama. Normalmente se llama repetidamente hasta que se lanza una
   excepción "OSError", lo que indica que no hay más valores
   disponibles.

   Lanza un auditing event "winreg.EnumKey" con argumentos "key",
   "index".

   Distinto en la versión 3.3: Ver above.

winreg.EnumValue(key, index)

   Enumera los valores de una clave de registro abierta y retorna una
   tupla.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *index* es un número entero que identifica el índice del valor a
   recuperar.

   La función recupera el nombre de una subclave cada vez que se
   llama. Normalmente se llama repetidamente, hasta que se lanza una
   excepción "OSError", lo que indica que no hay más valores.

   El resultado es una tupla de 3 elementos:

   +---------+----------------------------------------------+
   | Índice  | Significado                                  |
   |=========|==============================================|
   | "0"     | Una cadena de caracteres que identifica el   |
   |         | nombre del valor                             |
   +---------+----------------------------------------------+
   | "1"     | Un objeto que contiene los datos del valor y |
   |         | cuyo tipo depende del tipo de registro       |
   |         | subyacente                                   |
   +---------+----------------------------------------------+
   | "2"     | Un número entero que identifica el tipo de   |
   |         | datos de valor (consulte la tabla en los     |
   |         | documentos para "SetValueEx()")              |
   +---------+----------------------------------------------+

   Lanza un auditing event "winreg.EnumValue" con argumentos "key",
   "index".

   Distinto en la versión 3.3: Ver above.

winreg.ExpandEnvironmentStrings(str)

   Expande los marcadores de posición de la variable de entorno
   "%NAME%" en cadenas como "REG_EXPAND_SZ":

      >>> ExpandEnvironmentStrings('%windir%')
      'C:\\Windows'

   Lanza un auditing event "winreg.ExpandEnvironmentStrings" con el
   argumento "str".

winreg.FlushKey(key)

   Escribe todos los atributos de una clave en el registro.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   No es necesario llamar a "FlushKey()" para cambiar una clave. Los
   cambios en el registro se descargan en el disco mediante el
   registro mediante su vaciador diferido. Los cambios en el registro
   también se vacían en el disco cuando se apaga el sistema. A
   diferencia de "CloseKey()", el método "FlushKey()" retorna solo
   cuando todos los datos se han escrito en el registro. Una
   aplicación solo debe llamar a "FlushKey()" si requiere absoluta
   certeza de que los cambios de registro están en el disco.

   Nota:

     Si no sabe si se requiere una llamada "FlushKey()", probablemente
     no lo sea.

winreg.LoadKey(key, sub_key, file_name)

   Crea una subclave bajo la clave especificada y almacena la
   información de registro de un archivo especificado en esa subclave.

   *key* es un identificador retornado por "ConnectRegistry()" o una
   de las constantes "HKEY_USERS" o "HKEY_LOCAL_MACHINE".

   *sub_key* es una cadena de caracteres que identifica la subclave a
   cargar.

   *file_name* es el nombre del archivo desde el que cargar los datos
   de registro. Este archivo debe haber sido creado con la función
   "SaveKey()". En el sistema de archivos de la tabla de asignación de
   archivos (FAT), es posible que el nombre del archivo no tenga
   extensión.

   Una llamada a "LoadKey()" falla si el proceso de llamada no tiene
   el privilegio "SE_RESTORE_PRIVILEGE". Tenga en cuenta que los
   privilegios son diferentes de los permisos; consulte la RegLoadKey
   documentation para obtener más detalles.

   Si *key* es un identificador retornado por "ConnectRegistry()",
   entonces la ruta especificada en *file_name* es relativa a la
   computadora remota.

   Lanza un auditing event "winreg.LoadKey" con los argumentos "key",
   "sub_key", "file_name".

winreg.OpenKey(key, sub_key, reserved=0, access=KEY_READ)
winreg.OpenKeyEx(key, sub_key, reserved=0, access=KEY_READ)

   Abre la clave especificada, retornando a handle object.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *sub_key* es una cadena de caracteres que identifica la sub_key
   para abrir.

   *reserved* es un número entero reservado y debe ser cero. El valor
   predeterminado es cero.

   *access* es un número entero que especifica una máscara de acceso
   que describe el acceso de seguridad deseado para la clave. El valor
   predeterminado es "KEY_READ". Ver Access Rights para otros valores
   permitidos.

   El resultado es un nuevo identificador para la clave especificada.

   Si la función falla, se lanza "OSError".

   Lanza un auditing event "winreg.OpenKey" con los argumentos "key",
   "sub_key", "access".

   Lanza un auditing event "winreg.OpenKey/result" con el argumento
   "key".

   Distinto en la versión 3.2: Permite el uso de argumentos con
   nombre.

   Distinto en la versión 3.3: Ver above.

winreg.QueryInfoKey(key)

   Retorna información sobre una clave, como una tupla.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   El resultado es una tupla de 3 elementos:

   +---------+-----------------------------------------------+
   | Índice  | Significado                                   |
   |=========|===============================================|
   | "0"     | Un número entero que indica el número de      |
   |         | subclaves que tiene esta clave.               |
   +---------+-----------------------------------------------+
   | "1"     | Un número entero que da el número de valores  |
   |         | que tiene esta clave.                         |
   +---------+-----------------------------------------------+
   | "2"     | Un número entero que indica la última vez que |
   |         | se modificó la clave (si está disponible)     |
   |         | como cientos de nanosegundos desde el 1 de    |
   |         | enero de 1601.                                |
   +---------+-----------------------------------------------+

   Lanza un auditing event "winreg.QueryInfoKey" con el argumento
   "key".

winreg.QueryValue(key, sub_key)

   Recupera el valor sin nombre de una clave, como una cadena de
   caracteres.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *sub_key* es una cadena de caracteres que contiene el nombre de la
   subclave con la que está asociado el valor. Si este parámetro es
   "None" o está vacío, la función recupera el valor establecido por
   el método "SetValue()" para la clave identificada por *key*.

   Los valores del registro tienen componentes de nombre, tipo y
   datos. Este método recupera los datos del primer valor de una clave
   que tiene un nombre "NULL". Pero la llamada a la API subyacente no
   retorna el tipo, así que siempre use "QueryValueEx()" si es
   posible.

   Lanza un auditing event "winreg.QueryValue" con los argumentos
   "key", "sub_key", "value_name".

winreg.QueryValueEx(key, value_name)

   Recupera el tipo y los datos de un nombre de valor especificado
   asociado con una clave de registro abierta.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *value_name* es una cadena de caracteres que indica el valor a
   consultar.

   El resultado es una tupla de 2 elementos:

   +---------+-------------------------------------------+
   | Índice  | Significado                               |
   |=========|===========================================|
   | "0"     | El valor del elemento de registro.        |
   +---------+-------------------------------------------+
   | "1"     | Un número entero que proporciona el tipo  |
   |         | de registro para este valor (consulte la  |
   |         | tabla en docs para "SetValueEx()")        |
   +---------+-------------------------------------------+

   Lanza un auditing event "winreg.QueryValue" con los argumentos
   "key", "sub_key", "value_name".

winreg.SaveKey(key, file_name)

   Guarda la clave especificada y todas sus subclaves en el archivo
   especificado.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *file_name* es el nombre del archivo en el que se guardarán los
   datos del registro. Este archivo no puede existir ya. Si este
   nombre de archivo incluye una extensión, no se puede usar en
   sistemas de archivos de tabla de asignación de archivos (FAT)
   mediante el método "LoadKey()".

   Si *key* representa una clave en una computadora remota, la ruta
   descrita por *file_name* es relativa a la computadora remota. El
   invocador de este método debe poseer el privilegio de seguridad
   **SeBackupPrivilege**. Tenga en cuenta que los privilegios son
   diferentes a los permisos -- consulte la documentación sobre
   conflictos entre derechos de usuario y permisos para más detalles.

   Esta función pasa "NULL" para *security_attributes* a la API.

   Lanza un auditing event "winreg.SaveKey" con los argumentos "key",
   "file_name".

winreg.SetValue(key, sub_key, type, value)

   Asocia un valor con una clave especificada.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *sub_key* es una cadena de caracteres que nombra la subclave con la
   que está asociado el valor.

   *type* es un número entero que especifica el tipo de datos.
   Actualmente debe ser "REG_SZ", lo que significa que solo se admiten
   cadenas de caracteres. Utilice la función: "SetValueEx()" para
   admitir otros tipos de datos.

   *value* es una cadena de caracteres que especifica el nuevo valor.

   Si la clave especificada por el parámetro *sub_key* no existe, la
   función SetValue la crea.

   Las longitudes de los valores están limitadas por la memoria
   disponible. Los valores largos (más de 2048 bytes) deben
   almacenarse como archivos con los nombres de archivo almacenados en
   el registro de configuración. Esto ayuda a que el registro funcione
   de manera eficiente.

   La clave identificada por el parámetro *key* debe haber sido
   abierta con acceso "KEY_SET_VALUE".

   Lanza un auditing event "winreg.SetValue" con argumentos "key",
   "sub_key", "type", "value".

winreg.SetValueEx(key, value_name, reserved, type, value)

   Almacena datos en el campo de valor de una clave de registro
   abierta.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   *value_name* es una cadena de caracteres que nombra la subclave con
   la que está asociado el valor.

   *reserved* puede ser cualquier cosa — cero siempre se pasa a la
   API.

   *type* es un número entero que especifica el tipo de datos.
   Consulte Value Types para los tipos disponibles.

   *value* es una cadena de caracteres que especifica el nuevo valor.

   Este método también puede establecer un valor adicional e
   información de tipo para la clave especificada. La clave
   identificada por el parámetro clave debe haber sido abierta con
   acceso "KEY_SET_VALUE".

   Para abrir la clave, use los métodos "CreateKey()" o "OpenKey()".

   Las longitudes de los valores están limitadas por la memoria
   disponible. Los valores largos (más de 2048 bytes) deben
   almacenarse como archivos con los nombres de archivo almacenados en
   el registro de configuración. Esto ayuda a que el registro funcione
   de manera eficiente.

   Lanza un auditing event "winreg.SetValue" con argumentos "key",
   "sub_key", "type", "value".

winreg.DisableReflectionKey(key)

   Desactiva la reflexión del registro para los procesos de 32 bits
   que se ejecutan en un sistema operativo de 64 bits.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   Generalmente lanzará "NotImplementedError" si se ejecuta en un
   sistema operativo de 32 bits.

   Si la clave no está en la lista de reflexión, la función tiene
   éxito pero no tiene ningún efecto. La desactivación de la reflexión
   de una clave no afecta la reflexión de ninguna subclave.

   Lanza un auditing event "winreg.DisableReflectionKey" con el
   argumento "key".

winreg.EnableReflectionKey(key)

   Restaura la reflexión del registro para la clave deshabilitada
   especificada.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   Generalmente lanzará "NotImplementedError" si se ejecuta en un
   sistema operativo de 32 bits.

   La restauración de la reflexión de una clave no afecta la reflexión
   de ninguna subclave.

   Lanza un auditing event "winreg.EnableReflectionKey" con el
   argumento "key".

winreg.QueryReflectionKey(key)

   Determina el estado de reflexión para la clave especificada.

   *key* es una clave ya abierta, o una de las predefinidas HKEY_*
   constants.

   Retorna "True" si la reflexión está deshabilitada.

   Generalmente lanzará "NotImplementedError" si se ejecuta en un
   sistema operativo de 32 bits.

   Lanza un auditing event "winreg.QueryReflectionKey" con el
   argumento "key".

## Constantes

The following constants are defined for use in many "winreg"
functions.

### HKEY_* Constantes

winreg.HKEY_CLASSES_ROOT

   Las entradas de registro subordinadas a esta clave definen tipos (o
   clases) de documentos y las propiedades asociadas con esos tipos.
   Las aplicaciones Shell y COM utilizan la información almacenada en
   esta clave.

winreg.HKEY_CURRENT_USER

   Las entradas de registro subordinadas a esta clave definen las
   preferencias del usuario actual. Estas preferencias incluyen la
   configuración de variables de entorno, datos sobre grupos de
   programas, colores, impresoras, conexiones de red y preferencias de
   la aplicación.

winreg.HKEY_LOCAL_MACHINE

   Las entradas de registro subordinadas a esta clave definen el
   estado físico de la computadora, incluidos los datos sobre el tipo
   de bus, la memoria del sistema y el hardware y software instalados.

winreg.HKEY_USERS

   Las entradas de registro subordinadas a esta clave definen la
   configuración de usuario predeterminada para nuevos usuarios en la
   computadora local y la configuración de usuario para el usuario
   actual.

winreg.HKEY_PERFORMANCE_DATA

   Las entradas de registro subordinadas a esta clave le permiten
   acceder a los datos de rendimiento. Los datos no se almacenan
   realmente en el registro; las funciones de registro hacen que el
   sistema recopile los datos de su fuente.

winreg.HKEY_CURRENT_CONFIG

   Contiene información sobre el perfil de hardware actual del sistema
   informático local.

winreg.HKEY_DYN_DATA

   Esta clave no se usa en versiones de Windows posteriores a la 98.

### Access Rights

Para más información, ver Registry Key Security and Access.

winreg.KEY_ALL_ACCESS

   Combina los derechos de acceso STANDARD_RIGHTS_REQUIRED,
   "KEY_QUERY_VALUE", "KEY_SET_VALUE", "KEY_CREATE_SUB_KEY",
   "KEY_ENUMERATE_SUB_KEYS", "KEY_NOTIFY", y "KEY_CREATE_LINK".

winreg.KEY_WRITE

   Combina los derechos de acceso STANDARD_RIGHTS_WRITE,
   "KEY_SET_VALUE", y "KEY_CREATE_SUB_KEY".

winreg.KEY_READ

   Combina los valores STANDARD_RIGHTS_READ, "KEY_QUERY_VALUE",
   "KEY_ENUMERATE_SUB_KEYS", y "KEY_NOTIFY".

winreg.KEY_EXECUTE

   Equivalente a "KEY_READ".

winreg.KEY_QUERY_VALUE

   Requerido para consultar los valores de una clave de registro.

winreg.KEY_SET_VALUE

   Requerido para crear, eliminar o establecer un valor de registro.

winreg.KEY_CREATE_SUB_KEY

   Necesario para crear una subclave de una clave de registro.

winreg.KEY_ENUMERATE_SUB_KEYS

   Requerido para enumerar las subclaves de una clave de registro.

winreg.KEY_NOTIFY

   Requerido para solicitar notificaciones de cambio para una clave de
   registro o para subclaves de una clave de registro.

winreg.KEY_CREATE_LINK

   Reservado para uso del sistema.

#### Específico de 64 bits

Para más información, ver Accessing an Alternate Registry View.

winreg.KEY_WOW64_64KEY

   Indica que una aplicación en Windows de 64 bits debería funcionar
   en la vista de registro de 64 bits. En Windows de 32 bits, esta
   constante se ignora.

winreg.KEY_WOW64_32KEY

   Indica que una aplicación en Windows de 64 bits debería funcionar
   en la vista de registro de 32 bits. En Windows de 32 bits, esta
   constante se ignora.

### Tipos de valor

Para más información, ver Registry Value Types.

winreg.REG_BINARY

   Datos binarios en cualquier forma.

winreg.REG_DWORD

   Número de 32 bits.

winreg.REG_DWORD_LITTLE_ENDIAN

   Un número de 32 bits en formato little-endian. Equivalente a
   "REG_DWORD".

winreg.REG_DWORD_BIG_ENDIAN

   Un número de 32 bits en formato big-endian.

winreg.REG_EXPAND_SZ

   Cadena de caracteres terminada en nulo que contiene referencias a
   variables de entorno ("%PATH%").

winreg.REG_LINK

   Un enlace simbólico Unicode.

winreg.REG_MULTI_SZ

   Una secuencia de cadenas de caracteres terminadas en nulo,
   terminadas por dos caracteres nulos. (Python maneja esta
   terminación automáticamente).

winreg.REG_NONE

   Sin tipo de valor definido.

winreg.REG_QWORD

   Un número de 64 bits.

   Added in version 3.6.

winreg.REG_QWORD_LITTLE_ENDIAN

   Un número de 64 bits en formato little-endian. Equivalente a
   "REG_QWORD".

   Added in version 3.6.

winreg.REG_RESOURCE_LIST

   Una lista de recursos de controladores de dispositivo.

winreg.REG_FULL_RESOURCE_DESCRIPTOR

   Una configuración de hardware.

winreg.REG_RESOURCE_REQUIREMENTS_LIST

   Una lista de recursos de hardware.

winreg.REG_SZ

   Una cadena de caracteres terminada en nulo.

## Objetos de control del registro

Este objeto envuelve un objeto HKEY de Windows y lo cierra
automáticamente cuando se destruye. Para garantizar la limpieza, puede
llamar al método "Close()" en el objeto, o a la función "CloseKey()".

Todas las funciones de registro de este módulo retornan uno de estos
objetos.

Todas las funciones de registro de este módulo que aceptan un objeto
identificador también aceptan un número entero, sin embargo, se
recomienda el uso del objeto identificador.

Los objetos de control proporcionan semántica para "__bool__()" -- así

   if handle:
       print("Yes")

imprimirá "Yes" si el controlador es válido actualmente (no se ha
cerrado o desprendido).

Los objetos de identificador se pueden convertir a un número entero
(por ejemplo, usando la función incorporada "int()" function), en cuyo
caso se retorna el valor de identificador de Windows subyacente.
También puede usar el método "Detach()" para retornar el identificador
de enteros y también desconectar el identificador de Windows del
objeto identificador.

PyHKEY.Close()

   Cierra el identificador de Windows subyacente.

   Si el controlador ya está cerrado, no se lanza ningún error.

PyHKEY.Detach()

   Separa el identificador de Windows del objeto identificador.

   El resultado es un número entero que contiene el valor del
   identificador antes de que se separe. Si el controlador ya está
   separado o cerrado, esto retornará cero.

   Después de llamar a esta función, el identificador se invalida
   efectivamente, pero el identificador no se cierra. Llamaría a esta
   función cuando necesite que el identificador Win32 subyacente
   exista más allá de la vida útil del objeto identificador.

   Lanza un auditing event "winreg.PyHKEY.Detach" con el argumento
   "key".

PyHKEY.__enter__()
PyHKEY.__exit__(*exc_info)

   El objeto HKEY implementa "__enter__()" y "__exit__()" y, por lo
   tanto, admite el protocolo de contexto para la declaración "with":

      with OpenKey(HKEY_LOCAL_MACHINE, "foo") as key:
          ...  # work with key

   cerrará automáticamente *key* cuando el control abandone el bloque
   "with".
