Flask Setup:

1. Setup Environment:

   - this is needed to store all dependencies in this folder.
     `python -m venv env`

2. Setup and Install Flask:

   - open cmd
     `mkdir flask_project` # make the folder named "flask_project"
     `cd flask_project` # redirect to the folder
     `code .` # this is to open your vscode, try alternative ways if you're not using same code editor.

   - press ctrl + `# this will open the command shell of the vscode, and put the command`python -m venv env`# env is the name of the folder`env\Scripts\activate`# run's the environment`pip install flask` # installs the flask and its dependencies

3. Make a file "app.py"
4. Run this in the command shell:
   `flask run` or `flask --app app run` # the app is the file you've made

Application of flask must have folder named "templates" to be rendered by flask.
