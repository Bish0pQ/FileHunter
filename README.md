# FileHunter
A program that hunts target hosting websites ([pomf](https://pomf.sinister.ly), [imgur](https://imgur.com), etc...) for files.
Please beware that this might download infected files, please always upload to VirusTotal or Malwr.

### Usage
_Outlined in `--help`_  
```
inori@lost-christmas ~/file-hunter $ python file-hunter.py --help
usage: file-hunter.py [--help] [--verbose] [--ext ex] [--results n] [--length n]
[--proxy adr] [--ssl] url

Hunt for files on hosting sites like pomf, mixtape.moe, or imgur. You can find
a list of alternatives here: https://goo.gl/wPDXdV

positional arguments:
  url                  url of the search target

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        enable verbose logging
  -e ex, --ext ex      extension to look for (no .)
  -r n, --results n    number of results to print
  -l n, --length n     length of file names
  -p adr, --proxy adr  proxy to use in IP:PORT format
  -s, --ssl            use SSL for proxies
```

##### Additional information
The following default arguments are currently in place:  
> `--verbose` : `false`  
> `--ext` : `zip`  
> `--results` : `5`  
> `--length` : `6`
