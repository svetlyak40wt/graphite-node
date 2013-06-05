Graphite Node
=============

This is a bunch of scripts to setup and run Graphite monitoring on Ubuntu Linux.
This script installs Graphite locally and don't require you to create /opt/graphite
directory. I don't know why Graphite's creators have choosen such weird layout, but
in my opinion, running easy_install or pip with root priveleges is a bad idea.

Installation
------------

* Checkout the repository anywhere you like;
* Run `./install` script and go have a cup of coffee;
* If there is no errors, run `./carbon-cache start` to make collecting daemon up and running;
* Run `./graphite-web` to start the web frontend on localhost:8080;
* Push some data using any available library. For test, you can use `./ping` script.
