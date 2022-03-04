# colorscript.py

import time
import typer
import pathlib
from random import randint
from rich.console import Console
from rich.text import Text
from rich.color import Color
from rich.traceback import install

install()

app = typer.Typer()
console = Console()

name_path = pathlib.Path.cwd() / 'name'
name_files = sorted(name_path.glob('*'))

def load_file(file_path:pathlib.Path) -> str:
    with file_path.open(mode='r') as file:
        file_to_str = file.read()
    return file_to_str

def rand_file(file_list:list) -> pathlib.Path:
    rand_num = randint(0, len(file_list) - 1)
    return file_list[rand_num]

def rand_color() -> str:
    rand_num = randint(0,255)
    return Color.from_ansi(rand_num).name

def _print(
        text:str, 
        color:str=None, 
        random_color:bool=False, 
        blink:bool=False
        ) -> None:
    style_list = []
    if blink: 
        style_list.append('blink')
    if random_color:
        if color is None:
            style_list.append(rand_color())
    if color is not None:
        style_list.append(color)
    style = ' '.join(style_list)
    if len(style) == 0:
        console.print(text)
    else:
        console.print(text, style=style)

@app.command()
def config(
        path:str,
        load:bool = typer.Option(False, '-l', help='load config file'),
        create:bool = typer.Option(False, '-c', help='create config file'),
        ) -> None:
    '''
    Configure Application
    '''
    if load:
        console.print("WIP! config load selected", style='bold red')
    if create:
        console.print("WIP! config create selected", style='bold red')

@app.callback(invoke_without_command=True)
def callback(
        color:str = typer.Option(None, '-c', help='user defined color'),
        random_color:bool = typer.Option(False, '-r', help='use random color'),
        blink:bool = typer.Option(False, '-b', help='make text blink'),
        ) -> None:
    '''
    Print ANSII Text Art in Shell.
    '''
    file = rand_file(name_files)
    file_str = load_file(file)
    _print(file_str, color=color, blink=blink, random_color=random_color)

if __name__ == '__main__':
    app()
