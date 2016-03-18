Title: Basic Python Setup for Data Science on Linux
Date: 2016-03-17
Category: data science
Tags: datascience, python
Authors: Ivan Marin
Summary: How to setup a basic data science environment with Python and Linux

Data scientists usually have a very diverse background and very different proficiency levels with some tools. This, as I usually say, is not negative, on the contrary! The best data science teams should have this diversity because the problems that they face are diverse by nature. 

So the idea of this post is to explain some basic concepts about Linux, linux shells, environment variables and how to glue everything together on a productive Python environment. 

## Linux and Linux shells
First, to get this out of the way: I really like the open source software philosophy and the software that the community writes, but sometimes you have to give and see that some battles are best fought elsewhere. *Linux*, technically, is just the [kernel](https://en.wikipedia.org/wiki/Linux_kernel) of a [operating system](https://en.wikipedia.org/wiki/Operating_system), usually composed of free and open source software, called [distribution](https://en.wikipedia.org/wiki/Linux_distribution). 
That's why sometimes you see "Debian GNU/Linux" distribution, because Debian, the Linux distribution, is composed of the [GNU](https://www.gnu.org/home.en.html) tools and the Linux kernel. But the name "Linux" got very popular and usually means *both* the kernel and the distribution. So don't worry if you say only Linux. I don't. 

So, after this enormous rant, what is a shell? A [shell](https://en.wikipedia.org/wiki/Unix_shell) command line interpreter that works as a user interface. A command line interpreter is exactly that, it interpretes and executes the commands given into instructions to the operating system. So shell is mostly just a program that reads commands typed into it! And best of all, it hides the details of the operating system. Shells can be used in an interactive fashion, where users type the commands, or in an automated way via *scripts*. A script is a file with a series of commands to be executed.

