# Anaconda


- __Anaconda:__ is an open-source distribution of the Python and R programming languages designed to simplify package and environment management for data science, machine learning, and scientific computing. 
- It includes the conda package manager, a large collection of pre-installed libraries, and a graphical user interface (GUI) called Anaconda Navigator. 


- __Virtual environments__ created with Anaconda (called __conda environments__) are isolated directories that allow you to manage different projects with specific Python versions and packages without conflicts. 

## How to Set Up Virtual Environments Using Anaconda?

- After installing Anaconda, you can create and manage environments using either the __command-line interface (CLI)__ or the __Anaconda Navigator GUI__. 

### Using the Conda Command Line Interface (CLI)
- This is the most common and versatile method. 
- Open the terminal:
    - __Windows:__ Open the __Anaconda Prompt__ from the Start menu.
    - __macOS/Linux:__ Open a standard __Terminal__.

#### Create a new environment: 
- Use the `conda create` command, specifying a name for your environment and the desired Python version (optional).
```bash
# create venv only for this project in current working directory use -p option
conda create -p demo1-venv python=3.14
# create venv at global level use -n
conda create -n glb-venv python=3.10
conda create --name myenv python=3.10
# Replace myenv with your desired environment name and 3.10 with the Python version you need (e.g., python=3.8)
```

#### Activate the environment:

```bash
# list all existing envs
conda env list
conda activate myenv/
#Your command prompt should now show the environment's name in parentheses (e.g., (myenv)) to indicate it is active.
```

#### Install packages: 
- Install necessary packages using conda install or pip install.
```bash
conda install pandas numpy
# or
pip install scikit-learn
# or 
conda install pandas=1.5
```

#### Verifying the Installation
- Once the installation finishes, you can verify the packages are present by running: 
- `conda list` (Shows all packages in the active environment).
- Inside Jupyter Notebook:
```python
import pandas as pd
import matplotlib.pyplot as plt
print(pd.__version__)
```
- __Note:__ If a package isn't available via conda, you can still use pip install <package_name> while the environment is active, but it's best to try conda first to maintain environment consistency. 

#### Deactivate the environment: 
- When you are finished working in the environment, you can exit it.
```bash
conda deactivate
```

#### Manage environments:

```bash
#List all environments: 
conda env list
# Remove an environment: 
conda remove --name myenv --all
```

---

### Using the Anaconda Navigator (GUI)
- If you prefer a graphical interface, the Navigator is an excellent option. 

- Open Anaconda Navigator: Search for and launch "Anaconda Navigator" in your operating system's applications or Start menu.
- Navigate to the Environments tab: In the left sidebar, click on the Environments tab.
- Create a new environment: Click the Create button at the bottom of the environments list.
- Configure the environment: In the dialog box, enter a name for the environment and select the desired Python (or R) version from the dropdown menu.

- Finalize creation: Click Create. Navigator will set up the environment, and you can then manage installed/not-installed packages via the central panel.

- Activate an environment: Click on an environment name in the list to activate it. A green bar or arrow indicates the active environment. 

---


## How to setup an environment for a jupyter notebook using anaconda?

- To set up a specific Anaconda environment for use within a Jupyter Notebook, you must register that environment as a "kernel." 
- This allows you to switch between different environments directly from the Jupyter interface. 

### Quick Setup Guide (Command Line)

- Perform these steps in your Anaconda Prompt (Windows) or Terminal (macOS/Linux):
- __Activate your environment:__  `conda activate myenv`
- __Install the IPython kernel:__ This package allows Jupyter to communicate with this specific environment. `conda install ipykernel`
- Register the environment as a kernel: This makes it appear in the Jupyter menu.
`python -m ipykernel install --user --name myenv --display-name "Python (myenv)"   `
- __Launch Jupyter:__ You can now start Jupyter from your base environment or the new one.
```bash
conda install jupyter
jupyter notebook
```
### How to Use the Environment in Jupyter?

- Once Jupyter opens in your browser:
- New Notebooks: Click the New button (top right) and select your environment name from the dropdown list.
- Existing Notebooks: Open the notebook, `go to the top menu, select Kernel > Change Kernel, and pick your environment.` 

---

### Alternative: Automated Management 
- If you have many environments, you can install the `nb_conda_kernels` package in your base environment. - This automatically discovers any other environment that has `ipykernel` installed, removing the need to manually run the registration command (Step 3) for every new project. 

Do you need help installing specific data science libraries like Pandas or Matplotlib into your new environment? 


---
---


## in which directory new packages will be installed?

- When you install new packages in Anaconda, they are primarily stored in two locations:

### 1. The Environment's site-packages (Active Files)
- The actual library files that your Python code uses are installed within the specific environment's folder. The typical path follows this structure: 
- __Windows:__ `C:\Users\<Username>\anaconda3\envs\<env_name>\Lib\site-packages\`
- __macOS/Linux:__ /Users/<Username>/anaconda3/envs/<env_name>/lib/python<version>/site-packages/ 

### 2. The Package Cache (pkgs folder) 
- To save space, Anaconda first downloads and extracts every package into a central package cache directory. Instead of copying these large files into every environment that needs them, it uses hard links to point to this central cache. 

- __Windows:__ `C:\Users\<Username>\anaconda3\pkgs\`
- __macOS/Linux:__ `/opt/anaconda3/pkgs` 

### How to find your specific directory:
- Since installation paths can vary depending on where you installed Anaconda, you can use these commands to see exactly where your files are: 
- To find the environment path: Run `conda info --envs` or `conda env list`.
- To find the exact package location: Activate your environment and run:
- __Windows:__ where python
- __macOS/Linux:__ which python
- __Inside Python:__ Run import sys; print(sys.path) to see all directories where Python looks for packages. 


---


### References:

1. https://youtu.be/8unFN-JVVDk


