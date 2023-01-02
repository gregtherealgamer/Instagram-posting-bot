from selenium import webdriver

# Specify the path to the ChromeDriver executable
driver = webdriver.Chrome('/path/to/chromedriver')

# Navigate to Instagram's login page
driver.get('https://www.instagram.com/accounts/login/')

# Find the username and password input fields and enter your login credentials
username_input = driver.find_element_by_name('username')
password_input = driver.find_element_by_name('password')
username_input.send_keys('your-username')
password_input.send_keys('your-password')

# Find the login button and click it
login_button = driver.find_element_by_css_selector('button[type="submit"]')
login_button.click()

# Wait for the page to load
driver.implicitly_wait(10)

# Navigate to the "Create Post" page
driver.get('https://www.instagram.com/create/details/')

# Find the file input field and enter the path to the photo you want to upload
photo_input = driver.find_element_by_name('photo')
photo_input.send_keys('/path/to/photo.jpg')

# Enter a caption for the post
caption_input = driver.find_element_by_css_selector('textarea[aria-label="Write a caption…"]')
caption_input.send_keys('My awesome Instagram post')

# Find the "Post" button and click it
post_button = driver.find_element_by_css_selector('button[type="submit"]')
post_button.click()

# Wait for the post to be published
driver.implicitly_wait(10)

# Close the browser
driver.close()
