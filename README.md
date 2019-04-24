# WheelGear

Project for a thought controlled wheelchair.

Used eMotiv Mindwave mobile reader 2.
Needs Thinkgear connector to fetch eeg values.

Program.cs is the c# script for collecting eeg values from the single channel reader at realtime and send to a mqtt server.
ambujes new algo has the rnn classifer and weight files.

readbotmqtt.py recieves the values from the mqtt server and moves the bot.
