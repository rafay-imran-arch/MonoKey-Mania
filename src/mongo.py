
from browser import document, window 

img_up = "src/bongo2.png"
img_down = "src/bongo1.png"

total_slams = 0
revealed_text = ""
secret_phrase = "Thank you! MAX the one true King of ONEKEY land. Thank you so much. I knew the ONE-KEY was real"

def init(target_key):
    global total_slams, revealed_text
    total_slams = 0
    revealed_text = ""
    document["game-title"].text = "===Engine 4: TypingMongo ==="
    render_view(img_down)

def render_view(image_src):
    document["game-content"].html = f"""
        <div style="text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <!--Mongo max?-->
            <img src="{image_src}" alt="Typing Max" style="max-width: 320px; height: auto; padding: 5px;" />
            <div style="text-align: center; margin-top: 15px; font-weight: bold; color: #8a7c6b; font-family: monospace; font-size: 1.2em; letter-spacing: 1px;">
                Total slams: {total_slams}
            </div>
        </div>    

        <!-- Magical secret max reveal-->
        <div style="margin-top: 25px; min-height: 40px; font-family: monospace; font-size: 1.3em; color: #8a7c6b; font-weight: bold; max-width: 500px; line-height: 1.4; letter-spacing: 2px;">
            {revealed_text}<span style="animation: blink 1s infinite;">_</span> 
        </div>
    """ 

def start_press():
    global total_slams, revealed_text
    total_slams += 1

    if len(revealed_text) < len(secret_phrase):
        revealed_text += secret_phrase[len(revealed_text)]
    
    render_view(img_up)

def stop_press():
    render_view(img_down)