# PIP:Python Package Installer

- It is the tool used to download and install external Python libraries.

- Example
- Python by default has only basic features.
- But if you want Spark support, you must install:
```shell
    pip install pyspark
```
- So pip brings PySpark from Python Package Index (PyPI).

### System Python:
- MacOS comes with its own Python setup that is used internally by the OS.
```shell
sudo pip install something
``` 
- You may break: Mac system tools, OS scripts, Default libraries
- So we avoid touching system Python.

---

## 3. Where does pip install store packages?

This depends on whether you're using:

✅ System Python
OR
✅ Virtual Environment

#### ✅ Case 1: Installing using System Python (Not Recommended)

If you do:

```shell
pip install numpy
pip show numpy
```

- without activating env, Packages go to global location like:`/usr/local/lib/python3.x/site-packages/`

- In my local it is stored in `/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/`

- if you run `pip uninstall numpy` it will show where it is installed and which files will be removed
- This means: All projects share the same library and Version conflicts possible


---

#### ✅ Case 2: Installing inside Virtual Environment ✅ (Recommended)

- If env is active:

```shell
source spark-env/bin/activate
pip install pyspark
```

- Then packages are installed inside:
- pyspark-learning/spark-env/lib/python3.x/site-packages/


- So ONLY that project uses it.


#### ✅ How pip decides where to install?

Answer: pip installs packages into the currently active Python environment.

- Check which Python is running
- Inside env:
- if `which python` shows `.../pyspark-learning/spark-env/bin/python` your `venv` location then it will be installed inside `spark-env`
- If `which python` shows `/usr/bin/python` then Then pip installs globally.


### ✅ How to see where pip is installing?

- show command tells the exact folder.

```shell 
pip show pyspark

# Example output:
#Location: /Users/prasad/pyspark-learning/spark-env/lib/python3.11/site-packages
```

---

✅ Important Concepts Summary

| Term | Meaning |
| ----- | ------- | 
| Python	| Programming language |
|pip	| Tool to install libraries |
| Package	| External library like pyspark |
| System Python |	Default OS Python |
| Virtual Env	| Separate isolated Python setup |
| site-packages	| Folder where libraries are stored |


#### ✅ Real-World Analogy

Think like this:

System Python = Whole Computer Software
Virtual Env = Separate Room for One Project
pip install = Bringing books into that room

So books (libraries) stay inside that room only.

✅ Quick Practical Check for You

Run these inside your env:

which python
which pip
pip show pyspark

