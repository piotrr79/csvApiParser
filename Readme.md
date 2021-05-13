# Parser:
Python parser to combine api and csv results

## Installation:
Install Python3
Download pip: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
Install pip: `python3 get-pip.py`
Run `pip3 install -r requirements.txt` from project directory
Rename `env.dist `to `.env` or set env vars with values

## Runtime params:
Define CSV_PATH where input and output files will be hosted.
Path is relative to script root dir. It can be also root, but it is good practice to set it to separate folder, e.g 1 level above root
In case of empty CSV_PATH user defined paths can be added to command, like `/some_apth/input.csv`, `/some_other_path/output.csv`
Script must have access and permissions to read and write dir / dirs with input and output files

## Run mock api server:
Cd to `cd ~/parser` and from project directory run `python3 server/apiMock.py`
This will run simple Flask server with two api channels, one for success response with sample api data under `/api-success` and another one for 404 response under `/`

## Run form console:
Open new terminal window, cd to `cd ~/parser` and from project directory run: `python3 command.py your_input_file.csv your_output_file.csv`
Input files should be in directory defined in env CSV_PATH
In case of any problems follow console messages
Sample input files can be found in `test/testPayload/csvFiles` folder

## Tests:
From new terminal window while mock servier is runnig execute tests with `python3 -m unittest tests/command_test.py`
Tests are functional, requires Api url to be callable and responding
