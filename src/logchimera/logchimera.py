import csv
from collections import Counter
import pandas as pd
import random
import ast

NO_UNIQUE_WORDS_PLATEAU = 4450
NO_UNIQUE_CHARS_PLATEAU = 90
NO_UNIQUE_LOG_LENGTHS_PLATEAU = 180

HETEROGENEITY_LEVEL = 0.23

def load_log_data(input_file):
    file = open(input_file, 'r')
    log_lines = []
    log_templates = []
    log_variables = []

    line = ""
    with open(input_file, newline='') as f:
        reader = csv.reader(f)
        line = next(reader)
        print(str(line))

    print(line)

    if str(line) == "['LineId', 'Content', 'EventId', 'EventTemplate']":
        for _, line, _, template in csv.reader(file, delimiter=','):
            log_lines.append(line)
            log_templates.append(template)
            log_variables = []
        return [log_lines, log_templates, log_variables]

    if str(line) == "['Content', 'EventTemplate', 'Variables']":
        for line, template, _ in csv.reader(file, delimiter=','):
            log_lines.append(line)
            log_templates.append(template)
            log_variables = []
        return [log_lines, log_templates, log_variables]

    if str(line) == "['LineId', 'Content', 'EventId', 'EventTemplate', 'Dataset']":
        for _, line, _, template, _ in csv.reader(file, delimiter=','):
            log_lines.append(line)
            log_templates.append(template)
            log_variables = []
        return [log_lines, log_templates, log_variables]

    return [log_lines, log_templates, log_variables]

def compute_no_unique_words(log_lines):
    """Proxy metric 1, 40% weight"""
    all_words = []
    for line in log_lines:
        words = line.split(" ")
        all_words.append(words)

    words_for_histogram = []

    for line in all_words:
        for word in line:
            words_for_histogram.append(word)

    res = Counter(words_for_histogram)
    res = len(res.keys())
    print("words", res)

    return res

def compute_percentage_no_unique_words(res):
    if res < 800:
        return 0.01
    elif res >= 4000:
        return 1
    else:
        return res*100/NO_UNIQUE_WORDS_PLATEAU/100

def compute_no_unique_chars(log_lines):
    """Proxy metric 2, 20% weight"""
    all_chars = []
    for line in log_lines:
        chars = list(line)
        all_chars.append(chars)
    
    chars_for_histogram = []
    
    for line in all_chars:
        for char in line:
            chars_for_histogram.append(char)
    
    res_chars = Counter(chars_for_histogram)
    res_chars = len(res_chars.keys())

    print("chars", res_chars)

    return res_chars

def compute_percentage_no_unique_chars(res):
    # res = 90
    if res < 40:
        return 0.01
    elif res >= 90:
        return 1
    else:
        return res*100/NO_UNIQUE_CHARS_PLATEAU/100

def compute_no_unique_log_lengths(log_lines):
    """Proxy metric 3, 40% weight"""
    all_num_of_chars = []
    for line in log_lines:
        number = len(line)
        all_num_of_chars.append(number)

    num_of_chars_for_histogram = []
    for number in all_num_of_chars:
        num_of_chars_for_histogram.append(number)
    
    res_number_of_chars = Counter(num_of_chars_for_histogram)
    res_number_of_chars = len(res_number_of_chars.keys())
    print("numbers", res_number_of_chars)

    return res_number_of_chars

def compute_percentage_no_unique_log_lengths(res):
    if res < 5:
        return 0.01
    elif res >= 180:
        return 1
    else:
        return res*100/NO_UNIQUE_LOG_LENGTHS_PLATEAU/100

