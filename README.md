# dhiyoga
World's free yoga repository

### SETUP

#### UBUNTU Setup
1. [Download WSL 20.04](https://www.microsoft.com/en-us/p/ubuntu-2004-lts/9n6svws3rx71?activetab=pivot:overviewtab)
2. in WSL, setup environment:
```
// populate apt-get's cache
$ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
// good to have gcc and g++
$ sudo apt-get install gcc g++ make
// install node and npm
$ sudo apt install nodejs
// check 
$ npm -v 
$ node -v
$ git clone https://github.com/stanleymok/dhiyoga.git
$ cd dhiyoga
$ npm init
$ sudo npm install @vue/cli
// store path to ./node_modules/.bin in your .bashrc file
$ vim ~/.bashrc
// add this line to end of file
// export PATH=/Users/Stanley/Desktop/dhiyoga/node_modules/.bin:$PATH
$ vue create dhiyoga
// pick merge
```
![image](https://user-images.githubusercontent.com/43771723/115562138-c966c500-a2e8-11eb-9398-4db0fffd1897.png)
```
$ cd dhiyoga
$ npm run server
```
