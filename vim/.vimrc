set vb
filetype plugin indent on 
set nocp
set autoindent
set cindent
set ts=4
set scrolloff=2
set clipboard=unnamedplus
execute pathogen#infect()
syntax on
let g:SuperTabDefaultCompletionType = "context"
let g:jedi#popup_on_dot = 0  " disables the autocomplete to popup whenever you press .
