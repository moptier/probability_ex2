import os, sys

VOCABULARY_SIZE = 300000
LIDESTONE_SPLIT_RATE = 0.9

# preprocessing
def get_events_in_file(filename):
    events = []
    with open(filename) as f:
        lines = f.read().split('\n')[::2]
        content_lines = lines[1::2]
        for content in content_lines:
            events += content.strip().split(" ")
    return events

# for unigram uniform
def calc_p_uniform():
    return 1 / VOCABULARY_SIZE

# check validity of supplied files
def check_files_if_valid(base_dir, develop_file, test_file, output_file):
    if not os.path.isfile(os.path.join(base_dir,  develop_file)) or \
        not os.path.isfile(os.path.join(base_dir, test_file)) or \
        not os.path.isfile(os.path.join(base_dir, output_file)):
        return False
    return True

def lidstone_split(events_list):
    train_dev = []
    validation_dev = []

    split_index = round(LIDESTONE_SPLIT_RATE * len(events_list))
    train_set = events_list[:split_index]
    validation_set = events_list[split_index:]

    return train_set, validation_set

if __name__ == "__main__":
    # TODO- CHECK IF THIS IS NEEDED?
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    # a list for saving outputs to write to files at end of the run
    outputs_list = []

    # get parameters
    develop_file = sys.argv[1]
    test_file = sys.argv[2]
    input_word = sys.argv[3]
    output_file = sys.argv[4]

    # check validity of supplied files
    if not check_files_if_valid(BASE_DIR, develop_file, test_file, output_file):
        print('Invalid inputs')
        exit(1)

    # Bullet 1 - outputs
    outputs_list.append("id xxx id xxx")
    outputs_list.append(develop_file)
    outputs_list.append(test_file)
    outputs_list.append(input_word)
    outputs_list.append(output_file)
    outputs_list.append(VOCABULARY_SIZE)
    outputs_list.append(calc_p_uniform())

    # parse developer.txt file
    develop_file_full_path = os.path.join(BASE_DIR, develop_file)
    # hold all the words from all files
    events_list = get_events_in_file(develop_file_full_path)

    # Bullet 2 - outputs
    # total number of events in the development set
    outputs_list.append(len(events_list))

    train_set, validation_set = lidstone_split(events_list)
    train_set_len = len(train_set)
    validation_set_len = len(validation_set)

    # Bullet 3 - outputs
    # Output 8
    outputs_list.append(validation_set_len)
    # Output 9
    outputs_list.append(train_set_len)

    observed_vocabulary_in_train_set = set(train_set)
    # Output 10
    outputs_list.append(len(observed_vocabulary_in_train_set))

    # Output 11
    outputs_list.append(train_set.count(input_word))

