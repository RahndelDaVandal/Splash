# colorscript.py

import time
import typer
from pathlib import Path
from random import randint
from rich.console import Console
from rich.text import Text
from rich.color import Color
from rich.traceback import install

install()

app = typer.Typer()
console = Console()

name_path = Path.cwd() / 'name'
name_files = sorted(name_path.glob('*'))

def splash_text() -> None:
    path = Path.cwd() / 'splash_text'
    with path.open(mode='r') as file:
        splash_str = file.read()
    console.print(splash_str)

def load_file(file_path:Path) -> str:
    with file_path.open(mode='r') as file:
        file_to_str = file.read()
    return file_to_str

def rand_file(file_list:list) -> Path:
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
        console.print(Text.from_ansi(text), style=style)

@app.command()
def config(
        path:Path,
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
    file = rand_file(name_files)
    file_str = load_file(file)
    _print(file_str, color=color, blink=blink, random_color=random_color)

if __name__ == '__main__':
    app()
