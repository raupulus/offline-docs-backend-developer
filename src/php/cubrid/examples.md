---
title: Ejemplos
source_url: https://www.php.net/manual/es/cubrid.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 8850
---

## Ejemplos

El siguiente es un ejemplo sencillo que establece una conexión entre PHP y CUBRID. Esta conexión cubrirá la características más básicas y significativas. El siguiente código requiere conectarse a una base de datos CUBRID, lo que significa que CUBRID Server (servidor) y CUBRID Broker (agente) tienen que estar ejecutándose.

El ejemplo de abajo usa la base de datos demodb de ejemplo. Por defecto se crea durante la instalación. Asegúrese de que ha sido creada.

Ejemplo de Recuperación de Datos

```php
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=euc-kr">
    </head>
    <body>
    <center>
    <table border=2>
    <?php
        /**
         * Establecer la información para conexión de CUBRID. ip_host es la direccion
         * IP donde el Agente de CUBRID está instalado (localhost en este
         * ejemplo), y puerto_host es el número de puerto del Agente de CUBRID.
         * El número de puerto es el predeterminado dado durante la instalación.
         * Para más detalles, véase "Guía del Administrador."
         */
        $ip_host = "localhost";
        $puerto_host = 33000;
        $nombre_bd = "demodb";
        /**
         * Conectar al Servidor CUBRID. No realiza la conexión,
         * sólo conserva la información de ésta. La razón de no realizar
         * la conexión actual es manejar la transacción de forma más eficaz
         * en la arquitectura de 3 capas.
         */
        $cubrid_con = @cubrid_connect($ip_host, $puerto_host, $nombre_bd);

        if (!$cubrid_con) {
            echo "Error de Conexión con la Base de Datos";
            exit;
        }
    ?>
    <?php
        $sql = "select sports, count(players) as players from event group by sports";
        /**
         * Solicitar al Servidor CUBRID los resultados de la declaración SQL.
         * Ahora se hace la conexión actual al Servidor CUBRID.
         */
        $resultado = cubrid_execute($cubrid_con, $sql);

        if ($resultado) {
            /**
             * Obtener el nombre de las columnas del conjunto de resultados creado por la consulta SQL.
             */
            $columnas = cubrid_column_names($resultado);
            /**
             * Obtener el número de columnas del conjunto de resultados creado por la consulta SQL.
             */
            $número_campos = cubrid_num_cols($resultado);
            /**
             * Listar los nombres de las columnas del conjunto de resultados por la pantalla.
             */
            echo "<tr>";

            while (list($clave, $nomcol) = each($columnas)) {
                echo "<td align=center>$nomcol</td>";
            }

            echo "</tr>";

            /**
             * Obtener los resultados del conjunto de resultados.
             */
            while ($fila = cubrid_fetch($resultado)) {
                echo "<tr>";

                for ($i = 0; $i < $número_campos; $i++) {
                    echo "<td align=center>";
                    echo $fila[$i];
                    echo "</td>";
                }

                echo "</tr>";
            }
        }
        /**
         * El módulo de PHP en CUBRID se ejecuta en una arquitectura de 3 capas. Incluso cuando
         * se llama a SELECT para el procesamiento de la transacción, es pasado como parte
         * de la transacción. Por lo tanto, la transacción necesita ser reiniciada
         * llamando a commit o incluso cuando se llamó a SELECT para un rendimiento
         * pulido.
         */
        cubrid_commit($cubrid_con);
        cubrid_disconnect($cubrid_con);
    ?>
    </body>
    </html>
    
  
```

Ejemplo de Inserción de Datos

```php
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=euc- kr">
    </head>
    <body>
    <center>
    <table border=2>
    <?php
        /**
         * ip_host es la dirección IP de donde está instalado el Agente de CUBRID
         * puerto_host es el número de puerto del Agente de CUBRID
         * nombre_bd es el nombre de la Base de Datos de CUBRID
         */
        $ip_host = "localhost";
        $puerto_host = 33000;
        $nombre_bd = "demodb";
        $cubrid_con = @cubrid_connect($ip_host, $puerto_host, $nombre_bd);

        if (!$cubrid_con) {
            echo "Error en la Conexión a la Base de Datos";
            exit;
        }
    ?>
    <?php
        $sql = "insert into olympic (host_year,host_nation,host_city,"
            . "opening_date,closing_date) values (2008, 'China', 'Beijing',"
            . "to_date('08-08-2008','mm-dd- yyyy'),to_date('08-24-2008','mm-dd-yyyy')) ;";
        $resultado = cubrid_execute($cubrid_con, $sql);
        if ($resultado) {
            /**
             * Manejado con éxito, por lo que se envía.
             */
            cubrid_commit($cubrid_con);
            echo "Insertado con éxito";
        } else {
            /**
             * Ocurrió un error, por lo que el mensaje de error se imprime y se llama a rollback.
             */
            echo cubrid_error_msg();
            cubrid_rollback($cubrid_con);
        }
        cubrid_disconnect($cubrid_con);
    ?>
    </body>
    </html>
    
  
```
