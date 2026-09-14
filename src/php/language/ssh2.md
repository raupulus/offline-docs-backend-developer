---
title: ssh2://
description: Shell seguro 2
source_url: https://www.php.net/manual/es/wrappers.ssh2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/ssh2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 8bc832a46
order: 4710
---

ssh2://

Shell seguro 2

## Descripción

`ssh2.shell://` `ssh2.exec://` `ssh2.tunnel://` `ssh2.sftp://` `ssh2.scp://` (PECL)

> [!NOTE]
> Para utilizar la envoltura `ssh2://`, la extensión [SSH2](https://pecl.php.net/package/ssh2) disponible en [PECL](https://pecl.php.net/) debe ser instalada.

Además de aceptar las identificaciones tradicionales mediante la URI, la envoltura ssh2 reutilizará las conexiones abiertas pasando la recurso de conexión en la parte host de la URL.

## Uso

- `ssh2.shell://user:pass@example.com:22/xterm`

- `ssh2.exec://user:pass@example.com:22/usr/local/bin/somecmd`

- `ssh2.tunnel://user:pass@example.com:22/192.168.0.1:14`

- `ssh2.sftp://user:pass@example.com:22/path/to/filename`

## Opciones

| Atributo | ssh2.shell | ssh2.exec | ssh2.tunnel | ssh2.sftp | ssh2.scp |
|----|----|----|----|----|----|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen) | Sí | Sí | Sí | Sí | Sí |
| Permite la lectura | Sí | Sí | Sí | Sí | Sí |
| Permite la escritura | Sí | Sí | Sí | Sí | No |
| Permite el añadido | No | No | No | Sí (cuando sea soportado por el servidor) | No |
| Permite la lectura y escritura simultáneamente | Sí | Sí | Sí | Sí | No |
| Soporte de la función `stat` | No | No | No | Sí | No |
| Soporte de la función `unlink` | No | No | No | Sí | No |
| Soporte de la función `rename` | No | No | No | Sí | No |
| Soporte de la función `mkdir` | No | No | No | Sí | No |
| Soporte de la función `rmdir` | No | No | No | Sí | No |

Resumen de la envoltura {role="stream_wrapper"}

| Nombre | Uso | Por omisión |
|----|----|----|
| `session` | recurso ssh2 pre-conectado para reutilizar |  |
| `sftp` | recurso sftp pre-asignado para reutilizar |  |
| `methods` | métodos de intercambio de claves, hostkey, cifrado, compresión y MAC a utilizar |  |
| `callbacks` |  |  |
| `username` | Nombre de usuario para la conexión |  |
| `password` | Contraseña a utilizar durante la identificación por contraseña |  |
| `pubkey_file` | Nombre del archivo que contiene la clave pública a utilizar durante la identificación |  |
| `privkey_file` | Nombre del archivo que contiene la clave privada a utilizar durante la identificación |  |
| `env` | Array asociativo de variables de entorno a definir |  |
| `term` | Tipo de emulación de terminal a solicitar durante la asignación de un pty |  |
| `term_width` | Ancho del terminal a solicitar durante la asignación de un pty |  |
| `term_height` | Alto del terminal a solicitar durante la asignación de un pty |  |
| `term_units` | Unidades a utilizar con term_width y term_height | `SSH2_TERM_UNIT_CHARS` |

Opciones de contexto {role="stream_wrapper"}

## Ejemplos

Apertura de un flujo desde una conexión activa

```php
<?php
$session = ssh2_connect('example.com', 22);
ssh2_auth_pubkey_file($session, 'username', '/home/username/.ssh/id_rsa.pub',
                                            '/home/username/.ssh/id_rsa', 'secret');
$stream = fopen("ssh2.tunnel://$session/remote.example.com:1234", 'r');
?>

   
```

La variable `$session` debe permanecer disponible

Para utilizar la envoltura `ssh2.*://$session`, la variable de recurso `$session` debe ser conservada. El código a continuación no tendrá el efecto deseado:

```php
<?php
$session = ssh2_connect('example.com', 22);
ssh2_auth_pubkey_file($session, 'username', '/home/username/.ssh/id_rsa.pub',
                                            '/home/username/.ssh/id_rsa', 'secret');
$connection_string = "ssh2.sftp://$session/";
unset($session);
$stream = fopen($connection_string . "path/to/file", 'r');
?>

   
```

La función unset() cierra la sesión, ya que la variable `$connection_string` no contiene una referencia a la variable `$session`, sino solo una cadena derivada. Esto también ocurre cuando la función `unset` es implícita, durante una salida del ámbito (como en una función).
