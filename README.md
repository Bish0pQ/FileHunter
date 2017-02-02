# FileHunter
A program that hunts target hosting websites ([pomf](https://pomf.sinister.ly), [imgur](https://imgur.com), etc...) for files

### Usage
_Outlined in `--help`_  
```
inori@lost-christmas ~/file-hunter $ python file-hunter.py --help
usage: file-hunter.py [--help] [--verbose] [--ext ex] [--results n] [--length n] [--proxy str] url

Hunt for files on hosting sites like Pomf.cat, Mixtape.moe...
You can find a list of alternatives here: https://github.com/tsudoko/long-live-pomf/blob/master/long-live-pomf.md

positional arguments:
  url                url of the search target

optional arguments:
  -h, --help         show this help message and exit
  -v, --verbose      enable verbose logging
  -e ex, --ext ex    extension to look for (no .)
  -r n, --results n  number of results to print
  -l n, --length n   length of file names
  -p str, --proxy str A single HTTP proxy to use (IP:PORT format)
```

##### Additional information
The following default arguments are currently in place:  
> `--verbose` : `false`  
> `--ext` : `zip`  
> `--results` : `5`  
> `--length` : `6`
> `--proxy` : `none`
