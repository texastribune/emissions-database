# News Apps Django Template


A custom template for News Apps Django projects. In a constant state of development.

## Requirements

- Django 1.7
- `virtualenvwrapper`
- Willingness to change this README to something that makes sense with your project post-generation

## Getting started

Please note – this guide assumes you are using OS X. If you aren't, you hopefully know the equivalent commands to make these things happen. If you don't, find someone to help you!

First, create the folder for you project.

```bash
mkdir <folder-of-your-project>
```

Then, create the virtual environment for your project.

```bash
mkvirtualenv <name-of-your-project>-dev
```

Next, install Django.

```bash
pip install django
```

You may need to re-initialize your virtual environment for autocomplete of Django commands. (`workon <name-of-your-project>-dev`)

Now we're ready to start cookin'. (The name of your project doesn't have to be the same as the folder you created.)

```bash
django-admin startproject --template=https://github.com/texastribune/newsapps-django-template/archive/master.zip --extension=gitignore,html,py <name-of-your-project> <folder-of-your-project>
```

Jump into your newly created project folder, get `git` initialized, and make your first commit!

```bash
cd <folder-of-your-project>
git init
git add .
git commit -m "Initial commit"
```

Now, install your local development requirements.

```bash
pip install -r requirements/local.txt
```

You should be able to run your first `migrate` now! Give it a try.

```bash
python <name-of-your-project>/manage.py migrate
```

And it should be able to handle `runserver` now, too.

```bash
python <name-of-your-project>/manage.py runserver
```

If everything checks out, you're good to go. Don't forget to replace this README!
