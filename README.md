# GL-camp

To print host metrics you have to have installed `python 3+` on your host, clone repo or download `metrics.py` file and just type `python3 metrics.py`, this command will show CPU, memory and swap information.
If you want get specific data then type `python3 metrics.py mem` or `python3 metrics.py cpu`

Unfortunatelly i'm not so great in Linux, so i didn't found a way to run something in the docker namespace on behalf of root namespace, to get host data.
I have configured dockerfile in a way to sync `metrics.py` file from container to host through the docker volume, and you can run `metrics.py` from host in a volume, but it's doesn't make sense.

If you want to check a dockerfile:
  
  * execute the next command: `docker run --rm -d -v $(pwd)/:/script_folder/  pavelshalahai/gl-camp`
  * then execute: `python3 metrics.py` either `python3 metrics.py mem` or `python3 metrics.py cpu`
