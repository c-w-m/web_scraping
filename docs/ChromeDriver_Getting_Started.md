# ChromeDriver Getting started

This page documents how to start using ChromeDriver for __testing your website 
on desktop (Windows/Mac/Linux)__. 

You can also read:
* [Getting Started with Android](https://chromedriver.chromium.org/getting-started/getting-started---android) 
* [Getting Started withChromeOS](https://chromedriver.chromium.org/getting-started/chromeos)

## Setup
ChromeDriver is a separate executable that Selenium WebDriver uses to 
control Chrome. It is maintained by the Chromium team with help from 
WebDriver contributors. If you are unfamiliar with Selenium WebDriver, you 
should check out the [Selenium site](https://www.seleniumhq.org/).

Follow these steps to setup your tests for running with ChromeDriver:

* __Ensure Chromium/Google Chrome is installed in a recognized location__
  - ChromeDriver expects you to have Chrome installed in the default location 
for your platform. You can also [force ChromeDriver to use a custom location](https://chromedriver.chromium.org/capabilities#TOC-Using-a-Chrome-executable-in-a-non-standard-location) 
by setting a special capability.

* __Download the ChromeDriver binary for your platform under the [downloads](https://chromedriver.chromium.org/downloads)
section of this site__
  - unzip and mv to `/usr/bin/chromedriver`
    ```shell
    $ unzip chromedriver_linux64.zip
    $ sudo mv chromedriver /usr/bin/chromedriver
    $ sudo chown root:root /usr/bin/chromedriver
    $ sudo chmod +x /usr/bin/chromedriver
    ```
  
* __Help WebDriver find the downloaded ChromeDriver executable__
  - Any of these steps should do the trick:
1. include the ChromeDriver location in your `PATH` environment variable
2. (__Java only__) specify its location via the `webdriver.chrome.driver` system 
   property (see sample below)
3. (__Python only__) include the path to ChromeDriver when instantiating 
   `webdriver.Chrome` (see sample below)

## Sample test
__Java__:

```java
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.*;
import org.junit.Test;

public class GettingStarted {
  @Test
  public void testGoogleSearch() throws InterruptedException {
    // Optional. If not specified, WebDriver searches the PATH for chromedriver.
    System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");

    WebDriver driver = new ChromeDriver();
    driver.get("http://www.google.com/");
    Thread.sleep(5000);  // Let the user actually see something!
    WebElement searchBox = driver.findElement(By.name("q"));
    searchBox.sendKeys("ChromeDriver");
    searchBox.submit();
    Thread.sleep(5000);  // Let the user actually see something!
    driver.quit();
  }
}
```

__Python__:

```python
import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
```

## Controlling ChromeDriver's lifetime
The ChromeDriver class starts the ChromeDriver server process at creation 
and terminates it when quit is called. This can waste a significant amount 
of time for large test suites where a ChromeDriver instance is created per 
test. There are two options to remedy this:

1. Use the ChromeDriverService. This is available for most languages and 
   allows you to start/stop the ChromeDriver server yourself. See here for a Java example (with JUnit 4):

__Java__:
```java
import java.io.*;
import org.junit.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.*;
import org.openqa.selenium.remote.*;

public class GettingStartedWithService {

  private static ChromeDriverService service;
  private WebDriver driver;

  @BeforeClass
  public static void createAndStartService() throws IOException {
    service = new ChromeDriverService.Builder()
        .usingDriverExecutable(new File("/path/to/chromedriver"))
        .usingAnyFreePort()
        .build();
    service.start();
  }

  @AfterClass
  public static void stopService() {
    service.stop();
  }

  @Before
  public void createDriver() {
    driver = new RemoteWebDriver(service.getUrl(), new ChromeOptions());
  }

  @After
  public void quitDriver() {
    driver.quit();
  }

  @Test
  public void testGoogleSearch() {
    driver.get("http://www.google.com");
    // rest of the test...
  }
}
```

__Python__:
```python
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/path/to/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
driver.quit()
```

2. Start the ChromeDriver server separately before running your tests, and 
   connect to it using the Remote WebDriver.

__Terminal__:
```shell
$ ./chromedriver
Starting ChromeDriver 76.0.3809.68 (...) on port 9515
...
```

__Java__:
```java
import java.net.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.*;
import org.openqa.selenium.remote.*;

public class GettingStartedRemote {
  
  public static void main(String[] args) throws MalformedURLException {
    WebDriver driver = new RemoteWebDriver(
        new URL("http://127.0.0.1:9515"),
        new ChromeOptions());
    driver.get("http://www.google.com");
    driver.quit();
  }
}
```

# References

* [Web scraping |Easy Steps for Web Scraping | Methods | Python](https://medium.com/datadriveninvestor/web-scraping-easy-steps-for-web-scraping-methods-python-da3333f8d959)
* [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads)
* [Selenium](https://www.seleniumhq.org/)
* [How to Setup Selenium with ChromeDriver on Ubuntu 18.04 & 16.04](https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/)
* []()
* []()