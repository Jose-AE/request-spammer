# import required modules
from selenium import webdriver


# Driver Code
if __name__ == "__main__":
    # create object
    browser = webdriver.Edge("msedgedriver.exe")

    # open browser and navigate to facebook
    browser.get("https://www.facebook.com")