def get_heterogeneity(input_file):
    """Estimate log heterogeneity for a given file."""
    log_data = load_log_data(input_file)
    log_lines = log_data[0]
    log_templates = log_data[1]
    log_variables = log_data[2]

    no_unique_words = compute_no_unique_words(log_lines)
    no_unique_chars = compute_no_unique_chars(log_lines)
    no_unique_log_lengths = compute_no_unique_log_lengths(log_lines)

    no_unique_words_percentage = compute_percentage_no_unique_words(no_unique_words)
    no_unique_chars_percentage = compute_percentage_no_unique_chars(no_unique_chars)
    no_unique_log_lengths_percentage = compute_percentage_no_unique_log_lengths(no_unique_log_lengths)

    print("words percentage", no_unique_words_percentage)
    print("chars percentage", no_unique_chars_percentage)
    print("numbers percentage", no_unique_log_lengths_percentage)

    res = 0.4*no_unique_words_percentage + 0.2*no_unique_chars_percentage + 0.4*no_unique_log_lengths_percentage
    print("Heterogeneity is:", res, "for dataset", input_file)
    return [no_unique_words_percentage, no_unique_chars_percentage, no_unique_log_lengths_percentage]


def increase_heterogeneity_for_file(path, HETEROGENEITY_LEVEL, DSET):
    file = open(path, 'r')
    log_lines_to_change = []
    log_templates_to_change = []
    file.readline()

    if path == "experiments/Combined_Dataset/Combined_Dataset_2k.log_structured.csv":
        for _, line, _, template, _ in csv.reader(file, delimiter=','):
            log_lines_to_change.append(line)
            log_templates_to_change.append(template)
    else:
        for _, line, _, template in csv.reader(file, delimiter=','):
            log_lines_to_change.append(line)
            log_templates_to_change.append(template)

    df = pd.read_csv(path)
    s = df['EventTemplate'].value_counts()
    s = df['EventTemplate'].value_counts().to_dict()
    listofkeys = []
    keys = {}
    for key in s:
        listofkeys.append(key)
        keys[key] = s[key]

    mixed_file = open("outlier_data/pool_mixed_outlier_data.csv", 'r')
    mixed_file.readline()

    log_lines_mixed = []
    log_templates_mixed = []
    dict_mixed = {}
    for line, template, _, source in csv.reader(mixed_file, delimiter=','):
        if source == DSET:
            continue
        else:
            log_lines_mixed.append(line)
            log_templates_mixed.append(template)
            dict_mixed[line] = template
    
    random.seed(1)
    increased_hetero_sample_content = random.sample(log_lines_mixed, len(log_lines_mixed))

    increased_hetero_sample_templates = []
    for el in increased_hetero_sample_content:
        increased_hetero_sample_templates.append(dict_mixed[el])

    list_of_values_apache = df.values.tolist()

    print("\n\nNow increasing heterogenety...")

    a = 0
    replacements = {}

    normalization_factor = 0

    for key in keys:
        if keys[key] >= 100:
            normalization_factor += keys[key]

    for key in keys:
        a += 1
        if keys[key] >= 100:
            print(keys[key])
            print(normalization_factor)
            replacements[key] = int(keys[key]/normalization_factor*len(log_lines_mixed) * HETEROGENEITY_LEVEL)


    A = 0
    for line in replacements:
        for i in range(replacements[line]):
            for j in range(len(list_of_values_apache)):
                if list_of_values_apache[j][3] == line:
                    new_mixed_line = increased_hetero_sample_content.pop(0)
                    new_mixed_template = increased_hetero_sample_templates.pop(0)
                    list_of_values_apache[j][1] = new_mixed_line
                    list_of_values_apache[j][3] = new_mixed_template
                    A += 1
                    break

    final_list_apache = []
    for i in range(len(list_of_values_apache)):
        final_list_apache.append([list_of_values_apache[i][1], list_of_values_apache[i][3]])

    final_df = pd.DataFrame(final_list_apache, columns=['Content', 'EventTemplate'])
    final_df['LineId'] = "0"
    final_df['EventId'] = "0"
    final_df['Variables'] = "0"

    header = ["Content", "EventTemplate", "Variables"]

    write_path_structured_temp = f"mixed_{DSET}.csv"
    write_path_log_temp = f"mixed_{DSET}.csv"
    
    final_df.to_csv(write_path_structured_temp, columns = header, index=False)
    final_df.to_csv(write_path_log_temp, columns = ["Content"], index=False)
    
    df_99 = pd.read_csv(write_path_structured_temp)
    df_99 = df_99[["Content"]]
    df_99_list = df_99.values.tolist()

    df_original = pd.read_csv(f"experiments/{DSET}/{DSET}_2k.log_structured.csv")
    df_original = df_original[["Content"]]

    df_original_list = df_original.values.tolist()
    equals = 0
    a = 0
    for original, modified in zip(df_original_list, df_99_list):
        a += 1
        if original == modified:
            print(original)
            equals += 1
    print("HETEROGENEITY_LEVE", HETEROGENEITY_LEVEL)
    print("No original remaining: ", equals)
    print("Percentage replaced", 100-equals*100/2000)
    percentage = 100-equals*100/2000
    print("len(log_lines_mixed)", len(log_lines_mixed))
    print("A", A)

    final_write_path_structured = f"datasets_mixing/{int(percentage)}_{DSET}.csv"
    final_write_path_log = f"datasets_mixing/{int(percentage)}_{DSET}_log.csv"
    
    perc = int(percentage)

    if perc == 5 or perc == 10 or perc == 15 or perc == 20 or perc == 25 or perc == 8:
        final_df.to_csv(final_write_path_structured, columns = header, index=False)
        final_df.to_csv(final_write_path_log, columns = ["Content"], index=False)
        print("Now getting heterogeneity")
        get_heterogeneity(final_write_path_structured)

