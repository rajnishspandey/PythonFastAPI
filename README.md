#this repoository contains Fast API Code

create virtual env
	python -m venv env
Activate the virtual env
	.\env\Scripts\activate
install modules using requirement.txt
	pip install -r .\requirements.txt
	
	
Run Flask API - flask run
mac/linux - curl -i -X GET http://127.0.0.0:5000/

windows - curl http://127.0.0.1:5000

or

curl -i -X GET http://localhost:5000/
