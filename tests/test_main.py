from typer.testing import CliRunner

from clicom import CLIApp

runner = CliRunner()


def test_start_app():
    app = CLIApp()

    @app.command()
    def say_hello(name: str):
        print(f"Hello {name}")

    result = runner.invoke(app, ["exit"])
    assert result.exit_code == 0
