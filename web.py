'''
Please Note:
1.  The ChromeDriver is for the Version 104.0.5112.102 of Chrome,
    Please install another chromedriver.exe and add new .exe in this directory
    in case of difference in version

2. The given link (http://demoserver99.com/assignments/index2.html) was not working 
    hence I have found an altenative link (https://cybertext.wordpress.com/2007/04/30/fake-names-for-documentation/) 
    This link has a large record of names
    I have completed the assignment using this alternative link link

'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# function to validate input name and return name_list
def validate(name):
    # trim all extra spaces in string and return
    name = " ".join(name.split())
    name_list = name.split(" ")
    space_count = name.count(" ")
    
    if space_count == 0:
        return (False, [])
        
    if space_count == 1 or space_count == 2:
        for n in name_list:
            if not n.isalpha():
                return (False, [])

    return (True,name_list)


# Find names in the given link and calculate credits
def scrape(names):
    # Display "Searching" till data is extracted
    
    ops = Options()
    ops.add_experimental_option("detach", True)
    dc = DesiredCapabilities.CHROME
    driver = webdriver.Chrome(options=ops, desired_capabilities=dc)


    driver.get("https://cybertext.wordpress.com/2007/04/30/fake-names-for-documentation/")
    
    result = {}

    '''
    1. Full text search > If full name search gets all credits donot do partial search
    2. Search each name
    '''
    # 1. Try to match full name
    names = list(map(lambda x:x[0].upper() + x[1:].lower(), names))
    name_txt = " ".join(names)
    # Example xpath : '//*[text() = "John Doe"]'
    xpath = '//*[text() = \"' + name_txt + '\"]'
    result[name_txt] = {'type': 'full match', 
                        'credit': 0}

    try:
        element = driver.find_element("xpath",xpath)
    except Exception:
        print(f'Not Found: {name_txt}')
    else:
        result[name_txt]['tag'] = element.tag_name 
        result[name_txt]['txt_in_record'] = element.text 
        
        if name_txt == element.text:
            result[name_txt]['credit'] = len(names)

    finally:
        # 2. Partial search if full name does not match
        if result[name_txt]['credit'] != len(names):
        
            for name in names:
                result[name] = {}
                result[name] = {'type': 'partial match', 
                                'credit': 0}
                # Example xpath : '//li[contains(text(),"John")]'
                xpath = '//*[contains(text(),\"' + name + '\")]'
                
                try:
                    element = driver.find_element("xpath",xpath)
                except Exception:
                    print(f'Not Found: {name}')
                else:
                    result[name]['tag'] = element.tag_name 
                    result[name]['txt_in_record'] = element.text 
                    result[name]['credit'] = 1

    # Log the result into the console
    script = f"console.log({result})"
    driver.execute_script(script)
    