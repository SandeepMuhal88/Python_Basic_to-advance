
# python os module
## 1. Get Current Working Directory
```python
import os
cwd = os.getcwd()
print("Current Working Directory:", cwd)
```

## 2. Change Current Working Directory
```python
import os
os.chdir("/Users/username/Desktop")
print("Changed Directory:", os.getcwd())
```

## 3. List Files and Directories
```python
import os
files = os.listdir(".")
print("Files and Directories in Current Directory:", files)
```

## 4. Create a Directory
```python
import os
os.mkdir("new_folder")
print("Directory Created:", os.listdir("."))
```

## 5. Create Nested Directories
```python
import os
os.makedirs("folder1/folder2/folder3")
print("Nested Directories Created")
```

## 6. Remove a Directory
```python
import os
os.rmdir("new_folder")
print("Directory Removed:", os.listdir("."))
```

## 7. Remove Nested Directories
```python
import os
os.removedirs("folder1/folder2/folder3")
print("Nested Directories Removed")
```

## 8. Rename a File or Directory
```python
import os
os.rename("file1.txt", "new_file.txt")
print("File Renamed:", os.listdir("."))
```

## 9. Remove a File
```python
import os
os.remove("new_file.txt")
print("File Removed:", os.listdir("."))
```

## 10. Check if Path Exists
```python
import os
exists = os.path.exists("folder1")
print("Does folder1 exist?", exists)
```

## 11. Check if it’s a File or Directory
```python
import os
is_file = os.path.isfile("image.png")
is_dir = os.path.isdir("folder1")
print("Is image.png a file?", is_file)
print("Is folder1 a directory?", is_dir)
```

# Important commands
```python
pip install notebook
jupyter notebook
```

# Collaborating on a project
## steps
1. Go to GitHub and click on New Repository  
2. The owner adds the other two team members as collaborators  
3. everyone should Clone the Repository  
`git clone https://github.com/username/repository-name.git`  
4. Each person should work on a separate part of the project in different branches. 

```javascript
git switch -c branchName
git add .
git commit -m "saving file"
git push origin branchName
```
5. Pull Requests (PRs): Navigate to the Pull Requests tab and click on New Pull Request.
6. Keeping Your Branches Up to Date:
```javascript
git checkout backend-part
git pull origin main
```