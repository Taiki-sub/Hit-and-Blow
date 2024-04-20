from js import document
from pyodide.ffi import create_proxy

def add_new_content(event):
    print('Adding new content to tables')
    # For the player-table
    player_table = document.getElementById('player-table')
    new_row_player = player_table.insertRow(-1)
    for _ in range(3):  # Assuming there are three columns
        new_cell_player = new_row_player.insertCell(-1)
        new_cell_player.textContent = 'new'

    # For the cpu-table
    cpu_table = document.getElementById('cpu-table')
    new_row_cpu = cpu_table.insertRow(-1)
    for _ in range(3):  # Assuming there are three columns
        new_cell_cpu = new_row_cpu.insertCell(-1)
        new_cell_cpu.textContent = 'new'

add_button = document.getElementById('addContentBtn')
add_button.addEventListener('click', create_proxy(add_new_content))


def hoge(*args, **kwargs):
    input_test_element = document.getElementById('input_test')
    input_word = input_test_element.value
    print("fuga", "Input word: " + input_word)
    input_test_element.value = ''  # Clear input after processing
    print('Adding new content to tables')
    # For the player-table
    player_table = document.getElementById('player-table')
    new_row_player = player_table.insertRow(-1)
    for _ in range(3):  # Assuming there are three columns
        new_cell_player = new_row_player.insertCell(-1)
        new_cell_player.textContent = input_word

    # For the cpu-table
    cpu_table = document.getElementById('cpu-table')
    new_row_cpu = cpu_table.insertRow(-1)
    for _ in range(3):  # Assuming there are three columns
        new_cell_cpu = new_row_cpu.insertCell(-1)
        new_cell_cpu.textContent = input_word

test_button = document.getElementById('btn')
test_button.addEventListener('click', create_proxy(hoge))

def add_data_from_form(event):
    # Prevent form from submitting normally
    event.preventDefault()

    # Retrieve input values
    guess = document.getElementById('first-digit').value
    hit = document.getElementById('second-digit').value
    blow = document.getElementById('third-digit').value

    # Find table and add new row
    table = document.getElementById('player-table')
    new_row = table.insertRow(-1)
    new_row.insertCell(0).textContent = guess
    new_row.insertCell(1).textContent = hit
    new_row.insertCell(2).textContent = blow

    # Clear inputs after adding
    document.getElementById('first-digit').value = ''
    document.getElementById('second-digit').value = ''
    document.getElementById('third-digit').value = ''

form = document.getElementById('inputForm')
print(form)
form.addEventListener('submit', create_proxy(add_data_from_form))

def clear_terminal(self):
        self.console._js.terminal.clear()
    
def toggle_terminal(self, event):
    hidden = self.console.parent._js.getAttribute("hidden")
    if hidden:
        self.console.parent._js.removeAttribute("hidden")
    else:
        self.console.parent._js.setAttribute("hidden", "hidden")
        
#TODO:ヒント機能つけたい
#TODO:ターミナル実装
#TODO:デザインこだわる
#TODO:ゲーム続行機能

"""
* 実装順番
フォームの値を受け取ってplayer_numに設定   

"""