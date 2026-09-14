---
title: Ejemplos
source_url: https://www.php.net/manual/es/ftp.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24330
---

## Ejemplos

## Uso básico

Ejemplo con FTP

```php
<?php
// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Verificación de la conexión
if ((!$ftp) || (!$login_result)) {
    echo "¡La conexión FTP ha fallado!";
    echo "Intento de conexión al servidor $ftp_server para el usuario $ftp_user_name";
    exit;
} else {
    echo "Conexión al servidor $ftp_server, para el usuario $ftp_user_name";
}

// Carga de un fichero
$upload = ftp_put($ftp, $destination_file, $source_file, FTP_BINARY);

// Verificación del estado de la carga
if (!$upload) {
    echo "¡La carga FTP ha fallado!";
} else {
    echo "Carga de $source_file hacia $ftp_server como $destination_file";
}

// Cierre de la conexión FTP
ftp_close($ftp);
?>

    
```
