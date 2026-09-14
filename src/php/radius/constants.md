---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/radius.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67520
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`RADIUS_MPPE_KEY_LEN` (`int`)  
La longitud máxima de las claves MPPE.

## Opciones RADIUS

Varias funciones RADIUS aceptan opciones en forma de máscara de octetos. Las constantes que representan estas opciones se enumeran a continuación.

`RADIUS_OPTION_SALT` (`int`)  
Cuando se define, esta opción hará que el valor del atributo sea cifrado salt.

`RADIUS_OPTION_TAGGED` (`int`)  
Cuando se define, esta opción hará que el valor del atributo provenga del argumento tag.

## Tipos de paquetes RADIUS

Los paquetes RADIUS, ya sean solicitados o recibidos como respuesta, siempre incluyen un tipo. Esta constante se proporciona para facilitar la especificación de un tipo al utilizar la función `radius_create_request`, y al comparar el resultado con la función `radius_send_request`.

`RADIUS_ACCESS_REQUEST` (`int`)  
Un Access-Request, utilizado para autenticar un usuario en un servidor RADIUS. Los paquetes Access-Request deben incluir un atributo [`RADIUS_NAS_IP_ADDRESS`](#constant.radius-nas-ip-address), o un atributo [`RADIUS_NAS_IDENTIFIER`](#constant.radius-nas-identifier) pero también incluir un atributo [`RADIUS_USER_PASSWORD`](#constant.radius-user-password), y un atributo [`RADIUS_CHAP_PASSWORD`](#constant.radius-chap-password) o bien un atributo [`RADIUS_STATE`](#constant.radius-state), y deben incluir un atributo [`RADIUS_USER_NAME`](#constant.radius-user-name).

`RADIUS_ACCESS_ACCEPT` (`int`)  
Una respuesta Access-Accept a un paquete Access-Request indica que el servidor RADIUS ha autenticado al usuario con éxito.

`RADIUS_ACCESS_REJECT` (`int`)  
Una respuesta Access-Reject a un paquete Access-Request indica que el servidor RADIUS no ha logrado autenticar al usuario.

`RADIUS_ACCESS_CHALLENGE` (`int`)  
Una respuesta Access-Challenge a un paquete Access-Request indica que el servidor RADIUS requiere más información de otro paquete Access-Request antes de autenticar al usuario.

`RADIUS_ACCOUNTING_REQUEST` (`int`)  
Un paquete Accounting-Request, utilizado para transmitir información de contabilidad para un servicio del servidor RADIUS.

`RADIUS_ACCOUNTING_RESPONSE` (`int`)  
Una respuesta Accounting-Response a un paquete Accounting-Request.

`RADIUS_COA_REQUEST` (`int`)  
Un paquete CoA-Request, enviado desde un servidor RADIUS para indicar que los permisos han cambiado en la sesión del usuario. Se debe emitir una respuesta en forma de CoA-ACK o CoA-NAK.

Esta constante está disponible desde PECL radius 1.3.0 y versiones posteriores.

`RADIUS_COA_ACK` (`int`)  
Un paquete CoA-ACK, enviado al servidor RADIUS para indicar que los permisos del usuario han sido actualizados.

Esta constante está disponible desde PECL radius 1.3.0 y versiones posteriores.

`RADIUS_COA_NAK` (`int`)  
Un paquete CoA-NAK, enviado al servidor RADIUS para indicar que los permisos del usuario no han podido ser actualizados.

Esta constante está disponible desde PECL radius 1.3.0 y versiones posteriores.

`RADIUS_DISCONNECT_REQUEST` (`int`)  
Un paquete Disconnect-Request, enviado desde el servidor RADIUS para indicar que la sesión del usuario debe cerrarse.

Esta constante está disponible desde PECL radius 1.3.0 y versiones posteriores.

`RADIUS_DISCONNECT_ACK` (`int`)  
Un paquete Disconnect-ACK, enviado al servidor RADIUS para indicar que la sesión del usuario ha finalizado.

Esta constante está disponible desde PECL radius 1.3.0 y versiones posteriores.

`RADIUS_DISCONNECT_NAK` (`int`)  
Un paquete Disconnect-NAK, enviado al servidor RADIUS para indicar que la sesión del usuario no ha podido finalizar.

Esta constante está disponible desde PECL radius 1.3.0 y versiones posteriores.

## Tipos de atributo RADIUS

Estas constantes definen tipos de atributo RADIUS que pueden ser utilizadas con las funciones `radius_put_addr`, `radius_put_attr`, `radius_put_int` y `radius_put_string`.

`RADIUS_USER_NAME` (`int`)  
El atributo User-Name. El valor del atributo debe ser un string que contenga el nombre de usuario que desea autenticarse, y puede ser definido utilizando la función `radius_put_attr`.

`RADIUS_USER_PASSWORD` (`int`)  
El atributo User-Password. El valor del atributo debe ser un string que contenga la contraseña del usuario, y puede ser definido utilizando la función `radius_put_attr`. Este valor será cifrado durante la transmisión como se describe en la [sección 5.2 de la RFC 2865](https://datatracker.ietf.org/doc/html/rfc2865).

`RADIUS_CHAP_PASSWORD` (`int`)  
El atributo Chap-Password. El valor del atributo debe ser un string que contenga el primer octeto (que es el identificador CHAP), seguido de una subsecuencia de 16 octetos que contenga el hash MD5 del identificador CHAP, la contraseña en texto plano, y el valor del desafío CHAP, todo concatenado. Tenga en cuenta que el valor del desafío CHAP también debe ser enviado por separado en el atributo [`RADIUS_CHAP_CHALLENGE`](#constant.radius-chap-challenge).

Uso de contraseñas CHAP

```php
<?php
// Primero, creamos un manejador de autenticación y una solicitud.
$radh = radius_auth_open();
radius_add_server($radh, $server, $port, $secret, 3, 3);
radius_create_request($radh, RADIUS_ACCESS_REQUEST);

// Supongamos que $password contiene la contraseña en texto plano:

// Generación del desafío.
$challenge = mt_rand();

// Especifica un identificador CHAP.
$ident = 1;

// Añade el atributo Chap-Password.
$cp = hash('md5', pack('Ca*', $ident, $password.$challenge), true);
radius_put_attr($radh, RADIUS_CHAP_PASSWORD, pack('C', $ident).$cp);

// Añade el atributo Chap-Challenge.
radius_put_attr($radh, RADIUS_CHAP_CHALLENGE, $challenge);

/* A partir de aquí, podemos añadir los otros atributos
 * y llamar a la función radius_send_request(). */
?>

      
```

`RADIUS_NAS_IP_ADDRESS` (`int`)  
El atributo NAS-IP-Address. El valor del atributo esperado es la dirección IP del cliente RADIUS codificada como un entero, que puede ser definida utilizando la función `radius_put_addr`.

`RADIUS_NAS_PORT` (`int`)  
El atributo NAS-Port. El valor del atributo esperado es el puerto físico del usuario en el cliente RADIUS, codificado como un entero, que puede ser definido utilizando la función `radius_put_int`.

`RADIUS_SERVICE_TYPE` (`int`)  
El atributo Service-Type. El valor del atributo indica el tipo de servicio que el usuario solicita, y debe ser un entero, que puede ser definido utilizando la función `radius_put_int`.

Se proporcionan constantes para representar los valores posibles de este atributo. Aquí están: `RADIUS_LOGIN`, `RADIUS_FRAMED`, `RADIUS_CALLBACK_LOGIN`, `RADIUS_CALLBACK_FRAMED`, `RADIUS_OUTBOUND`, `RADIUS_ADMINISTRATIVE`, `RADIUS_NAS_PROMPT`, `RADIUS_AUTHENTICATE_ONLY`, `RADIUS_CALLBACK_NAS_PROMPT`

`RADIUS_FRAMED_PROTOCOL` (`int`)  
El atributo Framed-Protocol. El valor del atributo esperado es un entero, que indica el framing a utilizar para el acceso, y puede ser definido utilizando la función `radius_put_int`. Los valores posibles para este atributo son: `RADIUS_PPP`, `RADIUS_SLIP`, `RADIUS_ARAP`, `RADIUS_GANDALF`, `RADIUS_XYLOGICS`

`RADIUS_FRAMED_IP_ADDRESS` (`int`)  
El atributo Framed-IP-Address. El valor esperado es una dirección de la red del usuario codificada como un entero, que puede ser definida utilizando la función `radius_put_addr` y recuperada utilizando la función `radius_cvt_addr`.

`RADIUS_FRAMED_IP_NETMASK` (`int`)  
El atributo Framed-IP-Netmask. El valor esperado es una máscara de red del usuario, codificada como un entero, que puede ser definida utilizando la función `radius_put_addr` y recuperada utilizando la función `radius_cvt_addr`.

`RADIUS_FRAMED_ROUTING` (`int`)  
El atributo Framed-Routing. El valor esperado es un entero que indica el método de enrutamiento para el usuario, que puede ser definido utilizando la función `radius_put_int`.

Valores posibles: `0`: Sin enrutamiento, `1`: Enviar paquetes de enrutamiento, `2`: Escuchar paquetes de enrutamiento, `3`: Enviar y escuchar

`RADIUS_FILTER_ID` (`int`)  
El atributo Filter-ID. El valor esperado es una implementación específica, legible por humanos, de strings de filtros, que pueden ser definidas utilizando la función `radius_put_attr`.

`RADIUS_FRAMED_MTU` (`int`)  
El atributo Framed-MTU. El valor esperado es un entero, que indica el MTU a configurar para el usuario, y puede ser definido utilizando la función `radius_put_int`.

`RADIUS_FRAMED_COMPRESSION` (`int`)  
El atributo Framed-Compression. El valor esperado es un entero, que indica el protocolo de compresión a utilizar, y puede ser definido utilizando la función `radius_put_int`. Valores posibles: `RADIUS_COMP_NONE`: Sin compresión, `RADIUS_COMP_VJ`: Compresión de cabecera VJ TCP/IP, `RADIUS_COMP_IPXHDR`: Compresión de cabecera IPX, `RADIUS_COMP_STAC_LZS`: Compresión Stac-LZS (añadido en PECL radius 1.3.0b2)

`RADIUS_LOGIN_IP_HOST` (`int`)  
El atributo Login-IP-Host. El valor esperado es la dirección IP de conexión del usuario, codificada como un entero, que puede ser definido utilizando la función `radius_put_addr`.

`RADIUS_LOGIN_SERVICE` (`int`)  
El atributo Login-Service. El valor esperado es un entero que indica el servicio al que el usuario se conecta en el host de identificación. El valor puede ser convertido a un entero PHP mediante la función `radius_cvt_int`.

`RADIUS_LOGIN_TCP_PORT` (`int`)  
El atributo Login-TCP-Port. El valor esperado es un entero que indica el puerto al que el usuario se conecta en el host de identificación. El valor puede ser convertido a un entero PHP mediante la función `radius_cvt_int`.

`RADIUS_REPLY_MESSAGE` (`int`)  
El atributo Reply-Message. El valor esperado es un string que contiene un texto que puede ser mostrado al usuario en respuesta a una solicitud de acceso.

`RADIUS_CALLBACK_NUMBER` (`int`)  
El atributo Callback-Number. El valor esperado es un string que contiene la cadena de marcación a utilizar para la función de devolución de llamada.

`RADIUS_CALLBACK_ID` (`int`)  
El atributo Callback-Id. El valor esperado es un string que contiene el nombre de la implementación específica del lugar a llamar.

`RADIUS_FRAMED_ROUTE` (`int`)  
El atributo Framed-Route. El valor esperado es un string que contiene un conjunto de rutas de implementación específica a configurar para el usuario.

`RADIUS_FRAMED_IPX_NETWORK` (`int`)  
El atributo Framed-IPX-Network. El valor esperado es un entero que contiene la red IPX a configurar para el usuario, o `0xFFFFFFFE` para indicar que el cliente RADIUS debe seleccionar la red, y puede ser accedido mediante la función `radius_cvt_int`.

`RADIUS_STATE` (`int`)  
El atributo State. El valor esperado es un string que contiene la implementación definida incluida en un Access-Challenge desde un servidor que debe ser incluida en la subsiguiente Access-Request, y puede ser definido utilizando la función `radius_put_attr`.

`RADIUS_CLASS` (`int`)  
El atributo Class. El valor esperado es un string arbitrario que incluye el mensaje de un Access-Accept que debe ser enviado al servidor de cuentas en los mensajes Accounting-Request, y puede ser definido mediante la función `radius_put_attr`.

`RADIUS_VENDOR_SPECIFIC` (`int`)  
El atributo Vendor-Specific. En general, los valores del atributo del vendedor deben ser definidos utilizando las funciones `radius_put_vendor_addr`, `radius_put_vendor_attr`, `radius_put_vendor_int` y `radius_put_vendor_string`, en lugar de hacerlo directamente.

Esta constante es útil al interpretar los atributos específicos del vendedor en las respuestas de un servidor RADIUS; cuando se recibe un atributo específico del vendedor, la función `radius_get_vendor_attr` debe ser utilizada para acceder al identificador del vendedor, el tipo de atributo y el valor del atributo.

`RADIUS_SESSION_TIMEOUT` (`int`)  
Tiempo de espera de la sesión

`RADIUS_IDLE_TIMEOUT` (`int`)  
Tiempo de expiración

`RADIUS_TERMINATION_ACTION` (`int`)  
Acción de terminación

`RADIUS_CALLED_STATION_ID` (`int`)  
Identificador de la estación llamada

`RADIUS_CALLING_STATION_ID` (`int`)  
Identificador de la estación llamante

`RADIUS_NAS_IDENTIFIER` (`int`)  
Identificador NAS

`RADIUS_PROXY_STATE` (`int`)  
Estado del Proxy

`RADIUS_LOGIN_LAT_SERVICE` (`int`)  
Servicio de identificación LAT

`RADIUS_LOGIN_LAT_NODE` (`int`)  
Nodo de identificación LAT

`RADIUS_LOGIN_LAT_GROUP` (`int`)  
Grupo de identificación LAT

`RADIUS_FRAMED_APPLETALK_LINK` (`int`)  
Enlace framé Appletalk

`RADIUS_FRAMED_APPLETALK_NETWORK` (`int`)  
Red framé Appletalk

`RADIUS_FRAMED_APPLETALK_ZONE` (`int`)  
Zona framé Appletalk

`RADIUS_CHAP_CHALLENGE` (`int`)  
Desafío

`RADIUS_NAS_PORT_TYPE` (`int`)  
Tipo de puerto NAS: `RADIUS_ASYNC`, `RADIUS_SYNC`, `RADIUS_ISDN_SYNC`, `RADIUS_ISDN_ASYNC_V120`, `RADIUS_ISDN_ASYNC_V110`, `RADIUS_VIRTUAL`, `RADIUS_PIAFS`, `RADIUS_HDLC_CLEAR_CHANNEL`, `RADIUS_X_25`, `RADIUS_X_75`, `RADIUS_G_3_FAX`, `RADIUS_SDSL`, `RADIUS_ADSL_CAP`, `RADIUS_ADSL_DMT`, `RADIUS_IDSL`, `RADIUS_ETHERNET`, `RADIUS_XDSL`, `RADIUS_CABLE`, `RADIUS_WIRELESS_OTHER`, `RADIUS_WIRELESS_IEEE_802_11`

`RADIUS_PORT_LIMIT` (`int`)  
Límite del puerto

`RADIUS_LOGIN_LAT_PORT` (`int`)  
Puerto de identificación LAT

`RADIUS_CONNECT_INFO` (`int`)  
Información de conexión

`RADIUS_ACCT_STATUS_TYPE` (`int`)  
Tipo de estado de la cuenta: `RADIUS_START`, `RADIUS_STOP`, `RADIUS_ACCOUNTING_ON`, `RADIUS_ACCOUNTING_OFF`

`RADIUS_ACCT_DELAY_TIME` (`int`)  
Tiempo de espera máximo de identificación

`RADIUS_ACCT_INPUT_OCTETS` (`int`)  
Octetos de entrada de identificación

`RADIUS_ACCT_OUTPUT_OCTETS` (`int`)  
Octetos de salida de identificación

`RADIUS_ACCT_SESSION_ID` (`int`)  
Identificador de sesión de identificación

`RADIUS_ACCT_AUTHENTIC` (`int`)  
Identificación auténtica, uno entre: `RADIUS_AUTH_RADIUS`, `RADIUS_AUTH_LOCAL`, `RADIUS_AUTH_REMOTE`

`RADIUS_ACCT_SESSION_TIME` (`int`)  
Duración de la sesión de identificación

`RADIUS_ACCT_INPUT_PACKETS` (`int`)  
Paquetes de entrada de identificación

`RADIUS_ACCT_OUTPUT_PACKETS` (`int`)  
Paquetes de salida de identificación

`RADIUS_ACCT_TERMINATE_CAUSE` (`int`)  
Causa de la finalización de la identificación, uno entre: `RADIUS_TERM_USER_REQUEST`, `RADIUS_TERM_LOST_CARRIER`, `RADIUS_TERM_LOST_SERVICE`, `RADIUS_TERM_IDLE_TIMEOUT`, `RADIUS_TERM_SESSION_TIMEOUT`, `RADIUS_TERM_ADMIN_RESET`, `RADIUS_TERM_ADMIN_REBOOT`, `RADIUS_TERM_PORT_ERROR`, `RADIUS_TERM_NAS_ERROR`, `RADIUS_TERM_NAS_REQUEST`, `RADIUS_TERM_NAS_REBOOT`, `RADIUS_TERM_PORT_UNNEEDED`, `RADIUS_TERM_PORT_PREEMPTED`, `RADIUS_TERM_PORT_SUSPENDED`, `RADIUS_TERM_SERVICE_UNAVAILABLE`, `RADIUS_TERM_CALLBACK`, `RADIUS_TERM_USER_ERROR`, `RADIUS_TERM_HOST_REQUEST`

`RADIUS_ACCT_MULTI_SESSION_ID` (`int`)  
Identificador de una sesión múltiple de identificación

`RADIUS_ACCT_LINK_COUNT` (`int`)  
Número de enlaces de identificación

<!-- -->

`RADIUS_LOGIN`  

`RADIUS_FRAMED`  

`RADIUS_CALLBACK_LOGIN`  

`RADIUS_CALLBACK_FRAMED`  

`RADIUS_OUTBOUND`  

`RADIUS_ADMINISTRATIVE`  

`RADIUS_NAS_PROMPT`  

`RADIUS_AUTHENTICATE_ONLY`  

`RADIUS_CALLBACK_NAS_PROMPT`  

<!-- -->

`RADIUS_PPP`  

`RADIUS_SLIP`  

`RADIUS_ARAP`  

`RADIUS_GANDALF`  

`RADIUS_XYLOGICS`  

<!-- -->

`RADIUS_COMP_NONE`  

`RADIUS_COMP_VJ`  

`RADIUS_COMP_IPXHDR`  

`RADIUS_COMP_STAC_LZS`  

<!-- -->

`RADIUS_ASYNC`  

`RADIUS_SYNC`  

`RADIUS_ISDN_SYNC`  

`RADIUS_ISDN_ASYNC_V120`  

`RADIUS_ISDN_ASYNC_V110`  

`RADIUS_VIRTUAL`  

`RADIUS_PIAFS`  

`RADIUS_HDLC_CLEAR_CHANNEL`  

`RADIUS_X_25`  

`RADIUS_X_75`  

`RADIUS_G_3_FAX`  

`RADIUS_SDSL`  

`RADIUS_ADSL_CAP`  

`RADIUS_ADSL_DMT`  

`RADIUS_IDSL`  

`RADIUS_ETHERNET`  

`RADIUS_XDSL`  

`RADIUS_CABLE`  

`RADIUS_WIRELESS_OTHER`  

`RADIUS_WIRELESS_IEEE_802_11`  

<!-- -->

`RADIUS_START`  

`RADIUS_STOP`  

`RADIUS_ACCOUNTING_ON`  

`RADIUS_ACCOUNTING_OFF`  

<!-- -->

`RADIUS_AUTH_RADIUS`  

`RADIUS_AUTH_LOCAL`  

`RADIUS_AUTH_REMOTE`  

<!-- -->

`RADIUS_TERM_USER_REQUEST`  

`RADIUS_TERM_LOST_CARRIER`  

`RADIUS_TERM_LOST_SERVICE`  

`RADIUS_TERM_IDLE_TIMEOUT`  

`RADIUS_TERM_SESSION_TIMEOUT`  

`RADIUS_TERM_ADMIN_RESET`  

`RADIUS_TERM_ADMIN_REBOOT`  

`RADIUS_TERM_PORT_ERROR`  

`RADIUS_TERM_NAS_ERROR`  

`RADIUS_TERM_NAS_REQUEST`  

`RADIUS_TERM_NAS_REBOOT`  

`RADIUS_TERM_PORT_UNNEEDED`  

`RADIUS_TERM_PORT_PREEMPTED`  

`RADIUS_TERM_PORT_SUSPENDED`  

`RADIUS_TERM_SERVICE_UNAVAILABLE`  

`RADIUS_TERM_CALLBACK`  

`RADIUS_TERM_USER_ERROR`  

`RADIUS_TERM_HOST_REQUEST`  

`RADIUS_MICROSOFT_MS_CHAP_RESPONSE`  

`RADIUS_MICROSOFT_MS_CHAP_ERROR`  

`RADIUS_MICROSOFT_MS_CHAP_PW_1`  

`RADIUS_MICROSOFT_MS_CHAP_PW_2`  

`RADIUS_MICROSOFT_MS_CHAP_LM_ENC_PW`  

`RADIUS_MICROSOFT_MS_CHAP_NT_ENC_PW`  

`RADIUS_MICROSOFT_MS_MPPE_ENCRYPTION_POLICY`  

`RADIUS_MICROSOFT_MS_MPPE_ENCRYPTION_TYPES`  

`RADIUS_MICROSOFT_MS_RAS_VENDOR`  

`RADIUS_MICROSOFT_MS_CHAP_DOMAIN`  

`RADIUS_MICROSOFT_MS_CHAP_CHALLENGE`  

`RADIUS_MICROSOFT_MS_CHAP_MPPE_KEYS`  

`RADIUS_MICROSOFT_MS_BAP_USAGE`  

`RADIUS_MICROSOFT_MS_LINK_UTILIZATION_THRESHOLD`  

`RADIUS_MICROSOFT_MS_LINK_DROP_TIME_LIMIT`  

`RADIUS_MICROSOFT_MS_MPPE_SEND_KEY`  

`RADIUS_MICROSOFT_MS_MPPE_RECV_KEY`  

`RADIUS_MICROSOFT_MS_RAS_VERSION`  

`RADIUS_MICROSOFT_MS_OLD_ARAP_PASSWORD`  

`RADIUS_MICROSOFT_MS_NEW_ARAP_PASSWORD`  

`RADIUS_MICROSOFT_MS_ARAP_PASSWORD_CHANGE_REASON`  

`RADIUS_MICROSOFT_MS_FILTER`  

`RADIUS_MICROSOFT_MS_ACCT_AUTH_TYPE`  

`RADIUS_MICROSOFT_MS_ACCT_EAP_TYPE`  

`RADIUS_MICROSOFT_MS_CHAP2_RESPONSE`  

`RADIUS_MICROSOFT_MS_CHAP2_SUCCESS`  

`RADIUS_MICROSOFT_MS_CHAP2_PW`  

`RADIUS_MICROSOFT_MS_PRIMARY_DNS_SERVER`  

`RADIUS_MICROSOFT_MS_SECONDARY_DNS_SERVER`  

`RADIUS_MICROSOFT_MS_PRIMARY_NBNS_SERVER`  

`RADIUS_MICROSOFT_MS_SECONDARY_NBNS_SERVER`  

`RADIUS_MICROSOFT_MS_ARAP_CHALLENGE`  

## Tipos de atributo RADIUS específicos del vendedor

`RADIUS_VENDOR_MICROSOFT` (`int`)  
Atributos específicos de Microsoft ([RFC 2548](https://datatracker.ietf.org/doc/html/rfc2548)): `RADIUS_MICROSOFT_MS_CHAP_RESPONSE`, `RADIUS_MICROSOFT_MS_CHAP_ERROR`, `RADIUS_MICROSOFT_MS_CHAP_PW_1`, `RADIUS_MICROSOFT_MS_CHAP_PW_2`, `RADIUS_MICROSOFT_MS_CHAP_LM_ENC_PW`, `RADIUS_MICROSOFT_MS_CHAP_NT_ENC_PW`, `RADIUS_MICROSOFT_MS_MPPE_ENCRYPTION_POLICY`, `RADIUS_MICROSOFT_MS_MPPE_ENCRYPTION_TYPES`, `RADIUS_MICROSOFT_MS_RAS_VENDOR`, `RADIUS_MICROSOFT_MS_CHAP_DOMAIN`, `RADIUS_MICROSOFT_MS_CHAP_CHALLENGE`, `RADIUS_MICROSOFT_MS_CHAP_MPPE_KEYS`, `RADIUS_MICROSOFT_MS_BAP_USAGE`, `RADIUS_MICROSOFT_MS_LINK_UTILIZATION_THRESHOLD`, `RADIUS_MICROSOFT_MS_LINK_DROP_TIME_LIMIT`, `RADIUS_MICROSOFT_MS_MPPE_SEND_KEY`, `RADIUS_MICROSOFT_MS_MPPE_RECV_KEY`, `RADIUS_MICROSOFT_MS_RAS_VERSION`, `RADIUS_MICROSOFT_MS_OLD_ARAP_PASSWORD`, `RADIUS_MICROSOFT_MS_NEW_ARAP_PASSWORD`, `RADIUS_MICROSOFT_MS_ARAP_PASSWORD_CHANGE_REASON`, `RADIUS_MICROSOFT_MS_FILTER`, `RADIUS_MICROSOFT_MS_ACCT_AUTH_TYPE`, `RADIUS_MICROSOFT_MS_ACCT_EAP_TYPE`, `RADIUS_MICROSOFT_MS_CHAP2_RESPONSE`, `RADIUS_MICROSOFT_MS_CHAP2_SUCCESS`, `RADIUS_MICROSOFT_MS_CHAP2_PW`, `RADIUS_MICROSOFT_MS_PRIMARY_DNS_SERVER`, `RADIUS_MICROSOFT_MS_SECONDARY_DNS_SERVER`, `RADIUS_MICROSOFT_MS_PRIMARY_NBNS_SERVER`, `RADIUS_MICROSOFT_MS_SECONDARY_NBNS_SERVER`, `RADIUS_MICROSOFT_MS_ARAP_CHALLENGE`
