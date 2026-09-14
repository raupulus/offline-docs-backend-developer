---
title: Ejemplos
source_url: https://www.php.net/manual/es/yaf.tutorials.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/tutorials.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 198f577cb
order: 104510
---

## Ejemplos

Distribución clásica del directorio Application

    - index.php
    - .htaccess
    + conf
      |- application.ini //configuración de la aplicación
    - application/
      - Bootstrap.php
      + controllers
         - Index.php //controlador predeterminado
      + views
         |+ index
            - index.phtml //plantilla de vistas para la acción predeterminada
      + modules
      - library
      - models
      - plugins

Entrada

index.php en el directorio superior es la única forma de entrada de la aplicación, se deberían reescribir todas las peticiones al mismo (se puede emplear .htaccess de Apache+php_mod)

```php
<?php
define("APPLICATION_PATH",  dirname(__FILE__));

$app  = new Yaf_Application(APPLICATION_PATH . "/conf/application.ini");
$app->bootstrap() //llamar a los métodos de arranque definidos en Bootstrap.php
->run();
?>

  
```

Regla de sobrescritura

    #para apache (.htaccess)
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule .* index.php

    #para nginx
    server {
    listen ****;
    server_name  domain.com;
    root   document_root;
    index  index.php index.html index.htm;

    if (!-e $request_filename) {
      rewrite ^/(.*)  /index.php/$1 last;
    }
    }

    #para lighttpd
    $HTTP["host"] =~ "(www.)?domain.com$" {
    url.rewrite = (
        "^/(.+)/?$"  => "/index.php/$1",
    )
    }

Configuración de la aplicación

```php
[yaf]
;APPLICATION_PATH es la constante definida en index.php
application.directory=APPLICATION_PATH "/application/"

;la sección 'product' hereda de las sección 'yaf'
[product:yaf]
foo=bar

   
```

Controlador predeterminado

```php
<?php
class IndexController extends Yaf_Controller_Abstract {
   /* acción predeterminada */
   public function indexAction() {
       $this->_view->word = "hola mundo";
       //or
       // $this->getView()->word = "hola mundo";
   }
}
?>

   
```

Plantilla de vistas predeterminada

```php
  
  <html>
  <head>
    <title>Hola Mundo</title>
  </head>
  <body>
    <?php echo $word;?>
  </body>
  </html>
  
    
```

Ejecutar la aplicación

Resultado del ejemplo anterior es similar a:

    <html>
     <head>
       <title>Hola Mundo</title>
     </head>
     <body>
       hola mundo
     </body>
    </html>

       

> [!NOTE]
> También se puede generar el ejemplo de arriba usando el generado de código de Yaf, el cual se puede encontrar en yaf@github.
