## Secretsfile where lat / lon / dec / az / kwp are stored in URL format

def check_for_secret( secretfile ):
    try:
        importfile = open("solarsetup.env", "r")
    except OSError:
        print( "Could not open/read file: solarsetup.env" )
        return secret
    with importfile:
        secret = importfile.read()
        importfile.close
        return secret  