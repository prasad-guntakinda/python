# Virtual Environments:

### What is a Virtual Environment in Python?

- A virtual environment (venv) is a separate isolated Python setup created for a specific project.

- It allows you to install project-specific libraries without affecting your system Python or other projects.

#### Simple Real-Life Example

- Imagine:

- Project A needs:

```text
pyspark 3.4
pandas 1.5
```

- Project B needs:

```text
pyspark 3.1
pandas 2.0
```


- If both use the same system Python, packages will conflict.So we create separate environments:

- Env1 for Project A

- Env2 for Project B

---

### Why Virtual Environments Are Needed?

1. Avoid Package Conflicts: Each project can have its own versions.
2. Keep System Python Clean: Without venv, installing libraries globally can break Python or OS tools.

3. Required in Real Industry Projects Every Python project in companies uses:

    - ✅ virtualenv
    - ✅ venv
    - ✅ conda
    - ✅ poetry

4. Perfect for PySpark Setup, Spark requires correct versions of: `pyspark`, `py4j`, `pandas`

---

### How Virtual Environment Works?

- A virtual env creates Separate folder containing:

``` text

- myproject/
   venv/
      bin/
      lib/
      site-packages/


1. Python interpreter copy

2. Libraries (site-packages)

3. pip installer
```

---

### How to Create and Use Virtual Environment
✅ Step 1: Create Environment

```shell
python3 -m venv spark-env
```
- This creates a folder: `spark-env/`

✅ Step 2: Activate Environment

```shell
source spark-env/bin/activate
# On Windows:
spark-env\Scripts\activate
```
- After activation, you see: `(spark-env)`

✅ Step 3: Install Packages Inside It

```shell
pip install pyspark pandas
```

- These packages are installed only inside spark-env.

✅ Step 4: Deactivate When Done

```shell
deactivate
```
✅ Example Scenario (PySpark)

```shell
mkdir spark-learning
cd spark-learning

python3 -m venv spark-env
source spark-env/bin/activate

pip install pyspark

pip list
pip freeze
```
- Now Spark runs safely inside this environment.



✅ Virtual Environment vs System Python


| Feature | System Python | Virtual Environment |
| ------- | ------------- | ------------------- |
| Shared packages | 	✅ Yes	| ❌ No |
| Project isolation |	❌ No	 | ✅ Yes |
| Version conflicts |	✅ Possible |	❌ Avoided |




