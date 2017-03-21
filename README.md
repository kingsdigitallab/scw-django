# Spanish Civil War Django Project

## Apps
* cms: wagtail content management system
* scw: main django app
* visualisation: Visualisation of Neumayer data

## Data
Raw data files are stored in /data and data should be automatically loaded
into the database by the provisioning script

## Provisioning
This project uses *Vagrant*. Ensure both Vagrant and VirtualBox are installed.
To provision a new vm, `cd` to the project directory and run `vagrant up`.

Server provisioning using fabric has not been setup yet, so please do not
attempt to provision using fabric!

## Running/Stopping/Logging In
Once you have created the VM, the following commands can be run from the
project directory:
* `vagrant up` - starts the VM
* `vagrant halt` - stops the VM
* `vagrant ssh` - ssh into the VM
* `vagrant destroy` - removes the VM completely (and permanently)
* `vagrant provision` - forces re-provisioning

Once you are SSH'd into the VM, you can run the server by issuing:
`./manage.py runserver 0:8000`. The server will then be accessible at
[http://127.0.0.1:8000](http://127.0.0.1:8000).

You can log into the django admin [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
or wagtail admin [http://127.0.0.1:8000/wagtail](http://127.0.0.1:8000/wagtail) pages
using the username `vagrant` and password `vagrant`.

## Management Scripts
NM import scripts should be run in the following order:
* `import_countries`
* `import_years`
* `import_events`
They should only be run *once* - they are designed for initial import of data into
a clean database only.
