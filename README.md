# Namaste, Hello, here I have created an end to end project on Chicken Disease Classification, with deployment on Azure.

## Below is the project workflow:

1. Update config.yaml
2. Update secrets.yaml
3. Update params.yaml
4. Update the entity
5. Update the confirguration manager in src config
6. Update the components
7. Update pipeline.yaml
8. Update main.py
9. Update dvc.yaml

The above workflow has been followed throughout every stage.

# Run the project

### Step 01
Clone the repository
```bash
git clone https://github.com/markandey1414/Chicken-Disease
```

### Step 02
Create a python virtual environment
```bash
python -m venv chicken_venv
```

### Step 03
Install the requirements
```bash
pip install -r requirements.txt
```

### Step 04
Run the final command
```bash
python main.py
```
To run it on your local host, type the following command
```bash
python app.py
```
Now open your local host and port (8080: AWS, 80: Azure) 

### DVC commands
```
dvc init
```
```
dvc repro
```
```
dvc dag
```

-----------------------------------------------------------------

# AZURE-CICD-Deployment-with-Github-Actions

## Save the password.

## Run from terminal:
```bash
docker build -t chickenapp.azurecr.io/chicken:latest .
```
```bash
docker login chickenapp.azurecr.io
```
```bash
docker push chickenapp.azurecr.io/chicken:latest
```

## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run

-------------------------------------------------------------------

As of now, Azure deployment is showing error to case sensitivity that I absent-mindedly neglected while creating the docker image. I will be creating a new one in the upcoming days and re-work on deployment part.
Feel free to contribute :)
