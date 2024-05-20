import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()


@app.command("list")
def sample_func():
    subprocess.run(f"ls -l", shell=True)

@app.command("create-folder")
def sample_func():
    module_list_q = questions = [
        {
            'type':'list',
            'name': 'username',
            'message': 'Select any one username: ',
            'choices':[
                    {
                        'name': 'Eddie',
                    },
                    {
                        'name': 'Hughie',
                    },
                    {
                        'name': 'Matthew',
                    },
                    {
                        'name': 'Harvey',
                    },
            ],
        }
    ]

    username = prompt(module_list_q)

    rprint("[yellow]=============================================[yello]")
    rprint("[green bold]Enter folder name :[green bold]")
    folder_name = input()

    subprocess.run(f"mkdir {folder_name}_created_by_{username['username']}", shell=True)
@app.command("hello")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")



if __name__ == "__main__":
    app()
