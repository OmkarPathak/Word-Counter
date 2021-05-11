# Word-Counter

A Python Word Counter module

[![Downloads](https://pepy.tech/badge/wordcounter)](https://pepy.tech/project/wordcounter)

# Installation

```bash
pip install wordcounter
```

# Usage

- Import the module after installation

```python
import wordcounter
```

- Create a object with sentence and delimiter as arguments to WordCounter class. Default value for delimiter is ' ' (a single space) 

```python
word_counter = wordcounter.WordCounter('The, quick, brown, fox, jumps, over, the, lazy, dog', delimiter=', ')
```

- Get word count

```python
word_counter.get_word_count()
```

- Get count of specific words

```python
word_counter.count('the')       # a case insensitive count

# if you want to have a case sensitive search just set ignore_case=False
word_counter.count('the', ignore_case=False)       # a case sensitive count
```

- Get word frequencies

```python
word_counter.get_word_frequencies()
```
