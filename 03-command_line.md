# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >

1 cat: Streams a file to the terminal. $ cat temp.txt displays the contents of temp.txt

2 cp: copies a file from one file to another. cp -r command canp copy more directories with files in them.
(Put a / (slash) at the end of a directory? That makes sure the file is really a directory, so if the directory doesn't exist I'll get an error.)

3 env: shows hidden variables to terminal

4 pwd: displays the local directory.

5 pushd/popd: The pushd command saves the current working directory in memory so it can be returned to at any time, optionally changing to a new directory. The popd command returns to the path at the top of the directory stack.

6 mv: moves file from one specified directory to another.

7 rmdir: removes an entire directory.

8 grep: will search a given file for an expression, typically a string. grep "word" temp.txt.
grep "bl.g" temp.txt. The "." is a wildcard; it matches any character just once

9 touch: makes an empty file!
10 less: displays a file. This is one way to look at the contents of a file. It's useful because, if the file has many lines, it will "page" so that only one screenful at a time is visible.
---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  lists infmoration about files
`ls -a`  shows all entries, even hidden, those with start with "."
`ls -l`  long listing format
`ls -lh`  combines flag to show a long list, but formats the output into a human readable format
`ls -lah`  combines the previous flags to display all files, including hidden, in a human readable format
`ls -t`  lists files but sorts them by modification time
`ls -Glp`  inhibits display of group information, using a long listing format, and appends indicator to entries


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-a	Displays all files.
-b	Displays nonprinting characters in octal.
-c	Displays files by file timestamp.
-C	Displays files in a columnar format (default)
-d	Displays only directories.
-f	Interprets each name as a directory, not a file.
-F	Flags filenames.
-g	Displays the long format listing, but exclude the owner name.
-i	Displays the inode for each file.
-l	Displays the long format listing.
-L	Displays the file or directory referenced by a symbolic link.
-m	Displays the names as a comma-separated list.
-n	Displays the long format listing, with GID and UID numbers.
-o	Displays the long format listing, but excludes group name.
-p	Displays directories with /
-q	Displays all nonprinting characters as ?
-r	Displays files in reverse order.
-R	Displays subdirectories as well.
-t	Displays newest files first. (based on timestamp)
-u	Displays files by the file access time.
-x	Displays files as rows across the screen.
-1	Displays each entry on a line.
---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

The xargs command (by default) expects the input from stdin, and executes /bin/echo command over the input. The following is what happens when you execute xargs without any argument, or when you execute it without combining with any other commands.

Excelsior:~ X$ xargs 
hello there buddy
hello there buddy

