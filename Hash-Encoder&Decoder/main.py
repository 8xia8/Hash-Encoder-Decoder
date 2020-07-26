from md5decode import md5decode
from md5encode import md5encode
from sha1encode import sha1encode
from sha1decode import sha1decode
from sha256encode import sha256encode
from sha256decode import sha256decode
from sha512encode import sha512encode
from sha512decode import sha512decode
from base64encode import base64encode
from function import user_input
import subprocess
import time
import hashlib

subprocess.call(["clear"])

print('''



  __  __           _        ____           ___       _        ___  
 |  \/  |         | |      |  _ \         / _ \     (_)      / _ \ 
 | \  / | __ _  __| | ___  | |_) |_   _  | (_) |_  ___  __ _| (_) |
 | |\/| |/ _` |/ _` |/ _ \ |  _ <| | | |  > _ <\ \/ / |/ _` |> _ < 
 | |  | | (_| | (_| |  __/ | |_) | |_| | | (_) |>  <| | (_| | (_) |
 |_|  |_|\__,_|\__,_|\___| |____/ \__, |  \___//_/\_\_|\__,_|\___/ 
                                   __/ |                           
                                  |___/                            
Please Wait...
''')
time.sleep(3)
subprocess.call(["clear"])

print('''


 _    _           _           ______                     _                 _____                     _           
| |  | |         | |         |  ____|                   | |          ___  |  __ \                   | |          
| |__| | __ _ ___| |__       | |__   _ __   ___ ___   __| | ___ _ __( _ ) | |  | | ___  ___ ___   __| | ___ _ __ 
|  __  |/ _` / __| '_ \      |  __| | '_ \ / __/ _ \ / _` |/ _ \ '__/ _ \/\ |  | |/ _ \/ __/ _ \ / _` |/ _ \ '__|
| |  | | (_| \__ \ | | |     | |____| | | | (_| (_) | (_| |  __/ | | (_>  < |__| |  __/ (_| (_) | (_| |  __/ |   
|_|  |_|\__,_|___/_| |_|     |______|_| |_|\___\___/ \__,_|\___|_|  \___/\/_____/ \___|\___\___/ \__,_|\___|_|   



''')

user_input()


