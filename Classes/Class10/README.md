# More JSAPI
########

This class continues with material from [Class 9](https://github.com/WUSTL-GIS-Programming-spring-2014/classinfo/blob/master/Classes/Class9/README.md)  

Resouces used in class: http://gissl-aa.wustl.edu/arcgis/rest/services


We are also covering [GitHub Pages](http://pages.github.com/) in more detail.  

## GitHub Pages  
  
### User page  
To create a user page, use your personal github account (e.g. @blordcastillo). You get one such "page" per user, so it is often used as a code showcase. But you can also have multiple pages and folders under this page.  
In your personal account (not in your class repository), create a new repository named ```<accountname>>.github.io```.
  
Example: [https://github.com/blordcastillo/blordcastillo.github.io](https://github.com/blordcastillo/blordcastillo.github.io)  
  
This repository is known as a GitHub pages repository. Create an ```index.html``` file in this repository, and it will be the default page at ```<accountname>>.github.io```.  
It will probably take several minutes (up to 10) for this page to show up the first time you create it. This delay is from the page being registered with GitHub's Domain Name Server.  
Other html files that you place in this directory will be publicly available too. Here are some examples:  
http://blordcastillo.github.io/  
http://blordcastillo.github.io/index.html *This should be the same page as above*  
http://blordcastillo.github.io/map.html  

### Project page  
A project page goes with a repository. You can have a project page associated with every repository.  
  
This easiest way to create a new repository page is to auto-generate one. Refer to [GitHub Pages](http://pages.github.com/) and choose the Project Site and Generate a Site options for more help on this.  

To create this page from scratch, you have to create a new branch of your repository. Try this with your class repository.  
From your class repository page, https://github.com/WUSTL-GIS-Programming-spring-2014/<Your user name>, open the branch dialog by clicking on the button that reads branch: **master**. You will have the option to "Find or create a branch..."   
In this box, enter ```gh-pages``` and hit return. This will create a new branch.  
  
Now, when you switch to this branch, and html pages you create become part of your repository page. Your page will reside at https://WUSTL-GIS-Programming-spring-2014.github.io/<Your user name>  
Want to switch to an auto-generated page? Click on the branches tab at your repository and delete the ```gh-pages``` branch.  
