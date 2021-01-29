# Jaeger MongoDB grpc plugin

This is the repository that contains the MongoDB storage grpc plugin for Jaeger.

IMPORTANT: This plugin is still under development. The way it stores data may change.

The plugin uses [poetry](https://python-poetry.org/) to manage dependencies. To start, run

``poetry install``

## Compile

Jaeger requires a compiled version of this plugin in order to run it.

You can compile it using [pyinstaller](https://github.com/pyinstaller/pyinstaller). Use the main.spec file
to make sure that your plugin has all the dependencies it needs.

``pyinstaller main.spec``

This will create a dist folder in your local directory. You can then run the compiled plugin by running

``./dist/main/main``

## How it works

1. You need to checkout and build the last version of Jaeger (for testing purpose you can use the all-in-on).
2. You then need to build the plugin (follow the instructions above).
3. You then need to start a MongoDB server.
4. Using the env var ``SPAN_STORAGE_TYPE=grpc-plugin`` you can specify the storage type, in this case the grpc-plugin.
When you switch to this particular storage plugin you get two new flags:

* `--grpc-storage-plugin.binary` needs to be pointed to the grpc plugin that
   you compiled just above.
* `--grpc-storage-plugin.configuration-file` allows you to specify a path to a configuration file for your plugin. For now, this does nothing
as the plugin currently only supports ENV variable configuration.
  
These environment variables are 

* ``GRPC_PORT`` is the port your grpc plugin will run on. It defaults to ``1234``
* ``MONGO_URL`` is the connection string to the MongoDB server you started above. It defaults to ``localhost``.

5. You can now run Jaeger using the plugin. That looks like

``SPAN_STORAGE_TYPE=grpc-plugin  go run -tags ui ./cmd/all-in-one/main.go --grpc-storage-plugin.binary=./dist/main/main``

6. Now you can visit [http://localhost:16686/](http://localhost:16686/). By default
Jaeger traces itself. So you should be able to see some traces and you can have
a look at the raw data in MongoDB.
   
## Development

This project uses [black](https://github.com/psf/black), [pydocstyle](http://www.pydocstyle.org/en/5.1.1/usage.html),
and [isort](https://pycqa.github.io/isort/). To test the code, run

``pytest src``


### Formatting
This plugin is formatted by black. In order to format your code, run

``black src``

### Doc strings
This project use pyodcstyle to enforce Python docstring conventions. To check your code, run

``pydocstyle src``

### Import sorting

This project uses isort to sort its imports and maintain clean looking code. To sort your imports, run

``isort src``
