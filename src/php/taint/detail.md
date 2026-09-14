---
title: Más detalles
source_url: https://www.php.net/manual/es/taint.detail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/taint/detail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: taint
translation_status: ready
translation_reviewed: false
translation_revision: 4de6d1256
order: 93780
---

## Más detalles

## Funciones y sentencias que propagarán la marca de corrupción de una cadena corrupta

| Función/Sentencia                    | Desde |
|--------------------------------------|-------|
| = (asignación)                       | 0.1.0 |
| . (concatenación)                    | 0.1.0 |
| "{\$var}" (sustitución de variables) | 0.1.0 |
| .= (concatenación de asignación)     | 0.1.0 |
| strval                               | 0.3.0 |
| explode/split                        | 0.3.0 |
| implode/join                         | 0.3.0 |
| sprintf                              | 0.3.0 |
| vsprintf                             | 0.3.0 |
| trim                                 | 0.4.0 |
| rtrim                                | 0.4.0 |
| ltrim                                | 0.4.0 |
| strstr                               | 0.5.0 |
| str_pad                              | 0.5.0 |
| str_replace                          | 0.5.0 |
| substr                               | 0.5.0 |
| strtolower                           | 0.5.0 |
| strtoupper                           | 0.5.0 |

## Funciones y sentencias que comprobarán cadenas corrompidas

<table>
<thead>
<tr>
<th>Función/Sentencia</th>
<th>Desde</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Sentencias básicas</td>
</tr>
<tr>
<td>eval</td>
<td>0.1.0</td>
</tr>
<tr>
<td>include/include_once</td>
<td>0.1.0</td>
</tr>
<tr>
<td>require/require_once</td>
<td>0.1.0</td>
</tr>
<tr>
<td colspan="2">Funciones de salida</td>
</tr>
<tr>
<td>echo</td>
<td>0.1.0</td>
</tr>
<tr>
<td>print</td>
<td>0.1.0</td>
</tr>
<tr>
<td>printf</td>
<td>0.1.0</td>
</tr>
<tr>
<td>file_put_contents</td>
<td>0.1.0</td>
</tr>
<tr>
<td colspan="2">Funciones del sistema de ficheros</td>
</tr>
<tr>
<td>fopen</td>
<td>0.2.0</td>
</tr>
<tr>
<td>opendir</td>
<td>0.2.0</td>
</tr>
<tr>
<td>basename</td>
<td>0.2.0</td>
</tr>
<tr>
<td>dirname</td>
<td>0.2.0</td>
</tr>
<tr>
<td>file</td>
<td>0.2.0</td>
</tr>
<tr>
<td>pathinfo</td>
<td>0.2.0</td>
</tr>
<tr>
<td colspan="2">Funciones relacionadas con bases de datos</td>
</tr>
<tr>
<td>mysql_query</td>
<td>0.2.0</td>
</tr>
<tr>
<td>mysqli_query/MySQLi::query</td>
<td>0.2.0</td>
</tr>
<tr>
<td>sqlite_query/SqliteDataBase::query</td>
<td>0.3.0</td>
</tr>
<tr>
<td>sqlite_single_query/SqliteDataBase::singleQuery</td>
<td>0.3.0</td>
</tr>
<tr>
<td>oci_parse</td>
<td>0.3.0</td>
</tr>
<tr>
<td>PDO::query</td>
<td>0.3.0</td>
</tr>
<tr>
<td>PDO::prepare</td>
<td>0.3.0</td>
</tr>
<tr>
<td>SQLite3::query</td>
<td>2.0.1</td>
</tr>
<tr>
<td>SQLite3::prepare</td>
<td>2.0.1</td>
</tr>
<tr>
<td colspan="2">Funciones relacionadas con la línea de comandos</td>
</tr>
<tr>
<td>system</td>
<td>0.1.0</td>
</tr>
<tr>
<td>exec</td>
<td>0.1.0</td>
</tr>
<tr>
<td>proc_open</td>
<td>0.1.0</td>
</tr>
<tr>
<td>passthru</td>
<td>0.1.0</td>
</tr>
<tr>
<td>shell_exec</td>
<td>0.3.0</td>
</tr>
</tbody>
</table>

## Funciones que sanean cadenas corruptas

| Función                                              | Desde |
|------------------------------------------------------|-------|
| addslashes                                           | 0.1.0 |
| addcslashes                                          | 0.1.0 |
| htmlspecialchars                                     | 0.1.0 |
| htmlentities                                         | 0.1.0 |
| escapeshellcmd                                       | 0.1.0 |
| mysql_escape_string                                  | 0.1.0 |
| mysql_real_escape_string                             | 0.1.0 |
| mysqli_escape_string/MySQLi::escape_string           | 0.1.0 |
| mysqli_real_escape_string/MySQLi::real_escape_string | 0.1.0 |
| sqlite_escape_string/SqliteDataBase::escapeString    | 0.3.0 |
| PDO::quote                                           | 0.3.0 |
