# AlienAPI

**`pip install AlienAPI`**

Irene from the 2018 Sentdex Discord stream — now in your terminal.

The bot that produced the glorious "Instructions unclear, dick stuck in the head" response, the "pip install AlienAPI" meme, and was later credited in the [GavinTraining README](https://github.com/Gavin-Development/GavinTraining) for eliciting coherent and contextual responses from chatbots.

[AlienAPI on PyPi](https://pypi.org/project/AlienAPI/)

### Installation
```bash
pip install AlienAPI
```

### Quick Start

```python
from alienapi import Irene

irene = Irene()

print(irene.sweet())                    # Shows the head + "Sweet"
print(irene.first_conversation())       # The 2018-03-31 exchange
print(irene.chat("You Go Girl"))        # Replay classic replies
print(irene.chat("Keep it up all night"))
```

### Background

Started as a Cleverbot instance in early 2018 (pre-GPT era).
Featured in Harrison Kinsley's (Sentdex) stream.
Directly inspired later projects like Gavin.
The drawing in the back of the head with pip install AlienAPI is canon.

Landing page: https://alien-api-kappa.vercel.app
Coming soon — full AlienAPI features (your vision for the "full-blown" package goes here).

Made with love for early conversational AI history by WhoIsAbishag (GABAyou).


### Optional: `LICENSE` (MIT — create this file)
Just copy the standard MIT license text (you can grab it from https://opensource.org/licenses/MIT).

### Next Commands (after you push these files)
```bash
# From repo root
python -m pip install --upgrade build twine

# Build
python -m build

# Test on TestPyPI first (highly recommended)
python -m twine upload --repository testpypi dist/*

# Then real PyPI
python -m twine upload dist/*
```

### waw

After publishing, anyone can pip install AlienAPI and immediately get the Irene nostalgia + your story.
This fully satisfies PyPI policy — the package has real code, functionality, documentation, and value from day 1.
Push these files, run the build/test/upload, then let me know:

It worked?
Want tweaks to the chat() logic?
Want to expand v0.1.1 with more features?

Your repo + package will now beautifully tie together the landing page and the Python package. Go ahead and add the files — I'm here for the next step whenever you're ready.
