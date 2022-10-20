import os

import click
import uvicorn

from core.config import config


@click.command()
@click.option("--env", type=click.Choice(["local", "dev", "prod"], case_sensitive=False), default="local")
def main(env: str) -> None:
    """
    Fast API 앱 실행
    """
    os.environ["ENV"] = env
    uvicorn.run(
        app="core.server:main_app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True if config.ENV != "prod" else False,
        workers=1,
    )


if __name__ == "__main__":
    main()
