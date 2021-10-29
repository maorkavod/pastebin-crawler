# pastebin-crawler

This project is a Pastes crawler which using Django framework as code base.

the schedule job is managed by [django-cron]([Introduction &mdash; django-cron 0.5.1 documentation](https://django-cron.readthedocs.io/en/latest/introduction.html)). Django-cron lets you run Django/Python code on a recurring basis proving basic plumbing to track and execute tasks & using Django data models.



##### install

```bash
git pull git@github.com:maorkavod/pastebin-crawler.git -b master
cd pastebin-crawler
```

##### use

1. we first need to create virtual env 

    (you can use "which python" to locate your python bin path.)

```shell
python3 -m venv venv
```

2. now we can install all the requirements & migrate our model to SQLITE database. 
   
   (<u>for this project demo purpose</u> i choose sqlite db.)

```bash
./venv/bin/python3 -m pip install -r requirements.txt
./venv/bin/python3 manage.py makemigrations
./venv/bin/python3 manage.py migrate
```

3. Using the paste modal, you can view all the crawling data
   
   To gain access to the admin panel, we now create a Django super user.

```bash
./venv/bin/python3 manage.py createsuperuser
```

4. We will now enable our Django-cron. This modal will help us manage all the jobs we are iterating and view the output of each job. we will need to add this cron by using crontab. 

```bash
crontab -e
```

add this cron, and replace this placeholder with the actual <u>absolute</u> path to project folder {**path to project folder**}

```shell
* * * * * /{path to project folder}/venv/bin/python3 /{path to project folder}/manage.py runcrons
```





**<u>now after we set everything up, we will see this output inside our Django admin panel our schedule job runing results: </u>**

http://localhost:8000/admin/

<a href="https://i.ibb.co/bR6bPMX/Screen-Shot-2021-10-29-at-15-30-31.png"><img src="https://i.ibb.co/bR6bPMX/Screen-Shot-2021-10-29-at-15-30-31.png"/></a>

**<u>also specific job output within the model </u>**

<a href="https://i.ibb.co/b3kScYM/Screen-Shot-2021-10-29-at-15-35-51.png"><img width="60%" src="https://i.ibb.co/b3kScYM/Screen-Shot-2021-10-29-at-15-35-51.png"/></a>

**<u>As of now, pastebin results can also be viewed</u>**

<a href="https://i.ibb.co/7b174bC/Screen-Shot-2021-10-29-at-15-40-30.pnghttps://i.ibb.co/7b174bC/Screen-Shot-2021-10-29-at-15-40-30.png">
    
<img width='80%' src="https://i.ibb.co/7b174bC/Screen-Shot-2021-10-29-at-15-40-30.png"/></a>

###### note

The crawling function are located at : 

> https://github.com/maorkavod/pastebin-crawler/blob/master/app/jobs.py


