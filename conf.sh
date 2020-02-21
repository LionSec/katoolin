# Contains values used by all shell scripts #
#############################################

# The installation directory:
DIR="/usr/local/bin";

# The name of the program after installation:
PROGRAM="katoolin3";

# Show error message and quit:
die(){
    if [ "$*" ];
    then
        echo $*;
    fi
    exit 1;
}