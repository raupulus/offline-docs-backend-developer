---
title: Ejemplos
source_url: https://www.php.net/manual/es/expect.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/expect/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: expect
translation_status: ready
translation_revision: ca6054f60
order: 20760
---

## Ejemplos

## Ejemplos de uso de Expect

Ejemplo de uso de Expect

Este ejemplo conecta a un host remoto mediante SSH, y muestra el tiempo que lleva en funcionamiento dicho host con uptime.

```php
<?php
ini_set("expect.loguser", "Off");

$stream = fopen("expect://ssh root@remotehost uptime", "r");

$cases = array (
    array (0 => "password:", 1 => PASSWORD)
);

switch (expect_expectl ($stream, $cases)) {
    case PASSWORD:
        fwrite ($stream, "password\n");
        break;

    default:
        die ("Error al tratar de conectar con el host remoto\n");
}

while ($line = fgets($stream)) {
      print $line;
}
fclose ($stream);
?>

   
```

El siguiente ejemplo conecta con un host remoto, determina si el SO instalado es de 32 o de 64 bits, y finalmente actualiza el paquete que corresponda.

Otro ejemplo de uso de Expect

```php
<?php
ini_set("expect.timeout", -1);
ini_set("expect.loguser", "Off");

$stream = expect_popen("ssh root@remotehost");

while (true) {
    switch (expect_expectl ($stream, array (
            array ("password:", PASSWORD), // SSH pide contraseña
            array ("yes/no)?", YESNO), // SSH pide si almacenar o no el host
            array ("~$ ", SHELL, EXP_EXACT), // ¡Hemos conectado!
    ))) {
        case PASSWORD:
            fwrite ($stream, "secret\n");
            break;

        case YESNO:
            fwrite ($stream, "yes\n");
            break;

        case SHELL:
            fwrite ($stream, "uname -a\n");
            while (true) {
                    switch (expect_expectl ($stream, array (
                            array ("~$ ", SHELL, EXP_EXACT), // ¡Hemos conectado!
                            array ("^Linux.*$", UNAME, EXP_REGEXP), // salida de uname -a
                    ), $match)) {
                        case UNAME:
                            $uname .= $match[0];
                            break;

                        case SHELL:
                            // Ejecutar la actualización:
                            if (strstr ($uname, "x86_64")) {
                                    fwrite ($stream, "rpm -Uhv http://mirrorsite/somepath/some_64bit.rpm\n");
                            } else {
                                    fwrite ($stream, "rpm -Uhv http://mirrorsite/somepath/some_32bit.rpm\n");
                            }
                            fwrite ($stream, "exit\n");
                            break 2;

                        case EXP_TIMEOUT:
                        case EXP_EOF:
                            break 2;

                        default:
                            die ("Ha ocurrido un error\n");
                    }
            }
            break 2;

        case EXP_TIMEOUT:
        case EXP_EOF:
            break 2;

        default:
            die ("Ha ocurrido un error\n");
    }
}

fclose ($stream);
?>

   
```
