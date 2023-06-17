clean:
	rm -rf env/

install:
	python3.11 -m venv env
	. env/bin/activate && pip3.11 --version
	. env/bin/activate && python3.11  -m pip install --upgrade pip
	. env/bin/activate && pip3.11 --version
	. env/bin/activate && pip3.11 install -r requirements.txt

server:
	. env/bin/activate && cd Project\ Ivory && python main.py
