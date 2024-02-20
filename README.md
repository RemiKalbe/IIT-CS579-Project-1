# IIT-CS579-Project-1

## Installation

### Dependency Management

This project utilizes [pixi](https://pixi.sh/) for managing dependencies. To ensure a smooth setup, you must first install pixi. After installing pixi, navigate to the root directory of this project and run the following command:

```bash
pixi install
```

> [!WARNING]
> Please note that this project cannot run on Windows directly due to `graph-tool` not having a Windows binary available. To use this project on Windows, you would need to compile `graph-tool` yourself or leverage Windows Subsystem for Linux (WSL) for a compatible environment.

### Running the Project

You may either run the project in JupyterLab or in Visual Studio Code (VSCode).

#### JupyterLab

Simply run the following command in the terminal:
```bash
pixi run start
```

#### Visual Studio Code

When running the project in Visual Studio Code (VSCode), it's important to select the correct Python interpreter. Follow these steps:

1. Open the command palette with `Ctrl+Shift+P`.
2. Type and select `Python: Select Interpreter`.
3. Click on `Enter interpreter path...`.
4. Paste the following path: `.pixi/envs/default/python`.

This will set the Python interpreter to the one managed by pixi, aligning with the project's dependency management system.