pool_labeled_data_file = "fuzzing_experiments/pool_dataset/pool_labeled_data.csv"

def fuzz_data(input_file, DSET, R_LEVEL):
    dataset_lines = []
    dataset_templates = []

    file = open(input_file, 'r')
    dataset_lines = []
    dataset_templates = []
    file.readline()
    for line, template, _ in csv.reader(file, delimiter=','):
        dataset_lines.append(line)
        dataset_templates.append(template)

    file = open(pool_labeled_data_file, 'r')
    labeled_lines = []
    labeled_templates = []
    labeled_variables = []
    file.readline()
    for _, line, template, variable in csv.reader(file, delimiter=','):
        labeled_lines.append(line)
        labeled_templates.append(template)
        labeled_variables.append(variable)

    fuzzed_dset_lines = []
    fuzzed_dset_templates = []
    fuzzed_dset_variables = []
    
    found = False
    for line in dataset_lines:
        found = False
        for lbl_line, lbl_temp, lbl_var in zip(labeled_lines, labeled_templates, labeled_variables):
            if line == lbl_line:
                fuzzed_dset_lines.append(line)
                fuzzed_dset_templates.append(lbl_temp)
                fuzzed_dset_variables.append(lbl_var)
                found = True
                break
        if not found:
            print("\n\nNot found", line)

    for line, temp, var in zip(fuzzed_dset_lines, fuzzed_dset_templates, fuzzed_dset_variables):
        print(line, temp, var)
    
    dict = {'Content': fuzzed_dset_lines, 'EventTemplate': fuzzed_dset_templates, 'Variables': fuzzed_dset_variables}  
    df = pd.DataFrame(dict) 
    df.to_csv(f'final_logs_experiments/fuzzing/{DSET}_{R_LEVEL}_fuzzed.csv', index=False) 
    
    variables_unique_file = "variables_unique.csv"
    file = open(variables_unique_file, 'r')
    variables_unique_pool = []
    file.readline()
    for var in csv.reader(file, delimiter=','):
        variables_unique_pool.append(var)

    random.seed(1)
    variables_sample = random.sample(variables_unique_pool, 7000)
    a = 0
    for line, temp, var in zip(fuzzed_dset_lines, fuzzed_dset_templates, fuzzed_dset_variables):
        list_var = []
        if "[" in var:
            a += 1
            list_var = var.split(",")
            list_var[0] = list_var[0].replace("[", "")
            list_var[-1] = list_var[-1].replace("]", "")
            print(list_var)
            if a == 3:
                break
        else:
            print("line", line)
            break
    
    a = 0
    for i in range(len(fuzzed_dset_lines)):
        a += 1
        list_var = []
        if "[" in fuzzed_dset_variables[i]:
            print("fuzzed_dset_lines[i]", fuzzed_dset_lines[i])
            list_var = fuzzed_dset_variables[i].split(",")
            list_var[0] = list_var[0].replace("[", "")
            list_var[-1] = list_var[-1].replace("]", "")
            for vr in list_var:
                repl = variables_sample.pop(0)
                repl = repl[0]
                fuzzed_dset_lines[i] = fuzzed_dset_lines[i].replace(vr, repl)
            print("fuzzed_dset_lines[i]", fuzzed_dset_lines[i])
        else:
            print("fuzzed_dset_lines[i]", fuzzed_dset_lines[i])
            print("fuzzed_dset_variables[i]", fuzzed_dset_variables[i])
            repl = variables_sample.pop(0)
            repl = repl[0]
            print("variables_sample.pop(0)", repl)
            fuzzed_dset_lines[i] = fuzzed_dset_lines[i].replace(fuzzed_dset_variables[i], repl)
            print("fuzzed_dset_lines[i]", fuzzed_dset_lines[i])

    dict = {'Content': fuzzed_dset_lines, 'EventTemplate': fuzzed_dset_templates, 'Variables': fuzzed_dset_variables}  
    df = pd.DataFrame(dict) 
    df = df[df['Content'].str.len()<600]

    tail_no = 0
    if len(df.index) < 2000:
        tail_no = 2000 - len(df.index) 
    
    last_rows=df.tail(tail_no)
    df = pd.concat([df, last_rows])
    
    df.to_csv(f'final_logs_experiments/fuzzing/{DSET}_{R_LEVEL}_fuzzed.csv', index=False) 
    df = df["Content"]
    df.to_csv(f'final_logs_experiments/fuzzing/{DSET}_{R_LEVEL}_fuzzed_log.csv', index=False, header=False) 
    
    get_heterogeneity(f'final_logs_experiments/fuzzing/{DSET}_{R_LEVEL}_fuzzed.csv')
    return 0



