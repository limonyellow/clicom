import sys
from time import sleep
from clicom import CLIApp

import typer

# app = typer.Typer()

app = CLIApp()


@app.command()
def say_hello(name: str):
    print(f"Hello {name}")


@app.command()
def f1():
    print(f"Hello f1")


@app.command()
def f2():
    print(f"Hello f2")


if __name__ == "__main__":
    app.start_app()


    # while True:
    #     try:
    #         i = input("next command:")
    #         sys.argv = [sys.argv[0], *i.split(sep=" ")]
    #         app()
    #     except KeyboardInterrupt:
    #         break
    #     except BaseException as e:
    #         print(e)
    #         print(sys.exc_info())
    #         pass

    #
    #
    # try:
    #     app()
    # except BaseException:
    #     print("can't stop")
    #     while True:
    #         sleep(1)
    #         print("can't stop.")
