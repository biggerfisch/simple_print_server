Simple Print Server
===================
A simple way to host a print webapp for a home or small business. Easier than configuring printers on ever-changing computers and simpler for guests to use too. 


How it works
------------
When a file is uploaded, the server calls the configured command on the path of the uploaded file (default command is `lp`, which adds the file to the CUPS queue)

That's it. Improvements are in progress, but the core functionality is there now. 


Limitations
-----------
At this time, this has only been tested with one printer and on Linux and OS X. I have no idea how it would work on Windows, BSD, etc.


Setting it up
-------------
 * Connect a printer to your server of choice
 * Install cups, such as: `sudo apt install cups`
 * `pip install -r requirements.txt`
 * `./firstrun.py`
 * `./run.py`

And we're off to the races! In order to make the service visible on the network, you may need to do one of the following:
 * Change `app.run()` to `app.run('host=0.0.0.0')` in `run.py`
 * Do something else to forward the local port  


Reboot Persistance
------------------
TODO

Screenshot
----------
![Example of running application](http://i.imgur.com/poZ6ouj.png)
