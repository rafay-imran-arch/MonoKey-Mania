
from browser import document, window, ajax
import json

game_key = None
is_loading = False

def init(bound_key):
    global game_key, is_loading
    game_key = bound_key 
    is_loading = False

    document["game-title"].text = "=== Engine 3: WikiTap ==="
    display_prompt()

def display_prompt():
    document["game-content"].html = """
    <div style="text-align: center; font-family; monospace; padding: 15px;">
        <h2 style="color: #8a7c6b; margin-bottom: 5px;"> WikiTap <span style="font-style: italic;">Knowledge in one Key Tap</span> </h2>
        <p style="font-size: 0.85em; color: #bfae9e; margin-top: 0;"> Tap the KEY! Tap the KEY! Knowledge KEY! </p>

        <div id="wiki-display-box" style="min-height: 120px; background: #f7f5f0; border: 2px solid #8c7a6b; border-radius: 8px; padding: 15px;
        margin: 20px; text-align: left; font-size: 0.9em; line-height: 1.6; color: #4a3e3d;">
            <div style="text-align: center; color: #8c7a6; margin-top: 35px; font-style: italic;">       
                [You dare pause the Knowledge? TAP! TAP!]
            </div>
        </div>

        <p id="wiki-status" style="font-size: 0.7em; color: #bfae9e;"> [Connect to the Wiki-Verse] </p>
    </div>
"""

def on_api_complete(req):
    global is_loading
    is_loading = False
    document["wiki-status"].text = "[Recieving the Forbidden Knowledge]"

    try:
        data = json.loads(req.text)
        pages = data.get("query", {}).get("pages",{})

        page_id = list(pages.keys())[0]

        if page_id == "-1":
            raise Exception("Article abstract unreadable.")
        page = pages[page_id]
        title = page.get("title", "Unknown Title").upper()
        extract = page.get("extract","No extract summary available for this node.")

        if not extract.strip():
            extract = "The summary content for this transmission was blank. Try tapping again"

        document["wiki-display-box"].html = f"""
        <strong style="color: #8c7a6b; font-size: 1.1em; display: block; border-bottom: 1px dashed #b5a895;
        padding-bottom: 5px; margin-bottom: 10px;">
            Source: {title}
        </strong>
        <p style="margin: 0; font-family: 'Courier New', monospace;">{extract}</p>
        """ 

    except Exception as e:
        document["wiki-display-box"].html = f"""
        <div style="text-align: center; color: #ff3333; margin-top: 35px;">
            ERROR PARSING CONTENT TRACE<br>
            <span style="font-size: 0.8em; color: #8c7a6b;"> (API denied access to this knowledge. Try again)</span>
        </div>
        """

def fetch_random_wiki():
    global is_loading 
    if is_loading:
        return
    
    is_loading = True
    document["wiki-status"].text = "Connecting to Wiki-Verse Knowledge"
    document["wiki-display-box"].html = """
    <div style="text-align: center; color: #8c7a6b; margin-top: 35px; font-weight: bold;">
        Fetching randomness from the land of Wiki-Verse
    </div>
    """
    #API sourcing 
    url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=1&explaintext=1&generator=random&grnnamespace=0&origin=*"

    req = ajax.ajax()
    req.bind("complete", on_api_complete)
    req.open("GET", url, True)
    req.send()

def start_press():
    pass

def stop_press():
    if not is_loading:
        fetch_random_wiki()