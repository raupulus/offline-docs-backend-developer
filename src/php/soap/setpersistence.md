---
title: SoapServer::setPersistence
description: Activa el modo persistente de SoapServer
source_url: https://www.php.net/manual/es/soapserver.setpersistence.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapserver/setpersistence.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: true
translation_revision: 89ae180a8
order: 75430
---

SoapServer::setPersistence

Activa el modo persistente de SoapServer

## Descripción

```php
public SoapServer::setPersistence(int $mode): void
```php

Esta función permite cambiar la persistencia de un objeto SoapServer entre las peticiones. Permite guardar los datos entre las peticiones, mediante las sesiones PHP. Esta función solo tiene efecto después de haber exportado la lista de funciones mediante SoapServer::setClass.

> [!NOTE]
> La constante de persistencia `SOAP_PERSISTENCE_SESSION` hace persistentes únicamente los objetos de la clase dada, pero no los datos estáticos. En este caso, `$this->bar` en lugar de self::\$bar.

> [!NOTE]
> `SOAP_PERSISTENCE_SESSION` serializa los datos del objeto entre las peticiones. En el caso de los recursos (por ejemplo `PDO`), [\_\_wakeup()](#object.wakeup) y [\_\_sleep()](#object.sleep) deben ser utilizadas.

## Parámetros

`mode`  
Una de las constantes `SOAP_PERSISTENCE_*`.

`SOAP_PERSISTENCE_REQUEST` - Los datos de SoapServer no son persistentes entre las peticiones. Este es el comportamiento por **omisión** de todo objeto SoapServer después de llamar a setClass().

`SOAP_PERSISTENCE_SESSION` - Los datos de SoapServer persisten entre las peticiones. Esto se realiza serializando los datos de la clase SoapServer en `$_SESSION['_bogus_session_name']`, por lo que `session_start` debe ser llamada antes de pasar a este modo de persistencia.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo `SoapServer::setPersistence`

```
<?php
 class MyFirstPersistentSoapServer {
     private $resource; // (Por ejemplo PDO, mysqli, etc..)
     public $myvar1;
     public $myvar2;

     public function __construct() {
         $this->__wakeup(); // Se llama a nuestro wakeup para reiniciar nuestro recurso
     }

     public function __wakeup() {
         $this->resource = CodeToStartOurResourceUp();
     }

     public function __sleep() {
         // Se asegura de eliminar $resource aquí, así nuestros datos pueden persistir en sesión
         // Si se olvida, la deserialización en la próxima petición fallará y nuestro objeto
         // SoapObject no será persistente entre las peticiones.
         return array('myvar1','myvar2');
     }
 }

 try {
     session_start();
     $server = new SoapServer(null, array('uri' => $_SERVER['REQUEST_URI']));
     $server->setClass('MyFirstPersistentSoapServer');
     // setPersistence() DEBE ser llamada después de setClass(), ya que el comportamiento de setClass()
     // afecta SESSION_PERSISTENCE_REQUEST.
     $server->setPersistence(SOAP_PERSISTENCE_SESSION);
     $server->handle();
 } catch(SoapFault $e) {
     error_log("SOAP ERROR: ". $e->getMessage());
 }
?>

    
```php

## Véase también

SoapServer::setClass
