# Southeast Asia Nicknames
from pyscript import display, document

def search_nickname(e):
    document.getElementById('display1').innerHTML = " "
    nickname = document.getElementById('country_input').value

    display(nickname, target="display1")