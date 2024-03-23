import setuptools

with open('README.md', 'r', encoding ='utf-8') as f:
    long_description =f.read()

__version__ ='0.0.0'

REPO_NAME ='MLOPs'
AUTHOR_USER_NAME ='Kalyani Gunda'
SRC_REPO ='mlProject'
AUTHOR_EMAIL ='kalyani47124@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    version= __version__ ,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description ='A small Python Packagr for ml applications',
    long_description=long_description, 
    long_description_content_type= 'text/markdown',  
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={
        'Bug_Tracker':f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
        },
    package_dir={'':'src'},
    package=setuptools.find_packages(where='src')

)