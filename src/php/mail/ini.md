---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/mail.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mail/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mail
translation_status: ready
translation_reviewed: false
translation_revision: '912705841'
order: 44270
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [mail.add_x_header](#ini.mail.add-x-header) | "0" | `INI_PERDIR` |  |
| [mail.mixed_lf_and_crlf](#ini.mail.mixed_lf_and_crlf) | "0" | `INI_SYSTEM`\|`INI_PERDIR` | Disponible a partir de PHP 8.2.4 |
| [mail.log](#ini.mail.log) | NULL | `INI_SYSTEM`\|`INI_PERDIR` |  |
| [mail.force_extra_parameters](#ini.mail.force_extra_parameters) | NULL | `INI_SYSTEM`\|`INI_PERDIR` |  |
| [SMTP](#ini.smtp) | "localhost" | `INI_ALL` |  |
| [smtp_port](#ini.smtp-port) | "25" | `INI_ALL` |  |
| [sendmail_from](#ini.sendmail-from) | NULL | `INI_ALL` |  |
| [sendmail_path](#ini.sendmail-path) | "/usr/sbin/sendmail -t -i" | `INI_SYSTEM` |  |

Opciones de configuración para el correo

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`mail.add_x_header` `bool`  
Se añade un encabezado `X-PHP-Originating-Script` que incluye el UID del script, seguido por el nombre del fichero.

`mail.log` `string`  
La ruta del registro de todos los llamados a la función `mail`. Las entradas del registro incluyen la ruta completa hacia el script, el número de la línea, las direcciones `To` así como los encabezados.

`mail.mixed_lf_and_crlf` `bool`  
Permite volver al indicador de fin de línea para los encabezados de correo electrónico y los cuerpos de mensaje en LF (Line Feed), imitando el comportamiento no conforme de PHP 7. Se proporciona como medida de compatibilidad para ciertos Agentes de Transferencia de Correo (MTA) no conformes que fallan al tratar correctamente CRLF (Retorno de carro + Line Feed) como indicador de fin de línea en los encabezados de correo electrónico y el contenido de los mensajes.

`mail.force_extra_parameters` `string`  
Permite forzar la adición del parámetro especificado como parámetro adicional para sendmail. Estos parámetros reemplazarán al quinto parámetro de la función `mail`.

Además del comportamiento predeterminado para `INI_SYSTEM`, este valor también se puede establecer con `php_value` en `httpd.conf` (aunque no se recomienda).

`smtp` `string`  
Solo en Windows: nombre del host o dirección IP del SMTP que PHP debe utilizar para enviar un correo con la función `mail`.

`smtp_port` `int`  
Solo en Windows: número de puerto a utilizar para conectarse al servidor `SMTP` al enviar correo con la función `mail`; por omisión, es 25.

`sendmail_from` `string`  
Solo en Windows: valor del campo `"From:"` que debe ser utilizado al enviar correo vía SMTP (solo en Windows). Esta directiva definirá también el encabezado `"Return-Path:"`.

`sendmail_path` `string`  
Localización del programa `sendmail`: habitualmente `/usr/sbin/sendmail` o `/usr/lib/sendmail`. `configure` intenta detectar la presencia de sendmail por sí mismo, y asigna este resultado por omisión. En caso de problemas de localización, puede establecerse un nuevo valor por omisión aquí.

Todo sistema que no utilice `sendmail` debe establecer esta directiva al camino del programa de sustitución que reemplaza al servidor de correo, si aquel existe. Por ejemplo, los usuarios de [Qmail](http://cr.yp.to/qmail.html) pueden definirla a `/var/qmail/bin/sendmail` o `/var/qmail/bin/qmail-inject`.

`qmail-inject` no requiere opciones para tratar correctamente el correo.

Esta directiva funciona también en Windows. Si está definida, `smtp`, `smtp_port` y `sendmail_from` son ignorados y se ejecuta el comando especificado.
