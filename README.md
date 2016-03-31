# Flask example for the sloppy.io cloud

This is an example to run a [nginx](http://nginx.org) frontend with a python [flask](http://flask.pocoo.org/) backend.
The example json has 3 variables, which will be replaced with the values commited 
through the sloppy cli.

Variables:

* PROJECT: Your sloppy project
* URI: The url of the project

## To start the nginx-flask
 
```
sloppy start -var=PROJECT:test -var=URI:test.sloppy.zone flask.json
```

In this example you can reach the app under http://test.sloppy.zone.
To see the logs of the nginx and the flask container you can use the cli:

```
sloppy logs test
```

