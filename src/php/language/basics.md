---
title: Lo básico
source_url: https://www.php.net/manual/es/language.errors.basics.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/errors/basics.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: de9c65c91
order: 2290
---

## Lo básico

PHP notifica errores en respuesta a varias condiciones de error internas. Estas se pueden utilizar para señalar varias condiciones diferentes, mostrándose y/o registrándose si fuera necesario.

Cada error que genera PHP incluye un tipo. Existe una [lista de dichos tipos de error](#errorfunc.constants), junto con una breve descripción de su comportamiento y sus posibles causas.

## Manejo de errores con PHP

Si no se establece un manejador de errores, PHP manejará cada error que ocurra según su configuración. Los errores que se notifican y los que se ignoran se controla mediante la directiva [`error_reporting`](#ini.error-reporting) de php.ini, o durante la ejecución llamando a `error_reporting`. Sin embargo, se recomienda encarecidamente establecer la directiva de configuración, ya que algunos errores pueden ocurrir antes de comenzar la ejecución de un script.

En un entorno de desarrollo debería establecerse siempre [`error_reporting`](#ini.error-reporting) a `E_ALL`, debido a que es necesario reconocer y corregir los problemas generados por PHP. En producción, se podría establecer esta directiva a un nivel de menor verbosidad como `E_ALL & ~E_NOTICE & ~E_DEPRECATED`, aunque en muchos casos `E_ALL` también es apropiado, ya que puede proporcionar advertencias precoces de problemas potenciales.

Lo que PHP hace con estos errores depende de dos directivas más de php.ini. [`display_errors`](#ini.display-errors) controla si el error es mostrado como parte de la salida del script. Esta debería estar siempre deshabilitada en un entorno de producción, ya que puede incluir información confidencial tal como contraseñas de bases de datos, aunque a menudo es útil habilitarla en desarrollo debido a que asegura la notificación inmediata de problemas.

Además de mostrar errores, PHP puede registrarlos cuando la directiva [`log_errors`](#ini.log-errors) está habilitada. Esta registrará cualquier error en el fichero o registro del sistema definido por [`error_log`](#ini.error-log). Esta directiva puede ser extremadamente útil en un entorno de producción debido a que se pueden registrar los errores que ocurran y generar informes basados en ellos.

## Manejadores de errores de usuario

Si el manejo de errores predeterminado de PHP es inadecuado, también se pueden manejar muchos tipos de error con un manejador de errores propio mediante `set_error_handler`. Mientras que algunos tipos de error no se pueden manejar de esta forma, aquellos que sí se pueden lo hacen de la manera en que su script vea apropiada: por ejemplo, se puede emplear para mostrar al usuario una página de error personalizada y luego notificar más directamente mediante un registro, tal como el envío de un correo electrónico.
