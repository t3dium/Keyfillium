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
              2) -
""")

choice = input(" :")
if choice == ("1"):
    #max num of openssh keys
    user_input = input("how many openssh keys would you like to create?")
    user_input = int(user_input)

    #this number needs to keep incrementing by 1 for the file name
    number_zero = 0

    def incrementing_numbers():
        global incrementing_number
        #file name needs to keep incrementing by one
        incrementing_number = number_zero + 1
        print(incrementing_number)

    def permanent():
        global number_zero
        number_zero = incrementing_number

    def keygen():
        #making the openssh key
        key = RSA.generate(2048)
        private_key = key.export_key()
        #translating the number to a numberword to concatinate integers with a string
        incrementing_number_word = (num2words(incrementing_number))
        file_out = open("ida_rsa" + (incrementing_number_word), "wb")
        file_out.write(private_key)

        public_key = key.publickey().export_key()
        file_out = open(
            "public_key" + (incrementing_number_word) + ".pub", "wb")
        file_out.write(public_key)

    for x in range(0, user_input):
        incrementing_numbers()
        permanent()
        keygen()
