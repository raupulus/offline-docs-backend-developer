---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/oauth.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: true
translation_revision: bdee7e8c1
order: 56610
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

La mayoría de estas constantes implican problemas descritos en la documentación oficial de [informe de problemas](http://wiki.oauth.net/ProblemReporting) de OAuth. Tenga en cuenta, sin embargo, que los nombres de las constantes son específicos de PHP, a pesar del hecho de que el esquema de nomenclatura es similar.

`OAUTH_SIG_METHOD_RSASHA1` (`string`)  
Método de firma OAuth *RSA-SHA1*.

`OAUTH_SIG_METHOD_HMACSHA1` (`string`)  
Método de firma OAuth *HMAC-SHA1*.

`OAUTH_SIG_METHOD_HMACSHA256` (`string`)  
Método de firma OAuth *HMAC-SHA256*.

`OAUTH_AUTH_TYPE_AUTHORIZATION` (`string`)  
Esta constante representa el encabezado `Authorization`.

`OAUTH_AUTH_TYPE_NONE` (`string`)  
Esta constante indica una petición `NoAuth OAuth`.

`OAUTH_AUTH_TYPE_URI` (`string`)  
Esta constante representa los parámetros OAuth en el URI de la petición.

`OAUTH_AUTH_TYPE_FORM` (`string`)  
Esta constante representa los parámetros OAuth como parte del cuerpo HTTP POST.

`OAUTH_HTTP_METHOD_GET` (`string`)  
Utiliza el método *GET* para la petición OAuth.

`OAUTH_HTTP_METHOD_POST` (`string`)  
Utiliza el método *POST* para la petición OAuth.

`OAUTH_HTTP_METHOD_PUT` (`string`)  
Utiliza el método *PUT* para la petición OAuth.

`OAUTH_HTTP_METHOD_HEAD` (`string`)  
Utiliza el método *HEAD* para la petición OAuth.

`OAUTH_HTTP_METHOD_DELETE` (`string`)  
Utiliza el método *DELETE* para la petición OAuth.

`OAUTH_REQENGINE_STREAMS` (`int`)  
Utilizado por el método Oauth::setRequestEngine para definir el motor de [flujos PHP](#book.stream), en oposición a `OAUTH_REQENGINE_CURL` para [Curl](#book.curl).

`OAUTH_REQENGINE_CURL` (`int`)  
Utilizado por el método Oauth::setReqeustEngine para definir el motor de [Curl](#book.curl), en oposición a `OAUTH_REQENGINE_STREAMS` para los [flujos PHP](#book.stream).

`OAUTH_OK` (`int`)  
La vida es bella.

`OAUTH_BAD_NONCE` (`int`)  
El valor *oauth_nonce* ha sido utilizado para una petición previa, y no puede ser utilizado ahora.

`OAUTH_BAD_TIMESTAMP` (`int`)  
El valor *oauth_timestamp* no es aceptado por el proveedor de servicio. En este caso, la respuesta deberá también contener el parámetro *oauth_acceptable_timestamps*.

`OAUTH_CONSUMER_KEY_UNKNOWN` (`int`)  
*oauth_consumer_key* es temporalmente inaceptable por el proveedor de servicio. Por ejemplo, el proveedor de servicio sobrecarga al consumidor.

`OAUTH_CONSUMER_KEY_REFUSED` (`int`)  
La clave del consumidor ha sido rechazada.

`OAUTH_INVALID_SIGNATURE` (`int`)  
*oauth_signature* es inválida porque no coincide con la firma calculada por el proveedor de servicio.

`OAUTH_TOKEN_USED` (`int`)  
*oauth_token* ha sido consumido. Ya no puede ser utilizado porque ha sido utilizado en una o más peticiones previas.

`OAUTH_TOKEN_EXPIRED` (`int`)  
*oauth_token* ha expirado.

`OAUTH_TOKEN_REVOKED` (`int`)  
*oauth_token* ha sido revocado y no será aceptado.

`OAUTH_TOKEN_REJECTED` (`int`)  
*oauth_token* no ha sido aceptado por el proveedor de servicio. La razón es desconocida, pero podría ser que el token nunca haya sido utilizado, ya haya sido consumido, haya expirado y/o haya sido olvidado por el proveedor de servicio.

`OAUTH_VERIFIER_INVALID` (`int`)  
*oauth_verifier* es incorrecto.

`OAUTH_PARAMETER_ABSENT` (`int`)  
Un parámetro requerido no ha sido recibido. En este caso, la respuesta deberá también contener el parámetro *oauth_parameters_absent*.

`OAUTH_SIGNATURE_METHOD_REJECTED` (`int`)  
*oauth_signature_method* no ha sido aceptado por el proveedor de servicio.
