Dockerfiles for various software
================================

Scattered notes on working with Docker images and containers
------------------------------------------------------------

### List of some basic commands[1]

``` example
docker build -t friendlyname .  # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyname  # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyname         # Same thing, but in detached mode
docker ps                                 # See a list of all running containers
docker stop <hash>                     # Gracefully stop the specified container
docker ps -a           # See a list of all containers, even the ones not running
docker kill <hash>                   # Force shutdown of the specified container
docker rm <hash>              # Remove the specified container from this machine
docker rm $(docker ps -a -q)           # Remove all containers from this machine
docker images -a                               # Show all images on this machine
docker rmi <imagename>            # Remove the specified image from this machine
docker rmi $(docker images -q)             # Remove all images from this machine
docker login             # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag            # Upload tagged image to registry
docker run username/repository:tag                   # Run image from a registry
```

### Building a docker image

There are multiple ways of making a new docker image (detailed steps for each approach are below):

1.  Start by running a docker container (with `docker run`) based on an existing image with bash, install software and make necessary changes, and then exit from the docker and commit the docker as a new image.
2.  Build a docker from a Dockerfile. In this method the commands for installing software and making changes are put in a Dockerfile. And the docker image is built via the `docker build` command (see Getting started from Docker Documentation: <https://docs.docker.com/get-started/part2/#dockerfile>).

I prefer the first method for debugging and testing, but this method is not easy to replicate because the steps for making a docker image are not easily retrievable. So, I usually start by the first method and open up a Dockerfile and add the steps to the Dockerfile as I install software /modify my container from bash. Finally, I test the Dockerfile by building an image from it to make sure it works.

1.  Starting a docker from a container

    I often like to test a Dockerfile by trying the installation commands one by one inside an image. Here are some example commands/steps:

    -   First change to the directory that contains the necessary files (e.g. software binary files). Mounting the directory to docker (by flag `-v`) saves some time in testing.
    -   To start a docker container based on ubuntu:14.04

        ``` example
        docker run -it -v `pwd`:`pwd` -w `pwd` ubuntu:14.04 /bin/bash
        ```

    -   To make an image from a container:

        ``` example
        docker commit ec65269ee843 ubuntu1404-with-salome-8p2
        ```

2.  Building the docker from a Dockerfile

    -   Building the docker using a Dockerfile requires downloading the necessary files for installation (if any) and the Dockerfile in a directory.
    -   Build the docker image by running this command (from inside the folder that contains the Dockerfile):

        ``` example
        docker build -t salome-ubuntu14 .       
        ```

### Adding user to docker container/image

See example in salome Dockerfile Also see this: <https://stackoverflow.com/questions/27701930/add-user-to-docker-container>

### Good tutorials

-   Getting started from Docker Documentation: <https://docs.docker.com/get-started/>
-   Docker RUN vs CMD vs ENTRYPOINT <http://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/>

### Some examples for running applications headless (using xvfb)

-   docker-selenium-xvfb: <https://github.com/sminnee/docker-selenium-xvfb>
-   docker-chrome-xvfb: <https://github.com/kfatehi/docker-chrome-xvfb> Also see README in Docker Hub: <https://github.com/kfatehi/docker-chrome-xvfb> and this article: <https://www.theguild.nl/headless-cucumbers-and-capybaras-with-selenium-and-hudson/>

### Pulling and running the image from the remote repository:

You can use docker run and run your app on any machine with this command:

``` example
docker run  username/repository:tag 
```

**If the image isn’t available locally on the machine, Docker will pull it from the repository.**

### Running docker from the current directory

``` example
docker run -i -t -v `pwd`:`pwd` -w `pwd` -u $(id -u):$(id -g)  paraview5_4  /bin/bash       
```

Adding `-u $(id -u):$(id -g)` results in the right user and group for the generated files.

### Running paraview inside docker

``` example
Xvfb :1 -screen 0 1024x768x16 2>/dev/null &  
DISPLAY=:1 pvpython --mesa-llvm    saveSphere.py 
```

### Installing xvfb to run pvpython inside docker

``` example
apt-get update
apt-get install -y xorg xvfb  dbus-x11 xfonts-100dpi xfonts-75dpi xfonts-cyrillic
```

### Docker creates files as root in mounted volume

See these solutions:

<https://stackoverflow.com/questions/30052019/docker-creates-files-as-root-in-mounted-volume>

<https://stackoverflow.com/questions/27925006/using-host-environment-variables-with-dockerfile>

and

<https://github.com/moby/moby/issues/3206>

These two files are mentioned as part of the solution in the previous link:

<https://github.com/BD2KGenomics/cgl-docker-lib/blob/master/mutect/runtime/Dockerfile#L16>

<https://github.com/BD2KGenomics/cgl-docker-lib/blob/master/mutect/runtime/wrapper.sh#L5>

**This seems to be working fine:**

``` example
docker_run="docker run --rm  -i   -v `pwd`:`pwd` -w `pwd`  -u $(id -u):$(id -g) marmarm/paraview:v5_4   /bin/bash" 
```

Adding `-u $(id -u):$(id -g)` results in the right user and group for the generated files. **But sometimes this methods generates an error if a user is not added to the docker image already.** To solve this problem add the following lines to the Docker file to add a user to the docker image. The name of the user doesn't really matter.

``` example
RUN useradd -ms /bin/bash  newuser
USER newuser
```

### How do I move repositories among organization in Docker Hub?

<https://success.docker.com/Cloud/Solve/How_do_I_move_repositories_among_organization_in_Docker_Hub%3F>

### Copy directory to other directory at Docker using ADD command[2]

``` example
ADD go /usr/local/  
```

will copy the contents of your local go directory in the *usr/local* directory of your docker image.

To copy the go directory itself in *usr/local* use:

``` example
ADD go /usr/local/go    
```

or

``` example
COPY go /usr/local/go   
```

### Create an image from a container

-   First list the dockers:

    ``` example
    docker ps -a
    ```

    ``` example
    docker ps -a
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                          PORTS               NAMES
    c82891fffea4        ubuntu:16.04        "/bin/bash"         43 minutes ago      Exited (0) About a minute ago                       kind_yonath
    2ee33d4a1ca8        ubuntu:16.04        "/bin/bash"         55 minutes ago      Exited (100) 43 minutes ago                         frosty_hypatia
    72191b13e285        ubuntu:16.04        "/bin/bash"         About an hour ago   Exited (0) 58 minutes ago                           eager_lamarr
    d8e616176ecf        ubuntu:14.04        "/bin/bash"         3 hours ago         Exited (0) 2 hours ago 
    ```

    Then, use `commit` to add an image from a container. For example

    ``` example
    docker commit c82891fffea4 openfoam4notteste
    ```

### Removing old and unused Docker images and containers

``` example
docker container prune
docker image prune
```

### Creating small dockers:

See this page: <https://www.ianlewis.org/en/creating-smaller-docker-images> and <https://www.dajobe.org/blog/2015/04/18/making-debian-docker-images-smaller/> Some points:

-   Use **one** `RUN` to prepare, configure, make, install and cleanup. This avoids making several docker layers.
-   Cleanup with: `apt-get remove --purge -y $BUILD_PACKAGES $(apt-mark showauto) && rm -rf /var/lib/apt/lists/*`
-   I looked at this file as an example: [<file:~/Dropbox/program/docker/openFoam4/Dockerfile.example>](~/Dropbox/program/docker/openFoam4/Dockerfile.example)

### Using the RUN instruction in a Dockerfile with 'source' does not work

Replace `source` with `.`

Footnotes
---------

[1] <https://docs.docker.com/get-started/part2/#recap-and-cheat-sheet-optional>

[2] <https://stackoverflow.com/questions/26504846/copy-directory-to-other-directory-at-docker-using-add-command>
