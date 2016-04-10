let mapleader = ","
set nocompatible
filetype off
execute pathogen#infect()
execute pathogen#helptags()
filetype plugin indent on
syntax on
set number
set relativenumber
set ruler
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

set cursorline
set colorcolumn=81
highlight ColorColumn ctermbg=darkgrey
highlight SpellBad ctermbg=darkred
"execute "set colorcolumn=" . join(range(80,335), ',')

au BufRead /tmp/mutt-* set tw=72
au BufRead /tmp/mutt-* set spell
au BufRead /tmp/mutt-* set cursorline
au BufRead /tmp/mutt-* set colorcolumn=73
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

let g:syntastic_tex_checkers = []

set grepprg=grep\ -nH\ $*
let g:tex_flavor = "latex"
" use pdflatex
let g:Tex_DefaultTargetFormat='pdf'
let g:Tex_MultipleCompileFormats='pdf,dvi'
let g:Tex_CompileRule_pdf = 'mkdir -p tmp; pdflatex -output-directory tmp -interaction=nonstopmode $*; cp tmp/*.pdf .'

map <F6> :setlocal spell! spelllang=en_us<CR>
map <F8> :setlocal spell! spelllang=es<CR>
autocmd BufNewFile,BufRead *.tex set spell
autocmd BufNewFile,BufRead *.tex let g:indentLine_enabled=0
autocmd BufNewFile,BufRead *.md let g:indentLine_enabled=0
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

let g:ycm_semantic_triggers = {
\  'tex'  : ['\ref{', '\cref{', '\cite{', '\autocite{', '\mlacite{', '\nocite{',],
\ }

let g:jedi#force_py_version = 3
let g:calendar_google_calendar = 1
let g:calendar_google_task = 1

" vertical line indentation
let g:indentLine_color_term = 239
let g:indentLine_color_gui = '#09AA08'
let g:indentLine_char = '│'
let g:tex_comment_nospell= 1
let g:LatexBox_quickfix = 4
let g:LatexBox_viewer = "zathura"
let g:LatexBox_latexmk_preview_continuously = 1
let g:LatexBox_build_dir = '/tmp/parth-LaTeX'
let g:LatexBox_latexmk_options = "-cd -outdir='/tmp/parth-LaTeX'"

let g:powerline_pycmd = 'py3'
set laststatus=2 " Always display the statusline in all windows
set showtabline=2 " Always display the tabline, even if there is only one tab
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)
set smartcase
" Run the current file with rspec
map <Leader>rb :call VimuxRunCommand("clear; rspec " . bufname("%"))<CR>

" Prompt for a command to run
map <Leader>vp :VimuxPromptCommand<CR>

" Run last command executed by VimuxRunCommand
map <Leader>vl :VimuxRunLastCommand<CR>

" Inspect runner pane
map <Leader>vi :VimuxInspectRunner<CR>

" Close vim tmux runner opened by VimuxRunCommand
map <Leader>vq :VimuxCloseRunner<CR>

" Interrupt any command running in the runner pane
map <Leader>vx :VimuxInterruptRunner<CR>

" Zoom the runner pane (use <bind-key> z to restore runner pane)
map <Leader>vz :call VimuxZoomRunner()<CR>

let g:ycm_extra_conf_globlist = ['~/Code/UCSD-Extensions/CCppProgrammingOne/*']

autocmd bufnewfile *.c so ~/.vim/c_header.txt
autocmd bufnewfile *.h so ~/.vim/h_header.txt
autocmd bufnewfile *.cpp so ~/.vim/cpp_header.txt
autocmd bufnewfile *_Quiz.txt so ~/.vim/_Quiz.txt_header.txt
autocmd bufnewfile *.c exe "1," . 10 . "g/FILE_NAME.*/s//" .expand("%")
autocmd bufnewfile *.c exe "1," . 10 . "g/DATE.*/s//" .strftime("%B %e, %Y")
autocmd bufnewfile *.h exe "1," . 10 . "g/FILE_NAME.*/s//" .expand("%")
autocmd bufnewfile *.h exe "1," . 10 . "g/DATE.*/s//" .strftime("%B %e, %Y")
autocmd bufnewfile *.cpp exe "1," . 10 . "g/FILE_NAME.*/s//" .expand("%")
autocmd bufnewfile *.cpp exe "1," . 10 . "g/DATE.*/s//" .strftime("%B %e, %Y")
autocmd bufnewfile *_Quiz.txt exe "1," . 10 . "g/FILE_NAME.*/s//" .expand("%")
autocmd bufnewfile *_Quiz.txt exe "1," . 10 . "g/DATE.*/s//" .strftime("%B %e, %Y")
