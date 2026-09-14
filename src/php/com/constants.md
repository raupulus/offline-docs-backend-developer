---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/com.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 7630
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`CLSCTX_INPROC_SERVER` (`int`)  
El código que crea y gestiona los objetos de esta clase es una DLL que se ejecuta en el mismo proceso que el llamante de la función especificando el contexto de clase.

`CLSCTX_INPROC_HANDLER` (`int`)  
El código que gestiona los objetos de esta clase es un gestorador en proceso. Se trata de una DLL que se ejecuta en el proceso cliente e implementa las estructuras del lado cliente de esta clase cuando las instancias de la clase son accesibles a distancia.

`CLSCTX_LOCAL_SERVER` (`int`)  
El código EXE que crea y gestiona los objetos de esta clase se ejecuta en la misma máquina pero se carga en un espacio de procesos distinto.

`CLSCTX_REMOTE_SERVER` (`int`)  
Contexto distante. El código que crea y gestiona los objetos de esta clase se ejecuta en un ordenador diferente.

`CLSCTX_SERVER` (`int`)  
Indica un código servidor, ya sea en proceso, local o distante. Esta definición hace un OU lógico entre `CLSCTX_INPROC_SERVER`, `CLSCTX_LOCAL_SERVER`, y `CLSCTX_REMOTE_SERVER`.

`CLSCTX_ALL` (`int`)  
Indica todos los contextos de clase. Esta definición hace un OU lógico entre `CLSCTX_INPROC_HANDLER` y `CLSCTX_SERVER`.

`VT_NULL` (`int`)  
Referencia de puntero NULL.

`VT_EMPTY` (`int`)  
Una propiedad con un indicador de tipo `VT_EMPTY` no tiene datos asociados; es decir, el tamaño del valor es cero.

`VT_INT` (`int`)  
Valor entero signado de 4 bytes (equivalente a `VT_I4`).

`VT_I1` (`int`)  
Entero signado de 1 byte.

`VT_I2` (`int`)  
Dos bytes representando un valor entero signado de 2 bytes.

`VT_I4` (`int`)  
Valor entero signado de 4 bytes.

`VT_I8` (`int`)  
Valor entero signado de 8 bytes.

Solo en x64.

`VT_UINT` (`int`)  
Entero no signado de 4 bytes (equivalente a `VT_UI4`).

`VT_UI1` (`int`)  
Entero no signado de 1 byte.

`VT_UI2` (`int`)  
Entero no signado de 2 bytes.

`VT_UI4` (`int`)  
Entero no signado de 4 bytes.

`VT_UI8` (`int`)  
Entero no signado de 8 bytes.

Solo en x64

`VT_R4` (`int`)  
Valor en coma flotante IEEE 32 bits.

`VT_R8` (`int`)  
Valor en coma flotante IEEE 64 bits.

`VT_BOOL` (`int`)  
Valor bool.

`VT_ERROR` (`int`)  
Código de error; contiene el código de estado asociado a el error.

`VT_CY` (`int`)  
Entero en complemento a dos de 8 bytes (escalado por 10 000).

`VT_DATE` (`int`)  
Un número en coma flotante de 64 bits representando el número de días (no de segundos) transcurridos desde el `31 de diciembre de 1899`. Por ejemplo, `1 de enero de 1900` es `2,0`, `2 de enero de 1900` es `3,0`, etc. Este valor se almacena en la misma representación que `VT_R8`.

`VT_BSTR` (`int`)  
Puntero hacia una cadena Unicode terminada por un carácter nulo.

`VT_DECIMAL` (`int`)  
Una estructura decimal.

`VT_UNKNOWN` (`int`)  
Un puntero hacia un objeto que implementa la interfaz IUnknown.

`VT_DISPATCH` (`int`)  
Un puntero hacia un objeto que implementa la interfaz IDispatch.

`VT_VARIANT` (`int`)  
Un indicador de tipo seguido del valor correspondiente. `VT_VARIANT` puede ser utilizado únicamente con `VT_BYREF`.

`VT_ARRAY` (`int`)  
Si el indicador de tipo se combina con `VT_ARRAY` por un operador OU, el valor es un puntero hacia un `SAFEARRAY`. `VT_ARRAY` puede ser combinado por OU con los siguientes tipos de datos: `VT_I1`, `VT_UI1`, `VT_I2`, `VT_UI2`, `VT_I4`, `VT_UI4`, `VT_INT`, `VT_UINT`, `VT_R4`, `VT_R8`, `VT_BOOL`, `VT_DECIMAL`, `VT_ERROR`, `VT_CY`, `VT_DATE`, `VT_BSTR`, `VT_DISPATCH`, `VT_UNKNOWN` y `VT_VARIANT`.

`VT_BYREF` (`int`)  
Si el indicador de tipo se combina con `VT_BYREF` por un operador OU, el valor es una referencia. Los tipos de referencia se interpretan como una referencia hacia datos, similar al tipo referencia en C++.

`CP_ACP` (`int`)  
Página de código ANSI por omisión.

`CP_MACCP` (`int`)  
Página de código Macintosh.

`CP_OEMCP` (`int`)  
Página de código OEM por omisión.

`CP_UTF7` (`int`)  
Unicode (UTF-7).

`CP_UTF8` (`int`)  
Unicode (UTF-8).

`CP_SYMBOL` (`int`)  
Traducciones `SYMBOL`.

`CP_THREAD_ACP` (`int`)  
Página de código ANSI del hilo actual.

`VARCMP_LT` (`int`)  
El `bstr` de la izquierda es inferior al `bstr` de la derecha.

`VARCMP_EQ` (`int`)  
Los dos parámetros son iguales.

`VARCMP_GT` (`int`)  
El `bstr` de la izquierda es superior al `bstr` de la derecha.

`VARCMP_NULL` (`int`)  
Una de las expresiones es NULL.

`NORM_IGNORECASE` (`int`)  
Ignorar la sensibilidad a la casse.

`NORM_IGNORENONSPACE` (`int`)  
Ignorar los caracteres sin chasse.

`NORM_IGNORESYMBOLS` (`int`)  
Ignorar los símbolos.

`NORM_IGNOREWIDTH` (`int`)  
Ignorar la anchura de cadena.

`NORM_IGNOREKANATYPE` (`int`)  
Ignorar el tipo Kana.

`NORM_IGNOREKASHIDA` (`int`)  
Ignorar los caracteres kashida en árabe.

La disponibilidad depende de la biblioteca subyacente.

`DISP_E_DIVBYZERO` (`int`)  
Un error de retorno que indica una división por cero.

`DISP_E_OVERFLOW` (`int`)  
Un error que indica que un valor no ha podido ser convertido en su representación esperada.

`DISP_E_BADINDEX` (`int`)  
Un error que indica que un índice de array no existe.

`DISP_E_PARAMNOTFOUND` (`int`)  
Un valor de retorno que indica que uno de los ID de parámetro no corresponde a un parámetro del método.

`MK_E_UNAVAILABLE` (`int`)  
Código de estado iMoniker COM, devuelto en errores donde la llamada de función ha fallado debido a una indisponibilidad.

`LOCALE_NEUTRAL` (`int`)  
La configuración local neutra. Esta constante generalmente no se utiliza durante las llamadas a las API NLS. Utilizar en su lugar LOCALE_SYSTEM_DEFAULT.

`LOCALE_SYSTEM_DEFAULT` (`int`)  
La configuración local por omisión del sistema operativo.
