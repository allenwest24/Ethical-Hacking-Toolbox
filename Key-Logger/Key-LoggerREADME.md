# Key-Logger
Making a key logger tool while taking the ethical hacking course.

!!!This keylogger works if you download it and all the libraries it requires, however, it is very simple to package this into a .exe file. I want to stay out of jail so I didn't do that.!!! 

The following info will be the instructions on how to set up the workspace needed to make this yourself, as well as how it works and other concepts:
- This is for Windows. We need to install python. 
  - Google and download Sublime Text.
  - Run
  - Change settings according to your liking
  - print "hello" and save as a .py file. Now you can see what a python file looks like.
  - Install python2 and python3. (for Windows)
  - In the same folder you have the downloaded python versions, try to run your hello world program. 
- Now we can start making the keylogger.
  - In pycharm create new project. (or just use vim for all of this specifying that it is a .py file except for the .txt output file)
  - Create new file in pyinput and call it your key logger
- We need a module that will help us grab keys from the target machine.
  - Open a terminal. 
  - Type the following: pip install pyinput.
  - Consider installing pip3 as well.
  - Now we have our libraries and prerequisites.
  - import the library in your main file.
- The rest of the instructions will be commented into the keylogger itself. If any excessive information is needed it will be written below:
  - Note: if target machine is set in different language, the symbols will look different. We handle this problem with the try: using "utf-8"
  - In order to stop it, in terminal type: killall python
  - Due to the way the libraries work, this is going to be in python2
  
  
