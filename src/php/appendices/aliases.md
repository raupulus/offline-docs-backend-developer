---
title: Lista de alias
source_url: https://www.php.net/manual/es/aliases.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/aliases.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: e2274fb29
order: 20
---

## Lista de alias

Hay muchas funciones en PHP que pueden ser llamadas bajo diferentes nombres. En la mayoría de los casos, no hay un nombre preferido sobre otro, `is_int` y `is_integer` son exactamente idénticos, por ejemplo. Estos cambios de nombres se han realizado generalmente debido a un cambio en la API original o por otras razones y los antiguos nombres se conservan únicamente por razones de compatibilidad ascendente. Es una muy mala práctica utilizar estos alias, ya que pueden desaparecer en cualquier momento, quedar obsoletos sin previo aviso, o simplemente cambiar de nombre, lo que hace que el script sea inutilizable con versiones más recientes de PHP. Siempre se deben preferir las versiones oficiales. De hecho, esta lista está destinada principalmente a aquellos que deben actualizar sus scripts con las sintaxis más recientes.

| Alias | Nombre canónico de la función | Extensión madre |
|----|----|----|
| \_ | `gettext` | [Gettext](#ref.gettext) |
| chop | `rtrim` | Sintaxis base |
| close | `closedir` | Sintaxis base |
| com_get | `com_propget` | [COM](#ref.com) |
| com_propset | `com_propput` | [COM](#ref.com) |
| com_set | `com_propput` | [COM](#ref.com) |
| die | `exit` | [Funciones varias](#ref.misc) |
| diskfreespace | `disk_free_space` | [Filesystem](#ref.filesystem) |
| doubleval | `floatval` | Sintaxis base |
| fputs | `fwrite` | Sintaxis base |
| gzputs | `gzwrite` | [Zlib](#ref.zlib) |
| i18n_convert | `mb_convert_encoding` | [Multi-bytes Strings](#ref.mbstring) |
| i18n_discover_encoding | `mb_detect_encoding` | [Multi-bytes Strings](#ref.mbstring) |
| i18n_http_input | `mb_http_input` | [Multi-bytes Strings](#ref.mbstring) |
| i18n_http_output | `mb_http_output` | [Multi-bytes Strings](#ref.mbstring) |
| i18n_internal_encoding | `mb_internal_encoding` | [Multi-bytes Strings](#ref.mbstring) |
| i18n_ja_jp_hantozen | `mb_convert_kana` | [Multi-bytes Strings](#ref.mbstring) |
| i18n_mime_header_decode | `mb_decode_mimeheader` | [Multi-bytes Strings](#ref.mbstring) |
| i18n_mime_header_encode | `mb_encode_mimeheader` | [Multi-bytes Strings](#ref.mbstring) |
| imap_create | `imap_createmailbox` | [IMAP](#ref.imap) |
| imap_fetchtext | `imap_body` | [IMAP](#ref.imap) |
| imap_header | `imap_headerinfo` | [IMAP](#ref.imap) |
| imap_listmailbox | `imap_list` | [IMAP](#ref.imap) |
| imap_listsubscribed | `imap_lsub` | [IMAP](#ref.imap) |
| imap_rename | `imap_renamemailbox` | [IMAP](#ref.imap) |
| imap_scan | `imap_listscan` | [IMAP](#ref.imap) |
| imap_scanmailbox | `imap_listscan` | [IMAP](#ref.imap) |
| ini_alter | `ini_set` | Sintaxis base |
| is_double | `is_float` | Sintaxis base |
| is_integer | `is_int` | Sintaxis base |
| is_long | `is_int` | Sintaxis base |
| is_real | `is_float` | Sintaxis base |
| is_writeable | `is_writable` | Sintaxis base |
| join | `implode` | Sintaxis base |
| key_exists | `array_key_exists` | Sintaxis base |
| ldap_close | `ldap_unbind` | [LDAP](#ref.ldap) |
| mbstrcut | `mb_strcut` | [Multi-bytes Strings](#ref.mbstring) |
| mbstrlen | `mb_strlen` | [Multi-bytes Strings](#ref.mbstring) |
| mbstrpos | `mb_strpos` | [Multi-bytes Strings](#ref.mbstring) |
| mbstrrpos | `mb_strrpos` | [Multi-bytes Strings](#ref.mbstring) |
| mbsubstr | `mb_substr` | [Multi-bytes Strings](#ref.mbstring) |
| mysql | `mysql_db_query` | [MySQL](#ref.mysql) |
| mysql_createdb | `mysql_create_db` | [MySQL](#ref.mysql) |
| mysql_db_name | `mysql_result` | [MySQL](#ref.mysql) |
| mysql_dbname | `mysql_result` | [MySQL](#ref.mysql) |
| mysql_dropdb | `mysql_drop_db` | [MySQL](#ref.mysql) |
| mysql_fieldflags | `mysql_field_flags` | [MySQL](#ref.mysql) |
| mysql_fieldlen | `mysql_field_len` | [MySQL](#ref.mysql) |
| mysql_fieldname | `mysql_field_name` | [MySQL](#ref.mysql) |
| mysql_fieldtable | `mysql_field_table` | [MySQL](#ref.mysql) |
| mysql_fieldtype | `mysql_field_type` | [MySQL](#ref.mysql) |
| mysql_freeresult | `mysql_free_result` | [MySQL](#ref.mysql) |
| mysql_listdbs | `mysql_list_dbs` | [MySQL](#ref.mysql) |
| mysql_listfields | `mysql_list_fields` | [MySQL](#ref.mysql) |
| mysql_listtables | `mysql_list_tables` | [MySQL](#ref.mysql) |
| mysql_numfields | `mysql_num_fields` | [MySQL](#ref.mysql) |
| mysql_numrows | `mysql_num_rows` | [MySQL](#ref.mysql) |
| mysql_selectdb | `mysql_select_db` | [MySQL](#ref.mysql) |
| mysql_tablename | `mysql_result` | [MySQL](#ref.mysql) |
| ociassignelem | [OCICollection::assignElem](#ocicollection.assignelem) | [OCI8](#ref.oci8) |
| ocibindbyname | `oci_bind_by_name` | [OCI8](#ref.oci8) |
| ocicancel | `oci_cancel` | [OCI8](#ref.oci8) |
| ocicloselob | [OCILob::close](#ocilob.close) | [OCI8](#ref.oci8) |
| ocicollappend | [OCICollection::append](#ocicollection.append) | [OCI8](#ref.oci8) |
| ocicollassign | [OCICollection::assign](#ocicollection.assign) | [OCI8](#ref.oci8) |
| ocicollmax | [OCICollection::max](#ocicollection.max) | [OCI8](#ref.oci8) |
| ocicollsize | [OCICollection::size](#ocicollection.size) | [OCI8](#ref.oci8) |
| ocicolltrim | [OCICollection::trim](#ocicollection.trim) | [OCI8](#ref.oci8) |
| ocicolumnisnull | `oci_field_is_null` | [OCI8](#ref.oci8) |
| ocicolumnname | `oci_field_name` | [OCI8](#ref.oci8) |
| ocicolumnprecision | `oci_field_precision` | [OCI8](#ref.oci8) |
| ocicolumnscale | `oci_field_scale` | [OCI8](#ref.oci8) |
| ocicolumnsize | `oci_field_size` | [OCI8](#ref.oci8) |
| ocicolumntype | `oci_field_type` | [OCI8](#ref.oci8) |
| ocicolumntyperaw | `oci_field_type_raw` | [OCI8](#ref.oci8) |
| ocicommit | `oci_commit` | [OCI8](#ref.oci8) |
| ocidefinebyname | `oci_define_by_name` | [OCI8](#ref.oci8) |
| ocierror | `oci_error` | [OCI8](#ref.oci8) |
| ociexecute | `oci_execute` | [OCI8](#ref.oci8) |
| ocifetch | `oci_fetch` | [OCI8](#ref.oci8) |
| ocifetchinto | `oci_fetch_array`, `oci_fetch_row`, `oci_fetch_assoc`, `oci_fetch_object` | [OCI8](#ref.oci8) |
| ocifetchstatement | `oci_fetch_all` | [OCI8](#ref.oci8) |
| ocifreecollection | [OCICollection::free](#ocicollection.free) | [OCI8](#ref.oci8) |
| ocifreecursor | `oci_free_statement` | [OCI8](#ref.oci8) |
| ocifreedesc | `oci_free_descriptor` | [OCI8](#ref.oci8) |
| ocifreestatement | `oci_free_statement` | [OCI8](#ref.oci8) |
| ocigetelem | [OCICollection::getElem](#ocicollection.getelem) | [OCI8](#ref.oci8) |
| ociinternaldebug | `oci_internal_debug` | [OCI8](#ref.oci8) |
| ociloadlob | [OCILob::load](#ocilob.load) | [OCI8](#ref.oci8) |
| ocilogon | `oci_connect` | [OCI8](#ref.oci8) |
| ocinewcollection | `oci_new_collection` | [OCI8](#ref.oci8) |
| ocinewcursor | `oci_new_cursor` | [OCI8](#ref.oci8) |
| ocinewdescriptor | `oci_new_descriptor` | [OCI8](#ref.oci8) |
| ocinlogon | `oci_new_connect` | [OCI8](#ref.oci8) |
| ocinumcols | `oci_num_fields` | [OCI8](#ref.oci8) |
| ociparse | `oci_parse` | [OCI8](#ref.oci8) |
| ocipasswordchange | `oci_password_change` | [OCI8](#ref.oci8) |
| ociplogon | `oci_pconnect` | [OCI8](#ref.oci8) |
| ociresult | `oci_result` | [OCI8](#ref.oci8) |
| ocirollback | `oci_rollback` | [OCI8](#ref.oci8) |
| ocisavelob | [OCILob::save](#ocilob.save) | [OCI8](#ref.oci8) |
| ocisavelobfile | [OCILob::import](#ocilob.import) | [OCI8](#ref.oci8) |
| ociserverversion | `oci_server_version` | [OCI8](#ref.oci8) |
| ocisetprefetch | `oci_set_prefetch` | [OCI8](#ref.oci8) |
| ocistatementtype | `oci_statement_type` | [OCI8](#ref.oci8) |
| ociwritelobtofile | [OCILob::export](#ocilob.export) | [OCI8](#ref.oci8) |
| ociwritetemporarylob | [OCILob::writeTemporary](#ocilob.writetemporary) | [OCI8](#ref.oci8) |
| odbc_do | `odbc_exec` | [ODBC](#ref.uodbc) |
| odbc_field_precision | `odbc_field_len` | [ODBC](#ref.uodbc) |
| pg_clientencoding | `pg_client_encoding` | [PostgreSQL](#ref.pgsql) |
| pg_setclientencoding | `pg_set_client_encoding` | [PostgreSQL](#ref.pgsql) |
| pg_exec | `pg_query` | [PostgreSQL](#ref.pgsql) |
| pos | `current` | Sintaxis base |
| recode | `recode_string` | [Recode](#ref.recode) |
| show_source | `highlight_file` | Sintaxis base |
| sizeof | `count` | Sintaxis base |
| snmpwalkoid | `snmprealwalk` | [SNMP](#ref.snmp) |
| strchr | `strstr` | Sintaxis base |

Alias
