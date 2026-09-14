---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration81.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration81/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 4d2479dcf
order: 900
---

## Otros cambios

## Cambios en los módulos SAPI

### CLI

Usar `-a` sin la extensión [readline](#book.readline) ahora resultará en un error. Anteriormente, `-a` sin readline tenía el mismo comportamiento que llamar a `php` sin ningún argumento, excepto por la impresión de un mensaje adicional `"Modo interactivo activado"`. Este modo no era *interactivo*.

### PHPDBG

Las funcionalidades distantes de [phpdbg](#book.phpdbg) han sido eliminadas.

## Funciones cambiadas

### Núcleo

El orden de las propiedades utilizadas en [`foreach`](#control-structures.foreach), `var_dump`, `serialize`, la comparación de objetos, etc., ha cambiado. Las propiedades ahora están ordenadas de forma natural según su declaración y herencia. Las propiedades declaradas en una clase base se colocan antes que las propiedades de la clase hija.

Este orden es coherente con la disposición interna de las propiedades en la estructura `zend_object` y refleja el orden en `default_properties_table[]` y `properties_info_table[]`. El orden anterior no estaba documentado y era causado por detalles de implementación.

### Filtro

La bandera `FILTER_FLAG_ALLOW_OCTAL` del filtro `FILTER_VALIDATE_INT` ahora acepta cadenas octales con el prefijo octal (`"0o"`/`"0O"`).

### GMP

Todas las funciones [GMP](#book.gmp) ahora aceptan cadenas octales con el prefijo octal (`"0o"`/`"0O"`).

### PDO ODBC

PDO::getAttribute con `PDO::ATTR_SERVER_INFO` y `PDO::ATTR_SERVER_VERSION` ahora devuelven valores en lugar de lanzar `PDOException`.

### Reflection

ReflectionProperty::setAccessible y ReflectionMethod::setAccessible ya no tienen efecto. Las propiedades y métodos ahora siempre se consideran accesibles a través de la reflexión.

### Estándar

`syslog` ahora es seguro en términos de binarios.

## Otros cambios en las extensiones

### GD

`imagewebp` ahora puede realizar codificación WebP sin pérdidas pasando `IMG_WEBP_LOSSLESS` como calidad.

Esta constante solo está definida si la biblioteca GD utilizada soporta la codificación WebP sin pérdidas.

### MySQLi

mysqli_stmt::next_result y mysqli::fetch_all ahora están disponibles al compilar contra libmysqlclient.

### OpenSSL

- La [extensión OpenSSL](#book.openssl) ahora requiere al menos OpenSSL versión 1.0.2.

- OpenSSL 3.0 ahora es compatible. Tenga en cuenta que muchos cifrados ya no están habilitados por defecto (parte del proveedor heredado), y que la validación de parámetros (por ejemplo, tamaños mínimos de clave) ahora es más estricta.

### Phar

- SHA256 ahora se usa por defecto para las firmas.

- Se ha añadido soporte para las firmas OpenSSL_SHA256 y OpenSSL_SHA512.

### SNMP

- Se ha añadido soporte para SHA256 y SHA512 para el protocolo de seguridad.

### Estándar

`--with-password-argon2` ahora usa pkg-config para detectar libargon2. En consecuencia, una ubicación alternativa para libargon2 ahora debe especificarse usando `PKG_CONFIG_PATH`.

## Cambios en la gestión del archivo INI

- La directiva INI [log_errors_max_len](#ini.log-errors-max-len) ha sido eliminada. No tenía efecto desde PHP 8.0.0.

- Un dólar al inicio de una cadena citada ahora puede ser escapado: `"\${"` ahora será interpretado como una cadena con el contenido `${`.

- Las barras invertidas en las cadenas doblemente citadas ahora se tratan de manera más coherente como caracteres de escape. Anteriormente, `"foo\\"` seguido de algo más en una nueva línea no se consideraba una cadena terminada. Ahora se interpreta como una cadena con el contenido `foo\`. Sin embargo, como excepción, la cadena `"foo\"` seguida de una nueva línea continuará siendo tratada como una cadena válida con el contenido `foo\` en lugar de una cadena no terminada. Esta excepción existe para soportar los usos ingenuos de rutas de archivos de Windows como `"C:\foo\"`.
