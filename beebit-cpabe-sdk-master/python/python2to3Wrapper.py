# call code from python 2 library
import execnet


def call_python_version(Version, Module, Function, ArgumentList):
    gw      = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()

def setup(public_key, master_key):
    result = call_python_version("2.7", "pycpabe", "cpabe_setup",  [public_key, master_key]) 
    if result == -1:
        print("Setup failed!")
    else:
        print("Setup success!")
        print("Public key: %s" % public_key)
        print("Master key: %s" % master_key)

def keygen(professional_secret_key, public_key, master_key, professional_attributes):
    result = call_python_version("2.7", "pycpabe", "cpabe_vkeygen",  [professional_secret_key, public_key, master_key, len(professional_attributes), professional_attributes]) 
    if result == -1:
        print("Keygen failed!")
    else:
        print("Keygen success!")
        print("Secret key: %s" % professional_secret_key)

def enc(public_key, file_path, encryption_policy, ct):
    result = call_python_version("2.7", "pycpabe", "cpabe_fenc",  [public_key, file_path, encryption_policy, ct]) 
    if result == -1:
        print("Encrypt failed!")
    else:
        print("Encrypt success!")
        print("File (%s) encrypted to file (%s) with policy (%s)." % (file_path, ct, encryption_policy))

def dec(public_key, professional_secret_key, ct, pt):
    result = call_python_version("2.7", "pycpabe", "cpabe_fdec",  [public_key, professional_secret_key, ct, pt]) 
    if result == -1:
        print("Decrypt failed!")
    else:
        print("Decrypt success!")
        print("File (%s) decrypted to file (%s) " %(ct, pt))



def encdec():
    print("Sorry this feature hasn't been implemented yet :(")



