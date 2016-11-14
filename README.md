Simple Print Server
===================
A simple way to host a print webapp for a home or small business. Easier than configuring printers on ever-changing computers and simpler for guests to use too. 


How it works
------------
When a file is uploaded, the server calls the configured command on the path of the uploaded file (default command is `lpr`, which adds the file to the CUPS queue)

That's it. Improvements are in progress, but the core functionality is there now. 


Limitations
-----------
At this time, this has only been tested with one printer and on Linux and OS X. I have no idea how it would work on Windows, BSD, etc.


Setting it up
-------------
 * Connect a printer to your server of choice
 * `pip install -r requirements.txt`
 * `./firstrun.py`
 * `./run.py`

And we're off to the races! Note that you may need to do one of
 * Edit `run.py` to pass 'host=0.0.0.0' in `app.run()`
 * Do something else to forward the local port
if you want other computers to see the server


Reboot Persistance
------------------
TODO
