set nocompatible
filetype off
execute pathogen#infect()
execute pathogen#helptags()
filetype plugin indent on
syntax on
set ruler
set number
set vb
set nocp
set autoindent
set expandtab
set softtabstop=2
set shiftwidth=2
set cindent
set ts=2
set scrolloff=2
set clipboard=unnamedplus
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

set grepprg=grep\ -nH\ $*
let g:tex_flavor = "latex"
" use pdflatex
let g:Tex_DefaultTargetFormat='pdf'
let g:Tex_MultipleCompileFormats='pdf,dvi'
let g:Tex_CompileRule_pdf = 'mkdir -p tmp; pdflatex -output-directory tmp -interaction=nonstopmode $*; cp tmp/*.pdf .'

set cursorline
set colorcolumn=80
highlight ColorColumn ctermbg=darkgrey
"execute "set colorcolumn=" . join(range(80,335), ',')

map <F6> :setlocal spell! spelllang=en_us<CR>
map <F8> :setlocal spell! spelllang=es<CR>
autocmd BufNewFile,BufRead *.tex set spell
autocmd BufNewFile,BufRead *.java set ts=4
autocmd BufNewFile,BufRead *.java set softtabstop=4
autocmd BufNewFile,BufRead *.java set shiftwidth=4

set incsearch
set hlsearch

syntax enable


autocmd StdinReadPre * let s:std_in=1

let g:pymode_rope_lookup_project = 0
let g:pymode_rope = 0
let g:pymode_python = 'python3'
let g:pymode_lint_options_mccabe = {'complexity': 30}
set undofile
set undodir=~/.vim/undodir

let g:pymode_rope=0

set backspace=indent,eol,start
set complete-=i
set smarttab

if &t_Co == 8 && $TERM !~# '^linux'
  set t_Co=16
endif

let g:jedi#force_py_version = 3
let g:calendar_google_calendar = 1
let g:calendar_google_task = 1

" vertical line indentation
let g:indentLine_color_term = 239
let g:indentLine_color_gui = '#09AA08'
let g:indentLine_char = '│'
