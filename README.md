\# 🔔 any\_alarm — Universal Signal Notifier for ComfyUI



\*\*any\_alarm\*\* is a simple yet powerful node that plays a sound whenever it receives any signal (image, latent, conditioning, etc.). Perfect for notifications when a generation starts, completes, or any custom event.



!\[any\_alarm in action](screenshot.png) \*— add a screenshot later\*



\## ✨ Features



\- 🎭 \*\*Voice modes\*\*: female, male, robot (with emoji icons)

\- 📢 \*\*Events\*\*: start, load complete, work complete

\- 🎛️ \*\*Custom mode\*\*: use any .mp3/.wav from `sounds/custom/`

\- 🔇 \*\*Mute button\*\* — temporarily disable sound without removing node

\- 🔊 \*\*Volume control\*\* (0.0–1.0)

\- 💾 \*\*Saves settings\*\* — your choices persist between sessions

\- 🔌 \*\*Signal input\*\* — connect anything (images, latents, etc.)



\## 📁 Folder Structure



After installation, your `custom\_nodes/ComfyUI-any\_alarm/` should look like:



ComfyUI/

└── custom\_nodes/

└── ComfyUI-any\_alarm/

├── init.py

├── any\_alarm.py

├── requirements.txt

└── sounds/

├── female/

│ ├── start.wav

│ ├── load complete.wav

│ └── work complete.wav

├── male/

│ ├── start.wav

│ ├── load complete.wav

│ └── work complete.wav

├── robot/

│ ├── start.wav

│ ├── load complete.wav

│ └── work complete.wav

└── custom/ ← put your own sounds here





\## 🚀 Installation



1\. \*\*Clone or download\*\* this repository into `ComfyUI/custom\_nodes/`

&nbsp;  ```bash

&nbsp;  cd ComfyUI/custom\_nodes/

&nbsp;  git clone https://github.com/YOUR\_USERNAME/ComfyUI-any\_alarm.git



2\. Install pygame (required for sound playback)



bash

\# On Windows (adjust path to your ComfyUI python)

cd ComfyUI/python\_embeded

python.exe -m pip install pygame



\# On Linux/Mac

pip install pygame



3\. Add your sound files to the appropriate folders



Voice modes require exact filenames: start.wav, load complete.wav, work complete.wav



Custom mode accepts any .mp3 or .wav files



4\. Restart ComfyUI



🎮 How to Use

Find 🔔 any\_alarm in the alarm category



Connect any node output to the signal input



Choose:



Mode: female/male/robot + event, or 🎛️ custom + your file



Adjust volume if needed



Run your workflow — the sound will play every time a signal arrives



🛠️ Custom Sounds

For voice modes, files must be named exactly as the event



For custom mode, just put your .mp3/.wav in sounds/custom/ — they'll appear in the dropdown



📝 Requirements

Python 3.10+



pygame



🤝 Contributing

Feel free to fork, submit PRs, or suggest improvements!

