---
title: Programmable Completion Builtins
source_url: https://www.gnu.org/software/bash/manual
source_path: 046-programmable-completion-builtins.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 460
---

## Programmable Completion Builtins

completion builtins

Three builtin commands are available to manipulate the programmable completion facilities: one to specify how the arguments to a particular command are to be completed, and two to modify the completion as it is happening.

`compgen`  

compgen

    compgen [-V varname] [option] [word]

Generate possible completion matches for \<word\> according to the \<option\>s, which may be any option accepted by the `complete` builtin with the exceptions of `-p`, `-r`, `-D`, `-E`, and `-I`, and write the matches to the standard output.

If the `-V` option is supplied, `compgen` stores the generated completions into the indexed array variable \<varname\> instead of writing them to the standard output.

When using the `-F` or `-C` options, the various shell variables set by the programmable completion facilities, while available, will not have useful values.

The matches will be generated in the same way as if the programmable completion code had generated them directly from a completion specification with the same flags. If \<word\> is specified, only those completions matching \<word\> will be displayed or stored.

The return value is true unless an invalid option is supplied, or no matches were generated.

`complete`  

complete

    complete [-abcdefgjksuv] [-o comp-option] [-DEI] [-A action]
    [-G globpat] [-W wordlist] [-F function] [-C command]
    [-X filterpat] [-P prefix] [-S suffix] name [name …]
    complete -pr [-DEI] [name …]

Specify how arguments to each \<name\> should be completed.

If the `-p` option is supplied, or if no options or \<name\>s are supplied, print existing completion specifications in a way that allows them to be reused as input. The `-r` option removes a completion specification for each \<name\>, or, if no \<name\>s are supplied, all completion specifications.

The `-D` option indicates that other supplied options and actions should apply to the “default” command completion; that is, completion attempted on a command for which no completion has previously been defined. The `-E` option indicates that other supplied options and actions should apply to “empty” command completion; that is, completion attempted on a blank line. The `-I` option indicates that other supplied options and actions should apply to completion on the initial non-assignment word on the line, or after a command delimiter such as ‘`;`’ or ‘`|`’, which is usually command name completion. If multiple options are supplied, the `-D` option takes precedence over `-E`, and both take precedence over `-I`. If any of `-D`, `-E`, or `-I` are supplied, any other \<name\> arguments are ignored; these completions only apply to the case specified by the option.

