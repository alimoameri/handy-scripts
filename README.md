# handy-scripts
A collection of handy scripts for everyday tasks, most of which were written using AI assistants.

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
python3 ali.urldecoder.py <encoded_url>
```
