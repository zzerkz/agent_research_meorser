## Brief Overview

Meorser (Meme or Serious) is a sorting agent that takes various betting lines on prediction markets such as Kalshi and Polymarket and labels them as one of three catergories: Meme, Serious, and Grey (Grey is for lines that don't fit into the binary). The point of this is to allow further research on the correlation of absurd (meme) lines and betting traders. 
## How to run

### 1. Clone the repo
```shell
git clone https://github.com/zzerkz/agent_research_meorser.git
   cd agent_research_meorser
```
### 2. Create and activate a virtual environment
```shell
   python3 -m venv venv
   source venv/bin/activate
```
### 3. Install requirements.txt
```shell
pip3 install -r requirements.txt
```
### 4. Fetch Groq API Key 
```shell
export GROQ_API_KEY="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"
```
### 5. Run it:
```shell
python3 meorser.py "What will Shaquille O'Neal say during Inside the NBA?"
```
In the "" paste the betting line you want classified from either Kalshi or Polymarket (or make up a market, have fun with it).

## Prerequisites (If you wish to run Langflow via the web UI)

Install Langflow (the interface) https://github.com/langflow-ai/langflow?tab=readme-ov-file

Fetch an API key (you will need this to run the LLM): https://console.groq.com/keys

## How to Import and run this agent

### 1. Download the Flow File:
To run this project, you need to download the **meorserv14.json** file from this repository which is the built Langflow project

### 2. Import into Langflow:
Open your local Langflow dashboard in terminal: 
```shell
uv run langflow run
```
Open Langflow\
Click **Upload a flow** located next to the projects menu\
Select the meorserv14.json downloaded from earlier

### 3. Configure API Keys:
Once the flow loads on your canvas, you will see a few components with red warnings indicating missing credentials\
Click the LLM component\
Paste in your API key\
Select the model "Llama-4-scout"

### 4. Time to test!
Hit the **playground icon** in the top right\
Type in a betting line from your prediction market of choice (Kalshi, Polymarket)\
Press **run flow**\
You will be presented with a category (Meme, Serious, Grey) and a reason as to why this category was chosen\
Enjoy!


