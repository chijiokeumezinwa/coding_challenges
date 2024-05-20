The efficient way to communicate with the OS(operating system) is by using shell commands. Since CLI tools directly run on the terminal the execution time is faster. when you’re trying to automate the daily repeatable manual tasks a CLI tool is easy to develop, maintain, distribute and use.

In this tutorial, we are going to see how to create a CLI tool using python.

link:
https://episyche.com/blog/how-to-build-a-cli-tool-using-python

recommendation to run this program in virtual env
python3 -m venv ./venv
source venv/bin/activate

next make sure to run the updates for virtualenv
pip3 install "typer[all]"
pip3 install PyInquirer
pip3 install rich

if an error pops up that looks like this 
ImportError: cannot import name 'Mapping' from 'collections'
edit the from_dict.py 
nano venv/lib/python3.10/site-packages/prompt_toolkit/styles/from_dict.py

to change collections import Mapping to collections.abv import Mapping