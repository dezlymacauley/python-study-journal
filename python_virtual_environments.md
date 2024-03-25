## What is a Python virtual environment?

---

This is a self-contained location that enables you to maintain seperate
and isolated environments for each Python project.

This way each project can have its own Python version, packages,
and dependencies.

How to create a Python virtual environment?

First navigate to the directory 
where you want to create the virtual environment

In this guide I will be creating the environment 
in a directory called "Example"

```
cd /home/dezlymacauley/Example"
```

---

Next run this command to create the virtual environment:

```
python3 -m venv env
```

This will create a new directory in the folder called "env"

```
~/Example
❯ ls
 env
```

---

Next you need to activate the virtual environment:

Make sure you are still in the root of your project. 
I.e. not the "env" folder

```
cd /home/dezlymacauley/Example"
```


```
source env/bin/activate
```

Your virtual environment should now be activated. It will look like this:

```
~/Example
❯ source env/bin/activate

~/Example via  v3.11.8 (env)
❯
```

---

How to deactivate a Python environment:


Make sure you are still in the root of your project. 
I.e. not the "env" folder

```
cd /home/dezlymacauley/Example"
```

```
deactivate
```

---

## How to use pip to install packages:

To do that you will need pip which stands for "Preferred installer program" or
"PIP Installs Packages"

Note: To use this you will need to have pip installed on your system

```
sudo pacmam -S python-pip
```

---

To view which packages already exist in your virtual environment:

```
pip list
```

You will get an output like this:

```
~/Example via  v3.11.8 (env)
❯ pip list
Package    Version
---------- -------
pip        24.0
setuptools 65.5.0
```

---

You can download packages from "The Python Package Index":

https://pypi.org

In this guide I will be downloading a package called "requests"

```
pip install requests
```

After doing that if you use the "pip list" command again,
you should see an output like this:


```
~/Example via  v3.11.8 (env) took 4s
❯ pip list
Package            Version
------------------ --------
certifi            2024.2.2
charset-normalizer 3.3.2
idna               3.6
pip                24.0
requests           2.31.0
setuptools         65.5.0
urllib3            2.2.1
```

---

## How to save a list of all the dependencies used in your Python project:

"pip freeze" will list all of the Python packages installed in a project
and the version numbers of those packages. 

This output will then be saved to a text file called "requirements.txt"
```
pip freeze > requirements.txt
```

If you open that file, it will look like this:

```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
```

---

## How to use this requirements.txt file

Let's say that you have downloaded a Python project from someone.
In this scenario, you only have the code 
and the "requirements.txt" file of that project.

first create a virtual environment in that directory

```
python3 -m venv my_env
```

Activate the virtual environment:

```
source my_env/bin/activate
```

---

The next step is to install the dependencies listed in the "requirements.txt"
file

```
pip install -r requirements.txt
```

---
