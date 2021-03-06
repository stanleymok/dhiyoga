#dhiyoga

## Semantic Commit Messages

dhiyoga programmers uses the semantic commit messaging style

Format: `<type>(<scope>): <subject>`

`<scope>` is optional

### Example

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```

More Examples:

- `feat`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `refactor`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: (updating grunt tasks etc; no production code change)

References:

- https://www.conventionalcommits.org/
- https://seesparkbox.com/foundry/semantic_commit_messages
- http://karma-runner.github.io/1.0/dev/git-commit-msg.html

## frontend UBUNTU Setup
1. [Download WSL 20.04](https://www.microsoft.com/en-us/p/ubuntu-2004-lts/9n6svws3rx71?activetab=pivot:overviewtab)
2. in WSL, setup environment:
```
// populate apt-get's cache
$ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
// good to have gcc and g++
$ sudo apt-get install gcc g++ make
```
3. [Install nvm](https://itnext.io/nvm-the-easiest-way-to-switch-node-js-environments-on-your-machine-in-a-flash-17babb7d5f1b)
```
// install node and npm via nvm
$ nvm install --lts
// check 
$ npm -v 
$ node -v
$ git clone https://github.com/stanleymok/dhiyoga.git
$ cd dhiyoga
$ npm install
$ npm run serve
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Lints and fixes files
```
npm run lint
```

### Compiles and minifies for production
```
npm run build
=======
### SETUP

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
```

## backend UBUNTU Setup
1. [Download WSL 20.04](https://www.microsoft.com/en-us/p/ubuntu-2004-lts/9n6svws3rx71?activetab=pivot:overviewtab)
2. in WSL, setup environment:
```
$ cd dhiyoga
// pipenv manages libraries for your project so you can have multiple versions per project
$ pip3 install pipenv
// pipenv installs dependency based on pipflles
$ pipenv install
$ pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
// fix schema bug in backend
$ pipenv uninstall marshmallow
$ pip3 install marshmallow~=2.20.1 
$ pipenv shell
// run
(dhiyoga) $ python3 app.py
```


## backend package management
### install pip-compile
```
$ pip install --upgrade pip  # pip-tools needs pip==6.1 or higher (!)
$ pip install pip-tools
```
### creating the requirements and installing it back
```
$ pip-compile requirements.in
$ pip install -r requirements.txt
```

