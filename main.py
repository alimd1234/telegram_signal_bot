services:
  - type: worker
    name: telegram-bot
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python main.py"
    autoDeploy: true

