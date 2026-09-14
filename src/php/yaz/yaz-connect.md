---
title: yaz_connect
description: Prepara una conexión a un servidor Z39.50
source_url: https://www.php.net/manual/es/function.yaz-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_reviewed: false
translation_revision: dafb1509d
order: 107780
---

yaz_connect

Prepara una conexión a un servidor Z39.50

## Descripción

```php
yaz_connect(string $zurl, [mixed $options]): mixed
```php

Esta función devuelve un recurso de conexión en caso de éxito, cero en caso de fallo.

`yaz_connect` prepara una conexión a un servidor Z39.50. Esta función es no bloqueante y no intenta establecer una conexión - únicamente prepara la conexión para que pueda ser realizada posteriormente cuando se llame a la función `yaz_wait`.

> [!NOTE]
> El proxy [YAZ ](http://www.indexdata.dk/yazproxy/) es un proxy Z39.50 disponible gratuitamente.

## Parámetros

`zurl`  
Un string que toma la forma `host[:port][/database]`. Si se omite el port, se utilizará el port 210. Si se omite database se utilizará `Default` .

`options`  
Si se trata de un string, éste se trata como el string de autenticación Z39.50 V2 (OpenAuth).

Si se trata de un array, el contenido del array sirve como opciones.

user  
Nombre de usuario para la autenticación.

group  
Grupo para la autenticación.

password  
Contraseña para la autenticación.

cookie  
Cookie para la sesión (proxy YAZ).

proxy  
Proxy para la conexión (proxy YAZ).

persistent  
Un booleano. Si es `true` la conexión es persistente; Si es `false` la conexión no es persistente. Por defecto las conexiones son persistentes.

> [!NOTE]
> Si se abre una conexión persistente, no se podrá cerrar posteriormente con la función `yaz_close`.

piggyback  
Un booleano. Si es `true` piggyback está activado para las búsquedas; Si es `false` piggyback está desactivado. Por defecto piggyback está activado.

Activar piggyback es más eficiente y normalmente ahorra una ruta de ida y vuelta en la red para las cargas de los registros por primera vez. Sin embargo, unos pocos servidores Z39.50 no soportan piggyback o ignoran los nombres de los elementos configurados. Para ellos, se debe desactivar piggyback.

charset  
Un string que especifica el mapa de caracteres que será utilizado como lenguaje y mapa de caracteres en la negociación Z39.50. Utilizar strings como: `ISO-8859-1`, `UTF-8`, `UTF-16`.

Muchos servidores Z39.50 no soportan esta funcionalidad (y por ello, ésta es ignorada). Muchos servidores utilizan la codificación ISO-8859-1 para consultas y mensajes. Los registros MARC21/USMARC no están afectados por este parámetro

preferredMessageSize  
Un entero que especifica el tamaño máximo de byte para todos los registros que se devolverán por el objetivo durante la recuperación. Ver el estandard [Z39.50](http://www.loc.gov/z3950/agency/markup/04.html#3.2.1.1.4) para más información.

> [!NOTE]
> Esta opción está soportada en PECL YAZ 1.0.5 o posteriores.

maximumRecordSize  
Un entero que especifica el tamaño máximo de byte de un único registro a ser devuelto por un objetivo durante la recuperación. Esta entidad se denomina como un Exceptional-record-size en el standard [Z39.50](http://www.loc.gov/z3950/agency/markup/04.html#3.2.1.1.4).

> [!NOTE]
> Esta opción está soportada en PECL YAZ 1.0.5 o posteriores.

## Valores devueltos

Un recurso de conexión en caso de éxito, `false` en caso de error.

## Véase también

`yaz_close`
