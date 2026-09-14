---
title: Constantes de errores cURL
source_url: https://www.php.net/manual/es/constant.curl-error.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/constants_curl_error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: fab7349d0
order: 9610
---

`CURLE_ABORTED_BY_CALLBACK` (`int`)  
Abandonado por la función de retrollamada. Una función de retrollamada ha devuelto "abort" a libcurl.

`CURLE_BAD_CALLING_ORDER` (`int`)  

`CURLE_BAD_CONTENT_ENCODING` (`int`)  
Codificación de contenido no reconocida.

`CURLE_BAD_DOWNLOAD_RESUME` (`int`)  
La descarga no pudo ser reanudada porque el desplazamiento especificado estaba fuera de los límites del fichero.

`CURLE_BAD_FUNCTION_ARGUMENT` (`int`)  
Una función fue llamada con un argumento incorrecto.

`CURLE_BAD_PASSWORD_ENTERED` (`int`)  

`CURLE_COULDNT_CONNECT` (`int`)  
Fallo en la conexión al host o al proxy.

`CURLE_COULDNT_RESOLVE_HOST` (`int`)  
Resolución del host imposible. El host remoto no pudo ser resuelto.

`CURLE_COULDNT_RESOLVE_PROXY` (`int`)  
Resolución del proxy imposible. El proxy dado no pudo ser resuelto.

`CURLE_FAILED_INIT` (`int`)  
El código de inicialización ha fallado. Probablemente se trate de un error interno o de un problema de recursos donde algo fundamental no pudo ser hecho al momento de la inicialización.

`CURLE_FILESIZE_EXCEEDED` (`int`)  
Se ha superado el tamaño máximo del fichero.

`CURLE_FILE_COULDNT_READ_FILE` (`int`)  
Un fichero dado con FILE:// no pudo ser abierto. Lo más probable es que la ruta del fichero no corresponda a un fichero existente o debido a la falta de permisos de fichero adecuados.

`CURLE_FTP_ACCESS_DENIED` (`int`)  

`CURLE_FTP_BAD_DOWNLOAD_RESUME` (`int`)  

`CURLE_FTP_CANT_GET_HOST` (`int`)  
Se ha producido un error interno al buscar el host utilizado para la nueva conexión.

`CURLE_FTP_CANT_RECONNECT` (`int`)  

`CURLE_FTP_COULDNT_GET_SIZE` (`int`)  

`CURLE_FTP_COULDNT_RETR_FILE` (`int`)  
Esto fue una respuesta inesperada a una orden 'RETR' o una transferencia de cero octetos completa.

`CURLE_FTP_COULDNT_SET_ASCII` (`int`)  

`CURLE_FTP_COULDNT_SET_BINARY` (`int`)  

`CURLE_FTP_COULDNT_STOR_FILE` (`int`)  

`CURLE_FTP_COULDNT_USE_REST` (`int`)  
La orden FTP REST ha devuelto un error. Esto no debería ocurrir nunca si el servidor está sano.

`CURLE_FTP_PARTIAL_FILE` (`int`)  

`CURLE_FTP_PORT_FAILED` (`int`)  
La orden FTP PORT ha devuelto un error. Esto ocurre principalmente cuando la dirección especificada para libcurl no es suficientemente buena. Ver `CURLOPT_FTPPORT`.

`CURLE_FTP_QUOTE_ERROR` (`int`)  

`CURLE_FTP_SSL_FAILED` (`int`)  

`CURLE_FTP_USER_PASSWORD_INCORRECT` (`int`)  

`CURLE_FTP_WEIRD_227_FORMAT` (`int`)  
Los servidores FTP devuelven una línea 227 en respuesta a una orden PASV. Si libcurl falla al analizar esta línea, este código de retorno es devuelto.

`CURLE_FTP_WEIRD_PASS_REPLY` (`int`)  
Después de enviar la contraseña FTP al servidor, libcurl espera una respuesta apropiada. Este código de error indica que se ha devuelto un código inesperado.

`CURLE_FTP_WEIRD_PASV_REPLY` (`int`)  
Libcurl no ha podido obtener un resultado sensato del servidor en respuesta a una orden PASV o EPSV. El servidor es defectuoso.

`CURLE_FTP_WEIRD_SERVER_REPLY` (`int`)  
El servidor ha devuelto datos que libcurl no ha podido analizar. Este código de error es conocido como `CURLE_WEIRD_SERVER_REPLY` a partir de cURL 7.51.0.

`CURLE_FTP_WEIRD_USER_REPLY` (`int`)  

`CURLE_FTP_WRITE_ERROR` (`int`)  

`CURLE_FUNCTION_NOT_FOUND` (`int`)  
La función no ha sido encontrada. Una función zlib requerida no ha sido encontrada.

`CURLE_GOT_NOTHING` (`int`)  
Nada ha sido devuelto por el servidor, y en las circunstancias, no recibir nada es considerado como un error.

`CURLE_HTTP_NOT_FOUND` (`int`)  

`CURLE_HTTP_PORT_FAILED` (`int`)  

