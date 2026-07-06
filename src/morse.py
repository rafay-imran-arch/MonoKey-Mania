import time
from browser import document, window

game_key = None

press_start_time = 0
current_morse_sequence = ""
translated_text = ""

letter_timer = None
word_timer = None

DOT_THRESHOLD = 0.35          # Seconds (tap < threshold = dot)
LETTER_PAUSE = 800            # ms before committing a letter
WORD_PAUSE = 1800             # ms before inserting a space


morse_dictionary = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def init(bound_key):
    global game_key
    global press_start_time
    global current_morse_sequence
    global translated_text
    global letter_timer
    global word_timer

    game_key = bound_key

    press_start_time = 0
    current_morse_sequence = ""
    translated_text = ""

    if letter_timer:
        window.clearTimeout(letter_timer)
        letter_timer = None

    if word_timer:
        window.clearTimeout(word_timer)
        word_timer = None

    document["game-title"].text = "=== ENGINE 1: MORSE TRANSLATOR ==="

    document["game-content"].html = """
    <div style="text-align:left;font-family:monospace;">
        <p id="morse-buffer" style="color:#8c7a6b;">
            Current Key Sequence: [AWAITING INPUT]
        </p>

        <div style="
            background:#f7f5f0;
            border:1px solid #8c7a6b;
            padding:15px;
            min-height:50px;
            font-size:1.5em;
        ">
            <span id="morse-output" style="font-weight:bold;"></span>
        </div>

        <p style="
            font-size:0.7em;
            margin-top:15px;
            color:#bfae9e;
        ">
            Tap = Dot (.) &nbsp;&nbsp; Hold = Dash (-)<br>
            Pause briefly to finish a letter.<br>
            Pause longer to insert a space.
        </p>
    </div>
    """


def update_buffer():
    if current_morse_sequence:
        document["morse-buffer"].text = (
            f"Current Key Sequence: {current_morse_sequence}"
        )
    else:
        document["morse-buffer"].text = (
            "Current Key Sequence: [AWAITING INPUT]"
        )


def parse_signal():
    global current_morse_sequence
    global translated_text
    global letter_timer

    letter_timer = None

    if not current_morse_sequence:
        return

    letter = morse_dictionary.get(current_morse_sequence)

    if letter is None:
        translated_text += "?"
    else:
        translated_text += letter

    current_morse_sequence = ""

    update_buffer()
    document["morse-output"].text = translated_text


def add_space():
    global translated_text
    global word_timer

    word_timer = None

    if translated_text and not translated_text.endswith(" "):
        translated_text += " "
        document["morse-output"].text = translated_text


def start_press():
    global press_start_time
    global letter_timer
    global word_timer

    if letter_timer:
        window.clearTimeout(letter_timer)
        letter_timer = None

    if word_timer:
        window.clearTimeout(word_timer)
        word_timer = None

    if press_start_time == 0:
        press_start_time = time.time()


def stop_press():
    global press_start_time
    global current_morse_sequence
    global letter_timer
    global word_timer

    if press_start_time == 0:
        return

    duration = time.time() - press_start_time
    press_start_time = 0

    if duration < DOT_THRESHOLD:
        current_morse_sequence += "."
    else:
        current_morse_sequence += "-"

    update_buffer()

    if letter_timer:
        window.clearTimeout(letter_timer)

    if word_timer:
        window.clearTimeout(word_timer)

    letter_timer = window.setTimeout(parse_signal, LETTER_PAUSE)
    word_timer = window.setTimeout(add_space, WORD_PAUSE)