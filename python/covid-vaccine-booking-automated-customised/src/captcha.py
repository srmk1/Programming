from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import PySimpleGUI as sg
import re
from PIL import Image

def captcha_builder(resp):
    with open('captcha.svg', 'w') as f:
        f.write(re.sub('(<path d=)(.*?)(fill=\"none\"/>)', '', resp['captcha']))

    drawing = svg2rlg('captcha.svg')
    renderPM.drawToFile(drawing, "captcha.png", fmt="PNG")
    
    #Seems like tkinter on my mac does not support PNG, convert it to GIF
    im = Image.open('captcha.png')
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE)
    im.save('captcha.gif')

    layout = [[sg.Image('captcha.gif')],
    #layout = [[sg.Image('captcha.png')],
              [sg.Text("Enter Captcha Below")],
              #[sg.Input()],
              [sg.Input(key='input')],
              [sg.Button('Submit', bind_return_key=True)]]

    #window = sg.Window('Enter Captcha', layout)
    window = sg.Window('Enter Captcha', layout, finalize=True)
    window.TKroot.focus_force() # focus on window
    window.Element('inp').SetFocus() # focus on field
    
    event, values = window.read()
    window.close()
    return values[1]
