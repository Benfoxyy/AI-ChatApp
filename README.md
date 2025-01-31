<div align="center">
<h1 align="center">AI Chat Bot With Streamlit 🤖</h1>
<h3 align="center">This project is a AI chatbot application built using Streamlit and OpenAI's GPT model. The chatbot allows users to interact with an AI assistant in real-time.</h3>
</div>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://streamlit.io/" target="_blank"> <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo" width="50" height="35"> </a>
<a href="https://openai.com/" target="_blank"> <img src="https://www.svgrepo.com/show/306500/openai.svg" alt="OpenAI" width="50" height="35"> </a>
</p>

# Planning For Future
This bot is not compleated yet, And i've got multiple ideas to add it in future like :

- AI history
- Multiple AI models ( user can select through it )
- Plans system like <b>FREE, STANDARD, PRO, UNLIMITED</b>

# Setup 

### Deployment
If you wanna just see and work with the resualt, I've deployed my project with `Streamlit Cloud` and you can access to it with this url : https://benbot.streamlit.app

But if you need to use it in you project or deal with their structures,
you can follow these easy steps :

### Clone Project
For cloning this project in you computer you can just enter this `git` command in your `terminal` and open it :
```bash
git clone https://github.com/Benfoxyy/AI-ChatApp.git
cd <PROJECT_DIRECTORY>
```

### Virtual Environment
Now lets create a virtual environment ( venv ) for manage and our installing pakages :
```bash
python -m venv venv
```

Active your `venv` for working with it :
```bash
# Windows
venv\Scripts\activate

# macOS and Linux
source venv/bin/activate
```

### Requirements
I put every single pakages you need to install in `requeirements.txt` file, So you can just run this command in your `venv` :
```bash
pip install -r requirements.txt
```

### API Key
Set up OpenAI API Key: You will need to set up your OpenAI API key. You can get this key from <a href="https://platform.openai.com/account/api-keys">OpenAI's platform</a> .

Once you have your key, create a `.streamlit/secrets.toml` file in your project directory with the following content:
```toml
[openai]
api_key = "<YOUR_OPENAI_API_KEY>"
```

### Run It!
As i said ; I've used `streamlit` for this project, in spite of this we're gonna run it on streamlit client :
```bash
streamlit run AI.py
``` 
By running this command you will see the resault in you browser 🎉


### License
This project is licensed under the MIT License - see the <a href='https://github.com/Benfoxyy/AI-ChatApp/blob/main/LICENSE'>LICENSE</a> file for details.

<hr>

<div align="center">
<h1 align="center">Thanks for visiting</h1>
<h3 align="center">I hope that you enjoy it, Let me know if you have any suggestion 😉</h3>
</div>