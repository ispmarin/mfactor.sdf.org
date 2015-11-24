Title: Desktop Files on Debian/Ubuntu and XDG 
Date: 2015-11-23
Category: Linux
Modified: 2015-11-23 21:57
Tags: linux,desktop
Slug: desktop-files
Authors: Ivan Marin
Summary: Organizing custom launchers on Debian/Ubuntu XDG compliant

I've been struggling for a while now with custom launchers. First, a bit of organizatoin on how the launchers are supposed to work.

A `desktop file` is a file that describes a launcher for an application. This file will be indexed by a Window Manager, like KDE or XFCE and can be shown on the menus and etc. The [standard form](http://standards.freedesktop.org/desktop-entry-spec/latest/apa.html) of a desktop file is

```
[Desktop Entry]
Version=1.0
Type=Application
Name=Foo Viewer
Comment=The best viewer for Foo objects available!
Exec=fooview %F
Icon=fooview
Actions=Gallery;Create;
Categories=Network
```
This file should be put on a standard path in the system, like `~/.local/share/applications`. 

And how to check if the file you wrote is valid? Just run `desktop-file-validate` and it will point any errors that you have. 

## KDE blunder

After figuring it out how was the correct format for the file, my menus on KDE (and all actions, like changing the default application)was not changing anything. After searching for a long time, I found a solution: the context menu in Dolphin, to change the default application, was poiting to `.local/share/applications/mineapps.list` and KDE 5 was reading the file on `.config/mimeapps.list`. The solution? Exporting the default directory where KDE can find its icons. On my system, I changed .zshenv and added

```
XDG_DATA_DIRS=$XDG_DATA_DIRS:/home/ispmarin/.local/share/applications
```
done!
