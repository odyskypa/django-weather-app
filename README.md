# django-weather-app
## Setting-up a Django Application with AWS Elastic Beanstalk
### Deployment of the Application on Learner Lab Environment

Fo the deployment of the specific application follow the steps below:

1. Clone the repository locally with the following command:
    ```bash
        git clone git@github.com:odyskypa/django-weather-app.git
    ```

2. Downlaod and install `Python` version `3.8.10`
    - Find the installation files here: [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)

3. Configure the installed version of ***Python (3.8.10)*** to be your interpreter.

4. Install `virtualenv` and `awsebcli` in your main environment, with the following commands.
    
    ```bash
        sudo apt install virtualenv
        sudo apt install awsebcli
    ```

5. Create a new virtual environment, which will be used by AWS Elastic Beanstal for deploying the application, and then activate it.

    ```bash
        virtualenv ~/eb-virt
        source ~/eb-virt/bin/activate
    ```

6. Install the necessary dependencies of the application:

    ```bash
        pip install -r requirements.txt
    ```

7. In the main folder (where ***eb-env.py*** is located) create a file named `.env` and add the following infomation inside:
    ```
        AWS_ACCESS_KEY_ID = "YOUR-AWS_ACCESS_KEY_ID"
        AWS_SECRET_ACCESS_KEY = "YOUR-AWS_SECRET_ACCESS_KEY"
        AWS_SESSION_TOKEN = "YOUR-AWS_SESSION_TOKEN"
        AWS_REGION_NAME = "YOUR-AWS_REGION_NAME"
    ```
8. Run the `eb-env.py` script. It will print in the console commands for exporting the environmental variables required by the application to run. An example result is the following one:
    ```bash
        export AWS_ACCESS_KEY_ID="..."
        export AWS_SECRET_ACCESS_KEY="..."
        export AWS_SESSION_TOKEN="..."
        export AWS_REGION_NAME="..."
        eb create -ip LabInstanceProfile --service-role LabRole  --elb-type application --envvars "AWS_ACCESS_KEY_ID="...",AWS_SECRET_ACCESS_KEY="...",AWS_SESSION_TOKEN="...",AWS_REGION_NAME="...""
    ```
9. Copy the `export` commands to your terminal to generate the environmental variables. Skip the `eb create` command for now.

10. Check if the Django application is working properly in your local machine, by executing the following command:
    ```python
        python manage.py runserver
    ```
11. Shutdown the server by typing `Ctrl + C` for Windows or `Command + C` for MacOS.
12. Move inside the `ccbda` folder and initialize an AWS Elastic Beanstalk repository for handling the appllication. Start by executing the following commands:
    ```bash
        cd ./ccbda
        eb init -i
    ```
    - In the instructions appearing select the following options:
        - *Select a default region*:  `us-east-1 : US East (N. Virginia)`
        - *Select a platform*: `Python 3.8 running on 64bit Amazon Linux 2`
        - *Do you want to set up SSH for your instances*? `Y`
        - **All the remaining options just press `Enter` and allow the default values to be used**.
13. Once the initialization is completed, copy the last command of step **8** (`eb create ...`) and execute it in the terminal. The creation of the AWS EBS set-up will then start.
14. Once it is finished, you can check the health status of the AWS EBS with the following command:
    ```bash
        eb status
    ```
15. And for the development environment, once there are changes applied to the Django code, you can push the changes to AWS EBS with the following command:
    ```
        eb deploy
    ```
16. For accessing the logging system configured by Elastic Beanstalk, run the following command:
    ```
        eb logs
    ```
17. Ultimately, for terminating the EBS service on AWS for avoiding expenses, run the following command:
    ```
        eb terminate
    ```
    Then a message like the following is appearing: 
    
        - `The environment "ccbda-dev" and all associated instances will be terminated. To confirm, type the environment name: ccbda-dev`
    Type the environment name and press `Enter`
    After some minutes the deployment will be terminated.

### Comments on Current State of the Application
At the moment the code that integrates the QuickSight `embedURL` into the application's homepage is commented out, due to permission reasons. Although, in case the appropriate
permissions are enabled, by removing the comments of the file [views.py](https://github.com/odyskypa/django-weather-app/blob/main/ccbda/weatherapp/views.py) and removing the return statement `return "https://publuu.com/"` of the `get_url_quicksight` function, the application is functioning properly.