`CURLE_HTTP_POST_ERROR` (`int`)  
Es un error extraño que ocurre principalmente debido a una confusión interna.

`CURLE_HTTP_RANGE_ERROR` (`int`)  

`CURLE_HTTP_RETURNED_ERROR` (`int`)  
Esto se devuelve si `CURLOPT_FAILONERROR` está definido a `true` y que el servidor HTTP devuelve un código de error superior o igual a 400.

`CURLE_LDAP_CANNOT_BIND` (`int`)  
LDAP no puede enlazarse. La operación de enlace LDAP ha fallado.

`CURLE_LDAP_INVALID_URL` (`int`)  

`CURLE_LDAP_SEARCH_FAILED` (`int`)  
La búsqueda LDAP ha fallado.

`CURLE_LIBRARY_NOT_FOUND` (`int`)  

`CURLE_MALFORMAT_USER` (`int`)  

`CURLE_OBSOLETE` (`int`)  

`CURLE_OK` (`int`)  
Todo está bien. Proceda como de costumbre.

`CURLE_OPERATION_TIMEDOUT` (`int`)  
Operación expirada. El período de tiempo especificado ha sido alcanzado según las condiciones.

`CURLE_OPERATION_TIMEOUTED` (`int`)  

`CURLE_OUT_OF_MEMORY` (`int`)  
Una solicitud de asignación de memoria ha fallado.

`CURLE_PARTIAL_FILE` (`int`)  
Una transferencia de fichero ha sido más corta o más larga de lo esperado. Esto ocurre cuando el servidor señala primero un tamaño de transferencia esperado, y luego proporciona datos que no coinciden con el tamaño dado anteriormente.

`CURLE_PROXY` (`int`)  
Error de conexión al proxy. `CURLINFO_PROXY_ERROR` proporciona detalles adicionales sobre el problema específico. Disponible a partir de PHP 8.2.0 y cURL 7.73.0

`CURLE_READ_ERROR` (`int`)  
Hubo un problema al leer un fichero local o un error devuelto por la función de retrollamada de lectura.

`CURLE_RECV_ERROR` (`int`)  
Fallo en la recepción de los datos de red.

`CURLE_SEND_ERROR` (`int`)  
Fallo en el envío de los datos de red.

`CURLE_SHARE_IN_USE` (`int`)  

`CURLE_SSH` (`int`)  
Se ha producido un error no especificado durante la sesión SSH. Disponible a partir de cURL 7.16.1.

`CURLE_SSL_CACERT` (`int`)  

`CURLE_SSL_CACERT_BADFILE` (`int`)  
Problema de lectura del certificado SSL CA.

`CURLE_SSL_CERTPROBLEM` (`int`)  
Problema con el cliente de certificado local.

`CURLE_SSL_CIPHER` (`int`)  
Imposible utilizar el cifrado especificado.

`CURLE_SSL_CONNECT_ERROR` (`int`)  
Se ha producido un problema en algún lugar de la gestión SSL/TLS. La lectura del mensaje en el búfer de error proporciona más detalles sobre el problema. Podría ser de certificados (formatos de ficheros, rutas, permisos), contraseñas y otros.

`CURLE_SSL_ENGINE_NOTFOUND` (`int`)  
El motor de cifrado especificado no ha sido encontrado.

`CURLE_SSL_ENGINE_SETFAILED` (`int`)  
Fallo en la definición del motor de cifrado seleccionado como motor por defecto.

`CURLE_SSL_PEER_CERTIFICATE` (`int`)  

`CURLE_SSL_PINNEDPUBKEYNOTMATCH` (`int`)  
Fallo en la coincidencia de la clave pública especificada con `CURLOPT_PINNEDPUBLICKEY`.

`CURLE_TELNET_OPTION_SYNTAX` (`int`)  

`CURLE_TOO_MANY_REDIRECTS` (`int`)  
Demasiadas redirecciones. Al seguir las redirecciones, libcurl ha alcanzado el número máximo. El límite puede ser definido con `CURLOPT_MAXREDIRS`.

`CURLE_UNKNOWN_TELNET_OPTION` (`int`)  

`CURLE_UNSUPPORTED_PROTOCOL` (`int`)  
La URL pasada a libcurl utilizó un protocolo que libcurl no soporta. El problema podría ser una opción de compilación que no ha sido utilizada, una cadena de protocolo mal escrita o simplemente un protocolo para el cual libcurl no tiene código.

`CURLE_URL_MALFORMAT` (`int`)  
La URL no estaba correctamente formateada.

`CURLE_URL_MALFORMAT_USER` (`int`)  

`CURLE_WEIRD_SERVER_REPLY` (`int`)  
El servidor ha devuelto datos que libcurl no ha podido analizar. Este código de error era conocido como `CURLE_FTP_WEIRD_SERVER_REPLY` antes de cURL 7.51.0. Disponible a partir de PHP 7.3.0 y cURL 7.51.0

`CURLE_WRITE_ERROR` (`int`)  
Se ha producido un error al escribir los datos recibidos en un fichero local, o un error ha sido devuelto a libcurl desde una función de retrollamada de escritura.
