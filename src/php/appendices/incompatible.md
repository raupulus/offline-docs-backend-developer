---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration56.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration56/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: b67451f6f
order: 200
---

## Cambios incompatibles con versiones anteriores

Aunque la mayoría del código PHP 5 existente debería funcionar sin ninguna modificación, se deben tener en cuenta algunas incompatibilidades hacia atrás:

## Las claves de los arrays no se sobrescriben al definir un array como una propiedad de una clase a través de un literal de array

Anteriormente, los arrays declarados como propiedades de clase que mezclaban claves explícitas e implícitas podían ver sus elementos sobrescritos sin advertencia si una clave explícita era idéntica a una clave secuencial implícita. Por ejemplo:

```php
<?php
class C {
    const ONE = 1;
    public $array = [
        self::ONE => 'foo',
        'bar',
        'quux',
    ];
}

var_dump((new C)->array);
?>

   
```

Resultado del ejemplo anterior en PHP 5.5:

    array(2) {
      [0]=>
      string(3) "bar"
      [1]=>
      string(4) "quux"
    }

       

Resultado del ejemplo anterior en PHP 5.6:

    array(3) {
      [1]=>
      string(3) "foo"
      [2]=>
      string(3) "bar"
      [3]=>
      string(4) "quux"
    }

## Rigurosidad de `json_decode`

`json_decode` ahora rechaza las variantes no escritas en minúscula de los literales JSON `true`, `false` y `null`, de acuerdo con la especificación JSON, y `json_last_error` se establece de forma correspondiente. Anteriormente, los valores pasados a `json_decode` que contenían alguno de estos valores en mayúsculas o en una combinación de mayúsculas y minúsculas se aceptaban.

Este cambio solo afectará a los casos en los que se pase JSON inválido a `json_decode`: el JSON válido no se verá afectado y se analizará normalmente.

## Las envolturas de flujo ahora verifican de forma predeterminada los certificados de par y los nombres de host al usar SSL/TLS

Todos los flujos cifrados de cliente activan ahora la verificación de pares de forma predeterminada. De forma predeterminada, esto utilizará el paquete de CA predeterminado de OpenSSL para verificar el certificado de par. Para la mayoría de los usuarios, esto no debería causar problemas al comunicarse con servidores que tengan certificados SSL válidos, ya que la mayoría de los distribuidores configuran OpenSSL para usar las rutas de CA predeterminadas.

El paquete de CA predeterminado se puede sobrescribir a nivel global utilizando las opciones de configuración openssl.cafile o openssl.capath, o para cada solicitud utilizando las opciones de contexto [`cafile`](#context.ssl.cafile) o [`capath`](#context.ssl.capath) .

Aunque en general no se recomienda, es posible desactivar la verificación del certificado de par para una solicitud estableciendo la opción de contexto [`verify_peer`](#context.ssl.verify-peer) a `false`, y desactivar la validación del nombre del par configurando la opción de contexto [`verify_peer_name`](#context.ssl.verify-peer-name) a `false`.

## Los recursos [GMP](#book.gmp) ahora son objetos

Los recursos [GMP](#book.gmp) ahora son objetos. La API de la extensión GMP no ha cambiado y el código existente debería continuar funcionando sin modificación a menos que se realice una verificación explícita usando `is_resource` o equivalente.

## Las funciones [Mcrypt](#book.mcrypt) ahora requieren claves o IV válidos

`mcrypt_encrypt`, `mcrypt_decrypt`, `mcrypt_cbc`, `mcrypt_cfb`, `mcrypt_ecb`, `mcrypt_generic` y `mcrypt_ofb` ya no aceptan claves o vectores de inicialización (IVs) de tamaños incorrectos, y los modos de cifrado por bloques que requieren IVs fallarán ahora si no se proporciona un IV.

## Subida de archivos con [cURL](#book.curl)

La subida de archivos usando la sintaxis @file ahora requiere que la directiva CURLOPT_SAFE_UPLOAD esté definida como `false`. Se debe usar `CURLFile` en su lugar.
