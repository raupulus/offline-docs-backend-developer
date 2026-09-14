---
title: La clase Yaf_Router
source_url: https://www.php.net/manual/es/class.yaf-router.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-router.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 4d17b7b49
order: 104860
---

## Introducción

`Yaf_Router` es el enrutador estándar del framework. Enrutar es el proceso de tomar un extremo de un URI (la parte del URI que va antes del URL base: véase Yaf_Request_Abstract::setBaseUri) y descomponerlo en parámetros para determinar qué módulo, controlador, y acción de ese controlador deberían recibir la petición. Estos valores de módulo, controlador, acción y demás parámetros, son empaquetados en un objeto `Yaf_Request_Abstract` que es procesado por `Yaf_Dispatcher`. El enrutamiento sucede sólo una vez: cuando la petición es recibida inicialmente y antes de que el primer controlador sea despachado. La clase `Yaf_Router` está diseñada para tener en cuenta una funcionalidad parecida a la directiva mod_rewrite usando simples estructuras de PHP. Está basada indirectamente en el enrutamiento de Ruby on Rails y no requiere ningún conocimiento previo de la reescritura de URL del servidor web. Está diseñada para funcionar con una simple regla de la directiva mod_rewrite de Apache (una de):

Regla de reescritura para Apache

```php
RewriteEngine on
RewriteRule !\.(js|ico|gif|jpg|png|css|html)$ index.php

     
```

o (preferible):

Regla de reescritura para Apache

```php
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} -s [OR]
RewriteCond %{REQUEST_FILENAME} -l [OR]
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^.*$ - [NC,L]
RewriteRule ^.*$ index.php [NC,L]

     
```

Si se usa Lighttpd, la siguiente regla de reescritura es válida:

Regla de reescritura para Lighttpd

```php
url.rewrite-once = (
  ".*\?(.*)$" => "/index.php?$1",
  ".*\.(js|ico|gif|jpg|png|css|html)$" => "$0",
  "" => "/index.php"
)

     
```

Si se usa Nginx, utilice la siguiente regla de reescritura:

Regla de reescritura para Nginx

```php
server {
  listen ****;
  server_name  yourdomain.com;
  root   document_root;
  index  index.php index.html;

  if (!-e $request_filename) {
    rewrite ^/(.*)  /index.php/$1 last;
  }
}

     
```

## Enrutamiento predeterminado

`Yaf_Router` comes viene preconfigurada con un enrutamiento `Yaf_Route_Static` predeterminado, el cual comparará URIs en la forma de controlador/acción. Además, se puede especificar un nombre de módulo como el primer elemento de la ruta, permitiendo URIs de la forma módulo/controlador/acción. Finalmente, también comparará cualquier parámetro adicional añadido al URI por omisión - controlador/acción/variable1/valor1/variable2/valor2.

> [!NOTE]
> El nombre del módulo debe estar definido en la configuración, considerando application.module="Index,Foo,Bar", en este caso, solamente index, foo y bar pueden ser considerados como un nombre de módulo; si no está configurado, sólo existe un nombre de módulo llamado "Index".

Algunos ejemplos de cómo tales enrutamientos son comparados:

Ejemplo de `Yaf_Route_Static` (ruta predeterminada)

```php
// Se asume la siguiente configuración:
$conf = array(
   "application" => array(
      "modules" => "Index,Blog",
   ),
);

Solamente el controlador:
http://example/news
    controller == news
Solamente la acción (al definir yaf.action_prefer=1 en php.ini)
    action  == news

Un módulo inválido mapea el nombre del controlador:
http://example/foo
    controller == foo

Módulo + controlador:
http://example/blog/archive
    module     == blog
    controller == archive

Módulo + controlador + acción:
http://example/blog/archive/list
    module     == blog
    controller == archive
    action     == list

Módulo + controlador + acción + parámetros:
http://example/blog/archive/list/sort/alpha/date/desc
    module     == blog
    controller == archive
    action     == list
    sort       == alpha
    date       == desc

     
```

## Sinopsis de la clase

Yaf_Router

Yaf_Router

Propiedades

protected

\_routes

protected

\_current

Métodos

## Propiedades

`_routes`  
Pila de rutas registradas

`_current`  
Después de la fase de enrutamiento, esto indica el nombre de la ruta a usar para enrutar la petición actual. Se puede obtener este nombre mediante Yaf_Router::getCurrentRoute.