The process of applying these completion specifications when word completion is attempted is described above (see [Programmable Completion](#Programmable-Completion)).

Other options, if specified, have the following meanings. The arguments to the `-G`, `-W`, and `-X` options (and, if necessary, the `-P` and `-S` options) should be quoted to protect them from expansion before the `complete` builtin is invoked.

`-o comp-option`  
The \<comp-option\> controls several aspects of the compspec’s behavior beyond the simple generation of completions. \<comp-option\> may be one of:

`bashdefault`  
Perform the rest of the default Bash completions if the compspec generates no matches.

`default`  
Use Readline’s default filename completion if the compspec generates no matches.

`dirnames`  
Perform directory name completion if the compspec generates no matches.

`filenames`  
Tell Readline that the compspec generates filenames, so it can perform any filename-specific processing (such as adding a slash to directory names, quoting special characters, or suppressing trailing spaces). This option is intended to be used with shell functions specified with `-F`.

`fullquote`  
Tell Readline to quote all the completed words even if they are not filenames.

`noquote`  
Tell Readline not to quote the completed words if they are filenames (quoting filenames is the default).

`nosort`  
Tell Readline not to sort the list of possible completions alphabetically.

`nospace`  
Tell Readline not to append a space (the default) to words completed at the end of the line.

`plusdirs`  
After generating any matches defined by the compspec, attempt directory name completion and add any matches to the results of the other actions.

`-A action`  
The \<action\> may be one of the following to generate a list of possible completions:

`alias`  
Alias names. May also be specified as `-a`.

`arrayvar`  
Array variable names.

`binding`  
Readline key binding names (see [Bindable Readline Commands](#Bindable-Readline-Commands)).

`builtin`  
Names of shell builtin commands. May also be specified as `-b`.

`command`  
Command names. May also be specified as `-c`.

`directory`  
Directory names. May also be specified as `-d`.

`disabled`  
Names of disabled shell builtins.

`enabled`  
Names of enabled shell builtins.

`export`  
Names of exported shell variables. May also be specified as `-e`.

`file`  
File and directory names, similar to Readline’s filename completion. May also be specified as `-f`.

`function`  
Names of shell functions.

`group`  
Group names. May also be specified as `-g`.

`helptopic`  
Help topics as accepted by the `help` builtin (see [Bash Builtins](#Bash-Builtins)).

`hostname`  
Hostnames, as taken from the file specified by the `HOSTFILE` shell variable (see [Bash Variables](#Bash-Variables)).

`job`  
Job names, if job control is active. May also be specified as `-j`.

`keyword`  
Shell reserved words. May also be specified as `-k`.

`running`  
Names of running jobs, if job control is active.

`service`  
Service names. May also be specified as `-s`.

`setopt`  
Valid arguments for the `-o` option to the `set` builtin (see [The Set Builtin](#The-Set-Builtin)).

`shopt`  
Shell option names as accepted by the `shopt` builtin (see [Bash Builtins](#Bash-Builtins)).

`signal`  
Signal names.

`stopped`  
Names of stopped jobs, if job control is active.

`user`  
User names. May also be specified as `-u`.

`variable`  
Names of all shell variables. May also be specified as `-v`.

`-C command`  
\<command\> is executed in a subshell environment, and its output is used as the possible completions. Arguments are passed as with the `-F` option.

`-F function`  
The shell function \<function\> is executed in the current shell environment. When it is executed, the first argument (\$1) is the name of the command whose arguments are being completed, the second argument (\$2) is the word being completed, and the third argument (\$3) is the word preceding the word being completed, as described above (see [Programmable Completion](#Programmable-Completion)). When `function` finishes, programmable completion retrieves the possible completions from the value of the `COMPREPLY` array variable.

`-G globpat`  
Expand the filename expansion pattern \<globpat\> to generate the possible completions.

`-P prefix`  
Add \<prefix\> to the beginning of each possible completion after all other options have been applied.

`-S suffix`  
Append \<suffix\> to each possible completion after all other options have been applied.

`-W wordlist`  
Split the \<wordlist\> using the characters in the `IFS` special variable as delimiters, and expand each resulting word. Shell quoting is honored within \<wordlist\> in order to provide a mechanism for the words to contain shell metacharacters or characters in the value of `IFS`. The possible completions are the members of the resultant list which match a prefix of the word being completed.

`-X filterpat`  
\<filterpat\> is a pattern as used for filename expansion. It is applied to the list of possible completions generated by the preceding options and arguments, and each completion matching \<filterpat\> is removed from the list. A leading ‘`!`’ in \<filterpat\> negates the pattern; in this case, any completion not matching \<filterpat\> is removed.

The return value is true unless an invalid option is supplied, an option other than `-p`, `-r`, `-D`, `-E`, or `-I` is supplied without a \<name\> argument, an attempt is made to remove a completion specification for a \<name\> for which no specification exists, or an error occurs adding a completion specification.

`compopt`  

compopt

    compopt [-o option] [-DEI] [+o option] [name]

Modify completion options for each \<name\> according to the \<option\>s, or for the currently-executing completion if no \<name\>s are supplied. If no \<option\>s are given, display the completion options for each \<name\> or the current completion. The possible values of \<option\> are those valid for the `complete` builtin described above.

The `-D` option indicates that other supplied options should apply to the “default” command completion; the `-E` option indicates that other supplied options should apply to “empty” command completion; and the `-I` option indicates that other supplied options should apply to completion on the initial word on the line. These are determined in the same way as the `complete` builtin.

If multiple options are supplied, the `-D` option takes precedence over `-E`, and both take precedence over `-I`

The return value is true unless an invalid option is supplied, an attempt is made to modify the options for a \<name\> for which no completion specification exists, or an output error occurs.
