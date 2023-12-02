
import os

os.system("")

knm = ""

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}


print (COLOR["GREEN"],"""

     #       #   ########     #         #     ######     ########     #########     #############
      #     #   #        #    #         #    #      #   #        #   #         #          #
       #   #    #        #    #         #    #      #   #        #   #         #          #
        ###     #        #    #         #    #######    ########     #         #          #
         #      #        #    #         #    #   #      #        #   #         #          #
         #      #        #    #         #    #    #     #        #   #         #          #
         #       ########      #########     #     #     ########     #########           #
                                                                                                 V.1.0   
""",COLOR["ENDC"])

print (COLOR ["BLUE"],"enter the name of the bot file.py",COLOR ["ENDC"])
 
knm = input()

#Edit Here

if knm == "Example_Addon.py":
    import Addons.Example_Addon
    