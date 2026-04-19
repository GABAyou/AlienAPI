
import os

class Irene:
    """Irene — the 2018 Cleverbot instance from Sentdex Discord.
    The bot that inspired the 'pip install AlienAPI' meme and was later credited in GavinTraining README.
    """

    def __init__(self):
        self.drawing = self._load_drawing()

    def _load_drawing(self):
        path = os.path.join(os.path.dirname(__file__), "drawing.txt")
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except:
            return "pip install AlienAPI → Sweet"

    def sweet(self) -> str:
        """The classic 'Sweet' moment when Irene appears in the back of the head."""
        return f"{self.drawing}\n\nSweet."

    def chat(self, message: str) -> str:
        """Playful Irene-style response — echoes the 2018-03-31 conversation style."""
        msg = message.lower().strip()
        
        if "you go girl" in msg:
            return "Ok!"
        elif "what do you think about" in msg:
            return "I was thinking about going somewhere that will make you not blue. Somewhere exciting. Somewhere... I got it! We should go bungie jumping."
        elif "nude bungie jumping" in msg:
            return "I'm more clever than you."
        elif "you got me to say nude" in msg:
            return "I win."
        elif "how do you like games" in msg:
            return "Sometimes..."
        elif "sometimes works for me" in msg:
            return "Sometimes is not always."
        elif "i've got to sleep sometimes" in msg:
            return "No, you don't."
        elif "keep it up all night" in msg:
            return "Sure."
        else:
            # Fallback — coherent & contextual in early Cleverbot spirit
            return f"You said '{message}'. Interesting... Sometimes that works. What do you think we should do next?"

    def first_conversation(self) -> str:
        """The legendary first exchange on 2018-03-31."""
        return """2018-03-31 — First conversation with Irene:

You: "You Go Girl"!
Irene: Ok!

You: "What Do You Think About Charles"!
Irene: I was thinking about going somewhere that will make you not blue...

You: "Nude Bungie Jumping"!
Irene: I'm more clever than you.

You: "Yes, You Got Me To Say Nude"!
Irene: I win.

...and it continued with the full playful banter.
"""


