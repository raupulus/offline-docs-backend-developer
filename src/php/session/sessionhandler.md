---
title: La clase SessionHandler
source_url: https://www.php.net/manual/es/class.sessionhandler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 74030
---

## Introducción

`SessionHandler` es una clase especial que puede usarse para exponer el gestor de almacenamiento de sesiones interno actual de PHP por herencia. Existen siete métodos que envuelven las sietes retrollamadas del gestor de almacenamiento de sesiones (`open`, `close`, `read`, `write`, `destroy`, `gc` y `create_sid`). Por defecto, esta clase envolverá cualquier gestor de almacenamiento que esté establecido como está definido por la directiva de configuración [session.save_handler](#ini.session.save-handler), el cual normalmente es `files` por omisión. Otros gestores de almacenamiento de sesión internos son proporcionados por extensiones de PHP tales como SQLite (como `sqlite`), Memcache (como `memcache`), y Memcached (como `Memcached`).

Cuando se establece una simple instancia de `SessionHandler` como el gestor de almacenamiento usando `session_set_save_handler`, envolverá los gestores de almacenamiento actuales. Una clase que extienda de `SessionHandler` permite sobrescribir los métodos o interceptarlos o filtrarlos llamando a los métodos de la clase madre, los cuales en última instancia envolverán los gestores de sesiones de PHP internos.

Esto permite, por ejemplo, interceptar los métodos `read` y `write` para encriptar/desencriptar la información de sesión y luego pasar el resultado hacia y desde la clase madre. De forma alternativa se podría elegir sobrescribir por completo un método como la llamada de retorno del recolector de basura `gc`.

Ya que `SessionHandler` envuelve los métodos del gestor de almacenamiento interno actual, el ejemplo de arriba de encriptación puede aplicarse a cualquier gestor de almacenamiento interno sin tener que conocer los entresijos de los gestores.

Para usar esta clase, primero establezca el gestor de almacenamiento que desee exponer usando [session.save_handler](#ini.session.save-handler) y luego pasar una instancia de `SessionHandler` o una que la extienda a `session_set_save_handler`.

Observe que los métodos de llamda de retorno de esta clase están diseñados para ser llamados internamente por PHP y no para ser llamados desde código de espacio de usuario. Los valores devueltos son igualmente procesados internamente por PHP. Para más información sobre el flujo de trabajo de sesiones consulte `session_set_save_handler`.

## Sinopsis de la clase

SessionHandler

implements

SessionHandlerInterface

SessionIdInterface

Métodos

## Notas

> [!WARNING]
> Esta clase está diseñada para exponer el gestor de almacenamiento de sesiones interno de PHP, si quiere escribir sus propios gestores de almacenamiento, implemente la interfaz `SessionHandlerInterface` en lugar de extender desde `SessionHandler`.

## Ejemplos

Usar `SessionHandler` para añadir encriptación a los gestores de almacenamiento internos de PHP.

```php
<?php

 /**
  * decrypt AES 256
  *
  * @param data $edata
  * @param string $password
  * @return decrypted data
  */
function decrypt($edata, $password) {
    $data = base64_decode($edata);
    $salt = substr($data, 0, 16);
    $ct = substr($data, 16);

    $rounds = 3; // depends on key length
    $data00 = $password.$salt;
    $hash = array();
    $hash[0] = hash('sha256', $data00, true);
    $result = $hash[0];
    for ($i = 1; $i < $rounds; $i++) {
        $hash[$i] = hash('sha256', $hash[$i - 1].$data00, true);
        $result .= $hash[$i];
    }
    $key = substr($result, 0, 32);
    $iv  = substr($result, 32,16);

    return openssl_decrypt($ct, 'AES-256-CBC', $key, true, $iv);
  }

/**
 * crypt AES 256
 *
 * @param data $data
 * @param string $password
 * @return base64 encrypted data
 */
function encrypt($data, $password) {
    // Generate a cryptographically secure random salt using random_bytes()
    $salt = random_bytes(16);

    $salted = '';
    $dx = '';
    // Salt the key(32) and iv(16) = 48
    while (strlen($salted) < 48) {
      $dx = hash('sha256', $dx.$password.$salt, true);
      $salted .= $dx;
    }

    $key = substr($salted, 0, 32);
    $iv  = substr($salted, 32,16);

    $encrypted_data = openssl_encrypt($data, 'AES-256-CBC', $key, true, $iv);
    return base64_encode($salt . $encrypted_data);
}

class EncryptedSessionHandler extends SessionHandler
{
    private $key;

    public function __construct($key)
    {
        $this->key = $key;
    }

    public function read($id)
    {
        $data = parent::read($id);

        if (!$data) {
            return "";
        } else {
            return decrypt($data, $this->key);
        }
    }

    public function write($id, $data)
    {
        $data = encrypt($data, $this->key);

        return parent::write($id, $data);
    }
}

// interceptaremos el manejador nativo 'files', pero funcionaría igualmente
// con otros manejadores nativos internos como 'sqlite', 'memcache' o 'memcached'
// que son proporcionados por extensiones de PHP.
ini_set('session.save_handler', 'files');

$key = 'secret_string';
$handler = new EncryptedSessionHandler($key);
session_set_save_handler($handler, true);
session_start();

// proceder para establecer y recuperar valores por clave desde $_SESSION

    
```

> [!NOTE]
> Ya que los métodos de esta clase están diseñados para se llamados internamente por PHP como parte del flujo de trabajo normal, las llamadas de las clases hijas a los métodos padre (es decir, los gestores nativos internos reales) devolverán `false` a menos que la sesión haya sido iniciada realmente (automáticamente o explícitamente mediante `session_start`). Es importante considerar esto cuando se escriben unidades de pruebas donde los métodos de la clase podrían ser invocados manualmente.
