
import os

def get_algorithm_directories(base_data_dir):
    results = []

    for cur_dir, dirs, files in os.walk(base_data_dir):
        for sub_dir in dirs:
            results.append(os.path.join(cur_dir, sub_dir))

    return results

def read_run_contents(dir, filename):
    file = os.path.join(dir, filename)

    if not os.path.isfile(file):
        return []

    with open(file) as f:
        return map(lambda str: str.strip(), f.readlines())

def get_dataset_name(str):
    prefix = '-t datasets/'
    start = str.find(prefix) + len(prefix)
    next = str[start:].find('/') + 1 + start
    end = str[next:].find(' ')
    return str[next:(next + end)]

def build_output_path(dir, suffix, str):
    return os.path.join(dir, get_dataset_name(str) + suffix)

def run_algorithm(cmd, out_file):
    ## Uncomment this to skip files that have already been generated.
    #if os.path.isfile(out_file):
    #    return
    
    full_cmd = cmd + ' > ' + out_file
    print 'Running: ' + full_cmd
    os.system(full_cmd)

if __name__ == "__main__":
    data_dirs = [ 'nursery', 'spectrometer' ]
    run_files = [ '_to_run_train_cv.txt', '_to_run_test.txt' ]

    for basedir in data_dirs:
        for dir in get_algorithm_directories(basedir):
            for rf in run_files:
                run_cmds = read_run_contents(dir, rf)

                for cmd in run_cmds:
                    suffix = '.out.txt'

                    if ' -T ' in cmd:
                        suffix = '.test' + suffix
                    else:
                        suffix = '.train' + suffix

                    out_file = build_output_path(dir, suffix, cmd)
                    run_algorithm(cmd, out_file)

    print 'Done'
