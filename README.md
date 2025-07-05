# handy-scripts
A collection of handy scripts for everyday tasks, most of which were written using AI assistants.

## Installation
Place scripts in the `/usr/bin` directory. This allows you to run them directly from the shell using their name. For example:
```bash
handy.urldecoder https%3A%2F%2Fgoogle.com%2Fsearch%3Fq%3Durldecode%2Bbash.
```

Otherwise, you can run them with `python3` if it's a python scrpit or `bash` if it's a bash script:
```bash
python3 handy.urldecoder https%3A%2F%2Fgoogle.com%2Fsearch%3Fq%3Durldecode%2Bbash.
```

```bash
bash handy.mp4slen <directory_path>
```

## urldecoder
Decodes percent-encoded URLs, converting them back to their original human-readable format. 

### Input:
```
https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D9%85%D9%82%D8%AF%D9%85%D8%A7%D8%AA%DB%8C-mk346/%DA%A9%D8%A7%D8%B1-%D8%B9%DA%A9%D8%B3%D9%87%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-ch23774/%D8%A7%D8%AF%DB%8C%D8%AA-%D8%B9%DA%A9%D8%B3-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D8%A8%D8%AE%D8%B4-%D8%AF%D9%88%D9%85/
```

### Onput:
```
https://maktabkhooneh.org/course/آموزش-برنامه-نویسی-با-پایتون-مقدماتی-mk346/کار-عکسها-پایتون-ch23774/ادیت-عکس-پایتون-بخش-دوم/
```

### Usage:
```bash
python3 handy.urldecoder <encoded_url>
```

## mp4slen
Calculate the total length of all mp4 files in a directory.

### Usage:
```bash
bash handy.mp4slen <directory_path>
```