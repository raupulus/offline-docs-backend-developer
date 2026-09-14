---
title: mysqli::options
description: Define las opciones
source_url: https://www.php.net/manual/es/mysqli.options.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/options.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: e309a62b1
order: 55220
---

mysqli::options

mysqli_options

Define las opciones

## Descripción

Estilo orientado a objetos

```php
public mysqli::options(int $option, string $value): bool
```php

Estilo procedimental

```php
mysqli_options(mysqli $mysql, int $option, string $value): bool
```

Útil para definir opciones de conexión y así afectar el comportamiento de la conexión actual.

Esta función puede ser llamada múltiples veces para definir múltiples opciones.

`mysqli_options` debe ser llamada después de `mysqli_init` y antes de `mysqli_real_connect`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`option`  
La opción que se desea definir. Puede tomar uno de los siguientes valores:

| Nombre | Descripción |
|----|----|
| `MYSQLI_OPT_CONNECT_TIMEOUT` | Tiempo máximo de conexión en segundos |
| `MYSQLI_OPT_READ_TIMEOUT` | Tiempo de espera de ejecución de un comando en segundos. Disponible a partir de PHP 7.2.0. |
| `MYSQLI_OPT_LOCAL_INFILE` | Activa/desactiva el uso de `LOAD LOCAL INFILE` |
| `MYSQLI_OPT_LOAD_DATA_LOCAL_DIR` | Directorio a utilizar para `LOAD DATA LOCAL INFILE`. |
| `MYSQLI_INIT_COMMAND` | Comando a ejecutar después de la conexión al servidor MySQL |
| `MYSQLI_SET_CHARSET_NAME` | El juego de caracteres a definir por defecto. |
| `MYSQLI_READ_DEFAULT_FILE` | Lee las opciones desde el nombre de la opción en lugar del archivo `my.cnf` No soportado por mysqlnd |
| `MYSQLI_READ_DEFAULT_GROUP` | Lee las opciones del grupo desde `my.cnf` o desde el archivo especificado con `MYSQL_READ_DEFAULT_FILE`. No soportado por mysqlnd |
| `MYSQLI_SERVER_PUBLIC_KEY` | Archivo que contiene la clave pública RSA utilizada con la autenticación basada en SHA-256. |
| `MYSQLI_OPT_NET_CMD_BUFFER_SIZE` | El tamaño del buffer interno de comando/red. Únicamente válido para mysqlnd. |
| `MYSQLI_OPT_NET_READ_BUFFER_SIZE` | Tamaño, en bytes, máximo de la parte a leer durante la lectura del cuerpo de un paquete de comando MySQL. Únicamente válido para mysqlnd. |
| `MYSQLI_OPT_INT_AND_FLOAT_NATIVE` | Convierte las columnas enteras y de coma flotante en números PHP al utilizar declaraciones no preparadas. Válido únicamente para mysqlnd. |
| `MYSQLI_OPT_SSL_VERIFY_SERVER_CERT` | Si se debe verificar o no el certificado del servidor. |
| `MYSQLI_OPT_CAN_HANDLE_EXPIRED_PASSWORDS` | Si el cliente debe aceptar contraseñas expiradas. |
| `1` | Si se debe utilizar la compresión de comunicación de red. |

Opciones válidas {#mysqli.options.parameters}

`value`  
El valor para la opción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ver `mysqli_real_connect`.

## Notas

> [!NOTE]
> MySQLnd siempre asume el juego de caracteres predeterminado del servidor. Este juego de caracteres es enviado durante el intercambio de conexión/autenticación, el cual mysqlnd utilizará.
>
> Libmysqlclient utiliza el juego de caracteres predeterminado establecido en el `my.cnf` o mediante una llamada explícita a `mysqli_options` antes de llamar a `mysqli_real_connect`, pero después de `mysqli_init`.

## Véase también

`mysqli_init`, `mysqli_real_connect`
