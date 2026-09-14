---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/ldap.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_revision: 10e6a2b04
order: 42930
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`LDAP_DEREF_NEVER` (`int`)  
Regla de desreferenciación de alias - Nunca.

`LDAP_DEREF_SEARCHING` (`int`)  
Regla de desreferenciación de alias - Buscar.

`LDAP_DEREF_FINDING` (`int`)  
Regla de desreferenciación de alias - Encontrar.

`LDAP_DEREF_ALWAYS` (`int`)  
Regla de desreferenciación de alias - Siempre.

`LDAP_OPT_DEREF` (`int`)  
Aplica reglas alternativas para seguir los alias en el servidor.

`LDAP_OPT_SIZELIMIT` (`int`)  
Especifica el número máximo de entradas que pueden ser devueltas de una posición de búsqueda.

> [!NOTE]
> El límite real también puede ser dado del lado del servidor. El más pequeño de los dos será el utilizado.

`LDAP_OPT_TIMELIMIT` (`int`)  
Especifica el número de segundos a esperar los resultados de búsqueda.

> [!NOTE]
> El límite real también puede ser dado del lado del servidor. El más pequeño de los dos será el utilizado.

`LDAP_OPT_NETWORK_TIMEOUT` (`int`)  
Opción para `ldap_set_option` que permite definir el timeout. (Disponible desde PHP 5.3.0)

`LDAP_OPT_PROTOCOL_VERSION` (`int`)  
Especifica la versión del protocolo LDAP a utilizar (V2 o V3).

`LDAP_OPT_ERROR_NUMBER` (`int`)  
Último número de error de sesión.

`LDAP_OPT_REFERRALS` (`int`)  
Especifica si se deben o no seguir los referentes devueltos por el servidor.

`LDAP_OPT_RESTART` (`int`)  
Determina si la conexión debe o no ser reiniciada implícitamente.

`LDAP_OPT_HOST_NAME` (`int`)  
Define/obtiene los hosts separados por un espacio cuando se intenta conectar.

`LDAP_OPT_ERROR_STRING` (`int`)  
Alias de `LDAP_OPT_DIAGNOSTIC_MESSAGE`.

`LDAP_OPT_DIAGNOSTIC_MESSAGE` (`int`)  
Obtiene el último mensaje de error de sesión.

`LDAP_OPT_MATCHED_DN` (`int`)  
Define/obtiene el DN asociado correspondiente a la conexión.

`LDAP_OPT_SERVER_CONTROLS` (`int`)  
Especifica una lista de controles de servidor a enviar con cada petición.

`LDAP_OPT_CLIENT_CONTROLS` (`int`)  
Especifica una lista de controles de cliente a enviar con cada petición.

`LDAP_OPT_DEBUG_LEVEL` (`int`)  
Especifica un nivel para las trazas de depuración, en forma de máscara de bits.

`LDAP_OPT_X_KEEPALIVE_IDLE` (`int`)  
Especifica el número de segundos durante los cuales una conexión debe permanecer inactiva antes de que TCP comience a enviar sondas KeepAlive.

`LDAP_OPT_X_KEEPALIVE_PROBES` (`int`)  
Especifica el número máximo de sondas KeepAlive que TCP debe enviar antes de eliminar la conexión.

`LDAP_OPT_X_KEEPALIVE_INTERVAL` (`int`)  
Especifica el intervalo en segundos entre dos sondas KeepAlive.

`LDAP_OPT_X_TLS_CACERTDIR` (`int`)  
Especifica la ruta de acceso del directorio que contiene los certificados de autoridad de certificación.

`LDAP_OPT_X_TLS_CACERTFILE` (`int`)  
Especifica la ruta de acceso completa del archivo de certificado de la autoridad de certificación.

`LDAP_OPT_X_TLS_CERTFILE` (`int`)  
Especifica la ruta de acceso completa del archivo de certificado.

`LDAP_OPT_X_TLS_CIPHER_SUITE` (`int`)  
Especifica la suite de cifrado autorizada.

`LDAP_OPT_X_TLS_CRLCHECK` (`int`)  
Especifica la estrategia de evaluación de las CRL. Debe ser una de las siguientes: `LDAP_OPT_X_TLS_CRL_NONE`, `LDAP_OPT_X_TLS_CRL_PEER`, `LDAP_OPT_X_TLS_CRL_ALL`.

