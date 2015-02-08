#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main( int argc, char *argv[] )
{
    if ( argc != 2 ) {
	  fprintf(stderr,"Usage: update_tools_helper {mlocate|pkgfile|man|alpm}\n");
      return 1;
    }
    else if( strcmp(argv[1],"abs") == 0 )
    {
        setuid( 0 );
        system( "/usr/bin/abs" );
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
    else if(strcmp(argv[1],"man") == 0 )
    {
      setuid( 0 );
      system( "/usr/bin/mandb" );
      return 0;
    }
	else if(strcmp(argv[1],"alpm") == 0 )
	{
	  setuid( 0 );
	  system( "/usr/bin/pacman -Sy" );
	  system( "/usr/bin/pacman -Suw --noconfirm" );
	  return 0;
	}
	else if(strcmp(argv[1],"-h") == 0 )
	{
	  printf("Usage: update_tools_helper {mlocate|pkgfile|man|alpm}\n");
	  return 0;
	}
	else
    {
	  fprintf(stderr,"Usage: update_tools_helper {mlocate|pkgfile|man|alpm}\n");
      return 1;
	}
  
}
