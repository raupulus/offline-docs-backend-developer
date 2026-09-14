---
title: mail
description: Envío de correo
source_url: https://www.php.net/manual/es/function.mail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mail/functions/mail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mail
translation_status: ready
translation_reviewed: false
translation_revision: d43f29f6a
order: 44260
---

mail

Envío de correo

## Descripción

```php
mail(string $to, string $subject, string $message, [array $additional_headers], [string $additional_params]): bool
```php

Envía un correo.

## Parámetros

`to`  
El o los destinatarios del correo.

El formato de esta cadena debe corresponder con la [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822). A continuación se muestran algunos ejemplos: destinatario@example.com, destinatario@example.com, otro_destinatario@example.com, Destinatario \<destinatario@example.com\>, Destinatario \<destinatario@example.com\>, Otro destinatario \<otro_destinatario@example.com\>

`subject`  
Asunto del correo a enviar.

> [!CAUTION]
> El asunto debe cumplir con la [RFC 2047](https://datatracker.ietf.org/doc/html/rfc2047).

`message`  
Mensaje a enviar.

Cada línea debe estar separada por un carácter `CRLF` (`\r\n`). Las líneas no deben contener más de 70 caracteres.

> [!CAUTION]
> (Solo Windows) Cuando PHP se comunica directamente con un servidor SMTP, si se encuentra un punto al inicio de una línea, será eliminado. Para evitar este comportamiento, reemplace estas ocurrencias con dos puntos.
>
> ```
> <?php
>      $text = str_replace("\n.", "\n..", $text);
> ?>
>
>         
> ```

`additional_headers` (opcional)  
`String` o `array` a insertar al final de los encabezados del correo.

Este parámetro se utiliza típicamente para añadir encabezados adicionales (From, Cc y Bcc). Los encabezados adicionales deben estar separados por un carácter `CRLF` (`\r\n`). Si se utilizan datos externos para componer este encabezado, deben ser limpiados primero para evitar la inyección de datos no deseados en los encabezados.

Si se pasa un `array`, sus claves son los nombres de los encabezados y sus valores son los valores de los encabezados respectivos.

> [!NOTE]
> Al enviar un correo, el correo *debe* contener un encabezado `From`. Puede ser definido por el parámetro `additional_headers`, o puede ser un valor predeterminado definido en el `php.ini`.
>
> No hacerlo causará un mensaje de error similar a `Warning: mail(): "sendmail_from" not set in php.ini or custom "From:" header missing`. El encabezado `From` también define el encabezado `Return-Path` al enviar directamente vía SMTP (solo Windows).

> [!NOTE]
> Si el mensaje no es recibido, intente utilizar únicamente un carácter `LF` (`\n`). Algunos agentes de transferencia de correo Unix (por ejemplo [qmail](http://cr.yp.to/qmail.html)) reemplazan automáticamente el carácter `LF` por el carácter `CRLF` (lo que equivale a duplicar el carácter `CR` si se utiliza el carácter `CRLF`). Esto debe ser un último recurso ya que no cumple con la [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822).

`additional_params` (opcional)  
El parámetro `additional_params` puede ser utilizado para pasar banderas adicionales como opciones a la línea de comandos configurada para ser utilizada para enviar los correos utilizando el parámetro de configuración `sendmail_path`. Por ejemplo, esto puede ser utilizado para definir la dirección del remitente del sobre al utilizar sendmail con la opción `-f`.

Este parámetro es escapado por la función `escapeshellcmd` internamente para prevenir la ejecución de un comando. La función `escapeshellcmd` previene la ejecución de un comando, pero permite añadir parámetros adicionales. Por razones de seguridad, se recomienda al usuario limpiar este parámetro para evitar añadir parámetros no deseados al comando shell.

Dado que la función `escapeshellcmd` se aplica automáticamente, algunos caracteres permitidos en las direcciones de correo por las RFCs de internet ya no pueden ser utilizados. La función `mail` no puede permitir estos caracteres, por lo tanto, en los programas donde su utilización es necesaria, debería utilizarse un método alternativo para el envío de correos (como el uso de un framework o una biblioteca.

El usuario bajo el cual se ejecuta el servidor web debe ser añadido como usuario de confianza en la configuración de sendmail para que el encabezado `X-Warning` no sea añadido al mensaje cuando el remitente del sobre (-f) es definido utilizando este método. Para los usuarios de sendmail, este archivo es `/etc/mail/trusted-users`.

## Valores devueltos

Devuelve `true` si el correo ha sido aceptado para su entrega, `false` en caso contrario.

Es importante tener en cuenta que el hecho de que el correo haya sido aceptado para su entrega no garantiza que llegue a su destino.

## Historial de cambios

| Versión | Descripción                                             |
|---------|---------------------------------------------------------|
| 7.2.0   | El parámetro `additional_headers` ahora acepta `array`. |

## Ejemplos

Envío de un correo

Uso de la función `mail` para enviar un correo simple:

```
<?php
// El mensaje
$message = "Línea 1\r\nLínea 2\r\nLínea 3";

// En caso de que nuestras líneas contengan más de 70 caracteres, las cortamos utilizando wordwrap()
$message = wordwrap($message, 70, "\r\n");

// Envío del correo
mail('caffeinated@example.com', 'Mi Asunto', $message);
?>

    
```php

Envío de un correo con encabezados adicionales

Añadir encabezados simples, especificando al MUA las direcciones `"From"` y `"Reply-To"`:

```
<?php
     $to      = 'persona@example.com';
     $subject = 'el asunto';
     $message = '¡Hola!';
     $headers = 'From: webmaster@example.com' . "\r\n" .
     'Reply-To: webmaster@example.com' . "\r\n" .
     'X-Mailer: PHP/' . phpversion();

     mail($to, $subject, $message, $headers);
 ?>

    
```php

Envío de un correo con un `array` de encabezados adicionales

Este ejemplo envía el mismo correo que el ejemplo anterior, pero pasa los encabezados adicionales como un array (disponible desde PHP 7.2.0).

```
<?php
$to      = 'nadie@example.com';
$subject = 'el asunto';
$message = 'hola';
$headers = array(
    'From' => 'webmaster@example.com',
    'Reply-To' => 'webmaster@example.com',
    'X-Mailer' => 'PHP/' . phpversion()
);

mail($to, $subject, $message, $headers);
?>

    
```php

Envío de un correo con un parámetro adicional de línea de comandos

El parámetro `additional_params` puede ser utilizado para pasar un parámetro adicional al programa configurado para ser utilizado para enviar los correos utilizando `sendmail_path`.

```
<?php
     mail('persona@example.com', 'el asunto', 'el mensaje', null,
     '-fwebmaster@example.com');
?>

    
```php

Envío de correo HTML

También es posible enviar correos HTML con la función `mail`.

```
<?php
     // Varios destinatarios
     $to  = 'johny@example.com, sally@example.com'; // note la coma

     // Asunto
     $subject = 'Calendario de cumpleaños para Agosto';

     // mensaje
     $message = '
     <html>
      <head>
       <title>Calendario de cumpleaños para Agosto</title>
      </head>
      <body>
       <p>¡Aquí están los cumpleaños que se avecinan en el mes de Agosto!</p>
       <table>
        <tr>
         <th>Persona</th><th>Día</th><th>Mes</th><th>Año</th>
        </tr>
        <tr>
         <td>Josiane</td><td>3</td><td>Agosto</td><td>1970</td>
        </tr>
        <tr>
         <td>Emma</td><td>26</td><td>Agosto</td><td>1973</td>
        </tr>
       </table>
      </body>
     </html>
     ';

     // Para enviar un correo HTML, el encabezado Content-type debe ser definido
     $headers[] = 'MIME-Version: 1.0';
     $headers[] = 'Content-type: text/html; charset=iso-8859-1';

     // Encabezados adicionales
     $headers[] = 'To: Mary <mary@example.com>, Kelly <kelly@example.com>';
     $headers[] = 'From: Cumpleaños <cumpleanos@example.com>';
     $headers[] = 'Cc: cumpleanos_archivo@example.com';
     $headers[] = 'Bcc: cumpleanos_verif@example.com';

     // Envío
     mail($to, $subject, $message, implode("\r\n", $headers));
?>

    
```php

> [!NOTE]
> Si se planea enviar correos HTML u otros más complejos, se recomienda utilizar el paquete PEAR [PEAR::Mail_Mime](https://pear.php.net/package/Mail_Mime).

## Notas

> [!NOTE]
> La implementación SMTP (solo en Windows) de la función `mail` difiere significativamente de la implementación de sendmail. En primer lugar, no utiliza un programa local para componer los mensajes, sino que opera únicamente y directamente sobre los sockets, lo que significa que un `MTA` está necesariamente escuchando en un socket de red (que puede estar en la red local o en una máquina remota).
>
> En segundo lugar, los encabezados personalizados como `From:`, `Cc:`, `Bcc:` y `Date:` no son **interpretados** por el `MTA` en primer lugar, sino que son analizados por PHP.
>
> Además, el parámetro `to` no debe ser una dirección en el formato `"Algo <alguien@example.com>"`. El comando mail no analizará correctamente esto al comunicarse con el MTA.

> [!NOTE]
> Es importante tener en cuenta que la función `mail` no está recomendada para manejar grandes volúmenes de correos en un bucle. Esta función abre y cierra un socket SMTP para cada correo, lo que no es muy eficiente.
>
> Para enviar grandes volúmenes de correos, consulte los paquetes [PEAR::Mail](https://pear.php.net/package/Mail) y [PEAR::Mail_Queue](https://pear.php.net/package/Mail_Queue).

> [!NOTE]
> Las siguientes RFC pueden ser útiles: [RFC 1896](https://datatracker.ietf.org/doc/html/rfc1896), [RFC 2045](https://datatracker.ietf.org/doc/html/rfc2045), [RFC 2046](https://datatracker.ietf.org/doc/html/rfc2046), [RFC 2047](https://datatracker.ietf.org/doc/html/rfc2047), [RFC 2048](https://datatracker.ietf.org/doc/html/rfc2048), [RFC 2049](https://datatracker.ietf.org/doc/html/rfc2049) y [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822).

## Véase también

`mb_send_mail`, `imap_mail`, [PEAR::Mail](https://pear.php.net/package/Mail), [PEAR::Mail_Mime](https://pear.php.net/package/Mail_Mime)
