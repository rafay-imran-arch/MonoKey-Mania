from browser import document, window 
import random 

game_key = None
rolling_timer = None
roll_cycles = 0

def init(bound_key):
    global game_key, rolling_timer, roll_cycles
    game_key = bound_key 
    roll_cycles = 0

    if rolling_timer is not None:
        window.clearInterval(rolling_timer)
        rolling_timer = None
    
    document["game-title"].text = "=== Engine 3: Dice Roller ==="
    document["game-content"].html = """
    <div style ="text-align: center; font-family: monospace; padding: 10px;">
        <h2 style = "color: #8c7a6b; margin-bottom: 5px;"> ONEkey DICE </h2>
        <p style ="font-size: 0.8em; color: #bfae9e; margin-top: 0;"> Hear ye! Hear ye! tap your key to roll.</p>

        <div id="dice-box" style="width: 80px; line-height: 80px; font-size: 3em; font-weight: bold; background: #f7f5f0;
        border: 2px solid #8c7a6b; margin: 20px auto; border-radius: 10px; color: #8c7a6b; transition: all 0.1s;"> 
        ?
        </div>

        <p id="roll-status" style="font-size: 0.70em; color: #bfae9e;"> [Press and roooolllll!] </p>
    </div> 
    """

def run_scramble_cycle():
    global roll_cycles, rolling_timer
    roll_cycles += 1

    face_value = random.randint(1,6)
    document["dice-box"].text = str(face_value)

    shift_amt = "2px" if roll_cycles % 2 == 0 else "-2px"
    document["dice-box"].style.transform = f"rotate({shift_amt}) scale(1.05)"

    if roll_cycles >= 12:

        window.clearInterval(rolling_timer)
        rolling_timer = None
        document["dice-box"].style.transform = "rotate(0deg) scale(1.0)"
        document["dice-box"].style.background = "#9F8c76"
        document["dice-box"].style.color = "#f7f5f0"
        document["roll-status"].text = f"Rolled a {face_value}. Tap the key to roll again!"

def start_press():
    pass

def stop_press():
    global rolling_timer, roll_cycles
    if rolling_timer is not None:
        return
    
    roll_cycles = 0
    document["dice-box"].style.background = "#f7f5f0"
    document["dice-box"].style.color = "#8c7a6b"
    document["roll-status"].text = "Roooollllllllinnnnggg..."

    rolling_timer = window.setInterval(run_scramble_cycle, 70)