---
title: Instalación
source_url: https://www.php.net/manual/es/dba.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11480
---

## Instalación

Al utilizar la opción de compilación `--enable-dba=shared`, puede compilarse un módulo dinámico que active el soporte de las bases de datos de estilo DBM para PHP. Asimismo, debe añadirse el soporte de al menos uno de los siguientes gestores, especificando la opción de configuración `--with-XXXX` o `--enable-XXXX` durante la configuración de PHP.

> [!WARNING]
> Tras configurar y compilar PHP, deben ejecutarse las siguientes pruebas desde la línea de comandos: `php run-tests.php ext/dba`. Esto muestra si la combinación de controladores funciona. Los más problemáticos son `dbm` y `ndbm` que entran en conflicto con numerosas instalaciones. Esto se debe a que en muchos sistemas, estas bibliotecas forman parte de más de una biblioteca. La prueba de configuración impide simplemente configurar descriptores cuya combinación es defectuosa aunque funcionen correctamente por separado.

<table>
<caption>Gestores DBA soportados</caption>
<thead>
<tr>
<th>Gestor</th>
<th>Opción de configuración</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>dbm</code></td>
<td><p>Para activar el soporte de dbm, añada la opción de compilación <code role="configure">--with-dbm[=DIR]</code>.</p>

&#10;</div>
<p>dbm es una sobrecarga que suele dar lugar a fallos. Por tanto, solo debe utilizarse dbm si se está seguro de que funciona y se necesita este formato.</p>
</div></td>
</tr>
<tr>
<td><code>ndbm</code></td>
<td><p>Para activar el soporte de ndbm, añada la opción de compilación <code role="configure">--with-ndbm[=DIR]</code>.</p>

&#10;</div>
<p>ndbm es una sobrecarga que suele dar lugar a fallos. Por tanto, solo debe utilizarse ndbm si se está seguro de que funciona y se necesita este formato.</p>
</div></td>
</tr>
<tr>
<td><code>gdbm</code></td>
<td>Para activar el soporte de gdbm, añada la opción de compilación <code role="configure">--with-gdbm[=DIR]</code>.</td>
</tr>
<tr>
<td><code>db2</code></td>
<td><p>Para activar el soporte de Oracle Berkeley DB 2, añada la opción de compilación <code role="configure">--with-db2[=DIR]</code>.</p>

&#10;</div>
<p>db2 entra en conflicto con db3 y db4.</p>
</div></td>
</tr>
<tr>
<td><code>db3</code></td>
<td><p>Para activar el soporte de Oracle Berkeley DB 3, añada la opción de compilación <code role="configure">--with-db3[=DIR]</code>.</p>

&#10;</div>
<p>db3 entra en conflicto con db2 y db4.</p>
</div></td>
</tr>
<tr>
<td><code>db4</code></td>
<td><p>Para activar el soporte de Oracle Berkeley DB 4, añada la opción de compilación <code role="configure">--with-db4[=DIR]</code>.</p>

&#10;</div>
<p>db4 entra en conflicto con db2 y db3.</p>

&#10;</div>
<p>Las bibliotecas db con versiones comprendidas entre 4.1 y 4.1.24 no pueden utilizarse con ninguna versión de PHP.</p>
<p>El soporte DB5 se añadió en PHP 5.3.3.</p>
</div></td>
</tr>
<tr>
<td><code>cdb</code></td>
<td><p>Para activar el soporte de cdb, añada la opción de compilación <code role="configure">--with-cdb[=DIR]</code>.</p>

&#10;</div>
<p>Puede omitirse el uso de DIR, para aprovechar la biblioteca cdb proporcionada con PHP, que añade un gestor cdb_make, permite la creación de fichero cdb y permite el acceso a los ficheros cbd a través de la red con los flujos de PHP.</p>
</div></td>
</tr>
<tr>
<td><code>flatfile</code></td>
<td><p>Para activar el soporte de ficheros, añada la opción de compilación <code role="configure">--enable-flatfile</code>. Anteriormente a PHP 5.2.1 debía utilizarse la opción <code role="configure">--with-flatfile</code> en su lugar.</p>

&#10;</div>
<p>Esto se añadió para asegurar la compatibilidad con la extensión <code>dbm</code> que está obsoleta. Úsese este gestor solo cuando no pueda instalarse ningún otro gestor y no pueda utilizarse el gestor cdb integrado.</p>
</div></td>
</tr>
<tr>
<td><code>inifile</code></td>
<td><p>Para activar el soporte de <code>inifile</code>, añada la opción de compilación <code role="configure">--enable-inifile</code>. Anteriormente a PHP 5.2.1 debía utilizarse la opción <code role="configure">--with-inifile</code> en su lugar.</p>

&#10;</div>
<p>Esta opción se añadió para permitir leer y escribir en ficheros de inicialización de tipo Microsoft (<code>.ini</code>), como el <code>php.ini</code> por ejemplo.</p>
</div></td>
</tr>
<tr>
<td><code>qdbm</code></td>
<td><p>Para activar el soporte de qdbm, añada la opción de compilación <code role="configure">--with-qdbm[=DIR]</code>.</p>

&#10;</div>
<p>qdbm entra en conflicto con dbm y gdbm.</p>

&#10;</div>
<p>La biblioteca qdbm puede descargarse desde <a href="http://fallabs.com/qdbm/index.html">http://fallabs.com/qdbm/index.html</a>.</p>
</div></td>
</tr>
<tr>
<td><code>tcadb</code></td>
<td><p>Para activar el soporte de Tokyo Cabinet, añada la opción de compilación <code role="configure">--with-tcadb[=DIR]</code>.</p>

&#10;</div>
<p>La biblioteca Tokyo Cabinet puede ser descargada desde <a href="http://fallabs.com/tokyocabinet/">http://fallabs.com/tokyocabinet/</a>.</p>
</div></td>
</tr>
<tr>
<td><code>lmdb</code></td>
<td><p>Para activar el soporte de Lightning Memory-Mapped Database añada la opción de configuración <code role="configure">--with-lmdb[=DIR]</code>.</p>

&#10;</div>
<p>Esto se añadió en PHP 7.2.0. La biblioteca Lightning Memory-Mapped Database puede descargarse desde <a href="https://symas.com/lmdb/">https://symas.com/lmdb/</a>.</p>
</div></td>
</tr>
</tbody>
</table>
