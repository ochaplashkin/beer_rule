from socket import if_nameindex

import uvicorn
from app import App
import config

if __name__ == '__main__':
    cfg: config.Config = config.get_config()

    app: App = App(cfg)

    uvicorn.run(
        app=app,
        host=cfg.app.host,
        port=cfg.app.port
    )
