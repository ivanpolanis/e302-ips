# Setting Up a Virtual Environment (VENV)

To run this code, it's highly recommended to set up a Virtual Environment to manage dependencies.

**Create the Virtual Environment:**

```sh
python -m venv env
```
**Modify the activation script**

Before activating the virtual environment, add the following line at the end of the \`*env/bin/activate*\` file:

```sh
export PYTHONPATH=$(pwd):$PYTHONPATH
```
**Activate the Virtual Environment:**

After modifying the script, activate the virtual environment with:

```sh
source env/bin/activate
```

**Install required dependencies:**

Once the virtual environment is activated, install the dependencies listed in \`*requirements.txt*\`:

```sh
pip install -r requirements.txt
```


