---
title: Identificación HTTP con PHP
source_url: https://www.php.net/manual/es/features.http-auth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: features/http-auth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: features
translation_status: ready
translation_reviewed: true
translation_revision: cd4180557
order: 1580
---

## Identificación HTTP con PHP

Es posible utilizar la función `header` para solicitar una identificación (`"Authentication Required"`) al cliente, generando así la aparición de una ventana de solicitud de usuario y contraseña. Una vez que los campos han sido completados, la URL será llamada de nuevo, con las [variables predefinidas](#reserved.variables) `PHP_AUTH_USER`, `PHP_AUTH_PW` y `AUTH_TYPE` conteniendo respectivamente el nombre de usuario, la contraseña y el tipo de identificación. Estas variables predefinidas se encuentran en los arrays `$_SERVER`. *Solo* el método de identificación "Basic" es soportado. Consulte la función `header` para más información.

Aquí hay un ejemplo de script que fuerza la identificación del cliente para acceder a una página:

Ejemplo de identificación HTTP simple

```php
<?php
if (!isset($_SERVER['PHP_AUTH_USER'])) {
    header('HTTP/1.1 401 Unauthorized');
    header('WWW-Authenticate: Basic realm="My Realm"');
    echo 'Texto utilizado si el visitante usa el botón de cancelación';
    exit;
} else {
    echo "<p>Hola, {$_SERVER['PHP_AUTH_USER']}.</p>";
    echo "<p>Su contraseña es {$_SERVER['PHP_AUTH_PW']}.</p>";
}
?>

   
```

> [!NOTE]
> Sea muy cuidadoso al usar encabezados HTTP con PHP. Para garantizar la máxima compatibilidad entre los navegadores, la palabra clave "Basic" debe escribirse con una B mayúscula, y el texto de presentación debe colocarse entre comillas dobles (no simples), y exactamente un espacio debe preceder al código *401* en el encabezado *HTTP/1.1 401*. Los parámetros de autenticación deben estar separados por comas.

En lugar de mostrar simplemente las variables globales `PHP_AUTH_USER` y `PHP_AUTH_PW`, se preferirá verificar la validez del nombre de usuario y la contraseña. Por ejemplo, enviando esta información a una base de datos, o buscando en un fichero dbm.

> [!NOTE]
> PHP utiliza la presencia de la directiva `AuthType` para determinar si una identificación externa está activada.

Tenga en cuenta, sin embargo, que las manipulaciones anteriores no impiden que cualquier persona con una página no identificada robe las contraseñas de las páginas protegidas, en el mismo servidor.

> [!NOTE]
> La autenticación HTTP Basic es realmente básica, y no fue diseñada para soportar cierres de sesión. Dado que HTTP es un protocolo sin estado, la mayoría de los navegadores almacenarán en caché las credenciales proporcionadas tan pronto como se reciba un código de estado `2xx`, y las enviarán en cada solicitud, hasta que se cierre el navegador. No existe una forma definida para que un servidor solicite nuevas credenciales. A lo largo de los años, varias soluciones alternativas se han difundido como consejos en Internet, pero todas dependen de cómo los diferentes navegadores han elegido manejar casos límite no definidos (o incluso violaciones del estándar HTTP). Es mejor evitar tales soluciones alternativas y no utilizar la autenticación Basic para nada serio.

> [!NOTE]
> Para que la identificación HTTP funcione con un servidor IIS con la versión CGI de PHP, la directiva PHP [cgi.rfc2616_headers](#ini.cgi.rfc2616-headers) debe establecerse en `0` (el valor por defecto), y debe editar la configuración "`Directory Security`" de IIS. Haga clic en "`Edit`" y active solo "`Anonymous Access`", todos los demás campos deben dejarse inactivos.
