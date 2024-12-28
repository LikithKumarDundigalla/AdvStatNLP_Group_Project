# Running Docker Image
To run this file you should have docker installed on your system

Run the following command to install docker on ubuntu 
```
sudo apt install docker
```
For windows you need to install  Windows Subsystem For Linux and then you can install docker on windows.

- <a href='https://docs.docker.com/desktop/setup/install/windows-install/'>Docker Desktop for windows</a>

Once docker is installed run the following command to pull the image to local which starts the download of the image(need to be done only once).

```
docker pull likith04/course-project-container-livate
```

To run the docker image run the following command
```
docker run -it -p "8881:8000" -v "$PWD:/app" "likith04/course-project-container-livate"
```
You'll have a Jupyter-Notebook running on the following address\
```
https://localhost:8888
```

# Running Notebook

## ⚠️  You should get your own authorization token from your huggingface account ⚠️

- Use the following link to get authorization/access tokens:

  - <a href='https://huggingface.co/settings/tokens/new?tokenType=write'>Create Access Tokens</a>

 - Give name of the access token and hit `Create token`

- Copy the generated token.

- Once you get your authorization token assign to the `authorization_token` variable in second cell.

- Then run all cells. The results will be stored in `scripts` folder.