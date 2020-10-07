# Source
YouTube:
    Matering the Vim Language
    How to do 90% of What Plugins do (with just vim)

# Normal mode

All commands work as a word + noun (dw = delete word)

## Words:
`d` delete
`D` delete till the end of a line
`c` change (delete + insert)
`C` change till the end of a line
`>` indenti (works with hjkl operators)
`<` outdent 
`v` visually select
`V` visuall select lines
`y` yank/copy
`Y` yank whole line

## Nouns:
`w` word forward
`b` word backward
`2j` jump 2 ammount of lines
`f_` go to first appearance of character _ in that line
`F_` same thing but backwards
`t_` go to a character before the first appearance of character _ in that line
`T_` same thing but backwards
`/` search for any character, word
`?` same thing but backwards
`m` set mark, eg. mq sets q mark on place where the cursor is
`{}` beggining/end of paragraph
`%` goes to next paren of brackets
`.` repeats the last command executed (whatever it is)
`diw` delete the whole word on which the coursor is on
`di"` delete everything inside the ""
`di]` delete everything inside of []
`dip` delete everythins indside of paragraph
`dit` delete everything inside of a tag eg `<html>___ </html>`
`d'q` delete everyting until the marker q
 same operations work with c, v, y
`daw|"|]` same as diw but with a it captures also the space that follows i
`~` replace case upper --> lower
`gUw` change whole word to uppecrase
`guw` change whole word to lowercase
`gUU` whole line uppercase

## Registers
`"` used to name a registry
`"cyy` yank whole line to registry named "c"
`"cp` paste from "c" registry

## Commands:
`:find <file_name>` finds a file name in the current directory
`:read <file_name>` adds the content of the file to this document
`:ls` lists all files which are currently opened in vim
`:b <part_of_the_filename>` opens that file if it is already opened in vim
`:echo expand(%)` get the name of the currently opened file
`g` at the end of the command means it applies to the whole document
`v` means an NOT to match the given pattern

`ctrl + ]` jump to a definition of a tag
`ctrl + g]` will show all the occurencies of this defined tag 
`ctrl + t` jump back up the tag stack
`ctrl + n` autocompletes a word, n is for next
`ctrl + p` autocompletes a word, p is for previous
`ctrl + x ctrl + n` autocomplete but with words only within this file
`ctrl + x ctrl + f` autocompletes file names, great when path needs to be added to vim file
`ctrl + x ctrl + ]` autocompletes a tag 
`ctrl + w + s` split window horizontally
`ctrl + w + v` split window vertical
`ctrl + w + q` remove split
`ctrl + w + w` move to next window

### Buffers

Buffers are used when more that one files are open within the same Vim
`:ls` show available files in buffer
`:bn` go to next file in buffed
`:bp` go to previous file in buffer
`:b<number>` go to specific buffer
`:b#` go to previous active buffer
`:bd` close current buffer

## Plugin commands

### surround plugin
`ysiwX` surround word with X (.,[]{} whatever)
`cs"'` replace surrunding " with ' if text is already surrounded
`dsX` delete exisitng X surrundings

### comment plugin
`gcc` comment out a line
`gc2j` comment N number of lines below
`gcgc` uncomment adjacent commented lines

### vim-system-copy
`cpiw` copy word to system plugin
`cpi'` copy content inside of '' to system plugin
`cvi'` paste content of system clipboard inside of ''

### vim folding

`zi` switch folding on or off
`za` toggle current fold open/closed
`zc` close current fold
`zR` open all folds
`zM` close all folds
`zv` expand folds to reveal coursor

--- checkout theme groove-box ---
