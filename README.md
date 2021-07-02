# Download YouTube video using Python

This code is about to directly download YouTube video using `pytube` package.
You can just make your own txt file, which contain YouTube address and just run the `main.py`.


## .txt file example 
.txt file have to contain YouTube address that you want to download line by line as following example: 
```txt
https://www.youtube.com/watch?v=q-VV8pon-4s
https://www.youtube.com/watch?v=8thMw9JyxBE
```

## Environments Setting

The requirements.txt file contain all Python libraries needed to learn experiments.

```bash
pip install -r requirements.txt
```

Run the main code for downloading videos

```bash
python3 main.py --txt <txt file path > --save_path <save_folder_name>
```