def increase_heterogeneity_for_file_automatic(path, HETEROGENEITY_LEVEL, DSET):
    file = open(path, 'r')
    log_lines_to_change = []
    log_templates_to_change = []
    file.readline()

    parameter_list = []
    for _, line, _, template, parameter in csv.reader(file, delimiter=','):
        log_lines_to_change.append(line)
        log_templates_to_change.append(template)
        parameter_list.append(parameter)

    df = pd.read_csv(path)
    s = df['EventTemplate'].value_counts()
    print(s)
    s = df['EventTemplate'].value_counts().to_dict()
    print(s)
    print()
    listofkeys = []
    keys = {}
    for key in s:
        listofkeys.append(key)
        keys[key] = s[key]
    print("\n\n")
    print("keys", keys)
    print("listofkeys", listofkeys)

    mixed_file = open("outlier_data/pool_mixed_outlier_data.csv", 'r')
    mixed_file.readline()

    log_lines_mixed = []
    log_templates_mixed = []
    dict_mixed = {}
    for line, template, _, source in csv.reader(mixed_file, delimiter=','):
        if source == DSET:
            continue
        else:
            log_lines_mixed.append(line)
            log_templates_mixed.append(template)
            dict_mixed[line] = template
    
    random.seed(1)
    increased_hetero_sample_content = random.sample(log_lines_mixed, len(log_lines_mixed))

    increased_hetero_sample_templates = []
    for el in increased_hetero_sample_content:
        increased_hetero_sample_templates.append(dict_mixed[el])
    
    list_of_values_apache = df.values.tolist()

    print("\n\nNow increasing heterogenety...")

    a = 0
    replacements = {}

    normalization_factor = 0

    for key in keys:
        if keys[key] >= 100:
            normalization_factor += keys[key]

    for key in keys:
        a += 1
        if keys[key] >= 100:
            print(keys[key])
            print(normalization_factor)
            replacements[key] = int(keys[key]/normalization_factor*len(log_lines_mixed) * HETEROGENEITY_LEVEL)
    print("replacements", replacements)


    A = 0
    for line in replacements:
        for i in range(replacements[line]):
            for j in range(len(list_of_values_apache)):
                if list_of_values_apache[j][3] == line:
                    new_mixed_line = increased_hetero_sample_content.pop(0)
                    new_mixed_template = increased_hetero_sample_templates.pop(0)
                    list_of_values_apache[j][1] = new_mixed_line
                    list_of_values_apache[j][3] = new_mixed_template
                    A += 1
                    break

    final_list_apache = []
    for i in range(len(list_of_values_apache)):
        final_list_apache.append([list_of_values_apache[i][1], list_of_values_apache[i][3]])

    final_df = pd.DataFrame(final_list_apache, columns=['Content', 'EventTemplate'])
    final_df['LineId'] = "0"
    final_df['EventId'] = "0"
    final_df['Variables'] = "0"

    header = ["Content", "EventTemplate", "Variables"]

    write_path_structured_temp = f"automatic_fuzz_data/temp/{DSET}/mixed_{DSET}.csv"
    write_path_log_temp = f"automatic_fuzz_data/temp/{DSET}/mixed_{DSET}.csv"
    
    final_df.to_csv(write_path_structured_temp, columns = header, index=False)
    final_df.to_csv(write_path_log_temp, columns = ["Content"], index=False)
    
    df_99 = pd.read_csv(write_path_structured_temp)
    df_99 = df_99[["Content"]]
    df_99_list = df_99.values.tolist()

    df_original = pd.read_csv(f"automatic_fuzz_data/{DSET}.csv")
    df_original = df_original[["Content"]]

    df_original_list = df_original.values.tolist()
    equals = 0
    a = 0
    for original, modified in zip(df_original_list, df_99_list):
        a += 1
        if original == modified:
            print(original)
            equals += 1

    print("HETEROGENEITY_LEVE", HETEROGENEITY_LEVEL)
    print("No original remaining: ", equals)
    print("Percentage replaced", 100-equals*100/2000)
    percentage = 100-equals*100/2000
    print("len(log_lines_mixed)", len(log_lines_mixed))
    print("A", A)

    final_write_path_structured = f"automatic_fuzz_data/{DSET}/{int(percentage)}_{DSET}.csv"
    final_write_path_log = f"automatic_fuzz_data/{DSET}/{int(percentage)}_{DSET}_log.csv"
    
    perc = int(percentage)

    if perc == 5 or perc == 10 or perc == 15 or perc == 20 or perc == 25 or perc == 8:
        final_df.to_csv(final_write_path_structured, columns = header, index=False)
        final_df.to_csv(final_write_path_log, columns = ["Content"], index=False)
        print("Now getting heterogeneity")
        get_heterogeneity(final_write_path_structured)