> [!NOTE]
> Solo válido para OpenSSL.

`LDAP_OPT_X_TLS_CRLFILE` (`int`)  
Especifica la ruta de acceso completa del archivo CRL.

> [!NOTE]
> Solo válido para GnuTLS.

`LDAP_OPT_X_TLS_DHFILE` (`int`)  
Especifica la ruta de acceso completa del archivo que contiene los parámetros del intercambio de claves efímeras Diffie-Hellman.

> [!NOTE]
> Esta opción es ignorada por GnuTLS y Mozilla NSS.

`LDAP_OPT_X_TLS_KEYFILE` (`int`)  
Especifica la ruta de acceso completa del archivo de clave del certificado.

`LDAP_OPT_X_TLS_PROTOCOL_MIN` (`int`)  
Especifica la versión mínima del protocolo. Puede ser una de las siguientes: `LDAP_OPT_X_TLS_PROTOCOL_SSL2`, `LDAP_OPT_X_TLS_PROTOCOL_SSL3`, `LDAP_OPT_X_TLS_PROTOCOL_TLS1_0`, `LDAP_OPT_X_TLS_PROTOCOL_TLS1_1`, `LDAP_OPT_X_TLS_PROTOCOL_TLS1_2`, `LDAP_OPT_X_TLS_PROTOCOL_TLS1_3`

`LDAP_OPT_X_TLS_PROTOCOL_MAX` (`int`)  
Especifica la versión máxima del protocolo. Puede ser una de las siguientes: `LDAP_OPT_X_TLS_PROTOCOL_SSL2`, `LDAP_OPT_X_TLS_PROTOCOL_SSL3`, `LDAP_OPT_X_TLS_PROTOCOL_TLS1_0`, `LDAP_OPT_X_TLS_PROTOCOL_TLS1_1`, `LDAP_OPT_X_TLS_PROTOCOL_TLS1_2`, `LDAP_OPT_X_TLS_PROTOCOL_TLS1_3`. Disponible a partir de PHP 8.4.0.

`LDAP_OPT_X_TLS_RANDOM_FILE` (`int`)  
Define/obtiene el archivo aleatorio cuando uno de los valores por defecto del sistema no está disponible.

`LDAP_OPT_X_TLS_REQUIRE_CERT` (`int`)  
Especifica la estrategia de verificación de certificados. Debe ser una de las siguientes: `LDAP_OPT_X_TLS_NEVER`, `LDAP_OPT_X_TLS_HARD`, `LDAP_OPT_X_TLS_DEMAND`, `LDAP_OPT_X_TLS_ALLOW`, `LDAP_OPT_X_TLS_TRY`. (Disponible a partir de PHP 7.0.0)

`GSLC_SSL_NO_AUTH` (`int`)  
Modo de autenticación SSL - No se requiere autenticación. (solo para Oracle LDAP)

`GSLC_SSL_ONEWAY_AUTH` (`int`)  
Modo de autenticación SSL - Solo se requiere autenticación del servidor. (solo para Oracle LDAP)

`GSLC_SSL_TWOWAY_AUTH` (`int`)  
Modo de autenticación SSL - Se requiere autenticación del servidor y del cliente. (solo para Oracle LDAP)

