from logchimera.utils import (
    NO_UNIQUE_WORDS_PLATEAU, 
    NO_UNIQUE_CHARS_PLATEAU, 
    NO_UNIQUE_LOG_LENGTHS_PLATEAU
)
from collections import Counter

def compute_no_unique_words(log_lines):
    """Compute unique number of words in dataset (40% weight)"""
    lines_in_dataset = []
    for line in log_lines:
        words_per_line_in_dataset = line.split(" ")
        lines_in_dataset.append(words_per_line_in_dataset)

    words_in_dataset = []

    for line in lines_in_dataset:
        for word in line:
            words_in_dataset.append(word)

    no_unique_words = Counter(words_in_dataset)
    no_unique_words = len(no_unique_words.keys())

    return no_unique_words

def compute_no_unique_chars(log_lines):
    """Compute unique number of characters in dataset (20% weight)"""
    chars_per_line_in_dataset = []
    for line in log_lines:
        chars_in_line = list(line)
        chars_per_line_in_dataset.append(chars_in_line)
    
    chars_in_dataset = []
    
    for line in chars_per_line_in_dataset:
        for char in line:
            chars_in_dataset.append(char)
    
    no_unique_chars = Counter(chars_in_dataset)
    no_unique_chars = len(no_unique_chars.keys())

    return no_unique_chars

def compute_no_unique_log_lengths(log_lines):
    """Compute unique number of log lengths in dataset (40% weight)"""
    log_lengths_per_line_in_dataset = []
    for line in log_lines:
        log_length = len(line)
        log_lengths_per_line_in_dataset.append(log_length)

    log_lengths_in_dataset = []

    for log_length in log_lengths_per_line_in_dataset:
        log_lengths_in_dataset.append(log_length)

    no_unique_log_lengths = Counter(log_lengths_in_dataset)
    no_unique_log_lengths = len(no_unique_log_lengths.keys())

    return no_unique_log_lengths

def compute_percentage_no_unique_words(no_unique_words):
    """Compute percentage of unique number of words in dataset (40% weight)"""
    if no_unique_words < 800:
        return 0.01
    elif no_unique_words >= 4000:
        return 1
    else:
        return no_unique_words*100/NO_UNIQUE_WORDS_PLATEAU/100

def compute_percentage_no_unique_chars(no_unique_chars):
    """Compute percentage of unique number of chars in dataset (20% weight)"""
    if no_unique_chars < 40:
        return 0.01
    elif no_unique_chars >= 90:
        return 1
    else:
        return no_unique_chars*100/NO_UNIQUE_CHARS_PLATEAU/100

def compute_percentage_no_unique_log_lengths(no_unique_log_lengths):
    """Compute percentage of unique log lengths in dataset (40% weight)"""
    if no_unique_log_lengths < 5:
        return 0.01
    elif no_unique_log_lengths >= 180:
        return 1
    else:
        return no_unique_log_lengths*100/NO_UNIQUE_LOG_LENGTHS_PLATEAU/100