def fuzz_data_automatic(input_file, DSET, R_LEVEL):
    file = open(input_file, 'r')
    dataset_lines = []
    dataset_templates = []
    file.readline()

    labeled_lines = []
    labeled_templates = []
    labeled_variables = []

    for _, line, _, template, variables in csv.reader(file, delimiter=','):
        labeled_lines.append(line)
        labeled_templates.append(template)
        labeled_variables.append(variables)

    fuzzed_dset_lines = labeled_lines
    fuzzed_dset_templates = labeled_templates
    fuzzed_dset_variables = labeled_variables
    vars = []
    for el in fuzzed_dset_variables:
        el = ast.literal_eval(el)
        el = [n.strip() for n in el]
        vars.append(el)
    fuzzed_dset_variables = vars

    file = open(f"automatic_fuzz_data/{DSET}_Parsed/{R_LEVEL}_{DSET}_Parsed.csv", 'r')
    mixed_lines = []
    mixed_templates = []
    file.readline()
    for line, template, _ in csv.reader(file, delimiter=','):
        mixed_lines.append(line)
        mixed_templates.append(template)

    variables_unique_file = "variables_unique.csv"
    file = open(variables_unique_file, 'r')
    variables_unique_pool = []
    file.readline()
    for var in csv.reader(file, delimiter=','):
        variables_unique_pool.append(var)

    random.seed(1)
    variables_sample = random.sample(variables_unique_pool, 6000)

    file = open(pool_labeled_data_file, 'r')
    gdth_mix_labeled_lines = []
    gdth_mix_labeled_templates = []
    gdth_mix_labeled_variables = []
    file.readline()
    for _, line, template, variable in csv.reader(file, delimiter=','):
        gdth_mix_labeled_lines.append(line)
        gdth_mix_labeled_templates.append(template)
        gdth_mix_labeled_variables.append(variable)

    a = 0
    Z = 0
    for i in range(len(fuzzed_dset_lines)):
        if mixed_lines[i] == fuzzed_dset_lines[i] and len(fuzzed_dset_variables[i]) > 0:
            for vr in fuzzed_dset_variables[i]:
                repl = variables_sample.pop(0)
                repl = repl[0]
                fuzzed_dset_lines[i] = fuzzed_dset_lines[i].replace(vr, repl)
        elif mixed_lines[i] != fuzzed_dset_lines[i]:
            Z += 1
            a += 1
            try:
                zz = gdth_mix_labeled_lines.index(mixed_lines[i])
            except ValueError:
                continue
            
            list_var = []
            if "[" in gdth_mix_labeled_variables[gdth_mix_labeled_lines.index(mixed_lines[i])] and "]" in gdth_mix_labeled_variables[gdth_mix_labeled_lines.index(mixed_lines[i])] and "," in gdth_mix_labeled_variables[gdth_mix_labeled_lines.index(mixed_lines[i])]:
                list_var = gdth_mix_labeled_variables[gdth_mix_labeled_lines.index(mixed_lines[i])].split(",")
                list_var[0] = list_var[0].replace("[", "")
                list_var[-1] = list_var[0].replace("]", "")
                
                for vr in list_var:
                    repl = variables_sample.pop(0)
                    repl = repl[0]
                    mixed_lines[i] = mixed_lines[i].replace(vr, repl)
                    break

                if len(mixed_lines[i]) > 1200:
                    continue
                else:
                    fuzzed_dset_lines[i] = mixed_lines[i]
            else:
                fuzzed_dset_lines[i] = mixed_lines[i]
                
    a = 0
    for el in fuzzed_dset_lines:
        print(el)
        print()
        a+=1
        if a == 10:
            break

    dict = {'Content': fuzzed_dset_lines, 'EventTemplate': fuzzed_dset_templates, 'Variables': fuzzed_dset_variables}  
    df = pd.DataFrame(dict) 

    print("len(df.index) BEFORE", len(df.index))
    df = df[df['Content'].str.len()<300]
    print("len(df.index) AFTER", len(df.index))

    tail_no = 0
    if len(df.index) < 2000:
        tail_no = 2000 - len(df.index) 
    
    last_rows=df.tail(tail_no)
    df = pd.concat([df, last_rows])
    
    df.to_csv(f'automatic_fuzz_data/fuzzed_parsed/{DSET}_{R_LEVEL}_fuzzed.csv', index=False) 
    df = df["Content"]
    df.to_csv(f'automatic_fuzz_data/fuzzed_parsed/{DSET}_{R_LEVEL}_fuzzed_log.csv', index=False, header=False) 
    
    get_heterogeneity(f'automatic_fuzz_data/fuzzed_parsed/{DSET}_{R_LEVEL}_fuzzed.csv')
    return 0