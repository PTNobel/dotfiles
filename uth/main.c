
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int usage(char *argv[] ) 
{
    printf(argv[0]);
    printf(": update_tools_helper {abs|alpm|man|mlocate|pkgfile|units}\n");
    return 0;
}

int main( int argc, char *argv[] )
{
    if ( argc != 2 ) {
        usage(argv);
        return 1;
    }

    else if( strcmp(argv[1],"abs") == 0 )
    {
        setuid( 0 );
        system( "/usr/bin/abs" );
        return 0;
    }

    else if(strcmp(argv[1],"alpm") == 0 )
    {
      setuid( 0 );
      system( "/usr/bin/pacman -Syuw --noconfirm" );
      return 0;
    }

    else if(strcmp(argv[1],"man") == 0 )
    {
      setuid( 0 );
      system( "/usr/bin/mandb" );
      return 0;
    }

    else if( strcmp(argv[1],"mlocate") == 0 )
    {
      setuid( 0 );
      system( "/usr/bin/updatedb" );
      return 0;
    }

    else if( strcmp(argv[1],"pkgfile") == 0 )
    {
      setuid( 0 );
      system( "/usr/bin/pkgfile -u" );
      return 0;
    }

    else if( strcmp(argv[1],"texlive") == 0 )
    {
      setuid( 0 );
      system( "/usr/local/bin/tlmgr update --all" );
      return 0;
    }

    else if( strcmp(argv[1],"units") == 0 )
    {
      setuid( 0 );
      system( "/usr/bin/units_cur" );
      return 0;
    }

    else if(strcmp(argv[1],"-h") == 0 )
    {
      usage(argv);
      return 0;
    }

    else
    {
      usage(argv);
      return 1;
    }
}
