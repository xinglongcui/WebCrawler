# git basic user guide
## init workcopy environment
- mkdir [DIR]
- cd [DIR]
- git init
- git clone [URL]
## workcopy to stage
- add/rm
- checkout
## stage to HEAD
- commit
- reset
## HEAD to remote reposition
- push
- pull
## get specified version file
- git log [FILE]
- git checkout [version] [FILE]
## reset to specified version file
- git log [FILE]
- git checkout [version] [FILE]
- git add
- git commit
## More TODO

# add local project to github repository
## create a repository on github website
## cd local project, and init local git configuration
- cd Test
- git init
- git add .
- git commit "first commit" 
## set remote repository as local project URL
- git remote add origin https://github.com/xinglongcui/Test.git
- git remove -v
## push local project to remote
- git push origin master

# insert pic to markdown files
## insert internet pics
![Alt internet](https://github.com/xinglongcui/explorer/blob/master/Folder.jpg "internet jpg") 

## insert local pics
![avatar](italia.jpg "local 1") 
![avatar](2.jpg "local 2") 
![](italia.jpg "local 3") 
![](2.jpg "local 4") 
![Alt internet](2.jpg "local 5") 
![](resource/Folder.jpg "local 6") 

# spider project init
- scrapy startproject NAME
- cd NAME
- scrapy genspider DOMAIN URL
- cd NAME/spider
- edit DOMAIN.py
- scrapy crawl DOMAIN 
