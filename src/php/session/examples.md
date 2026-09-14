---
title: Ejemplos
source_url: https://www.php.net/manual/es/session.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 4de6272a1
order: 73700
---

## Ejemplos

## Uso básico

Las sesiones son una forma sencilla de almacenar datos individuales para cada usuario mediante un identificador de sesión único. Pueden utilizarse para persistir información entre varias páginas. Los identificadores de sesión se envían normalmente al navegador a través de cookies de sesión, y el identificador se utiliza para recuperar los datos existentes de la sesión. La ausencia de un identificador o de una cookie de sesión indica a PHP que debe crear una nueva sesión, generando así un nuevo identificador de sesión.

Las sesiones siguen una cinemática simple. Cuando se inicia una sesión, PHP recuperará una sesión existente utilizando el identificador de sesión pasado (habitualmente desde una cookie de sesión) o, si no se pasa ningún identificador de sesión, creará una nueva sesión. PHP poblará entonces la variable superglobal `$_SESSION` con todos los datos de la sesión una vez iniciada. Cuando PHP finaliza, tomará automáticamente el contenido de la variable superglobal `$_SESSION`, lo serializará y lo enviará para su almacenamiento al gestor de guardado de sesión.

Por omisión, PHP utiliza internamente el gestor de guardado `files` que está definido mediante la directiva [session.save_handler](#ini.session.save-handler). Los datos de sesión se guardarán en el servidor en el lugar especificado por la directiva de configuración [session.save_path](#ini.session.save-path).

Las sesiones pueden iniciarse manualmente utilizando la función `session_start`. Si la directiva de configuración [session.auto_start](#ini.session.auto-start) está definida como `1`, una sesión se iniciará automáticamente al comienzo de la solicitud.

Las sesiones se detienen automáticamente cuando PHP ha terminado de ejecutar un script, pero pueden detenerse manualmente utilizando la función `session_write_close`.

Almacenar una variable con `$_SESSION`.

```php
     
<?php
session_start();
if (!isset($_SESSION['count'])) {
  $_SESSION['count'] = 0;
} else {
  $_SESSION['count']++;
}
?>

    
```

Eliminar una variable de sesión con la superglobal `$_SESSION`.

```php
     
<?php
session_start();
unset($_SESSION['count']);
?>

    
```

> [!CAUTION]
> No utilice la función `unset` con `$_SESSION` de la forma `unset($_SESSION)` ya que esto hará imposible el almacenamiento de datos en la sesión utilizando la superglobal `$_SESSION`.

> [!WARNING]
> No se pueden utilizar referencias en variables de sesión ya que no hay ninguna manera factible de restaurar una referencia a otra variable.

> [!NOTE]
> Las sesiones basadas en ficheros (por omisión en PHP) bloquean el fichero de sesión cuando una sesión se abre mediante la función `session_start` o implícitamente mediante la directiva de configuración [session.auto_start](#ini.session.auto-start). Una vez bloqueado, ningún otro script puede acceder al mismo fichero de sesión hasta que la sesión no haya sido cerrada por el script que la abrió, o hasta que la función `session_write_close` no haya sido llamada.
>
> Esto puede ser problemático para los sitios web que utilizan AJAX y producen múltiples solicitudes concurrentes. La forma más sencilla de evitar este problema es llamar a la función `session_write_close` una vez que se hayan realizado los cambios en la sesión, preferiblemente al principio del script. También se puede utilizar otro gestor de sesión que soporte concurrencia.

## Pasar el identificador de sesión (session ID)

Existen dos métodos de propagación del identificador de sesión:

- Cookies

- Por URL

El módulo de sesión soporta ambos métodos. Las cookies son óptimas, pero como no son seguras (no todos los internautas las aceptan), no son fiables. El segundo método coloca el identificador de sesión directamente en las URL.

PHP es capaz de hacerlo de manera transparente. Si la opción de compilación `session.use_trans_sid` está activada, las URL relativas se modificarán para contener el identificador de sesión automáticamente.

> [!NOTE]
> La opción [arg_separator.output](#ini.arg-separator.output) de `php.ini` permite personalizar el separador de argumentos. Para estar completamente de acuerdo con las especificaciones XHTML, especifique \&amp; aquí.

Alternativamente, se puede utilizar la constante `SID` que está definida si la sesión ha comenzado. Si el cliente no envía una cookie de sesión apropiada, tendrá la forma `session_name=session_id`. De lo contrario, valdrá una cadena vacía. Así, en todos los casos se puede incluir en la URL.

El siguiente ejemplo muestra cómo almacenar una variable y cómo realizar un enlace correcto a otra página, con `SID`.

Contar el número de visitas de un usuario a una página

```php
     
<?php

session_start();

if (empty($_SESSION['count'])) {
   $_SESSION['count'] = 1;
} else {
   $_SESSION['count']++;
}
?>

<p>
 Hola visitante, ha visto esta página <?php echo $_SESSION['count']; ?> veces.
</p>

<p>
 Para continuar, <a href="nextpage.php?<?php echo htmlspecialchars(SID); ?>">haga clic aquí</a>.
</p>

    
```

La función `htmlspecialchars` se utiliza al mostrar el `SID` con el fin de contrarrestar los ataques XSS.

La visualización del `SID`, como se muestra en el ejemplo anterior, no es necesaria si [ --enable-trans-sid](#ini.session.use-trans-sid) se ha utilizado para compilar PHP.

> [!NOTE]
> Las URL no relativas se consideran externas al sitio y no recibirán el `SID`, ya que la fuga del `SID` a un servidor diferente presenta un riesgo de seguridad importante.

## Gestión personalizada de sesiones

Para implementar un almacenamiento en base de datos, u otro método, se necesitará la función `session_set_save_handler` para configurar las propias funciones de almacenamiento. Un gestor de sesión puede crearse utilizando la interfaz `SessionHandlerInterface` o extendiendo los gestores internos de PHP heredando de la clase `SessionHandler`.

Las funciones de retrollamada especificadas en `session_set_save_handler` son métodos llamados por PHP durante el ciclo de vida de la sesión: `open`, `read`, `write` y `close` así como las funciones de mantenimiento `destroy` para eliminar una sesión y `gc` para una recolección periódica de patrones.

Así, PHP siempre necesita un gestor de sesiones. Por omisión se trata del gestor interno 'files'. Un gestor personalizado puede indicarse mediante `session_set_save_handler`. Otros gestores alternativos pueden ser propuestos por extensiones PHP, como `sqlite`, `memcache` y `memcached` y pueden utilizarse mediante [session.save_handler](#ini.session.save-handler).

Cuando la sesión comienza, PHP llamará internamente a la función `open` del gestor, seguida de `read` que debe entonces devolver una cadena codificada exactamente como fue pasada durante el almacenamiento. Una vez que la función de retrollamada de `read` haya devuelto su cadena, PHP la decodificará y poblará la superglobal `$_SESSION` en consecuencia.

Cuando PHP finaliza (o cuando `session_write_close` es llamada), codificará internamente el contenido de `$_SESSION` y lo pasará con el ID de sesión a la función `write`. Después de `write`, PHP invocará `close`.

Cuando una sesión es destruida, PHP llamará a `destroy` con el ID de sesión.

PHP llamará a la función de retrollamada `gc` de vez en cuando para limpiar las sesiones expiradas según su tiempo de vida máximo. Esta llamada debería llevar a la destrucción de los registros en el soporte de almacenamiento que no han sido accedidos desde `lifetime`.
