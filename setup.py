from setuptools import setup,find_packages
file = "requirements.txt"
hyphon = "-e ."
def get_requirements():
    with open(file) as f:
        content = f.readlines()
    content_list = [con.replace("\n","") for con in content]
    if hyphon in content_list:
        content_list.remove(hyphon)
    return content_list

     
    
setup(
    name = "sensor",
    author= "Monu joshi",
    author_email= "monujoshi471@gamil.com",
    install_requires = get_requirements(),
    packages = find_packages()
)