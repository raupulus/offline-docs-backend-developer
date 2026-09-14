---
title: A Programmable Completion Example
source_url: https://www.gnu.org/software/bash/manual
source_path: 047-a-programmable-completion-example.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 470
---

## A Programmable Completion Example

The most common way to obtain additional completion functionality beyond the default actions `complete` and `compgen` provide is to use a shell function and bind it to a particular command using `complete -F`.

The following function provides completions for the `cd` builtin. It is a reasonably good example of what shell functions must do when used for completion. This function uses the word passed as `$2` to determine the directory name to complete. You can also use the `COMP_WORDS` array variable; the current word is indexed by the `COMP_CWORD` variable.

The function relies on the `complete` and `compgen` builtins to do much of the work, adding only the things that the Bash `cd` does beyond accepting basic directory names: tilde expansion (see [Tilde Expansion](#Tilde-Expansion)), searching directories in \<\$CDPATH\>, which is described above (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)), and basic support for the `cdable_vars` shell option (see [The Shopt Builtin](#The-Shopt-Builtin)). `_comp_cd` modifies the value of \<IFS\> so that it contains only a newline to accommodate file names containing spaces and tabs – `compgen` prints the possible completions it generates one per line.

Possible completions go into the \<COMPREPLY\> array variable, one completion per array element. The programmable completion system retrieves the completions from there when the function returns.

    # A completion function for the cd builtin
    # based on the cd completion function from the bash_completion package
    _comp_cd()
    {
        local IFS=$' \t\n'    # normalize IFS
        local cur _skipdot _cdpath
        local i j k

        # Tilde expansion, which also expands tilde to full pathname
        case "$2" in
        \~*)    eval cur="$2" ;;
        *)      cur=$2 ;;
        esac

        # no cdpath or absolute pathname -- straight directory completion
        if [[ -z "${CDPATH:-}" ]] || [[ "$cur" == @(./*|../*|/*) ]]; then
            # compgen prints paths one per line; could also use while loop
            IFS=$'\n'
            COMPREPLY=( $(compgen -d -- "$cur") )
            IFS=$' \t\n'
        # CDPATH+directories in the current directory if not in CDPATH
        else
            IFS=$'\n'
            _skipdot=false
            # preprocess CDPATH to convert null directory names to .
            _cdpath=${CDPATH/#:/.:}
            _cdpath=${_cdpath//::/:.:}
            _cdpath=${_cdpath/%:/:.}
            for i in ${_cdpath//:/$'\n'}; do
                if [[ $i -ef . ]]; then _skipdot=true; fi
                k="${#COMPREPLY[@]}"
                for j in $( compgen -d -- "$i/$cur" ); do
                    COMPREPLY[k++]=${j#$i/}        # cut off directory
                done
            done
            $_skipdot || COMPREPLY+=( $(compgen -d -- "$cur") )
            IFS=$' \t\n'
        fi

        # variable names if appropriate shell option set and no completions
        if shopt -q cdable_vars && [[ ${#COMPREPLY[@]} -eq 0 ]]; then
            COMPREPLY=( $(compgen -v -- "$cur") )
        fi

        return 0
    }

We install the completion function using the `-F` option to `complete`:

    # Tell readline to quote appropriate and append slashes to directories;
    # use the bash default completion for other arguments
    complete -o filenames -o nospace -o bashdefault -F _comp_cd cd

Since we’d like Bash and Readline to take care of some of the other details for us, we use several other options to tell Bash and Readline what to do. The `-o filenames` option tells Readline that the possible completions should be treated as filenames, and quoted appropriately. That option will also cause Readline to append a slash to filenames it can determine are directories (which is why we might want to extend `_comp_cd` to append a slash if we’re using directories found via \<CDPATH\>: Readline can’t tell those completions are directories). The `-o nospace` option tells Readline to not append a space character to the directory name, in case we want to append to it. The `-o bashdefault` option brings in the rest of the “Bash default” completions – possible completions that Bash adds to the default Readline set. These include things like command name completion, variable completion for words beginning with ‘`$`’ or ‘`${`’, completions containing pathname expansion patterns (see [Filename Expansion](#Filename-Expansion)), and so on.

Once installed using `complete`, `_comp_cd` will be called every time we attempt word completion for a `cd` command.

Many more examples – an extensive collection of completions for most of the common GNU, Unix, and Linux commands – are available as part of the bash_completion project. This is installed by default on many GNU/Linux distributions. Originally written by Ian Macdonald, the project now lives at <https://github.com/scop/bash-completion/>. There are ports for other systems such as Solaris and Mac OS X.

An older version of the bash_completion package is distributed with bash in the `examples/complete` subdirectory.

History, how to use
