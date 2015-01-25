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
au BufRead /tmp/mutt-* set tw=72
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
