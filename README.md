# IIT-CS579-Project-1

## Installation

### Python packages
Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

### Build & install `graph-tool` 
See if you have the required dependencies [here](https://git.skewed.de/count0/graph-tool/-/wikis/installation-instructions#manual-compilation).
`graph-tool` is included as a submodule in this repository. To build it, run the following commands:
```bash
./autogen.sh
```

> [!CAUTION]
> Choose the appropriate method for your system. The following are the two most common methods.

<details>
<summary> <b>Using python virtual environnement</b> </summary>
<br>

<dl>
  <dd>
  Activate the python environment and run the following commands:
  <br>
  <br>

  ```bash
  ./configure --prefix=$HOME/.local
  make
  ```

  </dd>
</dl>
</details>

<details>
<summary> <b>Not using python virtual environnement</b> </summary>
<br>

<dl>
  <dd>
  Run the following commands:
  <br>
  <br>

  ```bash
  ./configure
  make
  ```

  </dd>
</dl>
</details>


After compilation, the module can be installed in the default Python module directory by running:
```bash
make install
```