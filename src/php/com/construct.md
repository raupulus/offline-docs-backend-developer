---
title: com::__construct
description: Constructor de la clase com
source_url: https://www.php.net/manual/es/com.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/com/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 49ff12041
order: 7500
---

com::\_\_construct

Constructor de la clase com

## Descripción

```php
public com::__construct(string $module_name, [array $server_name], [int $codepage], [string $typelib])
```php

Construye un nuevo objeto com.

## Parámetros

`module_name`  
Puede ser un ProgID, Class ID o Moniker que nombra el componente a cargar.

Un ProgID es típicamente el nombre de la aplicación o del DDL, seguido de un punto, seguido del nombre del objeto. Por ejemplo: `Word.Application`.

Un Class ID es el UUID que identifica únicamente una clase dada.

Un Moniker es una forma especial de nombramiento, similar en concepto a un esquema URL, que identifica un recurso y especifica cómo debería ser cargado. Por ejemplo, se puede iniciar Word y recuperar un objeto que represente un documento de Word especificando la ruta completa del documento de Word como nombre de módulo, o se puede usar `LDAP:` como Moniker para usar la interfaz ADSI a LDAP.

`server_name`  
El nombre del servidor DCOM en el cual el componente debería ser cargado y ejecutado. Si `null`, el objeto es ejecutado utilizando el valor por defecto para la aplicación. El valor por defecto es típicamente ejecutar en la máquina local, sin embargo, el administrador puede haber configurado la aplicación para ser lanzada en una máquina diferente.

Si se especifica un valor no-`null` para el servidor, PHP se negará a cargar el objeto a menos que la opción [com.allow_dcom](#ini.com.allow-dcom) `php.ini` esté definida como `true`.

Si `server_name` es un `array`, debería contener los siguientes elementos (sensible a mayúsculas y minúsculas!). A notar que todos son opcionales (sin embargo, debe definir el Usuario y la Contraseña juntos); si omite el parámetro Server, se usará el servidor por defecto (como se mencionó anteriormente), y la instanciación del objeto no será afectada por la directiva `php.ini` [com.allow_dcom](#ini.com.allow-dcom).

| Clave | Tipo | Descripción |
|----|----|----|
| Server | `string` | El nombre del servidor |
| Username | `string` | El nombre de usuario para conectarse como. |
| Password | `string` | La contraseña para `Username`. |
| Domain | `string` | El dominio del `servidor`. |
| Banderas | `int` | Una o más de las siguientes constantes, ensambladas juntas gracias al OU lógico: `CLSCTX_INPROC_SERVER`, `CLSCTX_INPROC_HANDLER`, `CLSCTX_LOCAL_SERVER`, `CLSCTX_REMOTE_SERVER`, `CLSCTX_SERVER` y `CLSCTX_ALL`. El valor por defecto si no se define aquí es `CLSCTX_SERVER` si también se omite `Server`, o `CLSCTX_REMOTE_SERVER` si se define un servidor. Debe consultar la documentación de Microsoft para CoCreateInstance para más información sobre el significado de estas constantes; típicamente nunca las utilizará. |

Nombre de servidor DCOM

`codepage`  
Define la codepage que se utiliza para convertir las `string` en `string` unicode y viceversa. La conversión se aplica cuando una `string` PHP se pasa como parámetro o se devuelve desde un método de este objeto COM. La codepage es "pegajosa", lo que significa que se propagará a los objetos y variantes devueltos desde el objeto.

Los valores posibles son: `CP_ACP` (utiliza la codepage ANSI del sistema por defecto - por defecto si se omite este parámetro), `CP_MACCP`, `CP_OEMCP`, `CP_SYMBOL`, `CP_THREAD_ACP` (utiliza la codepage/configuración local definida para el hilo en ejecución), `CP_UTF7` y `CP_UTF8`. También puede utilizar el número para una codepage dada; consulte la documentación de Microsoft para más detalles sobre las codepages y sus valores numéricos.