`LDAP_EXOP_START_TLS` (`string`)  
Constantes de operaciones extendidas - Iniciar TLS ([RFC 4511](https://datatracker.ietf.org/doc/html/rfc4511)).

`LDAP_EXOP_MODIFY_PASSWD` (`string`)  
Constantes de operaciones extendidas - Modificar la contraseña ([RFC 3062](https://datatracker.ietf.org/doc/html/rfc3062)).

`LDAP_EXOP_REFRESH` (`string`)  
Constantes de operaciones extendidas - Actualizar ([RFC 2589](https://datatracker.ietf.org/doc/html/rfc2589)).

`LDAP_EXOP_WHO_AM_I` (`string`)  
Constantes de operaciones extendidas - WHOAMI ([RFC 4532](https://datatracker.ietf.org/doc/html/rfc4532)).

`LDAP_EXOP_TURN` (`string`)  
Constantes de operaciones extendidas - Girar ([RFC 4531](https://datatracker.ietf.org/doc/html/rfc4531)).

`LDAP_CONTROL_MANAGEDSAIT` (`string`)  
Constante de control - Gestionar DSA IT ([RFC 3296](https://datatracker.ietf.org/doc/html/rfc3296)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_PROXY_AUTHZ` (`string`)  
Constante de control - Autorización por Procuración ([RFC 4370](https://datatracker.ietf.org/doc/html/rfc4730)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_SUBENTRIES` (`string`)  
Constante de control - Subentrada ([RFC 3672](https://datatracker.ietf.org/doc/html/rfc3672)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_VALUESRETURNFILTER` (`string`)  
Constante de control - Filtro de valor devuelto ([RFC 3876](https://datatracker.ietf.org/doc/html/rfc3876)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_ASSERT` (`string`)  
Constante de control - Afirmación ([RFC 4528](https://datatracker.ietf.org/doc/html/rfc4528)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_PRE_READ` (`string`)  
Constante de control - Antes de leer ([RFC 4527](https://datatracker.ietf.org/doc/html/rfc4527)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_POST_READ` (`string`)  
Constante de control - Después de leer ([RFC 4527](https://datatracker.ietf.org/doc/html/rfc4527)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_SORTREQUEST` (`string`)  
Constante de control - Solicitud de ordenación ([RFC 2891](https://datatracker.ietf.org/doc/html/rfc2891)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_SORTRESPONSE` (`string`)  
Constante de control - Respuesta de ordenación ([RFC 2891](https://datatracker.ietf.org/doc/html/rfc2891)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_PAGEDRESULTS` (`string`)  
Constante de control - Resultados paginados ([RFC 2696](https://datatracker.ietf.org/doc/html/rfc2696)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_AUTHZID_REQUEST` (`string`)  
Constante de control - Solicitud de Autorización de Identidad ([RFC 3829](https://datatracker.ietf.org/doc/html/rfc3829)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_AUTHZID_RESPONSE` (`string`)  
Constante de control - Respuesta de Autorización de Identidad ([RFC 3829](https://datatracker.ietf.org/doc/html/rfc3829)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_SYNC` (`string`)  
Constante de control - Operación de sincronización de contenido ([RFC 4533](https://datatracker.ietf.org/doc/html/rfc4533)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_SYNC_STATE` (`string`)  
Constante de control - Estado de la operación de sincronización de contenido ([RFC 4533](https://datatracker.ietf.org/doc/html/rfc4533)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_SYNC_DONE` (`string`)  
Constante de control - Operación de sincronización de contenido completada ([RFC 4533](https://datatracker.ietf.org/doc/html/rfc4533)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_DONTUSECOPY` (`string`)  
Constante de control - No usar Copiar ([RFC 6171](https://datatracker.ietf.org/doc/html/rfc6171)). Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_PASSWORDPOLICYREQUEST` (`string`)  
Constante de control - Solicitud de la política de contraseña. Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_PASSWORDPOLICYRESPONSE` (`string`)  
Constante de control - Respuesta de la política de contraseña. Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_X_INCREMENTAL_VALUES` (`string`)  
Constante de control - Valores incrementales del directorio activo. Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_X_DOMAIN_SCOPE` (`string`)  
Constante de control - Alcance del dominio del directorio activo Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_X_PERMISSIVE_MODIFY` (`string`)  
Constante de control - Permiso de modificación del directorio activo. Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_X_SEARCH_OPTIONS` (`string`)  
Constante de control - Opción de búsqueda del directorio activo. Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_X_TREE_DELETE` (`string`)  
Constante de control - Eliminación del árbol del directorio activo. Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_X_EXTENDED_DN` (`string`)  
Constante de control - Directorio activo DN extendido. Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_VLVREQUEST` (`string`)  
Constante de control - Lista virtual de solicitud de vista. Disponible a partir de PHP 7.3.0.

`LDAP_CONTROL_VLVRESPONSE` (`string`)  
Constante de control - Lista virtual de respuesta de vista. Disponible a partir de PHP 7.3.0.

`LDAP_ESCAPE_DN` (`int`)  
Escapar una cadena de caracteres para su uso en un DN LDAP.

`LDAP_ESCAPE_FILTER` (`int`)  
Escapar una cadena de caracteres para su uso en un filtro LDAP.

`LDAP_MODIFY_BATCH_ATTRIB` (`string`)  
La clave del array de modificaciones que contiene los atributos: `attrib`.

`LDAP_MODIFY_BATCH_MODTYPE` (`string`)  
La clave del array de modificaciones que contiene el tipo de modificación: `modtype`.

`LDAP_MODIFY_BATCH_VALUES` (`string`)  
La clave del array de modificaciones que contiene los valores: `values`.

`LDAP_MODIFY_BATCH_ADD` (`int`)  
Añadir valores a un atributo de una entrada LDAP.

`LDAP_MODIFY_BATCH_REMOVE` (`int`)  
Eliminar valores de un atributo de una entrada LDAP.

`LDAP_MODIFY_BATCH_REMOVE_ALL` (`int`)  
Eliminar todas las valores de un atributo de una entrada LDAP.

`LDAP_MODIFY_BATCH_REPLACE` (`int`)  
Reemplazar todas las valores actuales de un atributo de una entrada LDAP por los valores especificados.

`LDAP_OPT_TIMEOUT` (`int`)  
Especifica un tiempo de espera (en segundos) después del cual las llamadas a las API LDAP sincrónicas serán abandonadas si no se recibe ninguna respuesta. También controla el tiempo de espera durante la comunicación con el KDC en caso de enlace SASL.

`LDAP_OPT_X_SASL_AUTHCID` (`int`)  
Devuelve la identidad de autenticación SASL.

`LDAP_OPT_X_SASL_AUTHZID` (`int`)  
Devuelve la identidad de autorización SASL.

`LDAP_OPT_X_SASL_MECH` (`int`)  
Devuelve el mecanismo SASL.

`LDAP_OPT_X_SASL_NOCANON` (`int`)  
Definir/obtener el flag `NOCANON`. Cuando no está definido, el nombre de host es canonizado.

`LDAP_OPT_X_SASL_REALM` (`int`)  
Devuelve el reino SASL.

`LDAP_OPT_X_SASL_USERNAME` (`int`)  
Devuelve el nombre de usuario SASL.

`LDAP_OPT_X_TLS_ALLOW` (`int`)  
Se solicita el certificado del par. Si no se proporciona ningún certificado, la sesión continúa normalmente. Si se proporciona un certificado incorrecto, será ignorado y la sesión continuará normalmente.

`LDAP_OPT_X_TLS_DEMAND` (`int`)  
Se solicita el certificado del par. Si no se proporciona ningún certificado, o si se proporciona un certificado incorrecto, la sesión se termina inmediatamente.

`LDAP_OPT_X_TLS_HARD` (`int`)  
Alias de `LDAP_OPT_X_TLS_DEMAND`.

`LDAP_OPT_X_TLS_NEVER` (`int`)  
No se solicita ni verifica el certificado del par.

`LDAP_OPT_X_TLS_TRY` (`int`)  
Se solicita el certificado del par. Si no se proporciona ningún certificado, la sesión continúa normalmente. Si se proporciona un certificado incorrecto, la sesión se termina inmediatamente.

`LDAP_OPT_X_TLS_CRL_ALL` (`int`)  
Verificar la lista de revocación de certificados (CRL) para toda la cadena de certificados.

`LDAP_OPT_X_TLS_CRL_NONE` (`int`)  
No se realiza ninguna verificación de CRL.

`LDAP_OPT_X_TLS_CRL_PEER` (`int`)  
Verificar la CRL del certificado del par.

`LDAP_OPT_X_TLS_PACKAGE` (`int`)  
Devuelve el nombre de la implementación TLS subyacente.

`LDAP_OPT_X_TLS_PROTOCOL_SSL2` (`int`)  
El protocolo SSL 2.0.

`LDAP_OPT_X_TLS_PROTOCOL_SSL3` (`int`)  
El protocolo SSL 3.0.

`LDAP_OPT_X_TLS_PROTOCOL_TLS1_0` (`int`)  
El protocolo TLS 1.0.

`LDAP_OPT_X_TLS_PROTOCOL_TLS1_1` (`int`)  
El protocolo TLS 1.1.

`LDAP_OPT_X_TLS_PROTOCOL_TLS1_2` (`int`)  
El protocolo TLS 1.2.

`LDAP_OPT_X_TLS_PROTOCOL_TLS1_3` (`int`)  
El protocolo TLS 1.3. Disponible a partir de PHP 8.4.0.
