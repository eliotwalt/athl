# Scraper

Start by downloading the<a href="https://chromedriver.chromium.org/downloads"> chromedriver version </a>matching your chrome install. Place the executable at the same level as `ch_scrap.py` and `fr_scrap.py` and rename it `chromedriver` if necessary.

## Swiss Athletics
First, Install requirements
```bash
pip install -r requirements.txt
```
The `ch_scrap.py` script has the following optional arguments:
```bash
python ch_scrap.py -h
usage: ch_scrap.py [-h] [--driver DRIVER] [--dest DEST]

optional arguments:
  -h, --help       show this help message and exit
  --driver DRIVER  path to chromedriver exectuable. defaults to `./chromedriver`
  --dest DEST      path to chromedriver exectuable. defaults to `data/ch/`.

```
To use default arguments, create a `data/` directory at the root of the directory.
```
athl/
\_ data/
    \_ ch/
    \_fr/
\_ scrap/
    \_ chromedriver
    \_ ch_scrap.py
    \_ (fr_scrap.py)
    \_ [...]
```
Then, run the script specifying arguments if necessary:
```bash
python ch_scrap.py [OPTIONS]
```
After the execution of the script, one csv file will be written to disk per discipline and per category at the location specified in the arguments.
```
dest/ # default is data/ch/
\_ 800
    \_ H.csv
    \_ F.csv
\_ 1500
    \_ H.csv
    \_ F.csv
[...]
\_ 10000
    \_ H.csv
    \_ F.csv
```
