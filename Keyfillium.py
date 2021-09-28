from Crypto.PublicKey import RSA

#why am i using num2words? Because this script was INCREDIBLY problematic
#for some strange reason python hates concatinating integers and string
#i cant just do 1+("word"), fortunately num2word translated 1 to one for example.

from num2words import num2words

print("""
██╗  ██╗███████╗██╗   ██╗███████╗██╗██╗     ██╗     ██╗██╗   ██╗███╗   ███╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝██║██║     ██║     ██║██║   ██║████╗ ████║
█████╔╝ █████╗   ╚████╔╝ █████╗  ██║██║     ██║     ██║██║   ██║██╔████╔██║
██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══╝  ██║██║     ██║     ██║██║   ██║██║╚██╔╝██║
██║  ██╗███████╗   ██║   ██║     ██║███████╗███████╗██║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝     ╚═╝
            Security by obscurity: the right way
----------------------------------------------------------------------------
               Choose an option below:

              1) Generate, ssh keys (openssh)
              2)
""")

choice = input(" :")
if choice == ("1"):
    user_input = int(input("how many openssh keys would you like to create?"))
    user_choice = int(input("How many bits (for e.g 4096, 2048, 1024...), Higher = more secure, but slower - Default = 2048:      "))
    priv_choice = str(input("What should the private key be called? Default = id_rsa:      "))
    pub_choice = str(input("What should the public key be called? Default = public_key:      "))

#this number needs to keep incrementing by 1 for the file name
number_zero = 0


def incrementing_numbers():
    global incrementing_number
    #file name 5needs to keep incrementing by one
    incrementing_number = number_zero + 1
    print(incrementing_number)


def permanent():
    global number_zero
    number_zero = incrementing_number


def keygen():
    #making the openssh key
    key = RSA.generate(user_choice)
    private_key = key.export_key()
    #translating the number to a numberword to concatinate integers with a string
    incrementing_number_word = (num2words(incrementing_number))
    file_out = open((priv_choice) + (incrementing_number_word), "wb")
    file_out.write(private_key)

    public_key = key.publickey().export_key()
    file_out = open(
        (pub_choice) + (incrementing_number_word) + ".pub", "wb")
    file_out.write(public_key)


for x in range(0, user_input):
    incrementing_numbers()
    permanent()
    keygen()
