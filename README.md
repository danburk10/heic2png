# heic2png
convert heic to png using pillow

# install requirements
pip  (on debian ```sudo apt install python3-pip```  )  
note: you can also use ```python -m pip install ...```  
pip install pillow  
pip install pillow_heif  

# to run  
assuming heic2png.py is in the directory you are working in  
form powershell: ```ls -name *.HEIC | python .\heic2png.py```
from linux: ```find IMG* | python3 .\heic2png.py```
