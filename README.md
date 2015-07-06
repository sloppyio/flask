# Flask example for the sloppy.io cloud

This is an example to run a [nginx](http://nginx.org) frontend with a python [flask](http://flask.pocoo.org/) backend.
The example json has 3 variables, which will be replaced with the values commited 
through the sloppy cli.

Variables:

* USERNAME: Your sloppy username
* PROJECT: Your sloppy project
* URI: The url of the project

## To start the nginx-flask
 
```
sloppy start flask.json -var=USERNAME:marc,PROJECT:test,URI:test.sloppy.zone
```

In this example you can reach the app under http://test.sloppy.zone.
To see the logs of the nginx and the flask container you can use the cli:

```
sloppy logs test
```

