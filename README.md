# What's this app about ?

This project has been created for running static analysis (SAST / SCA) or dynamic (DAST).

 *-- Has not been publicly deployed yet*

## How to install

**(Note that by default it will create the app using ports _8000_ for _Django server_, _5678_ for _debugpy_ and _5432_ for _PostgreSQL_)**.
######
**(And we have a volume set on `C:/Projects/CodeAnalizer:/opt`)**.
######
**(You can change that on the [docker-compose.yml](https://github.com/Joshbv6/CodeAnalizer/blob/master/Docker/docker-compose.yml)**
**and on [Dockerfile](https://github.com/Joshbv6/CodeAnalizer/blob/master/Docker/Dockerfile)**.
####

Below we can choose installing the app automatically by running some scripts for **_Windows_** (*install.bat*), **_Linux_** (*install.sh*) or **_manually_**.

 
### **Windows OS**

For installing this app on Windows, clone this repository and simply double-click on *[install.bat](https://github.com/Joshbv6/CodeAnalizer/blob/master/install.bat)*

This will run the docker commands to install the Django App and open it up in the browser.

### **Linux OS**

For installing this app on Linux, clone this repository and simply run the *[install.sh](https://github.com/Joshbv6/CodeAnalizer/blob/master/install.sh)*

This will run the docker commands to install the Django App and open it up in the browser.

### **Manual Installation**

For installing this app manually, clone this repository:

###### `git clone https://github.com/Joshbv6/CodeAnalizer.git`
####
Once inside the cloned repo, go to the `Docker` folder and run:

###### `docker build -t codeanalizer_image .`
####

This will create the image codeanalizer_image based on the [Dockerfile](https://github.com/Joshbv6/CodeAnalizer/blob/master/Docker/Dockerfile)

Right after, once we have our image created, we need to build the container, according to our [docker-compose.yml](https://github.com/Joshbv6/CodeAnalizer/blob/master/Docker/Docker/docker-compose.yml):

###### `docker-compose -p codeanalizer_project up -d`
####

Once we've run both commands, the app is ready to go.

We need to start the container and that's it. We've set the entrypoint on the [Dockerfile](https://github.com/Joshbv6/CodeAnalizer/blob/main/Docker/Dockerfile) to automatically start the Django server as soon as the container starts.

So you can start the container and go to [http://localhost:8000](http://localhost:8000)

## How does the app work ?

For the moment, in this app we've only set one screen and one type of analysis ( SAST )

You will see on [http://localhost:8000](http://localhost:8000) one simple page with a text input:

We can freely submit a URL (the app only supports `github` or `gitlab` for the moment) of a public repository.

This will run `Static Application Security Testing (SAST)` analysis on this repository and display the results.

### TODOs

Since we have this simply formulary for the moment, among the plans for the future we have:
- *Add **Software Composition Analysis (SCA**)*
- *Add **Dynamic Application Security Testing (DAST)***
- *Add **Authentication / Authentification** system*
- *Add Database connection to **store repositories** analyzed and results obtained*
- *Add **download system** for downloading the results in different formats (json, xml...)*
- *Create a **public API** so you can connect and run those analysis from your own system*
- *Add **Bug Hunting** analysis ( ideally )*
- *Add **Code Smells** analysis ( ideally )*
- *Add **Penetration Testing** analysis for several vulnerability types using different payloads ( ideally )*

While we have several planned functionalities for the future, we want to approach these features carefully. Some of these ideas, like Bug Hunting analysis, Code Smells analysis, and Penetration Testing analysis, are ideal additions, but we need to acknowledge that they may present unforeseen challenges as we move forward.

It's important to note that, though we see their potential value, there may be instances where implementing these functionalities could introduce more complexities than solutions, or even lead to new issues that we hadn’t initially considered. So, while these features remain part of our roadmap, we may prioritize them differently or adjust our approach as we continue development and evaluate the technical feasibility and impact.

Currently, the focus is on refining the existing features and ensuring that the app is stable. We will continue to self-assess and look for opportunities to enhance the platform in a sustainable way.
