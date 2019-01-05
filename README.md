# ImageRunner
Server-side code for an application that allows you to take a 
picture of code and run it. 
This was written for Hyland Software's hackathon.
### Running
First set up [pipenv](https://pipenv.readthedocs.io/en/latest/),
and in the project diretory run `pipenv install`. Next, make sure
that you have a authentication json file from your google cloud console, 
and haven't forgotten to set `GOOGLE_APPLICATION_CREDENTIALS`
to the location of your authentication file. Once that's done just run `python Main.py`,
and point your web browser to http://127.0.0.1:5000/.