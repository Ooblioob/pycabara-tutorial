pycabara-tutorial
=================

Tutorials on how to use pycabara (a Python implementation of Capybara). These tutorials use Behave, Selenium, and the Chrome webdriver.

###Feature files and Gherkin
The end-goal of automated acceptance testing (AAT) is to have a business analyst write every requirement as acceptance scenarios in a format that can be executed by a testing tool.

To achieve this:

1. All requirements must be written in format that can be read and interpreted by a testing tool. We are going to use the [Gherkin language](http://docs.behat.org/guides/1.gherkin.html), which is widely adopted by analysts and developers alike.
2. All requirements must be written in a deterministic way and should favor specification-by-example.
3. All requirements must be clear, consistent, and complete. In other works, if each and every feature is spelled out as a scenario in the AAT suite tests then, by definition, the application meets all expectations when all the tests pass.

In the end, if all an application's requirements are documented in the *feature* files, when the testing tool runs all the tests (and they all pass) then the application has met the acceptance criteria.

###Requirements that can be executed
In order to convert the requirements, as they are written by humans in the Gherkin language in the *feature* files, we use a Python testing framework called [Behave](https://behave.readthedocs.org/en/latest/). *Behave* is one in a category of testing tool generally described as behavior-driven development (BDD); hence the name *Behave*. In actuality it is a port of *Cucumber*, which was originally written for Ruby.

There are other BDD tools in the Python universe, to be sure. Today, we are starting with *Behave* in part to get the ball rolling and because it looks pretty good.

To learn more, please read the [Behave tutorials](http://jenisys.github.io/behave.example/tutorials/), look at [Behave on PyPI](https://pypi.python.org/pypi/behave), and check out [Behave on GitHub](https://github.com/behave/behave).

####Warning: name your *step* files with the 'steps_' prefix!
Don't name a Behave "step module" the same thing as another module, ever! The easy way to avoid naming conflicts is just add a prefix of *steps_* to the files' name. For example,

The following directory structure is good:

```
$PROJECT/
    +-- features/                   -- Contains all feature files.
    |       +-- steps/
    |       |     +-- steps_*.py    -- Step definitions for features.
    |       +-- environment.cfg     -- Settings file.
    |       +-- environment.py      -- Environment for global setup...
    |       +-- example*.feature    -- Feature files.
```


##Selenium
*Selenium* is a browser-testing tool that allows us to test a website from end-to-end, through the browser.

You can learn more about [Selenium](http://docs.seleniumhq.org/) at their website.

###Chrome Webdriver Prerequisite

1. As you might guess, the *ChromeDriver* requires the *Chrome* browser. Take a minute to read the information on the requirements for *Chrome* at the [Chrome Driver](https://code.google.com/p/selenium/wiki/ChromeDriver) wiki.
2. Install *ChromeDriver* version 26.0.1383.0, from January 2013, which can be downloaded from the *ChromeDriver* [downloads](https://code.google.com/p/selenium/downloads/list) page. Ensure that you select the proper driver for your environment, for example, in Ubuntu 64 development download chromedriver_linux64_26.0.1383.0.zip
3. Once downloaded, unzip the *chromedriver* file.

The Selenium driver will search the path for the *ChromeDriver* file, but it may be better to provide it the path to the folder where it is located. One that is accessible to the development environment.

By default the *ChromeDriver* is assumed to be copied to a folder that is accessible to all users and all projects.

```
$ sudo cp chromedriver /usr/bin/
```

###Running Behave

To start with, let's focus on only one feature file. It is under the *features* folder.

To install the dependencies:
```
$ workon pycabara-tutorial
$ pip install -r requirements.txt
```

Here's a quick way to see if everything is working.

```
$ python hello_world.py
```

Here's a quick example of how to run some *Behave* smoke tests.

```
$ behave -t=smoke_test
```
